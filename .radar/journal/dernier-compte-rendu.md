# Compte rendu — passe du 12/09/2026

Cadence : dernier run journalisé la veille (11/09), pas de rattrapage nécessaire.

## Priorité annoncée par la consigne (condensation `iv`) — vérifiée, toujours résorbée

La consigne du jour redemandait de condenser 15-20 fiches sur un backlog « 255
fiches, 159 en fenêtre live » daté du 19/08. Ce chiffre reste **périmé**,
confirmé une nouvelle fois : `validate.py` ne signale plus que 1 fiche `iv.g`
et 7 fiches `iv.w` au-delà du seuil WARN de 1200 caractères — les mêmes
qu'au 10-11/09, toutes déjà relues et classées légitimement denses (beaucoup
de contacts et de tarifs réels, pas un journal d'enquête). Rien touché sur ce
chantier aujourd'hui, à raison : forcer une condensation aurait supprimé des
faits réels pour gagner des caractères.

## Entretien du jour

- **Zombies purgés** : 2 fiches à `d2=2026-08-12` (Festival de Ramatuelle 41e
  édition, Gala Night Hotel Cala di Volpe). 374 → 372 événements.
- **Bandeau « Ouvertures & délais »** : 1 entrée périmée retirée
  (L'École des Arts Joailliers, `data-exp=2026-09-10`). 3 entrées actives
  restantes (Journées Particulières LVMH, Grand Prix de Monaco 2027, Royal
  Ascot 2027).
- **Liens à 7 jours** : 120 URL testées (les plus imminentes), 0 lien mort.
- **Mémoire du radar** (`memoire.py changements`) : 0 changement de date
  détecté sur 7 jours.
- **Correction factuelle, fiche Melbourne Cup / Birdcage (Flemington)** :
  un contrôle adversarial dédié (pas une recherche de nouveauté — la fiche
  existait déjà, complète, née le 24/08) a trouvé une dérive de deux ans sur
  la liste des marques du Birdcage citée dans `iv.o` : « Penfolds » a quitté
  le partenariat vin du VRC mi-2025 (remplacé par De Bortoli Wines, contrat
  de 3 ans) et le naming du Derby Day est passé de « Penfolds Victoria Derby
  Day » à « Howden Victoria Derby Day » ; « Myer » et « Emirates » n'apparaissent
  plus dans les annonces officielles VRC du Birdcage 2024-2026. Corrigé en
  français (liste ramenée aux marques confirmées : Lexus, Crown, G.H. Mumm ;
  prix du Rails Pedestrian Pass ajouté : 150 AUD). Le tarif du marquee
  (1895 AUD) était exact mais ambigu : précisé qu'il s'agit du seul Cup Day,
  les 3 autres journées du Carnival étant moins chères (Howden Victoria Derby
  Day 895 AUD, Oaks Day 795 AUD, Stakes Day 525 AUD). Les traductions
  `iv_o`/`iv_w` des 12 langues, devenues obsolètes par cette correction, ont
  été retirées (repli sur le français, exact) plutôt que laissées à décrire
  des marques parties — à retraduire à une prochaine passe. Date, contact
  billetterie/adhésion et séjour (Crown Towers Melbourne, Park Hyatt
  Melbourne, Vue de Monde, Attica) confirmés inchangés à la source.
- **Carte des destinations à conquérir** (doctrine, section Horizon roulant) :
  vérification systématique par mot-clé sur les 372 fiches. Constat notable :
  la quasi-totalité des destinations listées par la doctrine sont déjà
  couvertes par une fiche réelle et vérifiée (Sotogrande, Megève, Kitzbühel,
  Rio/Copacabana, Buenos Aires/Palermo, AlUla, Hong Kong, Bali, Mumbai,
  Maldives, Mustique, Las Vegas F1, Miami, Côme, Taormina, Porto Heli,
  Dubrovnik, Vienne...). Restent sans fiche : Aspen, Comporta/Melides,
  Udaipur, Harbour Island, Casa de Campo, Spetses. Recherche faite sur
  chacune pour un événement daté d'ici mi-décembre digne du site : rien de
  calibre ADN Riviera trouvé avec une porte d'entrée publiée et non privée
  (Aspen : galas déjà passés ou hors saison ; Spetses : régate classique en
  juin, hors saison ; les autres : rien de daté et billeté trouvé). Conforme
  à la consigne « au moindre doute, ne pas ajouter » : rien ajouté plutôt
  qu'une fiche fragile.

## Chantier engagé : traduction de `/note.html` (12 langues)

Chantier identifié dans `CHANTIERS.md` comme reste ouvert depuis le 27/08
(« /note.html : reste à traduire »). Constat : la page n'existait qu'en
français, `gen_pages.py` ne la générait jamais pour les 12 autres langues.
Corrigé :
- 22 clés de texte ajoutées au dictionnaire éditorial (`PFR` dans
  `gen_pages.py`) et à `pages-i18n.json` ;
- `gen_pages.py` génère désormais `/<lang>/note.html` pour les 13 langues,
  vitrine des 3 meilleures notes du moment localisée (nom d'événement et lien
  dans la langue de la page) ;
- traductions en cours via agent dédié au moment de la publication de ce
  compte rendu — si non arrivées à temps, les 12 pages existent déjà et
  s'affichent correctement en français par repli (comportement normal du
  site en cas de traduction manquante), sans régression ; à compléter dans
  la même journée ou la suivante dès réception.

