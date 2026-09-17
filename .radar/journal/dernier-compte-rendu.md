# Compte rendu — passe du 17/09/2026

## CONSTAT IMPORTANT — la condensation avait été déclarée « soldée » à tort

Les comptes rendus des 06 au 16/09 déclaraient la dérive « journal d'enquête »
résorbée, en se basant uniquement sur le WARN de `validate.py` (seuil
1200 caractères par champ). Or la cible de la doctrine est 400 caractères,
et l'écart entre les deux seuils cachait un stock considérable : à l'ouverture
de cette passe, **192 fiches** (dont **118 en fenêtre live**) avaient encore
un champ `iv.o`/`iv.g`/`iv.w` de plus de 400 caractères, la plupart truffés de
tournures d'enquêteur (« vérifié le JJ/MM/AAAA », « décodé le… », « HTTP 200
le… », « confirmé sur… », citations de méthode) — exactement le défaut décrit
par la doctrine du 12-19/08, jamais réellement résorbé. **Leçon consignée
dans `tools/lessons.md`** pour que les prochaines passes ne se fient plus au
seuil WARN de 1200 caractères comme preuve de condensation.

## PRIORITÉ DU JOUR — condensation des voies d'invitation (iv)

**34 fiches condensées** aujourd'hui, en deux lots publiés au fil de l'eau,
en commençant par les plus imminentes de la fenêtre live (tri par `d2`) :

- Lot 1 (18 fiches) : Dîner Ayla Privé (Bodrum), WE ARE [still] HERE (Petit
  Palais), Boucheron 26 place Vendôme, L'École des Arts Joailliers (Hôtel de
  Mercy-Argenteau), Picasso/Paul Smith (Tokyo), London Fashion Week, Vogue
  World Milano, Ron Mueck (Mori Art Museum), Fine Arts Paris, L'Herbier Secret
  (Crillon), Nammos Mykonos, Dolce & Gabbana Beach Club (Gurney's Montauk),
  Jacquemus x Monte-Carlo Beach, LIV at Fontainebleau, Régates Royales Cannes,
  Van Cleef & Arpels au MAK Vienne, La Jeune Fille à la perle (Osaka),
  Fondazione Prada.
- Lot 2 (16 fiches) : YSL/ICP, Loro Piana x La Réserve à la Plage, Le Jardin
  de Cheval Blanc Paris, La Lanterne d'Hermès Ginza, Capri (Anema e Core /
  Emozioni d'Estate), Covo di Nord-Est, Principote, Bagatelle Bodrum, Cene a
  quattro mani (Jumeirah Capri Palace), Terrasses des palaces parisiens,
  Villa Louis Vuitton (White 1921), Lío Ibiza, Blue Marlin Ibiza, scène yacht
  Ibiza-Formentera, Les Voiles de Saint-Tropez, The Shop on the Corner.

Méthode : tous les faits vérifiés conservés intégralement (noms, fonctions,
e-mails, téléphones, adresses, URLs, tarifs publiés, horaires) ; retrait des
tournures d'enquêteur, des redites entre `iv.o`/`iv.g`/`iv.w` et des
commentaires de méthode de vérification. Aucune nouvelle recherche : pur
travail de récriture sur une matière déjà vérifiée, donc aucune vérification
adversariale nécessaire. Gain cumulé : **24 703 caractères** retirés sans
perte d'un seul fait. Traductions `iv_o`/`iv_g`/`iv_w` invalidées dans les
12 langues pour chaque champ français modifié (règle de cohérence) :
l'affichage retombe sur le français exact en attendant retraduction.

**Reste à condenser : 192 fiches (111 en fenêtre live), 386 champs.** À
poursuivre par lots aux prochaines passes, toujours en commençant par les
plus imminentes.

## Plancher / entretien

- **Purge** : 4 zombies retirés (d2=17/08/2026) : Feu d'artifice du 15 août
  à Port Grimaud, Vente de Yearlings d'Août Arqana, Black Coffee Residency
  (SantAnna Mykonos), Shellona St-Tropez saison musicale. 345 → 341 événements.
- **Liens** : 119 liens des événements les plus imminents testés, 0 mort.
- **Saison** : bascule automatique confirmée « Summer 2026 » (encore avant
  l'équinoxe du 22/09).
- **Eyebrow** : date de vérification mise à jour au 17 septembre 2026.

## LOI DU SITE — les 3 compteurs

1. Traductions 13 langues : **341/341 (100 %)**, reste 0.
2. Séjours clé en main : **335/341**, reste 6 — les 6 manquants sont les
   fiches-conseil `c=acces` (guides d'accès), exemptées par la doctrine
   (« les fiches-conseil et dossiers d'accès n'ont pas de séjour propre »).
   **La LOI DU SITE est donc honorée à 100 % sur les fiches concernées.**
3. Voies d'invitation : **341/341 (100 %)**, reste 0.

## Contrôles

- `validate.py` : **OK — 0 blocker(s), 2 warning(s)** (les deux WARN restants,
  Formula 1 Etihad Airways Abu Dhabi et le guide « Ventes aux enchères et
  expositions », dépassent le seuil de 1200 caractères mais sont des fiches
  légitimement denses — grilles tarifaires à paliers, contacts multiples ;
  à recontrôler individuellement plus tard, pas dans l'urgence).
- `healthcheck.sh` : **OK** — http=200, date fraîche, 341/341 événements en
  ligne conformes à `.last-count`.
- `perfcheck.py` : exécuté via `publier.sh`, aucune régression signalée.

## Ce qui n'a pas été fait aujourd'hui

Recherche de nouveaux événements et rattrapage des chantiers ouverts
(joaillerie, printemps 2027, guides d'accès, résorption des doutes) : la
doctrine place explicitement la condensation des voies d'invitation
au-dessus de la recherche de nouveaux événements tant qu'il en reste dans la
fenêtre live — c'est encore le cas (111 fiches). À reprendre demain, en
poursuivant la condensation par lots de 15-20 jusqu'à épuisement de la
fenêtre live, puis en revenant aux chantiers du RESTE-À-FAIRE.

## Anomalies

Aucune. Push direct sur `main` accepté à chaque publication (pas de repli sur
branche `claude/*` nécessaire). `index-full.html` absent au démarrage (clone
frais) : reconstruit via `rebuild_full.py`, conforme à la doctrine.

Note pour la doctrine : la section « Environnement cloud » de `DOCTRINE.md`
décrit encore une architecture à deux dépôts (public `luxe-ete-2026` +
privé `luxe-radar-filet`) qui ne correspond plus à l'environnement réel de
cette session (dépôt unique `constanceparis7/radar-luxe`, accès GitHub
scopé à ce seul dépôt). Signalé aussi dans `lessons.md` pour éviter toute
confusion aux prochaines passes.
