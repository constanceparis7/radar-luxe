# Compte rendu — passe du 23/09/2026 (session cloud, rattrapage)

## Démarrage — anomalie de cadence

`precheck.sh` a signalé une cadence rompue (dernier run journalisé il y a 47 h,
> 30 h). Investigation : la session du 22/09 a bien démarré (`DEMARRAGE` dans
`passages.log`) mais n'a jamais poussé de `FIN` ni de compte rendu — seuls les
deux commits automatiques SANS IA (plancher `passe-quotidienne.yml` et
`surveillance.yml`) sont partis ce jour-là. Cause de l'arrêt non identifiable
depuis le dépôt (aucune trace d'erreur). Traité comme une passe de
RATTRAPAGE complète, conformément à la doctrine. `.radar/DOCTRINE.md`,
`.radar/PASSATION.md`, `.radar/REGLE-ALPHA.md` et `.radar/tools/lessons.md`
(1 212 lignes) lus intégralement avant tout travail. Clone superficiel
détecté et réparé (`git fetch --unshallow`).

## Purge et bascule de saison

6 zombies purgés (fin 23/08/2026, > 30 j) : Exposition Générale (nouvelle
Fondation), pop-up omakase Hatsune, 47e Festival La Versiliana, Prix Morny,
Hublot Polo Gold Cup Gstaad (44e édition), Regata Palermo-Montecarlo (21e).
332 → 326 événements. Liens des 118 événements les plus imminents retestés :
aucun mort. Bascule automatique de saison confirmée : **Autumn 2026** (le
badge et le titre indexé basculent tout seuls à l'équinoxe, `saison.py`) ;
les trois clés saisonnières de l'interface (`brandsub`, `intl_p1`,
`intl_p2`) ont été relues : leur contenu (« Septembre et octobre 2026 »)
reste factuellement exact pour la période en cours, aucune réécriture
nécessaire aujourd'hui — à surveiller quand novembre approchera.

## Correctif de fond : redirections de fiches vers un slug purgé = lien mort

La purge a fait apparaître 39 BLOQUEURS `V6` (lien interne cassé, 13 langues
× 3 pages) : les pages des deux événements venant d'être purgés (Hublot Polo
Gstaad, Versiliana) portaient chacune une ancienne redirection codée en dur
dans `gen_pages.py` (`FICHE_REDIRECTS`, héritée de la normalisation des lieux
du 17/09) vers un slug qui, en réalité, n'a **jamais** correspondu à une page
réellement générée — un slug fantôme resté invisible tant que la fiche
vivait sous son vrai nom. Corrigé à la source : `gen_pages.py` ne pointe
plus qu'une redirection dont la cible correspond à une fiche encore vivante ;
sinon elle renvoie vers le hub `evenements.html` de la langue. Détail et
règle générale consignés dans `lessons.md`. `validate.py` : 0 bloqueur après
correctif.

## Priorité du moment : condensation des voies d'invitation

Chantier en mode ENTRETIEN depuis le 21/09 (dernière lecture exhaustive :
zéro dérive réelle). Contrôle de non-régression ce jour : détecteur
automatique (motifs de dérive + sous-chaîne dupliquée > 60 car. entre
`iv.o`/`iv.g`/`iv.w`) sur les 76 fiches de la fenêtre live, puis lecture
intégrale des 13 candidates relevées (Shop on the Corner Saint-Tropez,
Negresco, Nikki Beach Ibiza, Loewe pop-up, Chaumet Vendôme, Amiri,
Dior Saint-Tropez, Melbourne Cup, ventes Sotheby's et Christie's Genève,
Fondazione Prada Venise, Airelles Courchevel, Alpina Gstaad). **Résultat :
zéro dérive.** Tout l'excédent est de la densité factuelle légitime (noms,
fonctions, e-mails professionnels, tarifs, horaires réels et nombreux par
fiche) — y compris une phrase partagée entre deux champs de la fiche
Sotheby's Genève (formalités d'enchère), simple répétition naturelle du
sujet et non un artefact de rédaction. Conformément à la doctrine, aucune
fiche n'a été retouchée pour ne pas dégrader du contenu déjà sain.

## État de la LOI DU SITE (iv + séjour + traductions)

`reste.py` : traductions 326/326 (100 %), voies d'invitation 326/326
(100 %), séjours 320/326 — les 6 manquants sont les fiches-guide `c=acces`,
exemptées par la doctrine. **0 écart réel.** Joaillerie : 15 fiches en
fenêtre live (plancher de 10 largement tenu). Bandeau Ouvertures & délais :
3 entrées, aucune périmée (échéances 30/09, 15/10, 31/01/2027).
`memoire.py changements` : 0 nouvelle date à consigner cette semaine.

## Bascule de majorité (21/09/2026)

Vérifiée sur pièces : `gen_pages.py` (constante `MAJORITE = 2026-09-21`) a
bien basculé `mentions-legales.html` — la page ne nomme plus Gérald Lefebvre,
elle indique que l'identité de la directrice de la publication n'est pas
rendue publique (LCEN art. 6-III-2°) et a été communiquée à l'hébergeur.
Bascule automatique confirmée fonctionnelle, sans intervention.

## Recherche de nouveaux événements

Non entreprise cette passe : le temps disponible a été consacré au
rattrapage de cadence, à la purge et au correctif de lien mort (bloquant
pour toute publication), conformément à l'ordre de priorité de la doctrine
(entretien et filet avant recherche). Rien de nouveau n'a donc été ajouté ;
c'est un résultat honnête, pas un renoncement à la mission.

## Analyse des visites

GoatCounter : 3 119 visiteurs/pages vues cumulés, contre 3 094 hier
(22/09) et 3 000 avant-hier (21/09) — croissance qui se poursuit, palier 1
de la feuille de route (35-100/jour), rien d'anormal.

## Anomalies et non-fait

- Cadence rompue le 22/09 (session interrompue sans trace d'erreur) —
  signalé ci-dessus, sans action corrective possible au-delà du constat.
- Search Console non consultée (pas d'accès direct dans cet outillage).
- Recherche de nouveaux événements et guides d'accès non traitées cette
  passe (voir ci-dessus).
- Le chantier « Feuille de route » (O1-O9) n'a pas été touché : hors du
  périmètre de la passe quotidienne de contenu.

## Publication

Commit `Passage : démarrage` poussé directement sur `main` en tout début de
passe. Un second commit (purge, bascule de saison, correctif `gen_pages.py`,
39 pages réparées) publié via `publier.sh` — `validate.py` : 0 bloqueur, 2
avertissements (fiches denses connues, sous le seuil bloquant) — puis
`git push origin main` réussi (aucun repli de branche nécessaire).
`healthcheck.sh` : OK (326/326, date fraîche). Signature
`radar-routine-claude` posée avant chaque commit. Journal privé
(`lessons.md`, ce compte rendu, `passages.log`) à pousser à la suite.
