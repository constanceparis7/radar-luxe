# Compte rendu de la passe du 03/10/2026

**Résultat : passe partielle, verrou vert, 14 fiches condensées. Aucune fiche ajoutée.**

## Fait
- Doctrine, passation et début des leçons lus ; identité git radar-routine-claude posée ; clone déshallowé. `validate.py` au démarrage : OK (0 blocage, 2 avertissements). La purge des 2 zombies du 02/10 avait déjà été faite par le plancher Actions.
- Compteurs `reste.py` : traductions 294/294, invitations 294/294, séjours 288/294 (reste 6).
- **Condensation des voies d'invitation** : 14 fiches de la fenêtre live, 19 champs `iv.o/g/w` réécrits à l'adresse du visiteur : Negresco, Nikki Beach Ibiza, Cap-Eden-Roc, Journées Particulières LVMH, Casino Barrière Le Touquet, Sofitel Le Faubourg (Icônes), Paris Fashion Week PE 2027, Kulm Saint-Moritz, Sommets Musicaux de Gstaad, TEFAF Maastricht 2027, Alpina Gstaad, New Year's Eve Regatta (Saint-Barth). Aucun fait supprimé : nouvel outil `.radar/tools/condenser_iv.py` qui REFUSE tout lot où un e-mail, téléphone, URL, montant, horaire ou date disparaît (exceptions listées et justifiées : doublons, mention périmée, fausse alerte de découpage).
- LVMH : `iv.g` disait encore « billetterie PAS encore ouverte au 29/08 » ; réécrit d'après le fait déjà vérifié dans `so` (réservations en trois vagues les 24, 28 et 30 septembre à 14h). `iv.o` : 45 Maisons (valeur corrigée le 28/09 dans `so`) au lieu de 46.
- Les traductions `iv_*` des champs modifiés ont été retirées (repli français exact) : aucune n'existait pour ces fiches.
- Restant en fenêtre live : 102 fiches ont encore un champ iv de plus de 400 caractères (29 au-delà de 900), presque toutes de la matière factuelle ; mesure faite après le lot.

## Constat sur la « dérive journal d'enquête »
Sur la fenêtre live, les phrases d'enquêteur sont devenues rares (9 occurrences repérées par motifs, dont 4 traitées). Ce qui dépasse 400 caractères est surtout de la matière factuelle dense (cartes, tarifs, horaires, paliers de mécénat) qu'on ne peut pas couper sans perdre un fait : Cala Rossa, Gstaad New Year (2 262 car.), Abu Dhabi, Dior Spa… laissés en l'état volontairement.

## Non fait / non vérifié
- Aucune recherche de nouveaux événements, aucun candidat du vivier traité (49 intacts), aucune revérification de la file `reverification-prioritaire.json`, pas de séjours (6 restants), pas de mesure mobile (pas un lundi).
- Aucun contenu externe consulté cette passe : pas de vérification web des faits condensés (ils proviennent des champs existants).
