# Compte rendu — passe du 20/09/2026 (session cloud)

## Anomalie de déclenchement

`precheck.sh` a signalé une cadence rompue : dernier run journalisé il y a 35 h
(seuil 30 h). Pas de trace de passe complète le 19/09 après-midi/soir — la
passe de ce jour est une passe de RATTRAPAGE. Aucune cause identifiée dans le
dépôt (pas d'erreur, pas de commit orphelin).

## Priorité du moment : condensation des voies d'invitation

Sélection au seuil CIBLE (≥400 caractères sur `iv.o`/`iv.g`/`iv.w`, priorité
fenêtre live, plus imminentes d'abord) : 110 fiches en fenêtre live dépassent
ce seuil. Avant de lancer des agents en série, lecture intégrale d'une
vingtaine des plus imminentes (Fondazione Prada Milan, ICP New York, Milano
Fashion Week, Nikki Beach Ibiza, Christie's Genève, Dior Saint-Tropez, Chaumet
Vendôme, Chanel East Hampton, Covo di Nord-Est, Sotheby's Genève…) : la
quasi-totalité sont déjà des modes d'emploi visiteur propres et directs, leur
longueur venant de faits réels nombreux (plusieurs contacts, tarifs, horaires
saisonniers), pas d'une dérive « journal d'enquête ». Un détecteur de motifs
(dates de vérification, formulations de méthode, redites entre champs) a
isolé 4 fiches avec une vraie dérive :

- **Amiri, boutique saisonnière Saint-Tropez** — condensée ET corrigée : l'adresse
  publiée (« avenue Maréchal Foch ») était fausse depuis l'origine ; vérifié ce
  jour à la source (store locator officiel amiri.com, en direct) : la boutique
  est au **21 rue Gambetta**. Corrigé dans le champ lieu et dans `iv`. Horaires
  aussi remis à jour (la fiche affichait un horaire d'été constant « 10h-21h » ;
  la période en cours, mi-septembre à octobre, ferme à 19h30, confirmé sur
  amiri.com/pages/stores). Retiré : une piste de contact presse explicitement
  non étayée que la fiche racontait au visiteur au lieu de la rejeter en
  silence.
- **Réouverture d'hiver de The Alpina Gstaad** — la liste des quatre agences
  presse par marché était recopiée mot pour mot dans `iv.o` ET `iv.g` ; gardée
  une seule fois (porte principale), `iv.g` recentré sur la nature de l'accès.
- **Réouverture d'hiver des Airelles Courchevel** — `iv.g` allégé du récit
  d'enquête (« aucune accréditation... aucun voyage de presse... ») en gardant
  tous les contacts, URL et téléphones.
- **Helter Skelter, Fondazione Prada Venise** — retiré le cadrage méthodologique
  (« vérifié à la source le 11/08/2026, page officielle lue en navigateur ») de
  `iv.g`/`iv.w`, gardé la citation officielle et tous les tarifs.

Contrôle mécanique `verif_faits.py` (dossiers séparés) : 1 alerte sur les 4
(URL Instagram raccourcie en `@amiri` sans le lien littéral) — corrigée avant
publication ; TOUT OK à la deuxième passe.

Le compteur global (186 fiches ≥400 car., 110 en fenêtre live) n'a pas bougé :
attendu, une fiche condensée qui garde plusieurs faits réels reste au-dessus
du seuil par construction (leçon du 20-21/08). Leçon nouvelle consignée dans
`tools/lessons.md` : le seuil de 400 caractères sert à SÉLECTIONNER, pas à
mesurer la dérive elle-même — seule la lecture le prouve. Poursuite aux
prochaines passes avec un détecteur de motifs pour trier les candidats avant
d'engager des agents, plutôt que de traiter tout le stock >400 comme une
dérive uniforme.

## Purge et vérification des liens

2 zombies purgés (fin de saison 20/08/2026, >30 j) : « White Party avec
Laurent Wolf, Casino Barrière » et « Dîner quatre mains Ayla Privé, Aret
Sahakyan × Francesco Sodano ». 338 → 336 événements en ligne. 119 liens des
événements les plus imminents testés : 0 mort. Bascule automatique de saison
du titre confirmée (Summer 2026, aucune anomalie — l'équinoxe n'est pas encore
atteint).

## LOI DU SITE — les trois compteurs (`reste.py`, fenêtre live)

- Traductions 13 langues : 336/336 (100 %)
- Voies d'invitation : 336/336 (100 %)
- Séjours clé en main : 330/336 (les 6 manquants sont des fiches-conseil
  `c=acces`, exemptées par doctrine)

Rien à rattraper de ce côté aujourd'hui.

## Bug d'environnement trouvé et corrigé

Le clone de cette session était **superficiel** (`git rev-parse
--is-shallow-repository` → true, 53 commits au lieu de ~650) : `main` local
avait aussi divergé de `origin/main` au démarrage (reset propre sur
`origin/main`, aucune perte — aucun travail local en cours). Le clone
superficiel désactivait en silence `tools/memoire.py changements` (règle
quotidienne de la doctrine), qui répondait poliment « rien à comparer » au
lieu d'échouer. Corrigé par `git fetch --unshallow origin` ; 6 changements de
dates ont alors été consignés dans `.radar/memoire.ndjson`. Leçon consignée
dans `tools/lessons.md`, et la section « Environnement cloud » de
`DOCTRINE.md` mise à jour (elle documentait encore, comme signalé le
17/09/2026, une architecture à deux dépôts qui n'existe plus pour cette
session — corrigé au passage).

## Contrôles

`validate.py` : OK — 0 blocker, 2 warnings résiduels (iv.g/iv.w encore >1200
car. sur 2+9 fiches, stables). `perfcheck.py` non lancé séparément (le
publieur l'inclut implicitement via `verrou.py`/`gen_pages`) — accueil à
852 Ko, cohérent avec la purge. `healthcheck.sh` : OK (http=200,
compte_live=336=attendu, date fraîche). 3 avertissements W1 mineurs
pré-existants (dates `dt` hors fenêtre machine sur Taste of Tennis New York,
Covo di Nord-Est, Nikki Beach Ibiza) : non traités, non bloquants — le
premier concerne un événement déjà passé qui sera purgé demain (30 j
atteints), les deux autres sont des dates d'ouverture de saison antérieures à
la fenêtre affichée, normales.

## Publication

Trois commits distincts poussés directement sur `main` (aucun repli de
branche nécessaire) : (1) purge + liens + saison, (2) condensation +
correction Amiri, (3) mémoire du radar. Journal privé (lessons.md, DOCTRINE.md,
ce compte rendu) poussé séparément.

## Non vérifié / reporté

- 110 fiches restent au-dessus du seuil-cible de condensation en fenêtre live,
  mais la lecture de ce jour indique que la grande majorité est déjà propre :
  à trier par détecteur de motifs avant d'engager des agents, plutôt qu'à
  traiter en bloc.
- Les 3 avertissements W1 (dates `dt`), non bloquants.
- Pas de recherche de nouveaux événements aujourd'hui : le temps de la passe
  est allé à la priorité de condensation, au diagnostic du clone superficiel
  et de la divergence de branche, conforme à la doctrine qui place la
  condensation avant la recherche.
- Analyse des visites non faite (GoatCounter non consulté ce jour, faute de
  temps) — à rattraper à la prochaine passe.
