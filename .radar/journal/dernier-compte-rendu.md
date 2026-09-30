# Compte rendu : passe du 30/09/2026

**Purge.** 11 zombies (fin 30/08/2026) purgés : 309 → 298 événements. Le verrou les bloquait, la purge (`passe_automatique.py --apply`) les a évacués.

**Condensation `iv`.** 0 dérive « journal d'enquête » sur la fenêtre live (8e jour consécutif, contrôle par motifs d'enquêteur). Rien à condenser. Restent 138 champs de plus de 600 caractères, mais ce sont des listes de tarifs et d'horaires publiés (Villa Carmignac, Biennale…) : les couper supprimerait des faits, donc laissés.

**Fraîcheur (5bis).** 1 fiche revérifiée : Design Miami / Paris 2026 (site officiel : 20-25 octobre 2026, Hôtel de Maisons, confirmés). Source et mention « vérifié le 30/09/2026 » écrites dans `so`. Le détail « Preview Day du 20 et public du 21 au 25 » n'est pas écrit sur la page officielle, il reste tel quel. Les autres fiches de la file (Cap-Eden-Roc, Gucci Flora, scène yacht Ibiza, palaces de la presqu'île) non revérifiées.

**Nouveaux événements.** Aucune recherche de nouveautés ce jour.
**LOI DU SITE.** 298 fiches : traductions 100 %, invitations 100 %, séjours 303/309 avant purge (reste 6, dont fiches-conseil c=acces).
**validate.py :** OK, 0 bloqueur, 2 avertissements (iv.g/iv.w longs ; Nikki Beach Ibiza dates écrites hors fenêtre).
**Non fait / non vérifié :** liens hebdo (jour non lundi), visites, dt incohérents signalés le 29/09.
**Publication :** le push direct de la trace de démarrage sur `main` a été refusé par le classifieur de la session ; publication par branche `claude/passe-2026-09-30` (workflow de fusion).
