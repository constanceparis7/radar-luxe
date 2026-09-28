#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""mesure_cdp.py : LCP, CLS, INP (approché) et poids transféré, mesurés par Chrome
headless et le protocole DevTools dans les conditions de Lighthouse mobile : écran
412x915 à 2,625 de densité, agent utilisateur Android, réseau 4G lent (1,6 Mbit/s,
150 ms), CPU ralenti 4 fois. Posé le 28/09/2026 parce que le quota de l'API PageSpeed
est épuisé en permanence et que Node (donc Lighthouse) n'est pas installé.

Dépendances : Google Chrome (chemin CHROME) et le module Python websocket-client
(python3 -m pip install --user websocket-client).

Usage : python3 .radar/tools/mesure_cdp.py URL [URL...]
        --log   ajoute une ligne par URL à .radar/tools/vitals-log.ndjson (mesure
                hebdomadaire, feuille de route O3) ; --offline force le mode hors ligne.
Seuils Google : LCP 2 500 ms, INP 200 ms, CLS 0,1. L'INP mesuré ici est le pire
événement de quelques interactions scriptées (thème, filtres, frappe), pas un 75e
centile de vrais visiteurs : c'est une borne haute honnête, pas la valeur CrUX.
"""
import json, subprocess, sys, time, tempfile, shutil, urllib.request
import websocket

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
PORT = 9333
UA = ("Mozilla/5.0 (Linux; Android 11; moto g power (2022)) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36")

OBS = r"""
window.__cp7 = {lcp: [], cls: 0, clsEntries: 0, events: [], paint: {}};
window.__errs = []; addEventListener('error', function (e) { window.__errs.push(String(e.message)); });
try {
  new PerformanceObserver(l => { for (const e of l.getEntries()) window.__cp7.lcp.push({t: e.startTime, size: e.size, el: (e.element && (e.element.tagName + (e.element.className ? '.' + String(e.element.className).split(' ')[0] : ''))) || ''}); })
    .observe({type: 'largest-contentful-paint', buffered: true});
  new PerformanceObserver(l => { for (const e of l.getEntries()) if (!e.hadRecentInput) { window.__cp7.cls += e.value; window.__cp7.clsEntries++; } })
    .observe({type: 'layout-shift', buffered: true});
  new PerformanceObserver(l => { for (const e of l.getEntries()) window.__cp7.events.push({name: e.name, dur: e.duration, delay: e.processingStart - e.startTime, target: e.target && e.target.tagName}); })
    .observe({type: 'event', buffered: true, durationThreshold: 16});
  new PerformanceObserver(l => { for (const e of l.getEntries()) window.__cp7.paint[e.name] = e.startTime; })
    .observe({type: 'paint', buffered: true});
} catch (e) { window.__cp7.err = String(e); }
"""

COLLECT = r"""
(() => {
  const n = performance.getEntriesByType('navigation')[0] || {};
  const res = performance.getEntriesByType('resource');
  const transf = (n.transferSize || 0) + res.reduce((s, r) => s + (r.transferSize || 0), 0);
  const c = window.__cp7 || {};
  const lcp = c.lcp && c.lcp.length ? c.lcp[c.lcp.length - 1] : null;
  const inp = c.events && c.events.length ? Math.max(...c.events.map(e => e.dur)) : null;
  return JSON.stringify({
    lcp_ms: lcp ? Math.round(lcp.t) : null, lcp_el: lcp ? lcp.el : null,
    cls: c.cls != null ? Math.round(c.cls * 1000) / 1000 : null,
    fcp_ms: c.paint && c.paint['first-contentful-paint'] != null ? Math.round(c.paint['first-contentful-paint']) : null,
    ttfb_ms: n.responseStart != null ? Math.round(n.responseStart) : null,
    dcl_ms: n.domContentLoadedEventEnd != null ? Math.round(n.domContentLoadedEventEnd) : null,
    load_ms: n.loadEventEnd != null ? Math.round(n.loadEventEnd) : null,
    transfert_ko: Math.round(transf / 1024), requetes: res.length + 1,
    inp_ms: inp != null ? Math.round(inp) : null, interactions: (c.events || []).length,
    pires: (c.events || []).slice().sort((a, b) => b.dur - a.dur).slice(0, 8).map(e => e.name + ':' + e.target + ':' + Math.round(e.dur) + 'ms'),
    err: c.err || null, erreurs_js: (window.__errs || []).slice(0, 3), titre: document.title
  });
})()
"""


class CDP:
    def __init__(self, url):
        self.ws = websocket.create_connection(url, suppress_origin=True)
        self.ws.settimeout(2)
        self.n = 0
        self.pending = []

    def send(self, method, **params):
        self.n += 1
        mid = self.n
        self.ws.send(json.dumps({"id": mid, "method": method, "params": params}))
        end = time.time() + 120
        while time.time() < end:
            try:
                msg = json.loads(self.ws.recv())
            except websocket.WebSocketTimeoutException:
                continue
            if msg.get("id") == mid:
                if "error" in msg:
                    raise RuntimeError(f"{method}: {msg['error']}")
                return msg.get("result", {})
            self.pending.append(msg)
        raise RuntimeError(f"{method}: pas de réponse")

    def wait(self, name, timeout=90):
        for m in list(self.pending):
            if m.get("method") == name:
                self.pending.remove(m)
                return m
        end = time.time() + timeout
        while time.time() < end:
            try:
                msg = json.loads(self.ws.recv())
            except websocket.WebSocketTimeoutException:
                continue
            if msg.get("method") == name:
                return msg
            self.pending.append(msg)
        return None

    def evaluate(self, expr):
        r = self.send("Runtime.evaluate", expression=expr, returnByValue=True)
        return r.get("result", {}).get("value")


def start_chrome(profile):
    p = subprocess.Popen([CHROME, f"--remote-debugging-port={PORT}", "--headless=new", "--no-first-run",
                          "--no-default-browser-check", f"--user-data-dir={profile}", "--disable-gpu",
                          "--hide-scrollbars", "--disable-extensions", "--disable-background-networking",
                          "about:blank"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    for _ in range(100):
        try:
            urllib.request.urlopen(f"http://127.0.0.1:{PORT}/json/version", timeout=1)
            return p
        except Exception:
            time.sleep(0.2)
    p.kill()
    raise SystemExit("Chrome ne démarre pas")


def new_target():
    req = urllib.request.Request(f"http://127.0.0.1:{PORT}/json/new?about:blank", method="PUT")
    return json.load(urllib.request.urlopen(req, timeout=5))


def tap(c, selector):
    rect = c.evaluate(f"(() => {{ const e = document.querySelector('{selector}'); if (!e) return null; e.scrollIntoView({{block:'center'}}); const r = e.getBoundingClientRect(); return JSON.stringify({{x: r.x + r.width/2, y: r.y + r.height/2}}); }})()")
    if not rect:
        return False
    pt = json.loads(rect)
    c.send("Input.dispatchTouchEvent", type="touchStart", touchPoints=[{"x": pt["x"], "y": pt["y"]}])
    c.send("Input.dispatchTouchEvent", type="touchEnd", touchPoints=[])
    time.sleep(0.8)
    return True


def mesure(url, offline=False, interactions=True):
    t = new_target()
    c = CDP(t["webSocketDebuggerUrl"])
    for m in ("Page.enable", "Network.enable", "Runtime.enable"):
        c.send(m)
    c.send("Emulation.setDeviceMetricsOverride", width=412, height=915, deviceScaleFactor=2.625, mobile=True)
    c.send("Emulation.setUserAgentOverride", userAgent=UA)
    c.send("Emulation.setTouchEmulationEnabled", enabled=True, maxTouchPoints=5)
    c.send("Network.setCacheDisabled", cacheDisabled=True)
    c.send("Network.emulateNetworkConditions", offline=offline, latency=150,
           downloadThroughput=1.6 * 1024 * 1024 / 8, uploadThroughput=750 * 1024 / 8)
    c.send("Emulation.setCPUThrottlingRate", rate=4)
    c.send("Page.addScriptToEvaluateOnNewDocument", source=OBS)
    c.send("Page.navigate", url=url)
    loaded = c.wait("Page.loadEventFired", timeout=120)
    time.sleep(3.0)
    if interactions and not offline:
        tap(c, ".theme-btn")
        tap(c, ".filter-toggle")
        if c.evaluate("!!document.querySelector('.search')"):
            c.evaluate("(() => { const s = document.querySelector('.search'); s.focus(); return true; })()")
            for ch in "paris":
                c.send("Input.dispatchKeyEvent", type="keyDown", text=ch, key=ch)
                c.send("Input.dispatchKeyEvent", type="keyUp", key=ch)
                time.sleep(0.15)
            time.sleep(1.0)
        tap(c, ".theme-btn")
        time.sleep(1.5)
    out = json.loads(c.evaluate(COLLECT))
    out["url"] = url
    out["load_event"] = bool(loaded)
    if offline:
        out["body_extrait"] = c.evaluate("(document.body && document.body.innerText || '').slice(0, 160)")
    c.ws.close()
    urllib.request.urlopen(f"http://127.0.0.1:{PORT}/json/close/{t['id']}", timeout=5).read()
    return out


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    offline = "--offline" in sys.argv
    profile = tempfile.mkdtemp(prefix="cp7-chrome-")
    p = start_chrome(profile)
    log = "--log" in sys.argv
    import datetime, os
    LOG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "vitals-log.ndjson")
    try:
        for u in args:
            r = mesure(u, offline=offline)
            print(json.dumps(r, ensure_ascii=False))
            if log:
                ligne = {"date": datetime.date.today().isoformat(), "url": u}
                ligne.update({k: r.get(k) for k in ("lcp_ms", "cls", "inp_ms", "fcp_ms", "ttfb_ms", "load_ms", "transfert_ko")})
                with open(LOG, "a", encoding="utf-8") as f:
                    f.write(json.dumps(ligne, ensure_ascii=False) + "\n")
    finally:
        p.kill()
        shutil.rmtree(profile, ignore_errors=True)
