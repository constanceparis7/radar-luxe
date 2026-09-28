# Matrice intention → adresse unique (cannibalisation, point 15 du registre)

Posée le 28/09/2026. Constat de départ (Search Console du 18/09) : Google servait parfois
une autre langue que celle du visiteur (la fiche arabe de Vogue World en tête des clics),
et plusieurs pages françaises répondaient à la même requête. Deux remèdes tiennent depuis :
les grappes hreflang complètes (13 alternates et x-default vers le français, contrôlées
par V10) et les alternates hreflang émis dans le sitemap. Cette matrice fixe, pour chaque
intention, LA page qui doit répondre, et le rôle des voisines.

## Règle

Trois familles de pages se partagent un même sujet ; chacune répond à une intention et
renvoie aux deux autres, jamais avec le même titre ni la même description :

| Famille | Intention | Titre en forme de requête | Durée de vie |
|---|---|---|---|
| Fiche (`/e/…`, 13 langues) | « dates, programme, comment entrer » de l'ÉDITION en cours | « Nom de l'édition · Ville » | une saison (purgée 30 jours après la fin) |
| Guide permanent (`/paris-fashion-week.html`, `/milano-fashion-week.html`, français) | « comment assister, invitations, accès » toute l'année | « Sujet 2026 : dates, accès, invitations » | permanente, réécrite à chaque édition |
| Lieu (`/lieu/<ville>.html`, 13 langues) | « événements de luxe à <ville> » | « Ville : agenda des événements de luxe et accès » | permanente |

Le guide permanent existe seulement en français (il porte la voix éditoriale) ; il ne
porte donc ni hreflang ni x-default, et ne concurrence pas les fiches étrangères.

## La matrice au 28/09/2026

| Intention (requête type) | Adresse qui doit répondre | Voisines (et lien réciproque vérifié) |
|---|---|---|
| paris fashion week dates / programme / septembre 2026 | `/e/paris-fashion-week-pret-a-porter-printemps-ete-2027-paris.html` (+ 12 langues) | guide `/paris-fashion-week.html` (lien ↔ vérifié), lieu `/lieu/paris.html`, moment `/moments/octobre-a-paris.html` |
| paris fashion week comment entrer / invitation / assister | `/paris-fashion-week.html` | fiche (lien ↔ vérifié), questions `/q/…` liées |
| milan fashion week dates / settembre 2026 | `/e/milano-fashion-week-printemps-ete-2027-milan.html` (+ 12 langues) | guide `/milano-fashion-week.html` (lien ↔ vérifié), lieu `/lieu/milan.html` |
| milan fashion week invitations / come entrare | `/milano-fashion-week.html` | fiche (lien ↔ vérifié) |
| vogue world milano 2026 | `/e/vogue-world-milano-2026-milan.html` (+ 12 langues) | lieu `/lieu/milan.html` ; aucun guide permanent (événement unique, pas de récurrence établie) |
| événements luxe milan / eventi lusso milano | `/lieu/milan.html` (+ 12 langues) | fiches de Milan |

Contrôle du 28/09 : les trois pages de chaque sujet ont des titres et des descriptions
distincts ; les liens réciproques guide ↔ fiche existent (2 liens du guide Milan vers sa
fiche, 1 du guide Paris ; 1 de chaque fiche vers son guide) ; canonical de chaque page
vers elle-même ; x-default des fiches vers le français.

## Ce qui reste à mesurer (bilan du 2/10)

Dans Search Console, par requête : la page servie doit être celle de la matrice, dans la
langue du visiteur. Si la fiche arabe (ou une autre) continue d'être servie à des
francophones pour « vogue world », le remède suivant est de différencier davantage les
descriptions par langue (aujourd'hui traduites mot à mot, donc jugées quasi identiques),
pas de retirer des langues.