## LOI DU SITE

`reste.py` : 372/372 traductions, 361/372 séjours, 369/372 invitations au
global — croisé avec la fenêtre live (auj.→+90j, 187 fiches) : **0 séjour et
0 invitation manquants**. Tous les manquants globaux sont des événements déjà
passés (conservés 30 jours avant purge). **LOI DU SITE honorée à 100 % sur ce
qu'un visiteur voit aujourd'hui.**

## Contrôles

- `validate.py` : **OK — 0 blocker, 3 warning(s)** (1 fiche `iv.g` et 7 fiches
  `iv.w` toujours > 1200 car., stables depuis le 10/09 et légitimement
  denses ; bandeau « Été » encore affiché — normal avant l'équinoxe du
  22-23/09).
- `healthcheck.sh` : **OK** — http=200, date fraîche, 372/372 événements
  servis en ligne, conforme au build publié.

## Publication

`publier.sh` a régénéré le socle SEO et les pages indexables, validé,
commité et **poussé directement sur `main`** — pas de repli sur branche
`claude/*` nécessaire aujourd'hui. Deux publications au fil de l'eau :
purge + bandeau, puis correction Melbourne Cup + infrastructure `/note.html`.

Étape 10 de la doctrine (republier l'artifact Claude) **non tentée** : panne
connue depuis le 21/08/2026 (« artifact not found »), sans conséquence pour
le public.

## Visites

**2644 visiteurs/pages vues le 12/09**, +13 vs la veille (2631), progression
lente et continue conforme à la tendance des sept derniers jours (+4,8 %/
semaine). Aperçu de la semaine (5-12/09, GoatCounter public) : l'accueil
reste la page la plus vue (46 visites sur la période) mais en repli (-54 %,
la mise à jour quotidienne du site répartissant le trafic sur plus de
fiches) ; plus notable, deux pages en forte hausse à la veille de leur
événement : la page Paris Fashion Week Printemps-Été 2027 (+375 %) et la
version arabe du SailGP Saint-Tropez, qui se tient précisément aujourd'hui
et demain (+333 %) — signe que le radar capte du trafic dans la fenêtre
utile, juste avant l'événement.

## Ce qui n'a pas été fait aujourd'hui, à reprendre

- Traductions `/note.html` : à vérifier/compléter si l'agent de traduction
  n'a pas rendu à temps pour cette publication (voir section dédiée).
- Registre `a-reverifier.md` : les 2 doutes encore vivants (Bagni Fiore/
  Langosteria Paraggi, d2 estimé 30/09 ; terrasses des palaces parisiens,
  d2 estimé 04/10) n'ont pas été retranchés — marge de 2-3 semaines, pas
  d'urgence. Piste trouvée mais non confirmée à la source primaire : le
  Plaza Athénée afficherait une saison « mai-septembre » pour sa Cour Jardin
  et sa Terrasse Montaigne (résumé de recherche, pas une page officielle
  lue directement) — à vérifier avant de raccourcir quoi que ce soit, le
  groupe restant sur le plancher du Crillon (04/10) en attendant.
- Aucune recherche de nouveaux événements hors vérification de la carte des
  destinations : le temps a été mis sur l'entretien, une correction
  factuelle vérifiée et le chantier de traduction, conformément à la
  consigne de ne rien ajouter sous doute.
