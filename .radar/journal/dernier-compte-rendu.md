# Compte rendu de la passe du 04/10/2026

**Résultat : passe partielle. 15 fiches condensées, 1 zombie purgé, aucune fiche ajoutée.**

## Fait
- Doctrine, passation et leçons lus ; identité git radar-routine-claude posée ; clone déshallowé ; `index-full.html` reconstruit.
- Au démarrage `validate.py` : FAIL (1 blocage : zombie Premio Internazionale Fondazione Taormina Art, d2 du 03/09). `passe_automatique.py --apply --max-liens 0` (purge seule) a fonctionné cette fois : fiche retirée (294 -> 293).
- Compteurs `reste.py` : traductions 294/294, invitations 294/294, séjours 288/294 (6 restants), avant purge.
- **Condensation iv** : 20 champs `iv.o/g/w` réécrits sur 15 fiches de la fenêtre live (celles qui finissent le plus tôt) : Cartier NGV, Circuit mannequins, The Shop on the Corner, David Guetta Ushuaïa, Sofitel Icônes, Paris Fashion Week PE 2027 et ses 4 dossiers d'accès, Negresco, Nikki Beach Ibiza et Mallorca, Palaces de la presqu'île, Loewe Saint-Tropez. Outil `condenser_iv.py` : aucun e-mail, téléphone, URL, montant, horaire ou date perdu (0 exception). Traductions `iv_*` des champs modifiés retirées (repli français exact).

## Non fait / non vérifié
- Aucune recherche de nouveautés, aucun candidat du vivier traité, aucune revérification (`reverification-prioritaire.json`), séjours restants non faits, pas de mesure mobile (pas un lundi).
- Aucun contenu externe consulté : les faits condensés viennent des champs existants, non revérifiés à la source.
- Fiches périmées dans le texte, à revérifier : Sofitel « Icônes » (exposition dite finie le 20/09 mais d2 au 06/10), Terrasses des palaces parisiens (La Cour Jardin « jusqu'au 13/09 »), Blue Marlin/Ushuaïa (saison finissant 4-5/10).
- Restent 97 fiches de la fenêtre live avec un champ iv de plus de 400 caractères (matière factuelle dense surtout).
