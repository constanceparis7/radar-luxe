# Compte rendu de la passe du 02/10/2026

**Résultat : passe interrompue, aucun contenu du site publié.**

## Ce qui s'est passé
- Doctrine, passation et leçons lus en entier. Identité git posée (radar-routine-claude). Clone déshallowé.
- `rebuild_full.py` OK. Compteurs `reste.py` : traductions 296/296, invitations 296/296, séjours 290/296 (reste 6, à situer dans la fenêtre live à la prochaine passe).
- `validate.py` au démarrage : FAIL, 2 blocages, tous deux des zombies non purgés (d2=2026-09-01) : « Soldes d'été à Milan (saldi estivi) » et « Sanctum Saint-Tropez, saison club 2026 ». 2 avertissements iv.g / iv.w > 1200 car. (non bloquants).
- Pour les purger j'ai lancé `.radar/tools/passe_automatique.py --apply`, puis son essai à blanc. Le classifieur de permissions de la session a refusé les deux appels (motif « Blind Apply »). Je n'ai pas cherché de contournement.
- Sans purge, `publier.sh` refuse de publier (verrou rouge). Je n'ai donc ni traité de candidats du vivier, ni revérifié de fiches, ni condensé de `iv`, plutôt que de préparer un travail impubliable.

## Ce que je n'ai pas pu faire / vérifier
- Aucune recherche d'événements nouveaux, aucune revérification (file `reverification-prioritaire.json`), aucune condensation `iv` (la lecture du 26/09 avait conclu à zéro dérive réelle).
- Réseau : `madparis.fr` renvoie 000 depuis cette session (déjà vu avec d'autres domaines), `wikipedia.org` répond 200.
- Le vivier `candidats-evenements.json` (49 candidats) reste intact.

## À faire
- Le workflow `passe-quotidienne.yml` (8h40 Paris) purge ces zombies sans IA : la prochaine passe repartira d'un verrou vert.
- Si le blocage « Blind Apply » persiste sur `passe_automatique.py`, autoriser l'outil ou le faire tourner côté Actions uniquement.
