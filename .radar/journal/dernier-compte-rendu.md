# Compte rendu — passe du 11/09/2026

Cadence : dernier run journalisé il y a 71 h (> seuil de 30 h) → passe de
RATTRAPAGE. Aucune trace d'anomalie particulière dans le dépôt (pas de
`DEMARRAGE` sans `FIN` la veille) ; simple absence de déclenchement le 10/09
au soir ou dans la nuit, traitée normalement.

## Priorité annoncée par la consigne (condensation `iv`) — vérifiée, déjà résorbée

La consigne de ce jour redemandait de condenser 15-20 fiches sur un backlog
« 255 fiches, 159 en fenêtre live » daté du 19/08. Ce chiffre est **périmé** :
le compte rendu du 10/09 avait déjà ramené ce backlog à 7 candidats au seuil
WARN de `validate.py` (≥1200 car.), tous relus intégralement et classés
légitimement denses (beaucoup de contacts/tarifs réels, pas un journal
d'enquête). Vérifications faites aujourd'hui avant de conclure à rien
condenser :
- Les 7 candidats au seuil WARN sont **exactement les mêmes 7 fiches** que
  le 10/09 (mêmes noms, longueurs quasi identiques) — aucune nouvelle
  dérive n'est apparue depuis.
- Balayage de l'ensemble des 374 fiches à la recherche des tournures
  d'enquêteur bannies (« OUI, une voie existe, mais… », « CE QUE LA MAISON
  MET RÉELLEMENT À DISPOSITION », etc.) : **0 occurrence** ailleurs que les
  mentions légitimes du badge « vérifié le JJ/MM/AAAA ».
Conclusion : le backlog de condensation annoncé par la consigne est déjà
soldé depuis le 10/09 ; forcer une condensation sur les 7 fiches restantes
aurait supprimé des faits réels pour gagner des caractères, contraire à la
règle « garder le fait, jamais l'inverse ». Rien touché sur ce chantier
aujourd'hui, à raison.

## Entretien du jour

- **Zombies purgés** : 5 fiches à `d2=2026-08-11` (exactement 31 jours,
  seuil franchi ce jour) — Les Grimaldines, Les Nuits du Château de la
  Moutte, Yerai Cortés (Fondation Maeght), Ravello Festival Concerto
  all'alba, Monte-Carlo Summer Festival (dîner-spectacle Lisa Stansfield).
  379 → 374 événements.
- **Liens à 7 jours** : 26 URL testées (événements démarrant ou finissant
  dans les 7 prochains jours), `curl -sL` avec vérification du corps.
  0 « page introuvable » confirmée. Détail :
  - 4 blocages anti-robot connus (403) : Espace Louis Vuitton Tokyo, rooftop
    Peninsula Paris, US Open Fan Week, CSIO League of Nations — pas une
    preuve d'absence.
  - 1 signal « suspect404 » sur `sailgp.com/` (chaîne « This page could not
    be found » présente) — cas déjà documenté le 08/09/2026 : c'est le
    composant générique `notFound` du bundle Next.js, la page réelle
    contient bien « September 12-13 — ROCKWOOL France Sail Grand Prix |
    Saint-Tropez ». Aucune action.
  - 2 échecs de connexion (code 000) : `twigafortedeimarmi.com` et
    `lacapanninadifranceschi.com`. Domaine témoin neutre (wikipedia.org)
    testé en parallèle : OK. Ce n'est donc pas un blocage général de la
    session (contrairement aux 12-13/08 et 19/08), mais un incident
    limité à ces deux hôtes italiens (le journal du proxy montre des
    échecs de tunnel TLS sur `lacapanninadifranceschi.com` dès 04h04 UTC
    ce matin). Un seul nouvel essai fait, toujours en échec — conforme à
    la règle de ne pas s'acharner. Rien changé aux fiches ; à retester à
    la prochaine passe.
- **Mémoire du radar** (`memoire.py changements`) : 0 changement de date
  détecté sur 7 jours.
- **Registre `a-reverifier.md`** : relu. Sur les 17 doutes encore ouverts
  (dates de fin de saison estimées, datés du 20-25/08), 12 fiches sont
  déjà purgées (le doute est devenu sans objet) ; il n'en reste que 4
  présentes, dont 2 hors fenêtre live (déjà passées, purge automatique
  dans les prochaines semaines) et 2 encore vivantes avec une marge
  confortable avant leur `d2` estimé (Bagni Fiore Paraggi/Langosteria,
  30/09 ; terrasses des palaces parisiens, 04/10) — pas d'urgence à les
  retrancher aujourd'hui, laissées en l'état pour une prochaine passe avec
  plus de temps dédié à la re-vérification à la source.

