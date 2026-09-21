# Compte rendu — passe du 21/09/2026 (session cloud)

## Démarrage

Clone superficiel (`git rev-parse --is-shallow-repository` → true, 53 commits
au lieu des ~650 réels) : `git fetch --unshallow origin` fait dès le début,
comme la leçon du 20/09 le demande. Aucune anomalie de cadence (dernier run
la veille, dans le seuil normal). `.radar/DOCTRINE.md`, `.radar/PASSATION.md`
et `.radar/tools/lessons.md` (1174 lignes) lus intégralement avant tout
travail.

## Priorité du moment : condensation des voies d'invitation — chantier retombé à zéro dérive réelle

Lecture intégrale des 11 champs `iv.o`/`iv.g`/`iv.w` au-dessus du seuil WARN
de `validate.py` (1200 car., de « POINT D'ENTRÉE, Ventes aux enchères »
2675 car. à « Milan en mode Ferragosto » 1207 car.) et des 25 fiches les plus
imminentes de la fenêtre live parmi les 86 encore au-dessus du seuil cible de
400 car. (Fondazione Prada, Ron Mueck, Nammos Mykonos, Loro Piana x La Réserve,
Chanel East Hampton, Le Jardin de Cheval Blanc, Hermès Ginza, Gucci Flora,
Capri, La Co(o)rniche, Bagni Fiore, Covo di Nord-Est, Bagatelle Bodrum,
Jumeirah Capri Palace, Grand Hôtel de Cala Rossa, F1 Abu Dhabi, Gstaad New
Year Festival, Melbourne Cup…), plus un détecteur automatique (motifs de
dérive + sous-chaîne >60 car. dupliquée entre champs, méthode du 20/09/2026).

**Résultat : zéro dérive « journal d'enquête » trouvée.** Tout l'excédent est
de la densité factuelle légitime — plusieurs contacts nominatifs, tarifs et
horaires réels par fiche, exactement le constat déjà fait le 20/09 sur un
échantillon plus restreint, mais ici sur la quasi-totalité du stock restant.
Conformément à la doctrine elle-même (« si tu n'as rien trouvé de digne, ne
publie rien »), aucune fiche n'a été retouchée : forcer un quota de 15-20
fiches condensées sur du contenu déjà sain aurait repris le risque identifié
les 21/08 et 25/08 (URL abrégées, adresses déformées par un exercice de
concision inutile). Nouvelle leçon consignée dans `lessons.md` avec le détail
des 11+25 fiches relues. Le chantier condensation passe donc en mode
ENTRETIEN : à ne relancer que si un nouveau signal de dérive réapparaît.

## Purge

1 zombie purgé (« Taste of Tennis New York 2026 », fin 21/08/2026, >30 j).
336 → 335 événements en ligne.

## Test hebdomadaire des liens (lundi)

232 URL uniques à venir testées (HEAD threadé) : 190×200, 26×403 (bloqué mais
vivant, convention du site), 4×429, 3×202, **0×404**. 6 domaines ont échoué de
façon persistante (chateaudechantilly.fr, theatre-chaillot.fr, atlantis.com,
marinabaysands.com, oneandonlyresorts.com, opera.mc) avec une erreur de
certificat TLS répétée (curl erreur 60) malgré 3 essais et un `--cacert`
explicite, alors que des domaines témoins (google.com) et la quasi-totalité
des 232 URL passaient normalement — incident d'environnement (tunnel proxy
capricieux, confirmé par `$HTTPS_PROXY/__agentproxy/status`), pas un verdict
sur les fiches. Rien changé, à retester la semaine prochaine. Détail et
nouvelle règle consignés dans `lessons.md`.

## Vague des imminents (lundi)

