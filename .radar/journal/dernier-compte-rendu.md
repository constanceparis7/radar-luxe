# Compte rendu — passe du 10/09/2026

Cadence : dernier run journalisé il y a 47 h (> seuil de 30 h) → passe de
RATTRAPAGE. Aucune anomalie trouvée dans le dépôt expliquant le jour manqué
(pas d'entrée `DEMARRAGE` sans `FIN` la veille) ; simple absence de
déclenchement, traitée normalement.

## Priorité du jour — condensation des voies d'invitation (`iv`)

Le backlog signalé (255 fiches, 159 en fenêtre live, le 19/08) est
**quasiment soldé** : au seuil WARN de `validate.py` (≥ 1200 caractères),
il ne restait que **7 candidats, tous dans la fenêtre live**. Les 7 ont été
lus intégralement (méthode du 02/09 : trier dérive réelle vs contenu
légitimement dense avant de toucher quoi que ce soit) :

- **1 fiche condensée** : « POINT D'ENTRÉE, Ventes aux enchères et
  expositions publiques (Christie's, Sotheby's, Drouot) » — `iv.w` réécrit
  en texte visiteur continu (suppression des titres en capitales et des
  commentaires de méthode type « brochure OFFRE 2025, à reconfirmer »),
  2951 → 2675 caractères. Contrôle mécanique (regex e-mails/URL/montants)
  avant/après : **aucun fait dur perdu** — un seul écart de forme
  (« www.drouot.com/... » devenu « drouot.com/... », même URL).
- **6 fiches examinées et laissées inchangées** (Villa Carmignac, Biennale
  Arte 2026, Yves Saint Laurent/ICP, Grand Hôtel de Cala Rossa, Gstaad New
  Year Music Festival, Formula 1 Abu Dhabi) : leur longueur vient de listes
  de tarifs/horaires/contacts réels et denses, pas d'un journal d'enquête —
  confirmé légitimement dense (même diagnostic que les 20-21/08 et 02/09).
  Les condenser aurait supprimé des faits pour gagner des caractères,
  contraire à la règle « garder le fait, jamais l'inverse ».

**Effet de bord attrapé en lisant ces 7 fiches** : 8 coordonnées
personnelles au format « mobile » explicitement labellisées comme telles
avaient migré dans le champ structuré `iv.c` de 3 fiches — en violation du
garde-fou de protection des personnes du 20/08/2026 (interdiction des
lignes présentées comme « directe » ou « mobile »). Retirées :
- Villa Carmignac : 3 portables (Juliette de Charmoy, Aurore Gallarino,
  Angie Linconnu) — noms et fonctions conservés.
- Gstaad New Year Music Festival : 3 portables suisses (Philippe Biland,
  Illyria Pfyffer, Caroline Murat) — noms et fonctions conservés.
- POINT D'ENTRÉE (ventes aux enchères) : 2 portables Drouot (Sophie
  Dufresne, Claire Jehl), explicitement labellisés « mobile publié par
  Drouot » dans le texte source — retirés ; leurs lignes directes de bureau
  (`+33 1 48 00 20 71` / `...37`, présentées comme numéros de poste
  professionnels du service presse, pas comme portables) sont restées en
  `iv.o`, où elles n'ont pas été touchées.

Aucune fiche ne perd sa dernière porte d'entrée (contrôle fait à la main
sur les 3 fiches touchées : chacune garde au moins un e-mail ou une ligne
de service).

## LOI DU SITE

`reste.py` (sur `index-full.html` reconstruit) : 379/379 traductions,
366/379 séjours, 376/379 invitations — les manquants sont recomptés
**tous hors fenêtre live** (événements passés, conservés 30 jours avant
purge). **LOI DU SITE honorée à 100 % sur la fenêtre live** (0 séjour et
0 invitation manquants parmi les 213 fiches auj.→+90j).

## Vérifications

- **Zombies** (`d2` < auj.-30j) : 0 — le plancher quotidien fait déjà son
  travail, rien à purger aujourd'hui.
- **Mémoire du radar** (`memoire.py changements`) : 0 changement de date
  détecté sur 7 jours.
- **Liens à 7 jours** : 27 URL uniques testées (événements qui démarrent ou
  se terminent dans les 7 prochains jours), `curl -sL` avec vérification du
  corps (pas seulement le code retour). Résultat : 0 « page introuvable »
  détectée dans le corps. Plusieurs 403 attendus (Espace Louis Vuitton
  Tokyo, Peninsula Paris, FEI League of Nations, Rocco Forte Verdura) —
  anti-robot connu de ces domaines, pas une preuve d'absence ; aucun
  signal de régression par rapport à leur état de vérification d'origine,
  pas d'action prise.
- `validate.py` : **OK — 0 blocker, 3 warning** (1 fiche `iv.g` et 7 fiches
  `iv.w` encore > 1200 car., toutes légitimement denses ; bandeau « Été »
  encore affiché au 10/09, normal — l'équinoxe n'est que le 22-23/09,
  bascule automatique par `saison.py`, rien à faire avant cette date).
- `perfcheck.py` : **OK — 0 régression** (poids 0.89 Mo gzip, -0.02 Mo vs
  dernier point, -13 événements/-7 séjours d'écart de référence — purges
  normales des jours précédents).

## Publication

`publier.sh` a régénéré le socle SEO (`gen_seo.py`) et les pages
indexables (`gen_pages.py`, 363 événements × 13 langues), validé, commité
et **poussé directement sur `main`** (pas de repli sur branche `claude/*`
nécessaire aujourd'hui). Eyebrow avancé au 10 septembre 2026.

Étape 10 de la doctrine (republier l'artifact Claude) **non tentée** :
panne connue et documentée le 21/08/2026 (« artifact not found »), sans
conséquence pour le public — constanceparis7.com reste la seule adresse qui
compte et elle est à jour.

## Visites

Relevé du jour ajouté (`relever_visites.py`, absent avant ce matin) :
**2615 visiteurs/pages vues le 10/09**, en progression régulière depuis une
semaine (2519 → 2529 → 2552 → 2573 → 2598 → 2615, soit +4 % sur 5 jours,
une croissance lente et continue plutôt qu'un pic). Le compteur global ne
détaille ni pays ni source d'entrée pour cette passe : aucune répartition
géographique ni provenance (Instagram/Google) n'a été consultée aujourd'hui
faute de temps dédié à l'analyse fine — à ne pas inventer, à reprendre à la
prochaine passe si utile.

## Ce qui n'a pas été fait aujourd'hui, à reprendre

- Pas de recherche de nouveaux événements ni d'élargissement de couverture
  (Riviera d'Athènes, Lac de Côme, etc.) : la priorité du jour (condensation
  + garde-fou vie privée) a occupé le temps disponible, et le backlog `iv`
  étant désormais quasi soldé, la prochaine passe peut revenir à la
  recherche/l'élargissement de couverture ou aux guides d'accès sans
  urgence de rattrapage.
- Pas de test hebdomadaire complet des liens (réservé au lundi ; nous
  sommes jeudi) — seul le test à 7 jours a été fait, conforme à la doctrine.
- Aucune nouvelle leçon à ajouter à `lessons.md` : rien d'inattendu
  rencontré aujourd'hui, la méthode de condensation du 20/08-02/09 a
  fonctionné sans incident sur les 7 candidats restants.
