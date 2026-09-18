# La règle alpha

Fixée par Constance le 18/09/2026. Elle prime sur toute demande future de contenu
ou d'idée : ces demandes s'y insèrent, elles ne la suspendent pas.

## L'ambition
ConstanceParis7 est dimensionné pour être un site de niveau mondial, techniquement
prêt pour un million de visiteurs par jour, et vise le haut des classements Google.
Le document de pilotage est `.radar/FEUILLE-DE-ROUTE.md` : neuf objectifs, leurs
micro-objectifs, et leur taux d'avancement, tenus à jour à chaque publication.

## Le cadre
1. L'hébergement reste GitHub Pages, comme maintenant (décision du 18/09/2026).
   Toute solution doit être compatible avec un site statique. Cloudflare, R2, D1 ne
   se rouvrent qu'à la main de Constance.
2. Impératif : le site est très rapide sur mobile, Android et iOS. L'objectif O3 de
   la feuille de route passe avant les autres tant qu'il n'est pas vert.
3. Aucun point faible : le registre `.radar/AUDIT-SANS-POINT-FAIBLE.md` se solde
   point par point ; le verrou de build (`.radar/tools/verrou.py`, appelé par
   validate.py) refuse toute publication incohérente.
4. Publication immédiate de chaque correction vérifiée (règle du 16/09) ; « fait »
   signifie « en ligne et vérifié ».
5. Promotion, réseaux, relais extérieurs et monétisation restent en pause jusqu'à
   ce que le site soit sans point faible (décision du 17/09).

## Le travail en équipe avec ChatGPT
Claude et ChatGPT ne sont pas adversaires : ils travaillent de concert et prennent
le meilleur des idées de chacun. Protocole :
- Avant tout chantier structurant, Claude expose le plan à ChatGPT (conversation
  « Critique du site de luxe », compte de Constance) et intègre ses objections
  fondées ; les désaccords sont tranchés par les faits (mesures, sources), sinon
  remontés à Constance.
- Après chaque grande vague, ChatGPT reçoit le récapitulatif et rend son bilan ;
  les points qu'il maintient entrent au registre.
- Ni l'un ni l'autre n'agit sur une affirmation non vérifiée : une page chargée,
  un chiffre mesuré, ou rien.

## Le rythme
Claude travaille tant qu'une session est ouverte et par ses routines automatiques
(passe de nuit, sonde du matin à 7h15, sentinelle du lundi, résorption du mercredi,
contrôle Google du vendredi, avancement quotidien de la feuille de route). Il ne
prétend pas à une présence continue qu'il n'a pas : chaque compte rendu dit ce qui
a été fait, ce qui reste, et le taux d'avancement réel.

## Ce que personne ne promet
Les positions Google se gagnent, elles ne se décrètent pas. Au 18/09/2026, le site
est en position 1 sur plus de soixante requêtes réelles et en position moyenne 5,2.
La feuille de route donne au site tout ce qui dépend de nous ; le reste appartient
à Google, et on le mesure chaque semaine plutôt que de le supposer.