Nouveau candidat détecté par le calcul systématique (Note du radar ≥ 85,
J+7 à J+28, durée ≤ 30 j) : **Qatar Prix de l'Arc de Triomphe 2026** (Note 88,
3-4 octobre, J+12) — le nom qui claque le plus mondialement reconnu de la
sélection du jour (deux autres candidats, un gala du New York Philharmonic et
un gala du New York City Ballet, écartés par prudence : notoriété trop
new-yorkaise/niche pour le test du nom, doctrine « en cas de doute,
s'abstenir »). Page de destination `/prix-de-larc-de-triomphe.html` créée,
composée uniquement de contenus déjà vérifiés (la fiche elle-même, 3 Questions
existantes sur le sujet : prix, dress code, enclosure), liens vers Le Protocole,
Octobre à Paris, deux galas parisiens de la même semaine (Global Gift Gala,
ADOR's Gala Dinner) et la fiche complète. `validate.py` : 0 blocage.

## Recherche complémentaire : Bal de la Rose / Gala Croix-Rouge Monaco 2027 — pas de fiche créée

Vérification à la source (montecarlosbm.com, croix-rouge.mc, communiqué de
presse officiel) : ce sont deux galas DISTINCTS (Bal de la Rose en mars,
Fondation Princesse Grace ; Gala de la Croix-Rouge monégasque en juillet,
Prince Albert II/Princesse Charlène), tous deux à la Salle des Étoiles du
Sporting Monte-Carlo. **Aucune date 2027 n'est encore annoncée pour l'un ou
l'autre** à ce jour. Conformément à la règle du « bouchon du 31 août »
(jamais de date devinée présentée comme sûre), aucune fiche n'a été créée
cette passe. Des contacts presse nominatifs réels existent pour le Gala
Croix-Rouge 2026 (Sylvie Cristin, SBM ; deux contacts Croix-Rouge monégasque)
mais au format `initiale.nom@`, donc à filtrer par `contacts_classer.py`
avant toute mise en fiche le jour où 2027 sera annoncé. À reprendre à une
passe future, une fois la date confirmée à la source.

## État de la LOI DU SITE (iv + séjour + traductions)

`reste.py` : traductions 335/335 (100 %), voies d'invitation 335/335 (100 %),
séjours 329/335 — les 6 manquants sont les fiches-guide `c=acces` (« POINT
D'ENTRÉE… »), exemptées par la doctrine. **0 écart réel.** Joaillerie : 13
fiches en fenêtre live (chantier du 20/08 résolu, largement au-dessus du
plancher de 10). Les 8 ancres printemps 2027 sont toutes présentes sur le
site. Bandeau Ouvertures & délais : 3 entrées, aucune périmée.
`memoire.py changements` : 0 changement de date à consigner cette semaine.
Bascule de saison : pas encore due (équinoxe d'automne calculé après le
21/09 ; le titre reste « Summer 2026 », normal, rien à retraduire).

## Analyse des visites

Compteur cumulé à 3 000 visiteurs/pages vues (GoatCounter), +39 depuis la
veille (2 961 → 3 000), dans la continuité de la croissance régulière des
derniers jours (+45, +49, +47, +29, +39) — toujours dans le palier 1 (35 à
100/jour) de la feuille de route, sans rupture ni pic.

## Anomalies et non-fait

- 6 domaines non vérifiables cette semaine (incident réseau, voir ci-dessus).
- `healthcheck.sh` OK (335/335, date fraîche) ; la page fraîchement publiée
  `/prix-de-larc-de-triomphe.html` répond encore 404 en direct au moment
  d'écrire ce compte rendu — propagation GitHub Pages normale, à confirmer à
  la prochaine passe.
- Search Console non consultée cette passe (pas d'accès direct dans cet
  outillage) ; à faire par Constance/Gérald ou une session avec cet accès.
- Le chantier « Feuille de route » (O1-O9, newsletter, en-têtes de sécurité,
  Cloudflare) n'a pas été touché : hors du périmètre de la passe quotidienne
  de contenu, laissé aux sessions dédiées à ce chantier. Compteur d'événements
  de O4 mis à jour (341 → 335).

## Publication

Deux commits poussés directement sur `main` (aucun repli de branche
nécessaire) : purge + nettoyage `.gitignore`, puis la page imminente Arc de
Triomphe. Signature `radar-routine-claude` posée avant chaque commit. Journal
privé (lessons.md, ce compte rendu) à pousser à la suite.
