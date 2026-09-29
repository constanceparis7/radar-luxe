#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""tableau_de_bord.py : le tableau de bord de pilotage du radar, en une page (O8 de la
feuille de route, 28/09/2026). Lit ce que les routines écrivent déjà et n'invente rien :

  stats/visites.ndjson                     visiteurs (cumul quotidien GoatCounter)
  .radar/tools/vitals-log.ndjson           LCP, INP, CLS mesurés (mesure_cdp.py)
  .radar/reverification-prioritaire.json   file de revérification des fiches
  .radar/FEUILLE-DE-ROUTE.md               taux par objectif
  .radar/tools/run-log.ndjson              dernières passes automatiques
  git log                                  dernières publications
  index.html                               nombre de fiches, date affichée

Sortie : .radar/tableau-de-bord-pilotage.html (privé : le dossier .radar n'est pas servi
par le site, vérifié le 28/09/2026 ; la page est publiée à Constance en artefact).
Usage : python3 .radar/tools/tableau_de_bord.py
"""
import datetime as dt
import html
import json
import os
import re
import subprocess

REPO = os.environ.get("RADAR_REPO") or os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(REPO, ".radar", "tableau-de-bord-pilotage.html")
esc = html.escape


def ndjson(p):
    rows = []
    if os.path.exists(p):
        for line in open(p, encoding="utf-8"):
            line = line.strip()
            if line:
                try:
                    rows.append(json.loads(line))
                except ValueError:
                    pass
    return rows


def fr(n):
    return f"{n:,}".replace(",", " ") if isinstance(n, int) else str(n)


# ---- visites -------------------------------------------------------------
vis = ndjson(os.path.join(REPO, "stats", "visites.ndjson"))
jours = []
for a, b in zip(vis, vis[1:]):
    jours.append((b["date"], b["visites"] - a["visites"]))
jours = jours[-21:]
cumul = vis[-1]["visites"] if vis else 0
maxi = max([j[1] for j in jours] + [1])

# ---- vitals --------------------------------------------------------------
vit = ndjson(os.path.join(REPO, ".radar", "tools", "vitals-log.ndjson"))
vit_acc = [v for v in vit if v.get("url", "").rstrip("/") == "https://constanceparis7.com"]
dernier_acc = vit_acc[-1] if vit_acc else {}
vit_fiches = [v for v in vit if "/e/" in v.get("url", "")]

# ---- fraîcheur -----------------------------------------------------------
frq = {}
p = os.path.join(REPO, ".radar", "reverification-prioritaire.json")
if os.path.exists(p):
    frq = json.load(open(p, encoding="utf-8"))

# ---- feuille de route ------------------------------------------------------
objectifs = []
p = os.path.join(REPO, ".radar", "FEUILLE-DE-ROUTE.md")
if os.path.exists(p):
    for m in re.finditer(r"^### (O\d) · (.*?) · (\d+) %", open(p, encoding="utf-8").read(), re.M):
        objectifs.append((m.group(1), m.group(2), int(m.group(3))))

# ---- passes et publications ------------------------------------------------
runs = ndjson(os.path.join(REPO, ".radar", "tools", "run-log.ndjson"))[-6:]
try:
    log = subprocess.run(["git", "-C", REPO, "log", "--format=%ad|%an|%s", "--date=format:%d/%m %H:%M", "-n", "8"],
                         capture_output=True, text=True, check=True).stdout.strip().splitlines()
except Exception:
    log = []

# ---- site ------------------------------------------------------------------
idx = open(os.path.join(REPO, "index.html"), encoding="utf-8").read()
m = re.search(r'<script[^>]*id="data"[^>]*>(.*?)</script>', idx, re.S)
n_fiches = len(json.loads(m.group(1))) if m else 0
m = re.search(r"vérifiées le ([^<]*?)<", idx)
date_site = m.group(1).strip() if m else "?"
n_pages = sum(1 for _, _, fs in os.walk(REPO) for f in fs if f.endswith(".html")) if os.path.isdir(REPO) else 0

now = dt.datetime.now().strftime("%d/%m/%Y à %H:%M")


def barres():
    out = []
    for d, n in jours:
        h = max(3, round(n / maxi * 110))
        out.append(f'<div class="b" style="height:{h}px" title="{d} : +{n}"><span>+{n}</span></div>')
    return "".join(out)


def etiquettes():
    return "".join(f"<span>{d[8:]}/{d[5:7]}</span>" for d, _ in jours)


def vital(nom, val, seuil, unite, inv=False):
    if val is None:
        return f'<div class="v"><div class="k">{nom}</div><div class="n">mesure absente</div></div>'
    ok = val <= seuil
    txt = (f"{val/1000:.2f} s" if unite == "s" else (f"{val}" if unite == "" else f"{val} {unite}"))
    return (f'<div class="v {"ok" if ok else "ko"}"><div class="k">{nom}</div><div class="n">{txt}</div>'
            f'<div class="s">seuil {seuil/1000:.1f} s</div></div>' if unite == "s" else
            f'<div class="v {"ok" if ok else "ko"}"><div class="k">{nom}</div><div class="n">{txt}</div>'
            f'<div class="s">seuil {seuil}{(" " + unite) if unite else ""}</div></div>')


objs = "".join(
    f'<div class="o"><div class="ot"><b>{o}</b> {esc(t)}</div><div class="bar"><i style="width:{p}%"></i></div><div class="op">{p} %</div></div>'
    for o, t, p in objectifs)

prio = frq.get("prioritaires", [])[:8]
prio_html = "".join(
    f'<li><span class="j">J{r["dans_jours"]:+d}</span> {esc(r["n"][:70])} <span class="m">{"jamais datée" if not r.get("verifie_le") else "vérifiée le " + r["verifie_le"]}</span></li>'
    for r in prio) or "<li>file vide</li>"

runs_html = "".join(
    f'<li><span class="j">{esc(str(r.get("date") or r.get("jour") or r.get("ts") or "")[:16])}</span> {esc(str(r.get("resume") or r.get("summary") or r.get("mode") or json.dumps(r, ensure_ascii=False))[:140])}</li>'
    for r in reversed(runs)) or "<li>aucune passe journalisée</li>"

log_html = "".join(
    f'<li><span class="j">{esc(l.split("|")[0])}</span> <span class="m">{esc(l.split("|")[1])}</span> {esc(l.split("|", 2)[2][:120])}</li>'
    for l in log if l.count("|") >= 2) or "<li>journal git indisponible</li>"

page = f"""<title>Pilotage ConstanceParis7</title>
<style>
:root{{--bg:#f7f6f2;--ink:#1c2230;--muted:#6b7280;--line:#e2dfd6;--or:#a07c2e;--or2:#d3b06a;--ok:#2f8f5b;--ko:#b3402e;--card:#ffffff}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#0f151f;--ink:#eceadf;--muted:#9fb0bd;--line:#273143;--or:#d3b06a;--or2:#a07c2e;--ok:#4cc38a;--ko:#e0705a;--card:#151d29}}}}
:root[data-theme="dark"]{{--bg:#0f151f;--ink:#eceadf;--muted:#9fb0bd;--line:#273143;--or:#d3b06a;--or2:#a07c2e;--ok:#4cc38a;--ko:#e0705a;--card:#151d29}}
body{{background:var(--bg);color:var(--ink);font-family:"Avenir Next",Avenir,-apple-system,"Segoe UI",Helvetica,Arial,sans-serif;line-height:1.5;margin:0}}
.wrap{{max-width:1040px;margin:0 auto;padding:28px 18px 60px}}
h1{{font-family:Didot,"Bodoni 72",Georgia,serif;font-weight:400;font-size:2rem;margin:0 0 4px}}
.sub{{color:var(--muted);font-size:.9rem;margin-bottom:22px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px;margin-bottom:22px}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px 18px}}
.card h2{{font-size:.78rem;letter-spacing:.12em;text-transform:uppercase;color:var(--or);margin:0 0 10px;font-weight:600}}
.big{{font-family:Didot,"Bodoni 72",Georgia,serif;font-size:2.4rem;line-height:1.1;font-variant-numeric:tabular-nums}}
.k{{font-size:.8rem;color:var(--muted)}}
.histo{{display:flex;align-items:flex-end;gap:5px;height:120px;border-bottom:1px solid var(--line);padding:0 2px}}
.b{{flex:1;background:var(--or2);border-radius:3px 3px 0 0;position:relative;min-width:6px}}
.b span{{position:absolute;top:-18px;left:50%;transform:translateX(-50%);font-size:10px;color:var(--muted);white-space:nowrap}}
.et{{display:flex;gap:5px;font-size:9px;color:var(--muted);padding-top:4px}}.et span{{flex:1;text-align:center;min-width:6px}}
.vit{{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}}
.v{{border:1px solid var(--line);border-radius:10px;padding:10px;text-align:center}}.v.ok{{border-color:var(--ok)}}.v.ko{{border-color:var(--ko)}}
.v .n{{font-size:1.4rem;font-variant-numeric:tabular-nums}}.v.ok .n{{color:var(--ok)}}.v.ko .n{{color:var(--ko)}}.v .s{{font-size:.72rem;color:var(--muted)}}
.o{{display:grid;grid-template-columns:1fr 160px 48px;gap:10px;align-items:center;padding:6px 0;border-bottom:1px solid var(--line);font-size:.92rem}}
.o:last-child{{border-bottom:0}}.bar{{height:8px;background:var(--line);border-radius:4px;overflow:hidden}}.bar i{{display:block;height:100%;background:var(--or)}}
.op{{text-align:right;font-variant-numeric:tabular-nums}}
ul{{list-style:none;margin:0;padding:0}}li{{padding:5px 0;border-bottom:1px solid var(--line);font-size:.9rem}}li:last-child{{border-bottom:0}}
.j{{display:inline-block;min-width:54px;color:var(--or);font-variant-numeric:tabular-nums}}.m{{color:var(--muted);font-size:.82rem}}
@media(max-width:640px){{.o{{grid-template-columns:1fr 90px 44px}}.vit{{grid-template-columns:1fr}}}}
</style>
<div class="wrap">
<h1>Pilotage ConstanceParis7</h1>
<div class="sub">Généré le {now} depuis les journaux du radar. Rien n'est saisi à la main.</div>
<div class="grid">
 <div class="card"><h2>Visiteurs</h2><div class="big">{fr(cumul)}</div><div class="k">cumul depuis l'ouverture du compteur · {("+" + str(jours[-1][1]) + " au relevé du " + jours[-1][0][8:] + "/" + jours[-1][0][5:7]) if jours else ""}</div></div>
 <div class="card"><h2>Le site</h2><div class="big">{n_fiches}</div><div class="k">fiches vivantes · {fr(n_pages)} pages publiées · date affichée : {esc(date_site)}</div></div>
 <div class="card"><h2>Fraîcheur des fiches</h2><div class="big">{frq.get("avec_date_verif", "?")}<span style="font-size:1rem;color:var(--muted)"> / {frq.get("total_vivantes", "?")}</span></div><div class="k">datées « vérifié à la source » · {len(frq.get("prioritaires", []))} à revérifier en priorité</div></div>
</div>
<div class="grid" style="grid-template-columns:2fr 1fr">
 <div class="card"><h2>Nouveaux visiteurs par jour (21 derniers relevés)</h2><div class="histo">{barres()}</div><div class="et">{etiquettes()}</div></div>
 <div class="card"><h2>Vitesse mobile de l'accueil (dernière mesure{(" du " + dernier_acc["date"][8:] + "/" + dernier_acc["date"][5:7]) if dernier_acc else ""})</h2>
  <div class="vit">{vital("LCP", dernier_acc.get("lcp_ms"), 2500, "s")}{vital("INP", dernier_acc.get("inp_ms"), 200, "ms")}{vital("CLS", dernier_acc.get("cls"), 0.1, "")}</div>
  <div class="k" style="margin-top:8px">Conditions Lighthouse mobile : 4G lent, CPU ralenti 4 fois. Fiches : {len(vit_fiches)} mesure(s), LCP max {max([v.get("lcp_ms") or 0 for v in vit_fiches] + [0])/1000:.2f} s.</div></div>
</div>
<div class="grid" style="grid-template-columns:1fr 1fr">
 <div class="card"><h2>Feuille de route · taux par objectif</h2>{objs}</div>
 <div class="card"><h2>File de revérification · les 8 premières</h2><ul>{prio_html}</ul></div>
</div>
<div class="grid" style="grid-template-columns:1fr 1fr">
 <div class="card"><h2>Dernières publications</h2><ul>{log_html}</ul></div>
 <div class="card"><h2>Dernières passes automatiques</h2><ul>{runs_html}</ul></div>
</div>
</div>
"""
os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, "w", encoding="utf-8").write(page)
print(f"tableau de bord : {os.path.relpath(OUT, REPO)} ({len(page)//1024} Ko) · visiteurs {cumul} · fiches {n_fiches} · fraîcheur {frq.get('avec_date_verif')}/{frq.get('total_vivantes')} · objectifs {len(objectifs)}")
