#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""controle_collision.py — le premier produit (décision du 02/10/2026) : pour une
fenêtre de dates et une ou plusieurs villes, le rapport des événements vérifiés qui
se chevauchent, leurs fenêtres d'action documentées, les dates qui ont bougé, et
les créneaux moins encombrés. Lit les données du radar telles qu'elles sont ; il
n'invente rien et il dit ce qu'il ne voit pas.

Sources lues :
  - index-full.html (bloc data) : fiches, voie d'entrée, source, « vérifié le »
  - api/evenements.json : note du radar et adresses publiques
  - .radar/memoire.ndjson : dates qui ont bougé, fenêtres annoncées, complets
  - .radar/fenetres.json : registre des fenêtres d'action (ouvertures, clôtures),
    constitué par lecture des sources officielles ; absent = aucune fenêtre connue

Usage :
  python3 .radar/tools/controle_collision.py --villes Paris --debut 2026-11-01 \
      --fin 2026-11-30 --sortie rapport.html [--autour 10] [--titre "..."] [--client "..."]
Aucune écriture dans les données du site.
"""
import argparse
import datetime as dt
import html
import json
import os
import re

REPO = os.environ.get("RADAR_REPO") or os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RXV = re.compile(r"(?:v[ée]rifi\w*|contr[oô]l[ée]\w*|checked)[^0-9]{0,30}?(\d{1,2}/\d{1,2}/\d{4})", re.I)
MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
JOURS = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
ACCES = {"public": "public", "inscription": "sur inscription", "mixte": "mixte", "invitation": "sur invitation", "vip": "VIP", "prive": "privé"}
STATUT = {"confirme": "confirmé", "probable": "probable", "averifier": "à vérifier"}


def d(s):
    return dt.date.fromisoformat(s[:10]) if s else None


def fr(x):
    return f"{x.day} {MOIS[x.month - 1]} {x.year}"


def fr_court(x):
    return f"{JOURS[x.weekday()]} {x.day} {MOIS[x.month - 1]}"


def esc(s):
    return html.escape(str(s if s is not None else ""), quote=True)


def date_verif(e):
    textes = [str(e.get("so") or "")] + [str(v) for v in (e.get("iv") or {}).values() if isinstance(v, str)]
    meilleurs = []
    for tx in textes:
        for m in RXV.finditer(tx):
            j, mo, a = m.group(1).split("/")
            try:
                meilleurs.append(dt.date(int(a), int(mo), int(j)))
            except ValueError:
                pass
    return max(meilleurs) if meilleurs else None


def charger():
    raw = open(os.path.join(REPO, "index-full.html"), encoding="utf-8").read()
    i = raw.find('id="data"'); j = raw.find(">", i) + 1; k = raw.find("</script>", j)
    txt = raw[j:k]
    ev = json.loads(txt[txt.find("["):txt.rfind("]") + 1].replace("<\\/", "</"))
    api = {}
    p = os.path.join(REPO, "api", "evenements.json")
    if os.path.exists(p):
        for x in json.load(open(p, encoding="utf-8"))["evenements"]:
            api[x["nom"]] = x
    mem = []
    p = os.path.join(REPO, ".radar", "memoire.ndjson")
    if os.path.exists(p):
        mem = [json.loads(l) for l in open(p, encoding="utf-8") if l.strip()]
    fen = []
    p = os.path.join(REPO, ".radar", "fenetres.json")
    if os.path.exists(p):
        fen = json.load(open(p, encoding="utf-8")).get("fenetres", [])
    return ev, api, mem, fen


def dans_villes(e, villes):
    v = (e.get("v") or "").strip().lower()
    return any(w.strip().lower() == v for w in villes)


def permanent(e):
    """Fiches-guides (« POINT D'ENTRÉE ») et saisons de plus de 180 jours : des voies
    permanentes, pas des rendez-vous ; elles n'entrent pas dans un contrôle de dates."""
    if (e.get("n") or "").startswith("POINT D'ENTRÉE"):
        return True
    return bool(e.get("d2")) and (d(e["d2"]) - d(e["d1"])).days > 180


def court(e):
    return (d(e.get("d2") or e["d1"]) - d(e["d1"])).days <= 14


def poids(e, note):
    duree = (d(e["d2"]) - d(e["d1"])).days + 1 if e.get("d2") else 1
    k = 1.0 if duree <= 7 else (0.35 if duree <= 14 else 0.15)
    return (note or 50) / 100.0 * k


def rapport(villes, debut, fin, autour=10, titre=None, client=None):
    ev, api, mem, fen = charger()
    aujourd = dt.date.today()
    D0, D1 = d(debut), d(fin)
    vivants = [e for e in ev if e.get("d1") and (d(e.get("d2") or e["d1"]) >= aujourd) and not permanent(e)]
    dedans, orbite, ailleurs = [], [], []
    for e in vivants:
        a, b = d(e["d1"]), d(e.get("d2") or e["d1"])
        chev = a <= D1 and b >= D0
        if dans_villes(e, villes):
            if chev:
                dedans.append(e)
            elif a <= D1 + dt.timedelta(days=autour) and b >= D0 - dt.timedelta(days=autour):
                orbite.append(e)
        elif chev:
            n = (api.get(e["n"]) or {}).get("note_radar") or 0
            if n >= 88:
                ailleurs.append(e)
    for L in (dedans, orbite, ailleurs):
        L.sort(key=lambda e: (e["d1"], e.get("d2") or e["d1"]))
    note = lambda e: (api.get(e["n"]) or {}).get("note_radar")

    courts = [e for e in dedans if court(e)]; longs = [e for e in dedans if not court(e)]
    # charge par jour et créneaux
    jours = [D0 + dt.timedelta(days=i) for i in range((D1 - D0).days + 1)]
    charge = {}
    for jr in jours:
        charge[jr] = sum(poids(e, note(e)) for e in dedans if d(e["d1"]) <= jr <= d(e.get("d2") or e["d1"]))
    forts = [e for e in dedans if (note(e) or 0) >= 80 and (d(e.get("d2") or e["d1"]) - d(e["d1"])).days <= 7]
    jours_forts = set()
    for e in forts:
        a, b = d(e["d1"]), d(e.get("d2") or e["d1"])
        for i in range((b - a).days + 1):
            jours_forts.add(a + dt.timedelta(days=i))
    candidats = [jr for jr in jours if jr.weekday() <= 3 and jr not in jours_forts and jr >= aujourd]
    candidats.sort(key=lambda jr: (charge[jr], jr))
    creneaux = candidats[:3]
    charge_courte = {jr: sum(poids(e, note(e)) for e in dedans if court(e) and d(e["d1"]) <= jr <= d(e.get("d2") or e["d1"])) for jr in jours}
    charges = [jr for jr in sorted(jours, key=lambda jr: -charge_courte[jr]) if charge_courte[jr] > 0][:3]

    noms = {e["n"] for e in dedans + orbite}
    mouvements = [m for m in mem if m.get("evenement") in noms]
    mouvements.sort(key=lambda m: m.get("date", ""), reverse=True)
    fenetres = [f for f in fen if f.get("evenement") in noms]

    T = titre or f"Contrôle de collision · {', '.join(villes)} · du {fr(D0)} au {fr(D1)}"
    css = """
    body{font-family:Georgia,'Times New Roman',serif;color:#1c1b1f;background:#fff;margin:0;line-height:1.5}
    .page{max-width:860px;margin:0 auto;padding:36px 28px 60px}
    h1{font-family:Didot,'Bodoni MT','Cormorant Garamond',Georgia,serif;font-weight:500;font-size:34px;line-height:1.1;margin:0 0 6px}
    h2{font-family:Didot,'Bodoni MT',Georgia,serif;font-weight:500;font-size:24px;margin:34px 0 10px;border-top:1px solid #d8d5cb;padding-top:16px}
    .eyebrow{font-family:Helvetica,Arial,sans-serif;font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:#7a786f;margin:0 0 10px}
    p{margin:0 0 10px;max-width:70ch}.lim{background:#f4f3ee;border-left:3px solid #9c8249;padding:10px 14px;margin:14px 0}
    table{border-collapse:collapse;width:100%;font-size:13.5px;font-family:Helvetica,Arial,sans-serif}
    th,td{text-align:left;vertical-align:top;padding:7px 8px;border-bottom:1px solid #e8e6de}
    th{font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:#7a786f;border-bottom:1px solid #d8d5cb}
    td.n{text-align:right;white-space:nowrap;font-variant-numeric:tabular-nums}
    .tag{display:inline-block;font-size:11px;padding:1px 6px;border:1px solid #d8d5cb;border-radius:3px;color:#4a4944;white-space:nowrap}
    .ok{border-color:#1f5c4a;color:#1f5c4a}.mid{border-color:#9c8249;color:#8a6d2a}.bad{border-color:#8c2f2f;color:#8c2f2f}
    .cre{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin:10px 0}
    .cre div{border:1px solid #d8d5cb;padding:10px 12px;font-family:Helvetica,Arial,sans-serif;font-size:13.5px}
    .cre b{display:block;font-size:15px;margin-bottom:4px}
    a{color:#1f5c4a}.small{font-size:12.5px;color:#4a4944}
    footer{margin-top:40px;border-top:1px solid #d8d5cb;padding-top:12px;font-size:12px;color:#7a786f;font-family:Helvetica,Arial,sans-serif}
    @media print{.page{padding:0}h2{page-break-after:avoid}table{page-break-inside:auto}tr{page-break-inside:avoid}}
    """
    o = []
    o.append(f"<!doctype html><html lang='fr'><head><meta charset='utf-8'><meta name='robots' content='noindex'><meta name='viewport' content='width=device-width,initial-scale=1'><title>{esc(T)}</title><style>{css}</style></head><body><div class='page'>")
    o.append(f"<p class='eyebrow'>ConstanceParis7 · rapport établi le {fr(aujourd)}" + (f" · pour {esc(client)}" if client else "") + "</p>")
    o.append(f"<h1>{esc(T)}</h1>")
    o.append("<p>Les événements du luxe vérifiés à leur source officielle qui se chevauchent sur cette fenêtre, ce qui tourne autour, les fenêtres d'action publiées, les dates qui ont bougé, et les créneaux moins encombrés.</p>")
    o.append("<div class='lim'><p><b>Ce que ce rapport ne voit pas.</b> Le radar ne recense que le calendrier public : les présentations et dîners privés des maisons n'y figurent jamais. Sa couverture est le luxe et la culture de prestige, pas tout ce qui se passe dans la ville. Un événement absent d'ici n'est pas un événement qui n'existe pas. Chaque ligne porte sa source officielle et la date à laquelle elle a été relue.</p></div>")

    # 1. vue d'ensemble
    nb = len(dedans)
    cf = {k: sum(1 for e in dedans if e.get("cf") == k) for k in ("confirme", "probable", "averifier")}
    o.append("<h2>1 · Vue d'ensemble</h2>")
    o.append(f"<p>{nb} événement{'s' if nb > 1 else ''} du radar dans la fenêtre, dont {len(courts)} rendez-vous daté{'s' if len(courts) > 1 else ''} et {len(longs)} exposition{'s' if len(longs) > 1 else ''} ou saison{'s' if len(longs) > 1 else ''} en cours : {cf['confirme']} confirmé{'s' if cf['confirme'] > 1 else ''}, {cf['probable']} probable{'s' if cf['probable'] > 1 else ''}, {cf['averifier']} à vérifier. {len(orbite)} en orbite dans les {autour} jours autour. {len(ailleurs)} rendez-vous majeur{'s' if len(ailleurs) > 1 else ''} ailleurs dans le monde sur la même période.</p>")
    if charges:
        o.append("<p><b>Les jours les plus chargés</b> : " + " ; ".join(f"{fr_court(jr)} ({', '.join(e['n'].split(',')[0] for e in courts if d(e['d1']) <= jr <= d(e.get('d2') or e['d1']))[:160] or 'expositions en cours seulement'})" for jr in charges if charge[jr] > 0) + ".</p>")
    o.append("<p><b>Les créneaux moins encombrés</b> (du lundi au jeudi, hors jours d'un rendez-vous majeur, selon ce que le radar voit) :</p><div class='cre'>")
    for jr in creneaux:
        encours = [e["n"].split(",")[0] for e in courts if d(e["d1"]) <= jr <= d(e.get("d2") or e["d1"])]
        nlong = sum(1 for e in longs if d(e["d1"]) <= jr <= d(e.get("d2") or e["d1"]))
        txt = ("Ce jour-là : " + "; ".join(encours)[:140]) if encours else ("Aucun rendez-vous daté" + (f", {nlong} exposition{'s' if nlong > 1 else ''} ou saison{'s' if nlong > 1 else ''} en cours" if nlong else ""))
        o.append(f"<div><b>{esc(fr_court(jr))}</b>{esc(txt)}</div>")
    if not creneaux:
        o.append("<div>Aucun créneau du lundi au jeudi sans rendez-vous majeur dans la fenêtre.</div>")
    o.append("</div>")

    # 2. tableau
    def ligne(e, orb=False):
        a = api.get(e["n"]) or {}
        dv = date_verif(e)
        tag = {"confirme": "ok", "probable": "mid", "averifier": "bad"}.get(e.get("cf"), "")
        return (f"<tr><td class='n'>{esc(e['d1'][8:10])}/{esc(e['d1'][5:7])}" + (f"<br>au {esc(e['d2'][8:10])}/{esc(e['d2'][5:7])}" if e.get("d2") and e["d2"] != e["d1"] else "") + "</td>"
                f"<td><b>{esc(e['n'])}</b><br><span class='small'>{esc(e.get('l') or e.get('v'))}</span></td>"
                f"<td>{esc(ACCES.get(e.get('a'), e.get('a')))}</td><td><span class='tag {tag}'>{esc(STATUT.get(e.get('cf'), e.get('cf')))}</span></td>"
                f"<td class='n'>{esc(a.get('note_radar') or '')}</td><td class='small'>{esc(dv.strftime('%d/%m/%Y')) if dv else 'non datée'}</td>"
                f"<td class='small'><a href='{esc(e.get('u'))}'>source</a></td></tr>")
    o.append("<h2>2 · Dans la fenêtre</h2>")
    if courts:
        o.append("<p><b>Les rendez-vous datés</b></p><table><tr><th>Dates</th><th>Événement</th><th>Accès</th><th>Statut</th><th>Note</th><th>Relu le</th><th></th></tr>" + "".join(ligne(e) for e in courts) + "</table>")
    else:
        o.append("<p>Aucun rendez-vous daté du radar dans cette fenêtre pour ces villes.</p>")
    if longs:
        o.append("<p><b>Les expositions et saisons en cours</b> (elles occupent les lieux et les agendas, sans mobiliser un soir précis)</p><table><tr><th>Dates</th><th>Événement</th><th>Accès</th><th>Statut</th><th>Note</th><th>Relu le</th><th></th></tr>" + "".join(ligne(e) for e in longs) + "</table>")
    o.append("<p class='small'>La note du radar (sur 100) suit le barème public : exclusivité de l'accès, personnalités attendues, lieu, proximité de la date.</p>")
    if orbite:
        o.append(f"<h2>3 · En orbite, {autour} jours avant et après</h2><table><tr><th>Dates</th><th>Événement</th><th>Accès</th><th>Statut</th><th>Note</th><th>Relu le</th><th></th></tr>" + "".join(ligne(e, True) for e in orbite) + "</table>")
    if ailleurs:
        o.append("<h2>Ailleurs, la même période</h2><p class='small'>Les rendez-vous les mieux notés du radar hors de ces villes : ils déplacent la presse et les clients.</p><table><tr><th>Dates</th><th>Événement</th><th>Accès</th><th>Statut</th><th>Note</th><th>Relu le</th><th></th></tr>" + "".join(ligne(e) for e in ailleurs) + "</table>")

    # 4. fenêtres d'action
    o.append("<h2>4 · Fenêtres d'action documentées</h2>")
    if fenetres:
        o.append("<table><tr><th>Événement</th><th>Action</th><th>Ouverture</th><th>Clôture</th><th>Éligibilité</th><th>Lu le</th><th></th></tr>")
        for f in fenetres:
            st = f.get("statut", "")
            o.append(f"<tr><td><b>{esc(f.get('evenement'))}</b></td><td>{esc(f.get('type'))}<br><span class='tag'>{esc(st)}</span></td><td>{esc(f.get('ouverture') or 'non publiée')}{(' ' + esc(f.get('heure'))) if f.get('heure') else ''}</td><td>{esc(f.get('cloture') or 'non publiée')}</td><td class='small'>{esc(f.get('eligibilite'))}</td><td class='small'>{esc(f.get('verifie_le'))}</td><td class='small'><a href='{esc(f.get('url') or f.get('page'))}'>page</a></td></tr>")
        o.append("</table>")
    sans = [e for e in dedans + orbite if e["n"] not in {f.get("evenement") for f in fenetres}]
    if sans:
        o.append("<p class='small'><b>Aucune fenêtre publiée au " + esc(fr(aujourd)) + "</b> pour : " + esc(" ; ".join(e["n"].split(",")[0] for e in sans)) + ". Pour ces événements, la voie d'entrée connue est celle de la fiche (source en colonne), sans date d'ouverture ni de clôture publiée.</p>")

    # 5. mouvements
    o.append("<h2>5 · Ce qui a bougé</h2>")
    if mouvements:
        o.append("<table><tr><th>Date</th><th>Événement</th><th>Mouvement</th><th>Preuve</th></tr>" + "".join(f"<tr><td class='n'>{esc(m.get('date'))}</td><td>{esc(m.get('evenement'))}</td><td>{esc(m.get('detail'))}</td><td class='small'>{esc(m.get('preuve'))[:160]}</td></tr>" for m in mouvements) + "</table>")
    else:
        o.append("<p>Aucun mouvement de date enregistré par la Mémoire du radar sur ces événements.</p>")

    # 6. calendrier par semaine
    o.append("<h2>6 · Calendrier</h2>")
    sem = {}
    for e in dedans + orbite:
        a = max(d(e["d1"]), D0 - dt.timedelta(days=autour))
        s = a - dt.timedelta(days=a.weekday())
        sem.setdefault(s, []).append(e)
    for s in sorted(sem):
        o.append(f"<p><b>Semaine du {esc(fr_court(s))}</b></p><ul>")
        for e in sorted(sem[s], key=lambda e: e["d1"]):
            long_ = (d(e.get("d2") or e["d1"]) - d(e["d1"])).days > 14
            o.append(f"<li>{esc(e['dt'] or e['d1'])} : {esc(e['n'])}{' (en cours)' if long_ else ''} · <span class='tag'>{esc(STATUT.get(e.get('cf'), ''))}</span></li>")
        o.append("</ul>")

    # 7. méthode
    o.append("<h2>7 · Méthode</h2><p>Chaque événement a été pris sur la page officielle de son organisateur, puis daté. « Confirmé » veut dire lu tel quel sur la source ; « probable », annoncé mais pas encore détaillé ; « à vérifier », une incertitude inscrite plutôt qu'une certitude inventée. Les dates de fin sont lues, jamais posées par défaut. Les coordonnées données sont des lignes de service, jamais une personne. Une place dans le radar ne s'achète pas : ce rapport analyse le calendrier, il ne le modifie pas.</p>")
    o.append(f"<footer>ConstanceParis7 · le radar des événements du luxe · {esc(fr(aujourd))} · ce rapport est fourni tel quel, sans promesse d'accès ni d'invitation.</footer></div></body></html>")
    return "\n".join(o), {"dedans": len(dedans), "orbite": len(orbite), "ailleurs": len(ailleurs), "fenetres": len(fenetres), "mouvements": len(mouvements), "creneaux": [c.isoformat() for c in creneaux]}


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--villes", required=True, help="villes séparées par des virgules")
    ap.add_argument("--debut", required=True); ap.add_argument("--fin", required=True)
    ap.add_argument("--autour", type=int, default=10); ap.add_argument("--titre"); ap.add_argument("--client")
    ap.add_argument("--sortie", required=True)
    a = ap.parse_args()
    h, stats = rapport([v.strip() for v in a.villes.split(",")], a.debut, a.fin, a.autour, a.titre, a.client)
    open(a.sortie, "w", encoding="utf-8").write(h)
    print(json.dumps(stats, ensure_ascii=False))
