#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""audit_axe.py : audit d'accessibilité automatisé (axe-core 4.10, WCAG 2.1 A/AA et bonnes
pratiques) sur des pages en ligne ou locales, injecté par le protocole DevTools de Chrome
(exempt de la CSP du site : rien n'est modifié sur le site). Posé le 28/09/2026 ; la
bibliothèque axe.min.js est téléchargée une fois à côté de ce fichier (gitignore).
Usage : python3 .radar/tools/audit_axe.py URL [URL...] [--mobile]   (0 violation attendue)"""
import json, os, sys, time, tempfile, shutil, urllib.request
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mesure_cdp import CDP, start_chrome, new_target

AXE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "axe.min.js")
if not os.path.exists(AXE):
    urllib.request.urlretrieve("https://cdnjs.cloudflare.com/ajax/libs/axe-core/4.10.2/axe.min.js", AXE)
axe_src = open(AXE, encoding="utf-8").read()

prof = tempfile.mkdtemp(prefix="cp7-axe-")
ch = start_chrome(prof)
try:
    for url in [a for a in sys.argv[1:] if not a.startswith("--")]:
        t = new_target()
        c = CDP(t["webSocketDebuggerUrl"])
        for m in ("Page.enable", "Runtime.enable"):
            c.send(m)
        if "--mobile" in sys.argv:
            c.send("Emulation.setDeviceMetricsOverride", width=390, height=844, deviceScaleFactor=3, mobile=True)
        c.send("Page.navigate", url=url)
        c.wait("Page.loadEventFired", timeout=90)
        time.sleep(3)
        c.send("Runtime.evaluate", expression=axe_src)
        r = c.send("Runtime.evaluate", expression="axe.run(document, {runOnly: {type: 'tag', values: ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'best-practice']}}).then(function(r){return JSON.stringify({v: r.violations.map(function(x){return {id: x.id, impact: x.impact, help: x.help, n: x.nodes.length, ex: x.nodes.slice(0, 2).map(function(nd){return nd.target.join(' ')})}}), passes: r.passes.length, incomplete: r.incomplete.length})})",
                   awaitPromise=True, returnByValue=True, timeout=120000)
        res = json.loads(r["result"]["value"])
        print("==", url)
        print(f"   règles satisfaites : {res['passes']}  | à examiner : {res['incomplete']}  | violations : {len(res['v'])}")
        for v in res["v"]:
            print(f"   [{v['impact']}] {v['id']} : {v['help']} ({v['n']} élément(s)) ex. {v['ex']}")
        c.ws.close()
        urllib.request.urlopen(f"http://127.0.0.1:9333/json/close/{t['id']}", timeout=5).read()
finally:
    ch.kill()
    shutil.rmtree(prof, ignore_errors=True)
