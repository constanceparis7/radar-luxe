# Compte rendu de la passe du 06/10/2026

**Résultat : passe partielle. 2 zombies purgés, 6 fiches condensées (16 champs), aucune fiche ajoutée. Publié directement sur main (le push sur main a été accepté, pas de repli claude/*). validate OK : 0 blocage, 2 avertissements de longueur.**

## Fait
- Doctrine, passation et leçons lus ; identité radar-routine-claude posée ; clone déshallowé ; `index-full.html` reconstruit.
- Au démarrage `validate.py` : FAIL (2 zombies d2 du 05/09 : Singapore Night Festival, Ravello Festival). `passe_automatique.py --apply --max-liens 0` a fonctionné (292 -> 290).
- **Condensation iv** sous contrôle des faits (`condenser_iv.py`) : Negresco, Fondazione Prada Venise (Helter Skelter), Cheval Blanc St-Barth (Réveillon), Melbourne Cup Birdcage, Christie's Magnificent Jewels, Clubs privés Mayfair. Aucun e-mail, téléphone, URL, tarif, horaire ou date perdu (le standard du Negresco a migré de iv.w vers iv.o). Christie's : l'incohérence entre iv.o (« salle non communiquée ») et iv.g (Four Seasons Hôtel des Bergues, confirmé) est résolue en faveur du lieu confirmé. Traductions `iv_*` des champs modifiés retirées (repli français exact).
- Compteurs `reste.py` : traductions 290/290, invitations 290/290, séjours 284/290 (6 restants).

## Non fait / non vérifié
- Seulement 6 fiches condensées sur les 15-20 demandées : sur 59 fiches de la fenêtre live au-dessus de 400 caractères, les autres lues (Maeght, Loewe, Nikki Beach, Dior Spa, etc.) sont des modes d'emploi propres, denses de faits réels ; les réécrire n'aurait gagné que quelques dizaines de caractères au prix d'un risque de perte de fait (leçons du 21/08, 25/08, 21/09). Il reste donc environ 53 fiches au-dessus de 400 car., en majorité de la densité factuelle légitime.
- Aucune recherche de nouveautés, aucun candidat du vivier, aucune revérification à la source, aucun séjour restant, pas de mesure mobile (pas un lundi). Faits condensés repris des champs existants, non revérifiés dehors.
- Textes périmés à revérifier : plusieurs fiches de saison d'été encore en cours (Milan Ferragosto, Villa Carmignac, Cap-Eden-Roc, Casa Amor, Chanel La Mistralée) ; Negresco (dernières dates de concerts publiées 30/09).
- Alerte cadence de `precheck.sh` (106 h) : à lire comme faux positif, `run-log.ndjson` n'est plus alimenté (passages.log montre une passe quotidienne).
