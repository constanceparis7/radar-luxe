#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""reverification.py — la liste des fiches à revérifier en priorité (point 9 du
registre « aucun point faible », 27/09/2026).

Constat : 219 fiches vivantes, 59 seulement portent une date de vérification
écrite (« vérifié le JJ/MM/AAAA » dans `so` ou `iv`), et parmi les fiches
imminentes ou en cours, 109 n'ont aucune date écrite ou une date de plus de
30 jours. La date de l'eyebrow de l'accueil dit quand la PASSE a vérifié quelque
chose ; le badge « Vérifié à la source le… » d'une fiche dit quand CETTE fiche
l'a été. Ce script tient la file d'attente entre les deux.

Règle : fiche non terminée, commençant dans 21 jours ou déjà en cours, dont la
dernière vérification écrite est absente ou date de plus de 30 jours ; triée par
imminence, puis par ancienneté de la vérification.

Sortie : .radar/reverification-prioritaire.json (lu par la passe de nuit, voir
DOCTRINE.md, étape 5bis). Aucune écriture dans les données du site.

Usage : python3 .radar/tools/reverification.py [AAAA-MM-JJ]
"""
import datetime as dt
import json
import os
import re
import sys

REPO = os.environ.get("RADAR_REPO") or os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(REPO, "index-full.html")
if not os.path.exists(SRC):
    SRC = os.path.join(REPO, "index.html")
OUT = os.path.join(REPO, ".radar", "reverification-prioritaire.json")

# Même motif que gen_pages.date_verif : on ne lit que ce qui est ÉCRIT.
RX_VERIF = re.compile(r"(?:v[ée]rifi\w*|contr[oô]l[ée]\w*|checked)[^0-9]{0,30}?(\d{1,2}/\d{1,2}/\d{4})", re.I)
IMMINENCE_JOURS = 21
FRAICHEUR_JOURS = 30


def date_verif(e):
    textes = [str(e.get("so") or "")]
    iv = e.get("iv")
    if isinstance(iv, dict):
        textes += [str(v) for v in iv.values() if isinstance(v, str)]
    best = None
    for tx in textes:
        for m in RX_VERIF.finditer(tx):
            j, mo, a = m.group(1).split("/")
            try:
                d = dt.date(int(a), int(mo), int(j))
            except ValueError:
                continue
            if best is None or d > best:
                best = d
    return best


def main():
    today = dt.date.fromisoformat(sys.argv[1]) if len(sys.argv) > 1 else dt.date.today()
    html = open(SRC, encoding="utf-8").read()
    m = re.search(r'<script[^>]*id="data"[^>]*>(.*?)</script>', html, re.S)
    if not m:
        sys.exit("reverification: bloc data introuvable")
    data = json.loads(m.group(1).replace("<\\/", "</"))
    # iv peut vivre hors de l'index léger : on le réinjecte si le fichier existe
    det_path = os.path.join(REPO, ".radar", "details-data.json")
    if os.path.exists(det_path):
        det = json.load(open(det_path, encoding="utf-8"))
        for e in data:
            if not e.get("iv"):
                k = f"{e.get('d1', '')}|{e.get('n', '')}"
                if k in det and det[k].get("iv"):
                    e["iv"] = det[k]["iv"]
    rows = []
    for e in data:
        if e.get("c") == "acces" or not e.get("d1") or not e.get("d2"):
            continue
        try:
            d1 = dt.date.fromisoformat(e["d1"])
            d2 = dt.date.fromisoformat(e["d2"])
        except ValueError:
            continue
        if d2 < today:
            continue
        v = date_verif(e)
        rows.append({
            "n": e["n"], "d1": e["d1"], "d2": e["d2"],
            "dans_jours": (d1 - today).days,
            "verifie_le": v.isoformat() if v else None,
            "age_jours": (today - v).days if v else None,
            "cf": e.get("cf"),
        })
    avec = [r for r in rows if r["verifie_le"]]
    prio = [r for r in rows if r["dans_jours"] <= IMMINENCE_JOURS
            and (r["age_jours"] is None or r["age_jours"] > FRAICHEUR_JOURS)]
    prio.sort(key=lambda r: (r["dans_jours"], -(r["age_jours"] or 9999)))
    out = {
        "genere_le": today.isoformat(),
        "regle": (f"fiche non terminée, commençant dans {IMMINENCE_JOURS} jours ou déjà en cours, "
                  f"dont la dernière vérification écrite est absente ou date de plus de "
                  f"{FRAICHEUR_JOURS} jours ; triée par imminence puis par ancienneté"),
        "total_vivantes": len(rows),
        "avec_date_verif": len(avec),
        "prioritaires": prio,
    }
    json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"reverification: {len(rows)} fiches vivantes, {len(avec)} avec date écrite, "
          f"{len(prio)} à revérifier en priorité -> {os.path.relpath(OUT, REPO)}")
    for r in prio[:5]:
        print(f"  J{r['dans_jours']:+d}  {r['verifie_le'] or 'jamais écrite'}  {r['n'][:60]}")


if __name__ == "__main__":
    main()