## LOI DU SITE

`reste.py` sur `index-full.html` reconstruit : 374/374 traductions,
361/374 séjours, 371/374 invitations au global — recompté en croisant avec
la fenêtre live (auj.→+90j, 187 fiches) : **0 séjour et 0 invitation
manquants**. Les manquants globaux sont tous des événements déjà passés
(conservés 30 jours avant purge). **LOI DU SITE honorée à 100 % sur ce
qu'un visiteur voit réellement aujourd'hui.**

## Couverture — vérification des priorités historiques de la doctrine

Trois chantiers marqués comme prioritaires par des sections plus anciennes
de la doctrine ont été recomptés ce jour et sont **résorbés** :
- Automne (sept-déc.) : 32 / 29 / 21 / 32 fiches à venir par mois — bien
  loin du trou d'octobre/novembre constaté fin juillet.
- Joaillerie en fenêtre live : **14 fiches** (contre 2 le 20/08, seuil
  cible de 10 dépassé).
- Guides d'accès (`c=acces`) : **16 fiches** en ligne, dont les six guides
  annoncés le 24/08 et les POINT D'ENTRÉE antérieurs.
Aucune action nécessaire sur ces trois fronts aujourd'hui.

## Contrôles

- `validate.py` : **OK — 0 blocker, 4 warning** (1 entrée périmée du
  bandeau Ouvertures & délais à retirer ; 1 fiche `iv.g` et 7 fiches
  `iv.w` toujours > 1200 car., toutes légitimement denses, cf. ci-dessus ;
  bandeau « Été » encore affiché — normal avant l'équinoxe du 22-23/09).
- `perfcheck.py` : **OK — 0 régression** (poids 0.88 Mo gzip, -0.01 Mo vs
  dernier point, -5 événements/-3 séjours — purge normale de ce matin).
- `healthcheck.sh` : **OK** — http=200, date fraîche, 374/374 événements
  servis en ligne, conforme au build publié.

## Publication

`publier.sh` a régénéré le socle SEO (`gen_seo.py`) et les pages
indexables (`gen_pages.py`), validé, commité et **poussé directement sur
`main`** — pas de repli sur branche `claude/*` nécessaire aujourd'hui.
Eyebrow avancé au 11 septembre 2026.

Étape 10 de la doctrine (republier l'artifact Claude) **non tentée** :
panne connue depuis le 21/08/2026 (« artifact not found »), sans
conséquence pour le public — constanceparis7.com reste la seule adresse
qui compte et elle est à jour.

## Visites

**2631 visiteurs/pages vues le 11/09**, en progression continue et lente
depuis une semaine (2511 → 2519 → 2529 → 2552 → 2573 → 2598 → 2615 → 2631,
soit +4,8 % sur 7 jours). Le compteur global ne détaille ni pays ni source
d'entrée pour cette passe ; aucune analyse fine (répartition géographique,
provenance Instagram/Google) faite aujourd'hui faute de temps dédié — à
reprendre à une prochaine passe si utile, sans inventer de chiffre.

## Ce qui n'a pas été fait aujourd'hui, à reprendre

- Pas de recherche de nouveaux événements ni d'élargissement de couverture
  géographique (destinations de la carte à conquérir) : la vérification
  de l'état des lieux (condensation, LOI DU SITE, couverture) a montré
  que le site est déjà sain sur tous les fronts prioritaires connus ; le
  temps a été mis sur l'entretien (purge, liens, registre de doutes)
  plutôt que sur l'ajout, ce qui est conforme à la consigne « au moindre
  doute, ne pas ajouter » plutôt que d'ajouter du contenu sous pression de
  temps.
- Registre `a-reverifier.md` : les 4 doutes encore présents sur le site
  n'ont pas été retranchés faute de recherche dédiée aujourd'hui — aucun
  n'est urgent (marge de 2-3 semaines avant leur `d2` estimé).
- Aucune nouvelle leçon à ajouter à `lessons.md` : rien d'inattendu
  aujourd'hui, si ce n'est la confirmation que le backlog de condensation
  annoncé par une consigne figée peut être périmé — déjà couvert par la
  discipline existante (toujours revérifier l'état réel plutôt que suivre
  un chiffre daté sans le recroiser).
