# Compte rendu — passe du 14/09/2026

Cadence : dernier run journalisé la veille (13/09), pas de rattrapage nécessaire.
Lecture complète de DOCTRINE.md, PASSATION.md et lessons.md faite avant toute action.

## Priorité annoncée par la consigne (condensation `iv`) — vérifiée honnêtement, toujours résorbée

La consigne du jour redemande de condenser 15-20 fiches sur le backlog « 255 fiches,
159 en fenêtre live » daté du 19/08/2026. Ce chiffre reste **périmé depuis plusieurs
jours** (confirmé stable les 10, 12 et 13/09). Au démarrage, `validate.py` ne signale
que 1 fiche `iv.g` et 7 fiches `iv.w` au-delà du seuil WARN de 1200 caractères — les
7 mêmes fiches qu'hier, aux mêmes longueurs exactes (Villa Carmignac, Biennale Arte,
ICP/YSL Photography, POINT D'ENTRÉE ventes aux enchères, Cala Rossa, Gstaad New Year
Festival, F1 Abu Dhabi ×2). Relu intégralement le contenu des deux fiches les plus
denses (POINT D'ENTRÉE ventes aux enchères, 2675 car. ; F1 Abu Dhabi, iv.g+iv.w) :
aucune trace de journal d'enquête (pas de « OUI, une voie existe, mais… », aucun
commentaire de méthode) — uniquement des noms, fonctions, e-mails, téléphones,
adresses, tarifs et dates réels, légitimement denses (ex. calendrier complet des
ventes Christie's Paris jusqu'en mars 2027, ou le détail des hospitalités du Grand
Prix d'Abu Dhabi). Conformément à la LOI « on ne supprime aucun fait » et à la leçon
du 20-21/08 (« le seuil-cible redétecte le travail déjà fait »), rien n'a été touché :
forcer une condensation ici aurait sacrifié des faits vrais pour gagner des
caractères. **Le chantier de condensation est soldé et le reste stable.**

## Plancher et entretien du jour

- **Zombies purgés** : 2 fiches à `d2=2026-08-14` (Hotel Pitrizza — dîner de gala,
  Disco del Sol / 23rd Anniversary Nikki Beach Marbella). 370 → 368 événements.
- **Contrôle hebdomadaire du lundi (aujourd'hui = lundi)** : les 251 URL de TOUS les
  événements à venir retestées (pas seulement les 120 plus imminents du plancher
  quotidien) :
  - **1 lien réellement anormal** : `petitpalais.paris.fr/en/we-are-still-here`
    (fiche « WE ARE [still] HERE ») renvoyait un 500 confirmé 3 fois de suite, alors
    que le reste du site répond normalement. L'exposition est bien réelle et en
    cours (confirmé par recherche indépendante, paris.fr, pariszigzag.fr).
    **Corrigé** : `u` et `so` basculés vers `petitpalais.paris.fr/expositions/
    we-are-still-here` (FR, 200, contenu vérifié) — une URL déjà présente dans le
    tableau de contacts `iv.c` de la fiche mais jamais promue en lien principal ;
    l'ancienne variante `/en/` (elle-même 404) retirée du même tableau. Aucun autre
    champ touché.
  - **7 liens en échec réseau** (timeout, reset, SSL) sur des domaines précis
    (Van Cleef & Arpels, Marina Bay Sands, Silencio, La Capannina di Franceschi,
    Théâtre de Chaillot, Opéra de Monte-Carlo, Château de Chantilly) — un domaine
    témoin neutre (Wikipedia) répondait normalement au même moment, donc pas un
    incident d'environnement généralisé, mais un blocage propre à ces hôtes
    (probable protection anti-robot). Aucune conclusion tirée, rien changé aux
    fiches : à revérifier à une prochaine passe, conformément à la leçon du 12-13/08.
  - Les 3 autres alertes initiales du script se sont résolues au nouvel essai
    (madparis.fr, Atlantis The Royal, One&Only, GemGenève) : flakiness, pas de panne.
- **Nouvel outil `.radar/tools/gen_ldjson.py`** : en voulant exécuter l'étape « régénérer
  le ld+json des 60 meilleurs événements » (doctrine, chaque lundi), constat que ce
  bloc n'avait AUCUN mécanisme de régénération automatique — il contenait encore un
  gala du 12/08, un mois après sa tenue. Reconstruit à la main ce jour (même formule
  que la Note du radar), puis **committé comme outil permanent et câblé dans
  `publier.sh`** : il tourne désormais à CHAQUE publication, pas seulement le lundi —
  il ne peut donc plus périmer en silence. Détail dans `lessons.md`.
- **Mémoire du radar** (`memoire.py changements`) : 0 changement de date détecté sur 7
  jours.
- **Bandeau « Ouvertures & délais »** : 4 entrées, aucune périmée (échéances 30/09,
  06/10, 15/10, 31/01/27).
- **Eyebrow** : date de vérification mise à jour au 14 septembre 2026.
- **Vague des imminents** : Paris Fashion Week déjà en page dédiée depuis le 13/09.
  Repéré un second candidat solide pour la prochaine occasion (Milano Fashion Week,
  22-28/09, note 89, même calibre que PFW) — non traité aujourd'hui, cette routine
  est en principe pilotée par sa propre tâche hebdomadaire dédiée (doctrine, « vague
  des imminents », lundi 7h30) : à vérifier si elle a tourné séparément.
- **Nouvelle destination** : recherche rapide sur les destinations à 0 fiche
  (Comporta/Melides, Spetses, Aspen, Udaipur, Tulum, Harbour Island, Casa de Campo) —
  rien trouvé qui passe le filtre ADN Riviera avec porte d'entrée publiée (ex. :
  aucun événement mondain daté trouvé pour Comporta/Melides, seulement un festival
  musical grand public). Conformément à la doctrine, rien ajouté plutôt que d'ajouter
  du grand public déguisé.

## LOI DU SITE

`reste.py` : 368/368 traductions, 357/368 séjours, 365/368 invitations au global —
croisé avec la fenêtre live (auj.→+90j, 197 fiches hors dossiers d'accès) : **0 séjour
et 0 invitation manquants**. Tous les manquants globaux sont des événements déjà
passés (conservés 30 jours avant purge). **LOI DU SITE honorée à 100 % sur ce qu'un
visiteur voit aujourd'hui.**

## Contrôles

- `validate.py` : **OK — 0 blocker, 3 warning(s)** (les 8 fiches `iv.g`/`iv.w`
  denses mais légitimes déjà décrites plus haut ; bandeau « Été » encore affiché —
  normal avant l'équinoxe du 22-23/09, à ne pas renommer sans l'accord de Gérald).
- `healthcheck.sh` : **OK** — http=200, date fraîche, 368/368 événements servis en
  ligne, conforme au build publié.

## Publication

Poussé **directement sur `main`**, au fil de l'eau, en trois temps : (1) plancher —
purge + eyebrow, (2) contrôle hebdomadaire — lien corrigé + ld+json régénéré,
(3) outil `gen_ldjson.py` committé et câblé dans le publieur. Pas de repli sur
branche `claude/*` nécessaire aujourd'hui.

Étape 10 de la doctrine (republier l'artifact Claude) **non tentée** : panne connue
depuis le 21/08/2026 (« artifact not found »), sans conséquence pour le public.

## Visites

**2681 visiteurs/pages vues le 14/09**, +27 vs la veille (2654), soit +1,0 % — dans
la continuité de la lente progression des dix derniers jours. Rien de saillant à
signaler côté pays ou sources aujourd'hui.

## Ce qui n'a pas été fait aujourd'hui, à reprendre

- Les 7 liens en échec réseau (Van Cleef & Arpels, Marina Bay Sands, Silencio, La
  Capannina di Franceschi, Chaillot, Opéra de Monte-Carlo, Chantilly) : à retester à
  froid la prochaine fois que le réseau de la session le permet, avant de les
  considérer comme des lignes mortes.
- Registre `a-reverifier.md` : les 2 doutes encore vivants (Bagni Fiore/Langosteria
  Paraggi, terrasses des palaces parisiens) n'ont pas bougé — pas d'urgence.
- Milano Fashion Week (22-28/09) reste un bon candidat pour une page « imminents »
  dédiée comme Paris Fashion Week, si la routine hebdomadaire spécialisée ne l'a pas
  déjà traité.
- Aucune nouvelle destination ajoutée à la carte du monde (recherche faite,
  infructueuse cette fois — voir plus haut) : à retenter à une prochaine passe avec
  un budget de recherche dédié plus large.
