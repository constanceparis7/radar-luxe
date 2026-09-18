# Compte rendu — passe du 18/09/2026 (session cloud)

## Priorité du moment : condensation des voies d'invitation

16 fiches condensées ce jour, sélectionnées par le seuil CIBLE (≥400 caractères
sur `iv.o`/`iv.g`/`iv.w`, pas le seuil WARN de tolérance à 1200 — leçon du
17/09), en commençant par les plus imminentes de la fenêtre live (Fine Arts
Paris, L'École des Arts Joailliers, Petit Palais, London/Milano Fashion Week,
Dior Spa Cheval Blanc, Régates Royales, Vogue World Milano, Ron Mueck, Zurich
Film Festival, Nammos Mykonos, Dolce & Gabbana Beach Club, Voiles de
Saint-Tropez, Jacquemus x Monte-Carlo Beach, LIV at Fontainebleau, Van Cleef &
Arpels au MAK de Vienne).

Un agent par fiche, prompt rappelant les règles de condensation (garder
intégralement noms/fonctions/e-mails/téléphones/adresses/URLs/tarifs/horaires,
jeter les tournures d'enquêteur, cible 400 car., jamais l'inverse) et le
garde-fou vie privée (retirer toute ligne « portable »/« ligne directe » ou
e-mail `prenom.nom@`/`initiale.nom@` visant une personne physique).

Contrôle mécanique `verif_faits.py` (dossiers entrée/sortie séparés — piège du
20/08 sur le même dossier évité) : 15/16 fiches sans aucune perte de fait ; la
seule alerte (Jacquemus x Monte-Carlo Beach) correspond exactement au retrait
volontaire signalé par l'agent lui-même (deux e-mails `initiale.nom@` d'un
directeur et d'une directrice du SBM, noms et fonctions conservés) —
c'est le garde-fou vie privée qui a fonctionné, pas une perte.

État du chantier : 197 → 190 fiches ≥400 car. au global, 135 → 129 en fenêtre
live. La baisse est modeste par fiche traitée : conforme à la leçon du 20-21/08
— une fiche condensée qui garde plusieurs contacts nominatifs légitimes reste
au-dessus de 400 caractères par construction (« garder le fait, jamais
l'inverse »), le compteur ne peut pas tomber à zéro. 174 fiches restent
(dont 129 en fenêtre live) à poursuivre par lots aux prochaines passes.

## Purge

1 zombie purgé : « Cavo Paradiso, Saison DJ 2026 » (d2=2026-08-18, > 30 j).
340 événements en ligne après purge (341 avant).

## Bug trouvé et corrigé dans le filet

`verrou.py` (le nouveau contrôle bloquant posé le 17/09) codait en dur
`~/radar-luxe` au lieu de suivre la convention `RADAR_REPO` de tout le reste
du filet — il plantait (`FileNotFoundError`) dans cette session cloud où le
dépôt vit à `/home/user/radar-luxe`, ce qui aurait fait échouer `validate.py`
(donc bloqué toute publication) à 100 % des passes cloud. Corrigé et publié.
Leçon consignée dans `tools/lessons.md`.

Erreur personnelle repérée et corrigée avant publication : une mise à jour de
la date de l'eyebrow par regex a d'abord empoisonné une clé du dictionnaire
i18n qui partage le même préfixe de texte (elle sert de gabarit, sans date en
dur) — repéré par relecture immédiate, corrigé avant tout commit. Leçon
consignée.

## LOI DU SITE — les trois compteurs (`reste.py`, fenêtre entière)

- Traductions 13 langues : 340/340 (100 %)
- Séjours clé en main : 334/340 (les 6 manquants sont des fiches-conseil
  `c=acces`, exemptées par doctrine)
- Voies d'invitation : 340/340 (100 %)

La LOI DU SITE est honorée à 100 % sur tout ce qui n'est pas explicitement
exempté — rien à rattraper de ce côté aujourd'hui.

## Contrôles

`validate.py` : OK — 0 blocker, 2 warnings (iv.g/iv.w encore >1200 car. sur
2+9 fiches résiduelles, en baisse). `verrou.py` (sous-contrôle de
validate.py, 6354 pages/340 fiches/5558 URLs sitemap) : 0 bloqueur, 3
avertissements W1 mineurs pré-existants (dates écrites dans `dt` légèrement
hors de la fenêtre machine sur 3 fiches — à vérifier à une prochaine passe,
non traité aujourd'hui faute de temps). `perfcheck.py` : OK, 0 régression
(poids -0,03 Mo, -12 événements/-9 séjours vs dernier point — cohérent avec
la purge). `healthcheck.sh` : OK (http=200, compte_live=340=attendu, date
fraîche).

## Publication

Un seul commit : `bash .radar/session/publier.sh` a poussé directement sur
`main` (pas de repli branche nécessaire aujourd'hui). Journal privé
(lessons.md, ce compte rendu) poussé séparément.

## Analyse des visites

2 885 visiteurs/pages vues aujourd'hui contre 2 836 hier (+1,7 %), en
croissance continue depuis le 15/09 (2 737 → 2 791 → 2 836 → 2 885) : une
progression régulière, sans pic ni chute, cohérente avec un site qui gagne
lentement en indexation plutôt qu'un effet ponctuel.

## Non vérifié / reporté

- Les 3 avertissements W1 du VERROU (dates `dt` hors fenêtre machine sur
  Taste of Tennis New York, Covo di Nord-Est, Nikki Beach Ibiza) — non
  bloquants, à trancher à une prochaine passe (corriger `dt` ou `d1/d2`,
  selon quelle donnée est fausse).
- 174 fiches restent au-dessus du seuil cible de condensation (129 en
  fenêtre live) — à poursuivre par lots de 15-20/passe.
- Pas de recherche de nouveaux événements ni de vérification des liens à
  7 jours effectuée aujourd'hui : tout le temps de la passe est allé à la
  priorité du moment (condensation) et au bug bloquant du filet, conforme à
  la doctrine qui place la condensation avant la recherche tant qu'il en
  reste.
