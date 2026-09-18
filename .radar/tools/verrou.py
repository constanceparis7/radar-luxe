#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""LE VERROU : contrôle bloquant de build (chantier « aucun point faible », 17/09/2026).

Refuse la publication dès qu'une incohérence apparaît dans les fichiers GÉNÉRÉS,
dans n'importe laquelle des 13 langues. Appelé par validate.py (et exécutable seul).

Bloqueurs :
  V1  None / null / undefined / NaN / [object Object] dans title, meta description,
      og:*, twitter:*, ou h1 d'une page générée ; title vide ou séparateur sans libellé.
  V2  Marque saisonnière périmée (été 2026, summer 2026, cet été, this summer) dans les
      métadonnées des pages de structure (accueil, hubs, catégories, lieux, outils).
      Les pages fiches sont exemptées : un nom d'événement est un fait.
  V3  Page générée sans <title>, sans meta description ou sans canonical.
  V4  Donnée : d2 < d1 sur une fiche.
  V5  Compteurs : les nombres affichés sur les hubs divergent du bloc de données.
  V6  Lien interne cassé : href vers un fichier local inexistant.
  V7  URL du sitemap sans fichier correspondant.
  V8  JSON-LD illisible (parse impossible).
  V9  hreflang d'une fiche vers un fichier absent.
Avertissements (candidats à promotion une fois le corpus propre) :
  W1  Date écrite dans dt hors de la fenêtre machine [d1-2j, d2+2j].
  W2  Page sans h1.
