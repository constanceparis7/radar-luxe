# Compte rendu — passe du 8 septembre 2026

## Plancher / purge
5 fiches zombies purgées (d2=08/08/2026, seuil des 30 jours franchi ce jour même) :
22e Authors Night East Hampton Library, Jingu Gaien Fireworks Festival, Copa del Rey
MAPFRE, Summer Hamptons Evening Northwell Health, Ravello Festival Serate Jazz.
388 → 383 événements après purge, 384 après la naissance du jour (voir plus bas).

## Condensation `iv` (priorité du moment)
10 fiches condensées ce jour (sélection au seuil WARN de `validate.py`, ≥ 1200
caractères sur `iv.o`/`iv.g`/`iv.w`) : Villa Carmignac, Biennale Arte 2026, Yves
Saint Laurent and Photography (ICP), POINT D'ENTRÉE Ventes aux enchères, Grand Hôtel
de Cala Rossa, Yacht & superyachts Ibiza-Formentera, Dubai Racing Carnival, Saint-Barth
Cata Cup, Formula 1 Abu Dhabi Grand Prix, Gstaad New Year Music Festival.

Contrôle mécanique `verif_faits.py` : **TOUT OK, aucune perte de fait** sur les 10
fiches. Constat important remonté par plusieurs agents condensateurs : la dérive
« journal d'enquête » décrite dans la doctrine n'était en réalité PLUS présente sur
la plupart de ces fiches (elles avaient déjà été nettoyées à une passe antérieure) —
le travail du jour a surtout consisté à resserrer la prose et à vérifier l'absence de
coordonnée personnelle interdite (aucune trouvée). Résultat : 3 fiches sont repassées
sous le seuil WARN (Ibiza yacht, Dubai Racing Carnival, Saint-Barth Cata Cup) ; les 7
autres restent légitimement au-dessus (Villa Carmignac, Biennale, YSL/ICP, POINT
D'ENTRÉE, Cala Rossa, Abu Dhabi GP, Gstaad) car elles portent une forte densité de
faits réels (grilles tarifaires multiples, plusieurs contacts nominatifs) qu'il est
interdit de couper pour respecter la cible de 400 caractères — conforme à la règle
« on garde le fait, jamais l'inverse ». **Reste à traiter aux prochaines passes** :
ces 8 fiches restent au-dessus du seuil WARN (1 sur `iv.g`, 7 sur `iv.w`), toutes
déjà examinées et jugées légitimement denses ce jour — à réexaminer périodiquement
pour confirmer que rien n'a dérivé à nouveau vers le journal d'enquête.

## Vérification des 7 prochains jours + liens
26 fiches imminentes (aujourd'hui → +7 jours) recensées. 22 liens testés :
- 15 confirmés 200 avec contenu positif du sujet (dont sailgp.com/ pour le Rockwool
  France Sail Grand Prix Saint-Tropez, confirmé malgré un faux signal « not found »
  provenant du bundle JS générique du site — voir leçon ajoutée à lessons.md) ;
- roccofortehotels.com (Sir Rocco Forte Captain's Trophy) : 403 en curl nu, 200 avec
  un user-agent de navigateur — confirmé, pas un problème du site ;
- 3 liens non vérifiables ce jour malgré plusieurs tentatives (curl + user-agent) :
  usopen.org (403 persistant), twigafortedeimarmi.com et lacapanninadifranceschi.com
  (échecs de connexion côté passerelle réseau, `ws_closed_mid_exchange`) ; espacelouisvuittontokyo.com et peninsula.com également bloqués (403, sites connus
  pour leur protection anti-robot). Aucune de ces 5 fiches n'a été modifiée ou
  retirée — un 403/timeout n'est pas une preuve d'absence (doctrine) ; à retester à
  une prochaine passe, éventuellement au navigateur si l'outil est disponible.

## Naissance complète : RHS Chelsea Flower Show 2027
Nouvelle fiche née COMPLÈTE (invitation + séjour + 12 langues), comblant un trou de
calendrier identifié dans `CHANTIERS.md` (« ENSUITE ÉLARGIR ») : dates 18-22 mai 2027
vérifiées sur rhs.org.uk (journées adhérents 18-19, journées publiques 20-22, soirée
« Chelsea Late » le 21), lieu Royal Hospital Chelsea. Voie d'invitation : adhésion RHS
individuelle (journées adhérents) + accréditation presse gratuite via la RHS Press
Team (pressoffice@rhs.org.uk, standard institutionnel +44 20 7821 3080 — AUCUNE
coordonnée personnelle utilisée, alors que la page source en publie plusieurs :
signalé explicitement par le contrôleur adverse et écarté). Séjour : The Cadogan
(A Belmond Hotel, Chelsea), Restaurant Gordon Ramsay (3 étoiles Michelin, même rue
que le salon), soirée Chelsea Late en expérience. Vérifié adversairialement (verdict
FIABLE=true, 8 points de contrôle, 0 correction nécessaire) avant publication.
Tarifs 2027 non publiés à ce jour (« Tickets on sale soon ») : dit franchement,
aucun prix inventé. Traduit en 12 langues (agent dédié, contrôle de forme OK).

## LOI DU SITE — 3 compteurs
- Traductions 13 langues : 384/384 (100%)
- Séjours clé en main : 370/384 manquent 14 (tous hors fenêtre live, déjà passés)
- Voies d'invitation : 381/384 manquent 3 (idem, hors fenêtre live)
- **Sur la fenêtre live (aujourd'hui → +90j, 278 fiches) : 100% — 0 séjour manquant,
  0 invitation manquante.**

## Autres
- Eyebrow mis à jour : « données collectées et vérifiées le 8 septembre 2026 ».
- Doute a-reverifier.md tranché : « Soirées d'été des Hôtels Barrière Deauville »
  conservée telle quelle — son propre texte reconnaît déjà honnêtement l'absence de
  programme public nommé, ce n'est pas une porte fantôme.
- Branding saisonnier : WARN inchangé (« Été » encore affiché) — proposition de
  bascule « Automne » à Gérald toujours en attente de son accord explicite, non
  renommé d'office (règle absolue de la doctrine).
- KPI accès mondain (iv) : 258/259 (99%), stable.
- Visites (GoatCounter, compteur cumulé) : 2 573 pages vues cumulées, +21 depuis
  hier (2 552 → 2 573). Détail pays/sources non accessible ce jour depuis cette
  session (page du tableau de bord GoatCounter non exploitable en script) — dit
  franchement plutôt qu'inventé, à reprendre à une prochaine passe.
- `validate.py` : 0 blocker, 3 warnings (2 iv denses légitimes + branding saison).
- `healthcheck.sh` : OK à chaque publication (200, date fraîche, compte conforme).
- 3 commits publiés sur `main` directement (pas de repli de branche nécessaire
  aujourd'hui) : purge, condensation, naissance Chelsea Flower Show + journal.

## Non vérifié / reporté
- Les 5 liens listés plus haut (usopen.org, twiga, capannina, espacelouisvuittontokyo,
  peninsula.com) restent à retester.
- Les ~18 doutes restants de `a-reverifier.md` (Dolce & Gabbana Casa Amor, Principote,
  Dioriviera Cannes, La Co(o)rniche, Bagni Fiore, Terrasses des palaces parisiens,
  etc.) n'ont pas été repris ce jour faute de nouvelle source (déjà recherchés à
  plusieurs reprises fin août sans succès) — inchangés, pas de régression.
- 7 fiches restent au-dessus du seuil WARN de condensation (voir plus haut) : jugées
  légitimement denses ce jour, à réexaminer périodiquement plutôt qu'à re-condenser
  mécaniquement (leçon du 20-21/08 : le seuil de sélection n'est pas le seuil cible).
