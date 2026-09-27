#!/usr/bin/env python3
"""Contrôle mécanique de non-perte de faits pour une traduction JSON par lots.

Compare deux listes JSON de questions/fiches appariées par "slug" (ou par
index si "slug" absent) : e-mails, URLs, téléphones et montants du texte
source doivent tous se retrouver dans le texte traduit (une traduction ne
doit RIEN inventer ni perdre — leçon du 20/08/2026, verif_faits.py). Ne
remplace jamais la lecture humaine des alertes : les signale seulement.

Usage :
    python3 verif_traduction.py source.json traduit.json [clé1 clé2 ...]

Les clés de texte à comparer par défaut : question, reponse_courte, details.
"""
import json
import re
import sys

EMAIL = re.compile(r'[\w.+-]+@[\w-]+(?:\.[\w-]+)+')
URL = re.compile(r'https?://[^\s)\]"\'>,]+')
# Bornée : un numéro ne traverse jamais une fin de phrase (point suivi d'espace+majuscule/chiffre isolé).
PHONE = re.compile(r'(?:\+?\d[\d .\-()]{5,18}\d)(?!\d)')
AMOUNT = re.compile(
    r'\d[\d .,]*\s?(?:€|\$|EUR|USD|CHF|AUD|MAD|fr\.|francs?|dirhams?|avro)',
    re.IGNORECASE,
)


def norm_phone(s):
    return re.sub(r'\D', '', s)[-9:]


def norm_amount(s):
    digits = re.sub(r'\D', '', s)
    return digits.lstrip('0')


SENTENCE_SPLIT = re.compile(r'(?<=[.!?;])\s+(?=[A-ZÀ-ÖØ-Þ0-9])')


def collect(text):
    # Un numéro ne doit jamais être reconstruit à travers une fin de phrase
    # (piège du 27/09/2026 : "...2661. 15 Aralık..." lu comme un seul numéro).
    emails, urls, phones, amounts = set(), set(), set(), set()
    for sentence in SENTENCE_SPLIT.split(text):
        emails |= set(EMAIL.findall(sentence))
        urls |= set(URL.findall(sentence))
        phones |= {norm_phone(p) for p in PHONE.findall(sentence) if len(re.sub(r'\D', '', p)) >= 8}
        amounts |= {norm_amount(a) for a in AMOUNT.findall(sentence)}
    return {"emails": emails, "urls": urls, "phones": phones, "amounts": amounts}


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    src_path, dst_path = sys.argv[1], sys.argv[2]
    keys = sys.argv[3:] or ["question", "reponse_courte", "details"]

    src = json.load(open(src_path, encoding="utf-8"))
    dst = json.load(open(dst_path, encoding="utf-8"))
    dst_by_slug = {d.get("slug", i): d for i, d in enumerate(dst)}

    issues = []
    for i, s in enumerate(src):
        slug = s.get("slug", i)
        d = dst_by_slug.get(slug)
        if d is None:
            issues.append((slug, "ENTRÉE ABSENTE DE LA TRADUCTION"))
            continue
        s_text = " ".join(s.get(k, "") for k in keys)
        d_text = " ".join(d.get(k, "") for k in keys)
        s_facts = collect(s_text)
        d_facts = collect(d_text)
        missing = {k: (s_facts[k] - d_facts[k]) for k in s_facts}
        missing = {k: v for k, v in missing.items() if v}
        if missing:
            issues.append((slug, missing))

    if not issues:
        print(f"OK — {len(src)} entrées comparées, aucune perte de fait dur détectée.")
        return
    print(f"ALERTE — {len(issues)}/{len(src)} entrée(s) à relire à la main "
          f"(un fait dur du français est absent de la traduction, ou un artefact "
          f"de regex à écarter après lecture — voir lessons.md du 20-21/08/2026) :")
    for slug, m in issues:
        print(f"  - {slug} : {m}")


if __name__ == "__main__":
    main()
