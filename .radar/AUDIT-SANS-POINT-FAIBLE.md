# Le chantier « aucun point faible »

Commande de Constance du 17/09/2026 : le site doit être irréprochable avant toute
promotion, monétisation ou contact investisseurs. Audit extérieur mené par
ChatGPT (mode approfondi, crawl réel) le 17/09 au soir, consolidé ici. Chaque
point porte son état. Règle : on avance point par point, publication immédiate
de chaque correction, et le verrou final est un validateur de build BLOQUANT.

## P0 : avant toute promotion

1. [FAIT 17/09] Totaux réconciliés : 325 = 341 moins les 16 points d'entrée non notés,
   désormais expliqué en toutes lettres sur note.html. Les « 240 » et « 96 vs 94 » de
   l'audit extérieur étaient des fantômes du cache de son moteur (vérifié : 94 partout).
   Test bloquant V5 en place : hub vs pages catégories vs base, et compteur de note.html.
2. [FAIT 17/09] Gala Planetary Health : d1/d2 disaient 25/09, le texte vérifié dit 18/09.
   Synchronisé. Généraliser : test bloquant date machine vs date écrite (chantier n° 20).
3. [FAIT 17/09 pour la description] Meta description FR de l'accueil encore estivale
   (avec un tiret long). Réécrite automne, 13 langues servies par la même page.
   [À FAIRE] Scan global de tous les fichiers générés : "été 2026", "summer 2026",
   "cet été", "None", "null", "undefined", "NaN", "[object Object]", clés i18n nues.
4. [EN COURS] Titres "None" corrigés en ligne le 17/09 ; l'index Google se resorbe.
   [À FAIRE] Garde bloquante : aucun title avec None/null/undefined/séparateur vide ;
   comparaison title servi vs title attendu pour chaque URL du sitemap.
5. [À FAIRE] Signal 502 vu par le navigateur d'audit (peut venir de son infra).
   Sonde de disponibilité sur 24 h : /, /en/, /ar/, fiches, sitemap ; taux de 5xx.

## P1 : SEO et crédibilité

6. [À FAIRE] Français résiduel dans les 12 langues : fil d'Ariane (« Londres » sur pages EN),
   « Divers lieux », pieds de page (À propos · Contact · Mentions légales), groupes
   de régions en français sur le hub arabe. Liste blanche : noms propres seulement.
