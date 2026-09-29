#!/bin/zsh
# Contrôle hebdomadaire du lundi (doctrine 5ter, 29/09/2026), lancé par launchd sur la
# machine où Chrome est installé : vitesse mobile réelle (LCP, INP, CLS), validité HTML
# (validateur W3C) et accessibilité (axe-core) sur trois pages. Journalise dans
# .radar/tools/vitals-log.ndjson et .radar/tools/qualite-log.ndjson, puis pousse.
# Ne modifie jamais le site. Tout échec est journalisé, jamais bloquant.
set -u
export PATH="/usr/local/bin:/opt/homebrew/bin:/usr/bin:/bin:$PATH"
REPO="$HOME/radar-luxe"
cd "$REPO" || exit 0
git pull -q --ff-only origin main 2>/dev/null || true
JOUR=$(date +%F)
PAGES=("https://constanceparis7.com/" "https://constanceparis7.com/e/paris-fashion-week-pret-a-porter-printemps-ete-2027-paris.html" "https://constanceparis7.com/ar/")
python3 .radar/tools/mesure_cdp.py --log "${PAGES[@]}" >/dev/null 2>&1 || echo "{\"date\": \"$JOUR\", \"erreur\": \"mesure_cdp\"}" >> .radar/tools/vitals-log.ndjson
# validité HTML
for u in "${PAGES[@]}"; do
  n=$(curl -s "$u" | curl -s -H "Content-Type: text/html; charset=utf-8" -A "cp7-controle" --data-binary @- "https://validator.w3.org/nu/?out=json" \
      | python3 -c "import sys,json; d=json.load(sys.stdin); print(sum(1 for m in d.get('messages',[]) if m.get('type')=='error'))" 2>/dev/null || echo "?")
  echo "{\"date\": \"$JOUR\", \"controle\": \"w3c\", \"url\": \"$u\", \"erreurs\": \"$n\"}" >> .radar/tools/qualite-log.ndjson
  sleep 2
done
# accessibilité
python3 .radar/tools/audit_axe.py "${PAGES[@]}" 2>/dev/null | python3 -c "
import sys,json,re
url=None
for l in sys.stdin:
    if l.startswith('== '): url=l[3:].strip()
    m=re.search(r'violations : (\d+)',l)
    if m and url: print(json.dumps({'date':'$JOUR','controle':'axe','url':url,'violations':int(m.group(1))}))
" >> .radar/tools/qualite-log.ndjson 2>/dev/null || true
git add .radar/tools/vitals-log.ndjson .radar/tools/qualite-log.ndjson 2>/dev/null
git commit -qm "Contrôle du lundi (automatique) : vitesse mobile, validité HTML, accessibilité" 2>/dev/null && git push -q origin main 2>/dev/null || true
