# Compte rendu — passe du 13/09/2026

Cadence : dernier run journalisé la veille (12/09), pas de rattrapage nécessaire.

## Priorité annoncée par la consigne (condensation `iv`) — vérifiée, toujours résorbée

La consigne du jour redemandait de condenser 15-20 fiches sur le backlog « 255
fiches, 159 en fenêtre live » daté du 19/08. Ce chiffre reste **périmé** : au
démarrage, `validate.py` ne signale que 1 fiche `iv.g` et 7 fiches `iv.w`
au-delà du seuil WARN de 1200 caractères — les mêmes qu'au 10-12/09. Relu
intégralement les 8 fiches (Villa Carmignac, Biennale Arte, ICP/YSL Photography,
POINT D'ENTRÉE ventes aux enchères, Cala Rossa, Gstaad New Year Festival, F1 Abu
Dhabi) : aucune trace de journal d'enquête (pas de « OUI, une voie existe,
mais… », pas de commentaire de méthode) — uniquement des contacts, tarifs,
horaires et adresses réels, légitimement denses. Rien touché, conformément à la
LOI « on ne supprime aucun fait » : forcer une condensation aurait sacrifié des
faits vrais pour gagner des caractères, exactement l'erreur identifiée le 20-21/08.

## Entretien du jour

- **Zombies purgés** : 2 fiches à `d2=2026-08-13` (Autobello Sotogrande 2026,
  Philharmonix / The Vienna Berlin Music Club, Dubrovačke ljetne igre).
  372 → 370 événements. `archives.json` les récupère automatiquement depuis
  l'historique Git (mécanisme du 12/08).
- **Bandeau « Ouvertures & délais »** : 3 entrées vérifiées, aucune périmée
  (échéances 30/09, 15/10, 31/01/27) — rien à retirer aujourd'hui.
- **Liens à 7 jours** : 12 URL testées (les plus imminentes, dont Chantilly
  Arts & Élégance qui se tient aujourd'hui même). 11 en 200 propre, aucun
  « not found »/« 404 » dans le corps. 1 cas à traiter :
  **CSIO 5\* Longines League of Nations (Saint-Tropez-Gassin)** :
  `leagueoffnations.fei.org` renvoie 403 au script ET à WebFetch. Réflexe de
  la leçon du 12/08 (« un 403 est une invitation à changer d'outil, pas une
  conclusion ») appliqué : recherche croisée sur sources indépendantes
  (page officielle du lieu hôte polo-st-tropez.com, article de presse FEI
  inside.fei.org). L'événement est bien réel. Petite divergence de bornage
  trouvée entre sources (le lieu-hôte parle du 17 au 20/09, la FEI elle-même
  du 16 au 20/09 pour l'étape complète) : la fiche du site (`d1=16/09`,
  `d2=20/09`) reste alignée sur la source FEI, la plus autorisée pour son
  propre circuit — aucune correction faite, écart jugé non significatif et
  non tranchable avec certitude au bénéfice d'une seule source secondaire.
- **Mémoire du radar** (`memoire.py changements`) : 0 changement de date
  détecté sur 7 jours.
- **Eyebrow** : date de vérification mise à jour au 13 septembre 2026.
- **Carte des destinations / anciennes saisonnières d'automne** : vérification
  rapide de couverture (Monaco Yacht Show, Mostra de Venise, Fashion Week
  Paris, Art Basel Paris, Voiles de Saint-Tropez) — tous déjà présents avec
  fiche(s) dédiée(s). Aucun ajout aujourd'hui : rien de nouveau trouvé qui
  passe le filtre ADN Riviera avec porte d'entrée publiée (recherche limitée
  par le temps de passe consacré à l'entretien et à la vérification des
  liens ci-dessus).

## LOI DU SITE

`reste.py` : 370/370 traductions, 359/370 séjours, 367/370 invitations au
global — croisé avec la fenêtre live (auj.→+90j, 91 fiches) : **0 séjour et
0 invitation manquants**. Tous les manquants globaux sont des événements déjà
passés (conservés 30 jours avant purge). **LOI DU SITE honorée à 100 % sur ce
qu'un visiteur voit aujourd'hui.**

## Contrôles

- `validate.py` : **OK — 0 blocker, 3 warning(s)** (1 fiche `iv.g` et 7 fiches
  `iv.w` toujours > 1200 car., stables et légitimement denses ; bandeau
  « Été » encore affiché — normal avant l'équinoxe du 22-23/09, à ne pas
  renommer sans l'accord de Gérald).
- `healthcheck.sh` : **OK** — http=200, date fraîche, 370/370 événements
  servis en ligne, conforme au build publié.

## Publication

`publier.sh` a régénéré le socle SEO et les pages indexables, validé, commité
et **poussé directement sur `main`** — pas de repli sur branche `claude/*`
nécessaire aujourd'hui. Deux publications au fil de l'eau : purge des 2
zombies, puis mise à jour de l'eyebrow + régénération SEO/pages.

Étape 10 de la doctrine (republier l'artifact Claude) **non tentée** : panne
connue depuis le 21/08/2026 (« artifact not found »), sans conséquence pour
le public.

## Visites

**2654 visiteurs/pages vues le 13/09**, +10 vs la veille (2644), progression
lente et continue, conforme à la tendance des dix derniers jours (environ
+0,4 %/jour). Rien de saillant à signaler aujourd'hui côté sources ou pays —
tendance stable, pas d'anomalie.

## Ce qui n'a pas été fait aujourd'hui, à reprendre

- Registre `a-reverifier.md` : les 2 doutes encore vivants (Bagni Fiore/
  Langosteria Paraggi, d2 estimé 30/09 ; terrasses des palaces parisiens,
  d2 estimé 04/10) n'ont pas été retranchés — marge de 2-3 semaines, pas
  d'urgence.
- Aucune recherche approfondie de nouveaux événements au-delà de la
  vérification de couverture des ancres d'automne déjà connues : le temps de
  passe a été concentré sur le plancher (purge, liens, condensation
  vérifiée, eyebrow). À reprendre à une prochaine passe avec un budget de
  recherche dédié.
- Contrôle hebdomadaire du lundi (retester tous les liens à venir + régénérer
  le ld+json des 60 meilleurs) : à faire demain, 14/09 (lundi).