7. [À FAIRE] Vérification de TOUTES les grappes hreflang (pas seulement l'accueil) :
   canonical auto-référente, 13 alternates accessibles, réciprocité, x-default.
8. [À FAIRE] JSON-LD Event à recalibrer : Event.url doit pointer la fiche CP7 (pas le site
   officiel), offers seulement si vraie offre publique, pas d'InStock par défaut,
   pas d'estimation déclarée EventScheduled, accueil en ItemList plutôt que
   des centaines d'Event complets, JSON-LD strictement égal au visible.
9. [À FAIRE] Fraîcheur : distinguer build quotidien / dernière modification / dernière
   vérification de source ; une fiche imminente se revérifie plus souvent.
10. [À FAIRE] Statuts des récurrents/saisons/sans-date : ne pas tout déclarer
    EventScheduled ; annulé = EventCancelled ; année cohérente partout.

## P1 : architecture, liens, indexation

11. [À FAIRE] Crawl complet interne : statuts, chaînes de redirections, ancres vides,
    pages orphelines, profondeur de clic.
12. [À FAIRE] Liens externes/sources : 404, domaines expirés, redirections génériques ;
    ne pas classer 403/429 comme morts (nos passes le font déjà en partie : vérifier la règle).
13. [À FAIRE] Canonicals et variantes d'URL (http/https, www, /index.html, slash, utm).
14. [À FAIRE] Sitemap : que du 200 indexable, lastmod honnête (pas renouvelé
    artificiellement chaque jour), compte exact par type et langue.
15. [À FAIRE] Cannibalisation : matrice intention -> URL unique (Milan events, PFW,
    Vogue World...) ; page ville vs landing imminente vs Questions.
16. [À FAIRE] 404 réel (pas de 200 déguisé), les 61 redirections en un seul saut,
    hors sitemap, liens internes pointant la destination finale.

## P1 : robustesse fonctionnelle

17. [À FAIRE] Accueil résilient : fetch en échec, JSON invalide, sans JavaScript ;
    jamais de page blanche, message d'erreur + réessayer, pas de faux « aucun événement ».
18. [À FAIRE] Favoris/localStorage : bloqué, navigation privée, quota, JSON corrompu,
    slug renommé, deux onglets ; un échec de favoris ne doit jamais casser le radar.
19. [À FAIRE] Recherche : accents, apostrophes typographiques, CJK/arabe/cyrillique,
    entrées longues, emojis, HTML échappé (jamais d'injection).
20. [À FAIRE] Dates et fuseaux : minuit, été/hiver, événement NY vu de Tokyo, 29 février ;
    définir et documenter le fuseau de référence d'« aujourd'hui ».

## P1 : mobile, performance, accessibilité, sécurité

21. [À FAIRE] Core Web Vitals sur téléphone moyen et réseau lent : LCP<2,5s, INP<200ms,
    CLS<0,1 ; poids du HTML de l'accueil (gros JSON-LD) à surveiller.
22. [À FAIRE] Petits écrans : 320/360/390 px, paysage, zoom 200 %, clavier ouvert,
    cibles 44 px, pas de défilement horizontal.
23. [À FAIRE] Accessibilité : H1 unique, landmarks, clavier, focus visible, labels,
    noms accessibles des coeurs (♡/◐/→), contraste deux thèmes, reduced-motion.
24. [À FAIRE] RTL arabe (nombres/dates isolés, flèches, fil d'Ariane) et CJK
    (polices, coupures, pas de troncature au compte de caractères latins).
25. [À FAIRE] En-têtes HTTP : HSTS, CSP (en mode rapport d'abord), nosniff,
    Referrer-Policy, frame-ancestors. Limite : GitHub Pages ne permet pas tout,
    documenter ce qui est hors de portée.
26. [À FAIRE, samedi 20/09] Newsletter : double opt-in, anti-spam, erreurs visibles,
    SPF/DKIM/DMARC, désinscription, politique de confidentialité.
27. [À FAIRE] Injection : échappement partout, pas d'innerHTML dangereux, pas de
    secrets dans le JS, target=_blank protégés, aucun fichier de travail publié.

## P2 : confort

28. [À FAIRE] Cohérence éditoriale : graphies (ConstanceParis7, Monte-Carlo/Monaco),
    formats de prix et de dates, vocabulaire confirmé/probable/à vérifier.
29. [À FAIRE] États vides : aucun favori, aucun résultat, fiche retirée, hors connexion.
30. [À FAIRE] Aperçus sociaux : og/twitter par page, rendu WhatsApp/iMessage/LinkedIn,
    impression propre des fiches.

## LE VERROU : le validateur de build bloquant

[EN SERVICE depuis le 17/09 au soir] .radar/tools/verrou.py, branché dans validate.py :
toute publication échoue sur V1 champs empoisonnés (None/null/undefined/NaN/[object
Object]) dans title/description/og/h1, V2 saison périmée dans les métadonnées de
structure, V3 page sans title/description/canonical, V4 d2 < d1, V5 compteurs
divergents, V6 lien interne cassé, V7 URL de sitemap sans fichier, V8 JSON-LD
illisible, V9 hreflang vers fichier absent. En avertissement (promotion à venir) :
W1 date écrite hors fenêtre machine, W2 page sans h1. 6 367 pages contrôlées en 3 s.
Dès sa première exécution, le verrou a attrapé : le lien du bandeau vers Royal Ascot
cassé par la normalisation des lieux, les liens mémoire brisés des pages Note en
12 langues, et la fiche D&G Casa Amor finissant en machine le 30/08 alors que son
texte vérifié dit le 31/10. Les trois sont corrigés.

Reste à durcir : divergence visible vs JSON-LD champ à champ (chantier 8), badge
vérifié sans source datée, W1 et W2 promus bloqueurs une fois le corpus purgé.

## Ordre d'exécution (validé avec l'audit extérieur)

1. Réconcilier données et compteurs (P0.1, P0.2 généralisé).
2. Purger les métadonnées estivales partout + accélérer le recrawl des pages None.
3. Construire le validateur bloquant 13 langues (LE VERROU).
4. Crawl complet : statuts, canonicals, hreflang, sitemap, liens, JSON-LD.
5. Pannes JS et localStorage.
6. Mobile, performance, accessibilité, RTL.
7. Sécurité, newsletter, délivrabilité (samedi 20/09).
