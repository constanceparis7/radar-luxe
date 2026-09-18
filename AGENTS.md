# ConstanceParis7 · à lire avant tout travail

Toute intelligence artificielle qui travaille sur ce dépôt lit d'abord, dans l'ordre :

1. `.radar/REGLE-ALPHA.md` : le cadre fixé par l'éditrice le 18/09/2026 (site de niveau
   mondial, GitHub Pages, vitesse mobile impérative, aucun point faible, travail en
   équipe avec ChatGPT). Il prime sur toute demande ultérieure de contenu ou d'idée.
2. `.radar/FEUILLE-DE-ROUTE.md` : les neuf objectifs, leurs micro-objectifs et leur taux
   d'avancement, à tenir à jour dans le même commit que tout progrès.
3. `.radar/AUDIT-SANS-POINT-FAIBLE.md` : le registre des points faibles et leur état.
4. `.radar/DOCTRINE.md` : la doctrine technique et éditoriale (pipeline, verrou,
   règles de rédaction, routines).

Règles immédiates : `index-full.html` est la source (non versionnée, reconstruite par
`.radar/tools/rebuild_full.py`) ; on n'édite jamais `index.html` ni `i18n-data/` à la
main ; pipeline obligatoire avant tout push : `split_i18n.py --apply`, `gen_seo.py DATE`,
`gen_pages.py`, `validate.py` (verrou inclus, FAIL = ne pas pousser) ; aucun tiret long
dans les textes ; aucun fait, date ou adresse inventé ; jamais de force push ; la marque
affichée ne change pas sans l'accord de l'éditrice et de Gérald.