"""
import json, os, re, sys, unicodedata
from datetime import date, timedelta

REPO = os.environ.get("RADAR_REPO") or os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LANGS = ["en","es","it","pt","de","ru","ar","zh","ja","ko","hi","tr"]
bloq, warn = [], []

def fichiers_generes():
    zones = ["", *[l+"/" for l in LANGS]]
    for z in zones:
        for dossier, _, fs in os.walk(os.path.join(REPO, z) if z else REPO):
            rel = os.path.relpath(dossier, REPO)
            # racine : ne pas redescendre dans les zones langues ni les outils
            if not z:
                premier = rel.split(os.sep)[0]
                if premier in LANGS or premier.startswith(".") or premier in ("node_modules",):
                    continue
            if any(p.startswith(".") for p in rel.split(os.sep)):
                continue
            for f in fs:
                if f.endswith(".html"):
                    yield os.path.join(dossier, f)
        if z:  # os.walk sur zone langue couvre déjà tout
            pass

def tous_les_html():
    vus = set()
    for dossier, dirs, fs in os.walk(REPO):
        rel = os.path.relpath(dossier, REPO)
        if rel == ".":
            rel = ""
        if any(p.startswith(".") or p == "node_modules" for p in rel.split(os.sep) if p):
            dirs[:] = []
            continue
        for f in fs:
            if f.endswith(".html"):
                p = os.path.join(dossier, f)
                if p not in vus:
                    vus.add(p)
                    yield p

RX_TITLE = re.compile(r"<title>(.*?)</title>", re.S)
RX_DESC = re.compile(r'name="description" content="([^"]*)"')
RX_META = re.compile(r'(?:property|name)="(?:og:|twitter:)[^"]*" content="([^"]*)"')
RX_H1 = re.compile(r"<h1[^>]*>(.*?)</h1>", re.S)
RX_CANON = re.compile(r'rel="canonical"')
RX_POISON = re.compile(r"\bNone\b|\bnull\b|\bundefined\b|\bNaN\b|\[object Object\]")
RX_SAISON = re.compile(r"été 2026|summer 2026|cet été|this summer", re.I)
RX_HREF = re.compile(r'href="(/[^"#?]*)"')
RX_LD = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.S)
RX_ALT = re.compile(r'rel="alternate"[^>]*href="https://constanceparis7\.com(/[^"]*)"')

def est_fiche(rel):
    return "/e/" in ("/" + rel.replace(os.sep, "/"))

def cible_existe(url):
    url = url.split("#")[0].split("?")[0]
    if not url or not url.startswith("/"):
        return True
    p = os.path.join(REPO, url.lstrip("/"))
    if url.endswith("/"):
        return os.path.isdir(p.rstrip("/")) and os.path.exists(os.path.join(p, "index.html")) or url == "/"
    if os.path.exists(p):
        return True
    return os.path.exists(p + ".html")

def controle_pages():
    n = 0
    for p in tous_les_html():
        rel = os.path.relpath(p, REPO)
        if os.path.basename(rel).startswith("google") and rel.endswith(".html"):
            continue  # fichiers de vérification Search Console : à garder tels quels
        h = open(p, encoding="utf-8", errors="replace").read()
        n += 1
        noindex = 'name="robots"' in h and "noindex" in h
        mt = RX_TITLE.search(h)
        titre = (mt.group(1).strip() if mt else "")
        desc = RX_DESC.search(h)
        metas = RX_META.findall(h)
        h1 = RX_H1.search(h)
        # V1
        champs = [("title", titre)] + ([("description", desc.group(1))] if desc else []) + \
                 [("og/twitter", m) for m in metas] + ([("h1", re.sub("<[^>]+>", "", h1.group(1)))] if h1 else [])
        for nom, val in champs:
            if RX_POISON.search(val or ""):
                bloq.append(f"V1 {rel} : {nom} empoisonné ({val[:80]!r})")
        if mt and (not titre or re.match(r"^[\s·:|-]+", titre)):
            bloq.append(f"V1 {rel} : title vide ou séparateur nu ({titre[:60]!r})")
        # V2 (pages de structure seulement)
        if not est_fiche(rel):
            for nom, val in champs:
                if RX_SAISON.search(val or ""):
                    bloq.append(f"V2 {rel} : saison périmée dans {nom} ({val[:80]!r})")
        # V3
        if not mt:
            bloq.append(f"V3 {rel} : pas de <title>")
        if not desc and not noindex and 'http-equiv="refresh"' not in h:
            bloq.append(f"V3 {rel} : pas de meta description")
        if not RX_CANON.search(h) and not noindex and 'http-equiv="refresh"' not in h:
            bloq.append(f"V3 {rel} : pas de canonical")
        if not h1 and 'http-equiv="refresh"' not in h and rel not in ("index.html", "google665df1b0964660cd.html") and not rel.endswith(os.sep + "index.html"):
            warn.append(f"W2 {rel} : pas de h1")
        # V6
        for u in set(RX_HREF.findall(h)):
            if not cible_existe(u):
                bloq.append(f"V6 {rel} : lien interne cassé vers {u}")
        # V8
        for m in RX_LD.finditer(h):
            try:
                json.loads(m.group(1).replace("<\\/", "</"))
            except Exception as ex:
                bloq.append(f"V8 {rel} : JSON-LD illisible ({ex})")
        # V9
        if est_fiche(rel):
            for u in set(RX_ALT.findall(h)):
                if not cible_existe(u):
                    bloq.append(f"V9 {rel} : hreflang vers fichier absent {u}")
    return n

MOIS = {"janvier":1,"février":2,"mars":3,"avril":4,"mai":5,"juin":6,"juillet":7,
        "août":8,"septembre":9,"octobre":10,"novembre":11,"décembre":12}
RX_DATE_FR = re.compile(r"\b(\d{1,2})(?:er)?\s+(" + "|".join(MOIS) + r")\s+(\d{4})\b", re.I)

def controle_donnees():
    h = open(os.path.join(REPO, "index.html"), encoding="utf-8").read()
    evts = json.loads(re.search(r'<script[^>]*id="data"[^>]*>(.*?)</script>', h, re.S).group(1))
    for e in evts:
        n = (e.get("n") or "")[:55]
        d1, d2 = e.get("d1"), e.get("d2")
        if d1 and d2 and d2 < d1:
            bloq.append(f"V4 fiche « {n} » : d2 {d2} avant d1 {d1}")
        # W1 : dates écrites dans dt vs fenêtre machine
        if d1 and e.get("dt"):
            try:
                a = date.fromisoformat(d1)
                b = date.fromisoformat(d2 or d1)
            except ValueError:
                continue
            fen = (a - timedelta(days=2), b + timedelta(days=2))
            trouvees = []
            for j, mois, an in RX_DATE_FR.findall(e["dt"]):
                try:
                    trouvees.append(date(int(an), MOIS[mois.lower()], int(j)))
                except ValueError:
                    pass
            if trouvees and not any(fen[0] <= t <= fen[1] for t in trouvees):
                warn.append(f"W1 fiche « {n} » : dates écrites {sorted(set(str(t) for t in trouvees))} hors fenêtre {d1}..{d2}")
    # V5 : compteurs affichés vs données
    notes = sum(1 for e in evts if e.get("sv") is not None)
    par_cat = {}
    for e in evts:
        par_cat[e.get("c", "autre")] = par_cat.get(e.get("c", "autre"), 0) + 1
    hub = os.path.join(REPO, "evenements.html")
    if os.path.exists(hub):
        hh = open(hub, encoding="utf-8").read()
        for m in re.finditer(r'/type/([a-z0-9-]+)\.html"[^>]*>[^<]*\((\d+)\)', hh):
            slug, nb = m.group(1), int(m.group(2))
            # correspondance slug -> compte reel : via la page categorie elle-meme
            page = os.path.join(REPO, "type", slug + ".html")
            if os.path.exists(page):
                pm = re.search(r'class="meta">(\d+) ', open(page, encoding="utf-8").read())
                if pm and int(pm.group(1)) != nb:
                    bloq.append(f"V5 hub ({nb}) vs page type/{slug} ({pm.group(1)}) : compteurs divergents")
    note_page = os.path.join(REPO, "note.html")
    if os.path.exists(note_page):
        nh = open(note_page, encoding="utf-8").read()
        m = re.search(r"(\d+)\s+événements not", nh)
        if m and int(m.group(1)) != notes:
            bloq.append(f"V5 note.html annonce {m.group(1)} événements notés, la base en compte {notes}")
    return len(evts)

def controle_hreflang_et_orphelines():
    """V10 : réciprocité des grappes hreflang des fiches. W3 : pages sans lien entrant."""
    import collections
    grappes = {}          # slug -> {langue: ensemble des alternates}
    entrants = collections.Counter()
    tous = set()
    for p in tous_les_html():
        rel = os.path.relpath(p, REPO).replace(os.sep, "/")
        if os.path.basename(rel).startswith("google"):
            continue
        h = open(p, encoding="utf-8", errors="replace").read()
        url = "/" + rel
        tous.add(url)
        for u in set(RX_HREF.findall(h)):
            u = u.split("#")[0].split("?")[0]
            if u and u != url:
                entrants[u] += 1
                if u.endswith("/"):
                    entrants[u + "index.html"] += 1
        if est_fiche(rel):
            alts = frozenset(RX_ALT.findall(h))
            slug = rel.split("/e/")[-1]
            grappes.setdefault(slug, {})[rel] = alts
    for slug, versions in grappes.items():
        jeux = set(versions.values())
        if len(jeux) > 1:
            bloq.append(f"V10 fiche {slug} : grappes hreflang divergentes entre langues "
                        f"({len(jeux)} jeux différents)")
        else:
            alts = next(iter(jeux))
            if alts and len(alts) < 13:
                bloq.append(f"V10 fiche {slug} : {len(alts)} alternates au lieu de 13")
    for u in sorted(tous):
        if u == "/index-full.html":
            continue  # source locale non versionnée (gitignore), jamais servie
        tete = open(os.path.join(REPO, u.lstrip("/")), encoding="utf-8", errors="replace").read()[:800]
        if entrants[u] == 0 and "/e/" not in u and not u.endswith("404.html") \
           and "http-equiv" not in tete and "noindex" not in tete:
            warn.append(f"W3 page sans aucun lien entrant : {u}")

def controle_sitemap():
    sm = os.path.join(REPO, "sitemap.xml")
    if not os.path.exists(sm):
        bloq.append("V7 sitemap.xml absent")
        return 0
    urls = re.findall(r"<loc>https://constanceparis7\.com(/[^<]*)</loc>", open(sm, encoding="utf-8").read())
    for u in urls:
        if not cible_existe(u):
            bloq.append(f"V7 sitemap : {u} sans fichier")
    return len(urls)

def main():
    os.chdir(REPO)
    npages = controle_pages()
    nevts = controle_donnees()
    nurls = controle_sitemap()
    controle_hreflang_et_orphelines()
    for b in bloq[:60]:
        print("BLOQUEUR ", b)
    if len(bloq) > 60:
        print(f"... et {len(bloq)-60} autres bloqueurs")
    for w in warn[:25]:
        print("AVERT    ", w)
    if len(warn) > 25:
        print(f"... et {len(warn)-25} autres avertissements")
    print(f"VERROU — {npages} pages, {nevts} fiches, {nurls} URLs de sitemap : "
          f"{len(bloq)} bloqueur(s), {len(warn)} avertissement(s)")
    sys.exit(1 if bloq else 0)

if __name__ == "__main__":
    main()
