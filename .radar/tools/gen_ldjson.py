#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""gen_ldjson.py — régénère la LISTE des 60 meilleurs événements à venir dans
le bloc <script type="application/ld+json"> d'index-full.html.

Pourquoi ce script existe (leçon du 14/09/2026)
------------------------------------------------
`gen_seo.py` ENRICHIT additivement les entrées déjà présentes dans le graphe
(eventStatus, organizer, offers) mais ne touche jamais à LA SÉLECTION des
événements. Sans ce script, le graphe se fige au jour où quelqu'un l'a
composé à la main et vieillit en silence : trouvé le 14/09/2026 avec un
événement du 12/08 encore en tête un mois plus tard.

Ce que fait ce script, et rien de plus :
  - lit le bloc `data` d'index-full.html (source de vérité) ;
  - calcule la Note du radar (même formule EXACTE que note_radar() dans
    gen_pages.py — une seule source de vérité, à faire évoluer ensemble) ;
  - retient les 60 meilleurs événements À VENIR (d2 >= aujourd'hui) qui ont
    une URL et un lieu ;
  - reconstruit le graphe avec les champs de BASE seulement (name, dates,
    lieu, image, description, url) — gen_seo.py se charge ensuite d'ajouter
    eventStatus/organizer/isAccessibleForFree/offers, comme toujours.

Usage :
    python3 gen_ldjson.py            # essai à blanc, affiche le résultat
    python3 gen_ldjson.py --apply    # écrit index-full.html

Doit tourner AVANT split_i18n.py (qui recopie le head, ld+json compris, tel
quel dans index.html) et donc avant gen_seo.py (qui enrichit index.html).
"""
import argparse
import json
import os
import re
from datetime import date

REPO = os.environ.get("RADAR_REPO") or os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FULL = os.path.join(REPO, "index-full.html")
HOME = "https://constanceparis7.com/"
TOP_N = 60


def parse_d(s):
    try:
        return date.fromisoformat((s or "")[:10])
    except Exception:
        return None


def note_radar(e, today):
    """Copie FIDÈLE de note_radar() dans gen_pages.py — à faire évoluer
    ensemble si la formule change (une seule source de vérité, doctrine)."""
    sv, sp, sl = e.get("sv"), e.get("sp"), e.get("sl")
    if sv is None or sp is None or sl is None:
        return None
    arrondi = lambda x: int(x + 0.5)
    d1, d2 = parse_d(e.get("d1")), parse_d(e.get("d2"))
    if not d1 or not d2:
        return None
    if d1 <= today <= d2:
        ds = 100
    elif d1 > today:
        ds = max(15, arrondi(100 - 2.2 * (d1 - today).days))
    else:
        ds = max(0, arrondi(55 - 4 * (today - d2).days))
    return arrondi(0.4 * sv + 0.3 * sp + 0.2 * sl + 0.1 * ds)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()

    html = open(FULL, encoding="utf-8").read()
    md = re.search(r'<script type="application/json" id="data">(.*?)</script>', html, re.S)
    data = json.loads(md.group(1).replace("<\\/", "</"))

    today = date.today()
    candidats = []
    for e in data:
        d2 = parse_d(e.get("d2")) or parse_d(e.get("d1"))
        if not d2 or d2 < today or not e.get("u") or not e.get("l"):
            continue
        n = note_radar(e, today)
        if n is not None:
            candidats.append((n, e))

    candidats.sort(key=lambda t: (-t[0], parse_d(t[1].get("d1")) or today))
    top = [e for _, e in candidats[:TOP_N]]

    graph = []
    for e in top:
        graph.append({
            "@type": "Event",
            "name": e.get("n"),
            "startDate": e.get("d1"),
            "endDate": e.get("d2"),
            "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
            "location": {
                "@type": "Place",
                "name": e.get("l"),
                "address": {"@type": "PostalAddress", "addressLocality": e.get("v") or ""},
            },
            "image": f"{HOME}og-image.png",
            "description": (e.get("sw") or e.get("ds") or "")[:200],
            "url": e.get("u"),
        })

    print(f"gen_ldjson : {len(candidats)} candidats à venir notés -> {len(top)} retenus")
    if top:
        print(f"  meilleure note : {candidats[0][0]} — {top[0]['n'][:60]}")
        print(f"  {len(top)}e note : {candidats[len(top) - 1][0]}")

    if not a.apply:
        print("(essai à blanc — rien n'a été écrit ; --apply pour appliquer)")
        return

    ml = re.search(r'(<script type="application/ld\+json">)(.*?)(</script>)', html, re.S)
    new_ld = json.dumps({"@context": "https://schema.org", "@graph": graph},
                         ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    new_html = html[:ml.start(2)] + new_ld + html[ml.end(2):]
    open(FULL, "w", encoding="utf-8").write(new_html)
    print(f"{FULL} mis à jour ({len(graph)} événements dans le graphe).")


if __name__ == "__main__":
    main()
