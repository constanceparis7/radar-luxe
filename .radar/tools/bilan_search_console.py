#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""bilan_search_console.py : lecture d'un export Search Console (dossier contenant
Pages.csv, Requêtes.csv, Pays.csv, Appareils.csv, tel que téléchargé depuis
« Performances » avec le bouton Exporter) et bilan en quelques nombres :

  - totaux (clics, impressions, taux de clic, position) ;
  - taux de clic par famille de pages (accueil, fiches, lieux, catégories, questions,
    guides, autres) et par langue de page ;
  - part des impressions servies hors français, et estimation de la langue de la
    demande d'après les requêtes (mots français / anglais / autres) ;
  - la matrice d'intentions (.radar/MATRICE-INTENTIONS.md) : pour « paris fashion
    week », « milan fashion week », « vogue world », quelles pages reçoivent les
    impressions, et dans quelle langue ;
  - comparaison avec le bilan précédent s'il existe.

Écrit .radar/journal/search-console-<date>.json (résumé seulement, jamais l'export brut).
Usage : python3 .radar/tools/bilan_search_console.py "<dossier de l'export>" [AAAA-MM-JJ]
"""
import csv, glob, json, os, re, sys
import datetime as dt

REPO = os.environ.get("RADAR_REPO") or os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LANGS = {"en", "es", "it", "pt", "de", "ru", "ar", "zh", "ja", "ko", "hi", "tr"}
FR_MOTS = re.compile(r"\b(événements?|evenements?|comment|entrer|soirée|soirees?|janvier|février|fevrier|mars|avril|mai|juin|juillet|août|aout|septembre|octobre|novembre|décembre|decembre|billets?|réserver|reserver|dates?|programme|défilé|defile)\b", re.I)
EN_MOTS = re.compile(r"\b(events?|how|get in|tickets?|january|february|march|april|june|july|august|september|october|november|december|schedule|dates?|party|parties|gala)\b", re.I)


def lire(dossier, nom):
    p = os.path.join(dossier, nom)
    if not os.path.exists(p):
        return []
    rows = []
    with open(p, encoding="utf-8-sig", newline="") as f:
        r = csv.reader(f)
        head = next(r, None)
        for row in r:
            if len(row) < 5:
                continue
            try:
                rows.append({"k": row[0], "clics": int(row[1]), "imp": int(row[2]),
                             "ctr": float(row[3].replace("%", "").replace(",", ".")), "pos": float(row[4].replace(",", "."))})
            except ValueError:
                continue
    return rows


def famille(url):
    p = url.replace("https://constanceparis7.com", "")
    seg = p.strip("/").split("/")
    if seg and seg[0] in LANGS:
        seg = seg[1:]
    if not seg or seg == [""] or p.rstrip("/") in ("", "/" + "/".join(seg)) and (not seg or seg[0] == ""):
        return "accueil"
    if not seg:
        return "accueil"
    if seg[0] == "e":
        return "fiche"
    if seg[0] == "lieu":
        return "lieu"
    if seg[0] == "type":
        return "categorie"
    if seg[0] == "q":
        return "question"
    if seg[0] in ("moments", "protocole"):
        return "guide"
    if seg[0].endswith(".html") and seg[0].replace(".html", "") in ("paris-fashion-week", "milano-fashion-week", "prix-de-larc-de-triomphe", "evenements", "entrer", "note", "methode"):
        return "guide"
    return "autre"


def langue(url):
    p = url.replace("https://constanceparis7.com", "").strip("/").split("/")
    return p[0] if p and p[0] in LANGS else "fr"


def agg(rows, cle):
    out = {}
    for r in rows:
        k = cle(r["k"])
        o = out.setdefault(k, {"clics": 0, "imp": 0, "pages": 0})
        o["clics"] += r["clics"]; o["imp"] += r["imp"]; o["pages"] += 1
    for o in out.values():
        o["ctr"] = round(100 * o["clics"] / o["imp"], 2) if o["imp"] else 0.0
    return dict(sorted(out.items(), key=lambda kv: -kv[1]["imp"]))


def main():
    dossier = sys.argv[1]
    jour = sys.argv[2] if len(sys.argv) > 2 else (re.search(r"(\d{4}-\d{2}-\d{2})", dossier) or [None, dt.date.today().isoformat()])[1]
    pages, req, pays, app = lire(dossier, "Pages.csv"), lire(dossier, "Requêtes.csv"), lire(dossier, "Pays.csv"), lire(dossier, "Appareils.csv")
    tot_c, tot_i = sum(r["clics"] for r in pages), sum(r["imp"] for r in pages)
    bilan = {
        "date": jour, "source": os.path.basename(dossier.rstrip("/")),
        "totaux": {"clics": tot_c, "impressions": tot_i, "ctr": round(100 * tot_c / tot_i, 2) if tot_i else 0, "pages": len(pages), "requetes": len(req)},
        "par_famille": agg(pages, famille),
        "par_langue": agg(pages, langue),
        "appareils": {r["k"]: {"clics": r["clics"], "imp": r["imp"], "ctr": r["ctr"]} for r in app},
        "pays_top": [{"pays": r["k"], "clics": r["clics"], "imp": r["imp"], "ctr": r["ctr"]} for r in pays[:8]],
    }
    hors_fr = sum(v["imp"] for k, v in bilan["par_langue"].items() if k != "fr")
    bilan["part_impressions_hors_fr"] = round(100 * hors_fr / tot_i, 1) if tot_i else 0
    fr_q = sum(r["imp"] for r in req if FR_MOTS.search(r["k"]))
    en_q = sum(r["imp"] for r in req if EN_MOTS.search(r["k"]) and not FR_MOTS.search(r["k"]))
    tq = sum(r["imp"] for r in req) or 1
    bilan["demande_estimee"] = {"francais_pct": round(100 * fr_q / tq, 1), "anglais_pct": round(100 * en_q / tq, 1), "autre_pct": round(100 * (tq - fr_q - en_q) / tq, 1)}
    # matrice d'intentions : quelles pages reçoivent les impressions
    matrice = {}
    for intent, motifs in (("paris fashion week", ("paris-fashion-week",)), ("milan fashion week", ("milano-fashion-week", "milan-fashion-week")), ("vogue world", ("vogue-world",))):
        hits = [r for r in pages if any(m in r["k"] for m in motifs)]
        hits.sort(key=lambda r: -r["imp"])
        matrice[intent] = [{"page": r["k"].replace("https://constanceparis7.com", ""), "langue": langue(r["k"]), "famille": famille(r["k"]), "clics": r["clics"], "imp": r["imp"], "ctr": r["ctr"], "pos": r["pos"]} for r in hits[:6]]
        matrice[intent + " · requetes"] = [{"q": r["k"], "clics": r["clics"], "imp": r["imp"], "ctr": r["ctr"], "pos": r["pos"]} for r in req if intent.split()[0] in r["k"].lower() and ("fashion" in r["k"].lower() or "vogue" in r["k"].lower())][:6]
    bilan["matrice"] = matrice
    bilan["top_pages"] = [{"page": r["k"].replace("https://constanceparis7.com", ""), "clics": r["clics"], "imp": r["imp"], "ctr": r["ctr"], "pos": r["pos"]} for r in sorted(pages, key=lambda r: -r["clics"])[:10]]
    bilan["top_requetes"] = [{"q": r["k"], "clics": r["clics"], "imp": r["imp"], "ctr": r["ctr"], "pos": r["pos"]} for r in sorted(req, key=lambda r: -r["clics"])[:12]]
    # comparaison avec le bilan précédent
    os.makedirs(os.path.join(REPO, ".radar", "journal"), exist_ok=True)
    prev = sorted(glob.glob(os.path.join(REPO, ".radar", "journal", "search-console-*.json")))
    prev = [p for p in prev if jour not in p]
    if prev:
        a = json.load(open(prev[-1], encoding="utf-8"))
        bilan["comparaison"] = {"avec": a["date"], "ctr_total": [a["totaux"]["ctr"], bilan["totaux"]["ctr"]],
                                "ctr_lieu": [a["par_famille"].get("lieu", {}).get("ctr"), bilan["par_famille"].get("lieu", {}).get("ctr")],
                                "ctr_categorie": [a["par_famille"].get("categorie", {}).get("ctr"), bilan["par_famille"].get("categorie", {}).get("ctr")],
                                "part_hors_fr": [a["part_impressions_hors_fr"], bilan["part_impressions_hors_fr"]]}
    out = os.path.join(REPO, ".radar", "journal", f"search-console-{jour}.json")
    json.dump(bilan, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    t = bilan["totaux"]
    print(f"bilan Search Console du {jour} : {t['clics']} clics, {t['impressions']} impressions, CTR {t['ctr']} %, {t['pages']} pages, {t['requetes']} requêtes")
    for k, v in bilan["par_famille"].items():
        print(f"  {k:10s} {v['pages']:4d} pages  {v['imp']:6d} imp  {v['clics']:4d} clics  CTR {v['ctr']} %")
    print(f"  impressions hors français : {bilan['part_impressions_hors_fr']} % ; demande estimée : FR {bilan['demande_estimee']['francais_pct']} %, EN {bilan['demande_estimee']['anglais_pct']} %")
    for intent in ("paris fashion week", "milan fashion week", "vogue world"):
        print(f"  {intent} :", "; ".join(f"{h['langue']} {h['famille']} {h['imp']} imp/{h['clics']} clics" for h in bilan["matrice"][intent][:4]) or "aucune page")
    if "comparaison" in bilan:
        print("  comparaison :", bilan["comparaison"])
    print(f"  -> {os.path.relpath(out, REPO)}")


if __name__ == "__main__":
    main()
