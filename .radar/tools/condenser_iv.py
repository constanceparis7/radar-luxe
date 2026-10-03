#!/usr/bin/env python3
"""Applique des condensations de iv.o / iv.g / iv.w sans perdre un fait.

Usage : python3 .radar/tools/condenser_iv.py lot.json [--appliquer]
lot.json : [{"n": "<nom exact>", "o": "...", "g": "...", "w": "...", "ok_perdus": ["jeton accepté perdu"]}]
Contrôle : tout e-mail, téléphone, URL/domaine, montant, horaire, date et nombre
présent dans l'ancien texte doit figurer dans le nouveau, sauf jeton listé dans
ok_perdus (périmé ou doublon, à justifier dans le compte rendu). Les traductions
iv_* du champ modifié sont retirées (repli français exact), règle de cohérence.
"""
import json, re, sys
TOK = re.compile(r"[\w.+-]+@[\w.-]+\.\w+|https?://\S+|\b(?:[\w-]+\.)+(?:com|fr|it|ch|org|net|eu|uk|au|ma|es)\b[/\w.-]*|\+?\d[\d ()./-]{6,}\d|\d+(?:[.,]\d+)?\s?(?:€|AUD|CHF|\$|£)|\d{1,2}h\d{0,2}|\d{1,2}/\d{1,2}(?:/\d{2,4})?|\b\d{3,}\b")
def jetons(t):
    return {re.sub(r"[ ().-]", "", x).rstrip(".,;:)") for x in TOK.findall(t or "")}
def main():
    lot = json.load(open(sys.argv[1], encoding="utf-8"))
    html = open("index-full.html", encoding="utf-8").read()
    m = re.search(r'(<script[^>]*id="data"[^>]*>)(.*?)(</script>)', html, re.S)
    ev = json.loads(m.group(2).replace("<\\/", "</"))
    par = {e["n"]: e for e in ev}
    bon = True
    for it in lot:
        c = [x for x in ev if x["n"] == it["n"]] or [x for x in ev if x["n"].startswith(it["n"])]
        e = c[0] if len(c) == 1 else None
        if e: it["n"] = e["n"]
        if not e:
            print("INTROUVABLE", it["n"]); bon = False; continue
        ok = {re.sub(r"[ ().-]", "", x) for x in it.get("ok_perdus", [])}
        for k in "ogw":
            if k not in it: continue
            ancien, neuf = e["iv"].get(k) or "", it[k]
            perdus = {j for j in jetons(ancien) - jetons(neuf) if not any(j in o or o in j for o in ok)}
            # un jeton retrouvé sous une autre écriture dans le texte brut n'est pas perdu
            brut = re.sub(r"[ ().-]", "", neuf)
            perdus = {j for j in perdus if j not in brut}
            print(f"{it['n'][:48]:48} {k} {len(ancien):4d} -> {len(neuf):4d}", "PERDUS:" if perdus else "ok", sorted(perdus) if perdus else "")
            if perdus: bon = False
            if "—" in neuf or "–" in neuf: print("  tiret long !"); bon = False
    if not bon: sys.exit("⛔ refus : corriger le lot")
    if "--appliquer" not in sys.argv: print("(essai, rien écrit)"); return
    for it in lot:
        e = par[it["n"]]
        for k in "ogw":
            if k in it:
                e["iv"][k] = it[k]
                for l, tr in (e.get("tr") or {}).items():
                    if isinstance(tr, dict): tr.pop("iv_" + k, None)
    neuf = json.dumps(ev, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    open("index-full.html", "w", encoding="utf-8").write(html[:m.start(2)] + neuf + html[m.end(2):])
    print("✓ index-full.html réécrit")
main()
