# Compte rendu — passe du 16/09/2026

## Anomalie de démarrage (à signaler)

La passe du 15/09 a démarré (04:04 UTC) mais s'est arrêtée après un seul
commit (« Vague des imminents : page Milano Fashion Week ») — pas de FIN dans
`passages.log`, pas de compte rendu mis à jour. Le plancher automatique
(`passe-quotidienne.yml`, 06:53 UTC) a pris le relais pour l'entretien de
base. Aucune perte de contenu constatée. Rien à corriger dans le filet :
c'est le cas déjà documenté « une limite de session tue les agents en vol »,
sans conséquence ici puisque le site est resté cohérent (352 événements
avant cette passe).

## PRIORITÉ DU JOUR — condensation des voies d'invitation (iv)

Relu à neuf les 8 fiches encore signalées par `validate.py` (1 `iv.g` et
7 `iv.w` au-delà de 1200 caractères) : Villa Carmignac, Biennale Arte 2026,
Yves Saint Laurent and Photography (ICP), le guide d'accès ventes aux
enchères, Grand Hôtel de Cala Rossa, Gstaad New Year Music Festival, F1 Abu
Dhabi. Aucune ne porte la dérive « journal d'enquête » décrite dans la
doctrine (pas de tournure d'enquêteur, pas de titre de section, pas de
commentaire de méthode) : ce sont des fiches légitimement denses — grilles
tarifaires à plusieurs paliers, plusieurs tables/restaurants, contacts de
privatisation nommés avec téléphone direct. Conforme à la règle « on garde
tous les faits, on ne coupe que le récit d'enquête » : il n'y a ici aucun
récit à couper sans perdre un fait vérifié. **Condensation confirmée soldée**
pour la 8e fois consécutive (dernières confirmations : 06, 07, 10, 11, 13,
14/09) — le défaut du 12-19/08 (255 fiches, 159 en fenêtre live) est résorbé
depuis début septembre. Aucune fiche condensée aujourd'hui : aucune n'en
avait besoin.

## Plancher / entretien

- **Purge** : 7 zombies retirés (d2=16/08/2026, au-delà du seuil de 30 jours) :
  Calder (Fondation Louis Vuitton), LINDER (Chanel Nexus Hall), Polo Côte
  d'Azur Cup, Ventes Besch Cannes Auction, Prix Jacques Le Marois, Pebble
  Beach Concours d'Elegance 75e, World Vision Charity Gala 2026.
  352 → 345 événements.
- **Liens** : 119 liens des événements les plus imminents testés, 0 mort.
- **Eyebrow** : date de vérification mise à jour au 16 septembre 2026.
- **Saison du titre** : recalculée, reste « Summer 2026 » — normal avant
  l'équinoxe du 22-23/09 (à ne pas renommer seul, comme convenu avec Gérald).

## LOI DU SITE

`reste.py` : 345/345 traductions, 338/345 séjours, 344/345 invitations au
global. Vérifié fiche par fiche : les 7 séjours manquants sont les 6 guides
d'accès (`c=acces`, exemptés par la doctrine) + 1 feu d'artifice local déjà
hors fenêtre (d2=17/08, se purgera demain) ; la seule invitation manquante
est ce même feu d'artifice. **0 séjour et 0 invitation manquants dans la
fenêtre live (auj.→+90j).** LOI DU SITE honorée à 100 % sur ce qu'un
visiteur voit aujourd'hui.

## Nouveaux événements

Recherche de piste neuve non menée en profondeur aujourd'hui : la fenêtre
des 45 prochains jours est déjà dense et au calibre Riviera-ADN (Régates
Royales de Cannes, Monaco Yacht Show, Voiles de Saint-Tropez, Fashion Weeks
Londres/Milan/Paris avec tout leur appareil d'accès, Frieze/PAD Londres,
Art Basel Paris, Journées Particulières LVMH, ventes Sotheby's/Christie's,
Prix de l'Arc de Triomphe…) — aucun trou évident à combler dans l'horizon
immédiat. Conformément à la doctrine, rien ajouté plutôt que de gonfler le
compteur sans piste solide.

## Vague des imminents

Registre à jour (4 pages) : Paris Fashion Week (13/09), Monaco Yacht Show
(14/09), Vogue World Milano (14/09), Milano Fashion Week (15/09, par la
passe d'hier). Rien à ajouter aujourd'hui — la routine hebdomadaire dédiée
(lundi 7h30) reste la responsable normale de ce registre.

## Contrôles

- `validate.py` : **OK — 0 blocker, 2 warning(s)** (les fiches denses
  décrites ci-dessus, légitimes).
- `healthcheck.sh` : **OK** — http=200, date fraîche, 345/345 événements
  servis en ligne, conforme au build publié.

## Publication

Poussé **directement sur `main`**, en une fois via `publier.sh` (purge,
liens et saison faits en amont via `passe_automatique.py --apply`, puis
inject/gen_ldjson/split_i18n/gen_seo/gen_pages/validate/commit/push).
Aucun repli sur branche `claude/*` nécessaire.

Étape 10 de la doctrine (republier l'artifact Claude) **non tentée** :
panne connue depuis le 21/08/2026 (« artifact not found »), sans
conséquence pour le public.

## Visites

**2791 visiteurs/pages vues le 16/09**, +54 vs la veille (2737), soit
+2,0 % — poursuite de la lente progression des deux dernières semaines.
Rien de saillant à signaler côté pays ou sources aujourd'hui.

## Ce qui n'a pas été fait aujourd'hui, à reprendre

- Recherche de nouvelles fiches non menée en profondeur (fenêtre déjà dense,
  voir plus haut) : à retenter avec un budget de recherche dédié si un
  circuit particulier semble se dégarnir (ex. printemps 2027, avril/juin
  encore minces mais hors fenêtre live).
- Doutes non tranchés de `a-reverifier.md` : non repris aujourd'hui, la
  routine hebdomadaire dédiée « résorption des doutes » (mercredi 7h30) a
  déjà traité une vague 1 hier soir (17h38) par une session de Constance ;
  à vérifier si la routine automatisée du mercredi a aussi tourné
  séparément aujourd'hui pour éviter un doublon d'effort.
- `python3 tools/memoire.py changements` relancé : 0 changement de date
  consigné sur les 7 derniers jours, rien à ajouter au registre.
