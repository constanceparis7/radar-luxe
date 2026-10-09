#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""lettre_hebdo.py — le brouillon de la lettre hebdomadaire (décision du 08/10/2026),
en anglais d'abord : cinq événements à connaître dans les quinze jours, deux fenêtres
qui ouvrent ou ferment, un changement de date. Tout vient des données du radar ; le
brouillon attend l'édito de Constance (trois phrases, le choix de la semaine).

Usage : python3 .radar/tools/lettre_hebdo.py [AAAA-MM-JJ] [--sortie fichier.html]
Aucune écriture dans les données du site.
"""
import datetime as dt, json, os, re, sys, html
REPO = os.environ.get("RADAR_REPO") or os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BASE = "https://constanceparis7.com"
args = [a for a in sys.argv[1:] if not a.startswith("--")]
today = dt.date.fromisoformat(args[0]) if args else dt.date.today()
sortie = sys.argv[sys.argv.index("--sortie") + 1] if "--sortie" in sys.argv else None
api = json.load(open(os.path.join(REPO, "api", "evenements.json"), encoding="utf-8"))["evenements"]
fen = json.load(open(os.path.join(REPO, ".radar", "fenetres.json"), encoding="utf-8"))["fenetres"] if os.path.exists(os.path.join(REPO, ".radar", "fenetres.json")) else []
mem = [json.loads(l) for l in open(os.path.join(REPO, ".radar", "memoire.ndjson"), encoding="utf-8") if l.strip()]
d = lambda s: dt.date.fromisoformat(s[:10])
def when(e):
    a, b = d(e["debut"]), d(e["fin"])
    if a == b: return a.strftime("%A %-d %B")
    if a.month == b.month: return f"{a.day} to {b.day} {a.strftime('%B')}"
    return f"{a.strftime('%-d %B')} to {b.strftime('%-d %B')}"
# 1. five to know : start within 14 days (or ongoing short), best notes
fen_fin = today + dt.timedelta(days=14)
cand = [e for e in api if d(e["fin"]) >= today and d(e["debut"]) <= fen_fin and (d(e["fin"]) - d(e["debut"])).days <= 14]
cand.sort(key=lambda e: (-(e.get("note_radar") or 0), e["debut"]))
cinq = cand[:5]
# 2. two windows opening or closing within 30 days
fen_dated = []
for f in fen:
    for key, verb in (("ouverture", "opens"), ("cloture", "closes")):
        v = f.get(key)
        if v and today <= d(v) <= today + dt.timedelta(days=30):
            fen_dated.append((d(v), verb, f))
fen_dated.sort(key=lambda x: x[0])
deux = fen_dated[:2]
# 3. one change (most recent date change)
chg = [m for m in mem if m.get("type") == "changement_date"]
chg.sort(key=lambda m: m.get("date", ""), reverse=True)
un = chg[0] if chg else None
E = lambda s: html.escape(str(s or ""))
o = [f"<p style='font-family:Georgia,serif;font-size:13px;color:#7a786f;margin:0 0 14px'>The weekly luxury radar · {today.strftime('%-d %B %Y')}</p>",
     "<p style='font-family:Georgia,serif;font-size:16px;line-height:1.5'>[ÉDITO : trois phrases de Constance, le choix de la semaine et pourquoi lui.]</p>",
     "<h2 style='font-family:Georgia,serif;font-weight:normal;font-size:20px;margin:22px 0 8px'>Five to know</h2><ul style='padding-left:18px;font-family:Georgia,serif;font-size:15px;line-height:1.5'>"]
for e in cinq:
    o.append(f"<li><b>{E(e['nom_en'] or e['nom'])}</b> · {E(when(e))} · {E(e['ville'])} · access: {E(e['acces'])} · <a href='{E(e['url']['en'])}'>details</a></li>")
o.append("</ul><h2 style='font-family:Georgia,serif;font-weight:normal;font-size:20px;margin:22px 0 8px'>Two windows</h2><ul style='padding-left:18px;font-family:Georgia,serif;font-size:15px;line-height:1.5'>")
if deux:
    for dd, verb, f in deux:
        o.append(f"<li><b>{E(f['evenement'])}</b> · {E(f['type'])} {verb} on {dd.strftime('%-d %B')}{(' at ' + E(f['heure'][:40])) if f.get('heure') else ''} · <a href='{E(f.get('url') or f.get('page'))}'>official page</a></li>")
else:
    o.append("<li>No dated opening or deadline published in the next 30 days among the windows the radar follows.</li>")
o.append("</ul><h2 style='font-family:Georgia,serif;font-weight:normal;font-size:20px;margin:22px 0 8px'>One change</h2>")
if un:
    o.append(f"<p style='font-family:Georgia,serif;font-size:15px;line-height:1.5'><b>{E(un['evenement'])}</b> · {E(un['detail'])} · source: {E(un['preuve'])[:140]}</p>")
o.append("<p style='font-family:Georgia,serif;font-size:13px;color:#7a786f;margin-top:24px'>Every date is read on the organiser's official page and dated. A place in the radar cannot be bought. <a href='https://constanceparis7.com/en/'>constanceparis7.com</a></p>")
out = "\n".join(o)
if sortie: open(sortie, "w", encoding="utf-8").write(out)
print(json.dumps({"cinq": [e["nom"][:50] for e in cinq], "fenetres": [(x[0].isoformat(), x[2]["evenement"][:40]) for x in deux], "changement": (un or {}).get("evenement", "")[:50]}, ensure_ascii=False))
