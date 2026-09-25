# Compte rendu — passe du 25/09/2026 (session cloud)

## Démarrage

`.radar/DOCTRINE.md` (953 lignes), `.radar/PASSATION.md`, `.radar/REGLE-ALPHA.md`,
`.radar/AUDIT-SANS-POINT-FAIBLE.md` et `.radar/tools/lessons.md` (1 246 lignes) lus
intégralement avant tout travail. Trace de démarrage poussée directement sur `main`.
Clone superficiel détecté et réparé (`git fetch --unshallow`, 674 commits récupérés).
`precheck.sh` : verrou libre, arbre propre, aucune cadence rompue (dernier passage
technique le 24/09 au soir — voir « anomalie » ci-dessous). `rebuild_full.py` :
321 événements, 12 langues réinjectées, 0 orpheline.

## Constat sur la priorité annoncée (condensation des voies d'invitation)

Le prompt de tâche décrit un arriéré de 255 fiches en dérive « journal d'enquête »
(159 en fenêtre live), chiffre qui date de mi-août. L'historique du dépôt montre que
ce chantier a été mené à son terme par les passes successives (10/09 : « 255 → 7
candidats » ; puis reconfirmations quotidiennes à zéro dérive du 11/09 au 23/09).
Vérification faite aujourd'hui plutôt que de me fier au chiffre du prompt :
`validate.py` relève 11 fiches au-dessus du seuil de sélection (1 200 caractères
sur `iv.o`/`iv.g`/`iv.w`, excédent total 4 192 caractères). Lecture intégrale de
3 des plus longues (POINT D'ENTRÉE ventes aux enchères, Gstaad New Year Music
Festival, Formula 1 Abu Dhabi) : dans les trois cas, l'excédent est fait de faits
durs légitimes (noms, fonctions, téléphones, adresses, tarifs, dates de vente) sans
aucune tournure d'enquêteur — exactement le motif déjà consigné les 20-21/08 et
23/09 (« le seuil de sélection redétecte le travail bien fait »). **Aucune fiche
condensée aujourd'hui : zéro dérive réelle constatée, comme lors des 13 dernières
vérifications.**

## Entretien effectué

- **Purge** : 0 zombie (`d2 < aujourd'hui-30j`, hors guides) — le plancher
  automatique de 8h40 fait déjà ce travail chaque jour.
- **Liens** : les 15 événements des 7 prochains jours retestés en `curl -sL`
  (Voiles de Saint-Tropez, Fashion Week Paris et ses 6 portes d'accès, galas NYC/NY
  Philharmonic, ventes Sotheby's Paris et Hong Kong, Caves du Roy, Global Gift Gala,
  Doha Jewellery and Watches). 2 x 403 (site vu et refusé, donc vivant, règle du
  12/08) ; 2 faux positifs de ma propre détection de « 404 caché dans un 200 »
  (mot « oops » trouvé dans un nom propre et dans une chaîne d'interface générique,
  vérifiés au corps de page). **0 lien mort.**
- **Mémoire du radar** : `memoire.py changements` — 0 nouvelle date sur 7 jours.
- **Bandeau Ouvertures & délais** : 3 entrées, aucune périmée (échéances 30/09,
  15/10, 31/01/2027) — pas de nouvelle fenêtre datée trouvée à ajouter aujourd'hui.
- **Eyebrow** : bloquée sur « 23 septembre » depuis 2 jours (la session du 24/09 a
  travaillé sur le chantier technique Feuille de route — rendu progressif des
  cartes O3, tirets purgés — sans lancer la passe de contenu quotidienne).
  Corrigée à « 25 septembre 2026 ».

## État de la LOI DU SITE (iv + séjour + traductions)

`reste.py` : traductions 321/321 (100 %), voies d'invitation 321/321 (100 %),
séjours 315/321 (100 % réel — les 6 manquants sont les 6 fiches-guide `c=acces`
exemptées par la doctrine). **0 écart réel.** Joaillerie : 15 fiches en fenêtre
live (plancher de 10 largement tenu). Guides d'accès (`c=acces`) : 16 en ligne.
Les 8 ancres du printemps 2027 (TEFAF, Art Basel HK, Watches and Wonders, Salone
del Mobile, Festival de Cannes, GemGenève, Grand Prix de Monaco, Royal Ascot)
sont toutes publiées.

## Recherche de nouveaux événements

Deux pistes de la doctrine (« élargir » le printemps/l'international) vérifiées à
la source, sans ajout :
- **Bal de la Rose Monaco** : le site officiel Monte-Carlo SBM n'affiche que
  l'édition 2026 (21 mars, déjà passée, page marquée « Concluded »), aucune date
  2027 publiée à ce jour. Confirme le constat du 06/09 (« date non publiable »).
  Non ajouté — aucune date réelle à afficher.
- **24 Heures du Mans 2027** (9-13 juin, dates officielles confirmées sur
  24h-lemans.com) : la porte VIP existe (page hospitalité officielle) mais je n'ai
  pas pu, en une passe solo sans vérification adverse, bâtir dans le temps imparti
  un séjour du calibre exigé (palace/table iconique à proximité du circuit) ni un
  contact d'invitation nominatif réellement publié. Conformément à la doctrine
  (« au moindre doute, ne pas ajouter » / « mieux vaut ne rien publier que d'ajouter
  du grand public déguisé »), non ajouté aujourd'hui — à reprendre lors d'une passe
  disposant de plus de temps ou d'agents de vérification adverses.

**Rien de digne trouvé à ajouter aujourd'hui au-delà de ce qui existe déjà : résultat
honnête, pas un renoncement.**

## Publication

`bash .radar/session/publier.sh` : `inject.py` (rien à récolter), `gen_ldjson.py`,
`split_i18n.py --apply`, `gen_seo.py`, `gen_pages.py`, `validate.py` → OK, 0
bloqueur, 2 avertissements (les deux mêmes fiches denses déjà connues, sous le
seuil bloquant). Poussé directement sur `main` (aucun repli de branche
nécessaire). `healthcheck.sh` : OK (321/321, date fraîche, http 200).

## Analyse des visites

GoatCounter : 3 189 visiteurs/pages vues cumulés, stable depuis le relevé de la
veille (24/09 : 3 189) — probablement un relevé pris tôt dans la journée, avant
la reprise du trafic ; la tendance des 5 derniers jours reste à la hausse régulière
(2 961 → 3 000 → 3 094 → 3 119 → 3 189), cohérente avec le palier 1 de la feuille
de route (35-100 visites/jour).

## Anomalies et non-fait

- Aucune passe de contenu n'a tourné le 24/09 (une session technique a travaillé
  sur la Feuille de route à la place — voir Feuille de route et Audit sans point
  faible, entrées « [FAIT 24/09] ») ; l'écart est resté sous le seuil de cadence
  (healthcheck du 24/09 21h32 a maintenu `precheck.sh` silencieux). Signalé pour
  mémoire, aucune action requise.
- Search Console non consultée (pas d'accès direct dans cet outillage).
- Chantier Feuille de route (O1-O9) non touché : hors périmètre de la passe
  quotidienne de contenu, comme les jours précédents.
- Résorption des doutes (`a-reverifier.md`, 170 entrées) et vague des imminents :
  routines hebdomadaires dédiées (mercredi, lundi), non dues aujourd'hui (vendredi).
