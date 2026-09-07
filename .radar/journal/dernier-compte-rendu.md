# Compte rendu — passe du 07/09/2026

## Plancher du jour (purge, liens, date)

`precheck.sh` a trouvé 4 blocages au démarrage : 4 zombies non purgés
(d2=2026-08-07, seuil des 30 jours franchi aujourd'hui même — même mécanique
que la leçon du 31/08). `passe_automatique.py --apply` : purge des 4 zombies
(Festival de Musique de Menton 77e édition, Copenhagen Fashion Week SS27,
Guild Hall Summer Gala 2026, Cowes Week 2026 Bicentenaire), **119 liens
testés** sur les plus imminents (0 mort), eyebrow mis à jour au 7 septembre
2026. Publié en premier (0 blocker), avant tout le reste.

## Priorité du moment : condensation des voies d'invitation — chantier confirmé soldé

Recontrôle exhaustif mécanique (recherche des marqueurs de dérive doctrinaux
« OUI, une voie existe, mais… », « CE QUE LA MAISON MET RÉELLEMENT… », etc.)
sur les 388 fiches : **0 occurrence**. Seules 11 fiches dépassent encore le
seuil WARN de 1200 caractères sur `iv.o`/`iv.g`/`iv.w` (1 + 10, avec
recoupement) — exactement le même lot que la passe d'hier (06/09), qui les
avait lues intégralement une par une et conclu à un contenu légitimement
dense (jusqu'à une dizaine de contacts/tarifs/horaires distincts par fiche),
sans dérive résiduelle. **Aucune fiche condensée aujourd'hui** : il n'y avait
rien à condenser sans perdre un fait, ce qui violerait la règle « on ne
supprime aucun fait ». Le défaut du 12-19/08 (255 fiches touchées à
l'origine) reste donc à zéro dérive résiduelle, reconfirmé pour la seconde
journée consécutive.

## LOI DU SITE — recomptée sur la fenêtre live (aujourd'hui → +90j)

| | fenêtre live |
|---|---|
| Traductions manquantes (13 langues) | 0 |
| Séjours manquants | **0** |
| Invitations manquantes | **0** |

100 % honoré sur ce qui est réellement montré aux visiteurs (388 fiches au
total, dont 95 dans la fenêtre live). Les 17 séjours et 4 invitations
manquants au global sont tous hors fenêtre (événements passés conservés 30
jours, ou au-delà de +90 jours) — vérifié par script (croisement `d2` /
aujourd'hui, méthode de la leçon du 19/08).

## Contrôle hebdomadaire du LUNDI : tous les liens à venir retestés

265 URL uniques d'événements à venir testées (au-delà des 120 les plus
imminents du plancher quotidien). **1 lien réellement mort trouvé** :
« Norton Museum of Art — Gala annuel 2027 » pointait vers
`norton.org/get-involved/Galas`, qui renvoie un vrai 404 (page « Page not
found », vérifié en corps de page, pas seulement au code retour — réflexe
de la leçon du 18/08). Recherche faite : le musée a migré sa navigation ;
la page existe toujours sous `norton.org/private-events/galas` (200,
contenu réel confirmé). URL corrigée et publiée. Au passage, la recherche a
confirmé que la date « 06/02/2027 » de cette fiche est une PROJECTION
DÉCLARÉE (le champ `dt` le dit explicitement, `cf: "à vérifier"`) : la seule
édition confirmée par le musée est celle du 07/02/2026 (déjà passée), 2027
n'est pas encore annoncée. La fiche est hors fenêtre live (février 2027,
au-delà de +90j) donc aucun visiteur n'y est actuellement exposé ; laissée
en l'état (date honnêtement qualifiée d'estimation dans le texte visiteur),
à reconfirmer quand le musée publiera l'édition 2027.

## Recherche de nouveauté

**Bal de la Rose de Monte-Carlo (Sporting Monte-Carlo)** : revérifié
directement sur montecarlosbm.com/en/agenda/bal-de-la-rose (chargement
réel, 437 Ko). Toujours affiché « Concluded — Saturday, 21 March 2026 »,
aucune date 2027 annoncée. Conforme au garde-fou anti-fabrication : fiche
toujours non créée, comme signalé dans `CHANTIERS.md` (chantier 08).

**JustMe Porto Cervo** (doute ouvert le 20/08, `d2`=07/09 = aujourd'hui) :
revérifié sur xceed.me — seule date trouvée dans la page : 2026-09-07,
aucune trace d'événement au-delà. La date actuelle de la fiche est donc
cohérente avec ce qui est publié ; elle sortira naturellement de l'écran
demain par le voile d'affichage (comportement correct, pas une perte de
donnée : conservée 30 jours dans les données).

Aucun nouvel événement composé aujourd'hui : l'effort de la passe a porté
sur le plancher, la vérification hebdomadaire des liens et le contrôle de
la condensation — pas de piste nouvelle assez solide identifiée dans le
temps disponible pour naître complète (invitation + séjour + 13 langues)
sans rien inventer.

## Mémoire et visites

- `memoire.py changements` : 0 changement de date consigné sur 7 jours.
- Visites : **2552** aujourd'hui contre 2529 hier (+0,9 %), progression
  continue depuis plus d'une semaine (2388 → 2552, soit +6,9 %). Pas de
  rupture ni de pic. Pas de recoupement pays/source disponible (aucun outil
  de répartition public au-delà du compteur total GoatCounter).

## Ce qui n'a pas pu être vérifié / reste en suspens

- Le rafraîchissement de saison « Été » → « Automne » reste en attente :
  décision qui appartient à Constance (branding jamais touché seul).
  `validate.py` continue de le rappeler en WARN, sans bloquer.
- `.radar/a-reverifier.md` (20 doutes ouverts) : pas repris intégralement
  aujourd'hui, faute de temps — plusieurs concernent des lieux dont la
  saison estivale touche à sa fin ; à reprendre à une prochaine passe. Le
  fichier reste volumineux, sa reconsolidation (méthode de la leçon du
  20/08 : dédoublonnage par clé) n'a pas été refaite ce jour.
- Bal de la Rose 2027 : à reprendre dès l'annonce officielle de la date
  (voir ci-dessus).

## Contrôles finaux

`validate.py` : 0 blocage, 3 avertissements (les 11 fiches `iv` légitimement
denses + 1 rappel de saison). `healthcheck.sh` : OK (http=200, compte
live=388=attendu, date fraîche). Publication faite en 2 commits sur `main`
(plancher + correctif du lien Norton), aucun repli de branche nécessaire
aujourd'hui — le push direct sur `main` a été accepté dans les deux cas.
