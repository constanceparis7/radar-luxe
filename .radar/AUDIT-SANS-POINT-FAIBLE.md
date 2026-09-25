# Le chantier « aucun point faible »

Commande de Constance du 17/09/2026 : le site doit être irréprochable avant toute
promotion, monétisation ou contact investisseurs. Audit extérieur mené par
ChatGPT (mode approfondi, crawl réel) le 17/09 au soir, consolidé ici. Chaque
point porte son état. Règle : on avance point par point, publication immédiate
de chaque correction, et le verrou final est un validateur de build BLOQUANT.

## P0 : avant toute promotion

0. [FAIT 18/09, dégât auto-infligé réparé] La normalisation des villes du 17/09 avait
   changé l'adresse de 63 fiches (la ville entre dans le slug) sans redirection :
   114 URL en 404 dans Search Console. 117 redirections permanentes de fiches
   générées par gen_pages, 13 langues. Leçon gravée : tout renommage de champ qui
   entre dans une adresse exige ses redirections dans le même commit.

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
4. [FAIT 17-18/09] Titres « None » corrigés ; garde bloquante V1 au verrou (title,
   description, og, h1). Search Console du 18/09 : les pages catégories étrangères
   avaient des centaines d'affichages et zéro clic, preuve de l'impact ; recrawl
   en cours, à mesurer au 2/10. [Reste : comparaison title servi vs attendu.]
5. [À FAIRE] Signal 502 vu par le navigateur d'audit (peut venir de son infra).
   Sonde de disponibilité sur 24 h : /, /en/, /ar/, fiches, sitemap ; taux de 5xx.

## P1 : SEO et crédibilité

6. [FAIT 18/09] Registre .radar/lieux-i18n.json (112 villes, 40 groupes, 4 libellés
   d'interface, 12 langues, vague de traduction vérifiée) branché dans les pages
   générées (fil d'Ariane, lieu, pied de page, hubs) et fusionné dans les tables de
   l'accueil (villes 127 vers 140, groupes 55 vers 61). Londres devient London,
   Лондон, 伦敦 selon la langue ; « Divers lieux » et « Mentions légales » traduits.
7. [FAIT 18/09] Grappes hreflang : contrôle V10 au verrou (13 alternates par fiche,
   jeux identiques entre langues, fichiers présents). Zéro divergence au premier passage.
8. [FAIT 20/09] JSON-LD Event recalibré (offre réelle seulement, statuts lus, gratuité écrite) ; à recalibrer : Event.url doit pointer la fiche CP7 (pas le site
   officiel), offers seulement si vraie offre publique, pas d'InStock par défaut,
   pas d'estimation déclarée EventScheduled, accueil en ItemList plutôt que
   des centaines d'Event complets, JSON-LD strictement égal au visible.
9. [À FAIRE] Fraîcheur : distinguer build quotidien / dernière modification / dernière
   vérification de source ; une fiche imminente se revérifie plus souvent.
10. [À FAIRE] Statuts des récurrents/saisons/sans-date : ne pas tout déclarer
    EventScheduled ; annulé = EventCancelled ; année cohérente partout.

## P1 : architecture, liens, indexation

11. [FAIT 18/09 pour l'essentiel] Liens internes et orphelines au verrou (V6, W3).
    Prises du premier passage : les 4 pages d'atterrissage imminentes et les pages
    Note étrangères n'avaient AUCUN lien entrant ; désormais liées depuis les fiches.
    [Reste : profondeur de clic, non critique.]
12. [FAIT 20/09, règle vérifiée] Liens externes : la passe traite 403, 405, 406 et 429
    comme « vu et refusé, donc vivant » ; seuls les 404 sont des morts. Contrôle quotidien.
13. [FAIT 18/09] Testé en ligne : http vers https 301, www vers domaine nu 301,
    /index.html en 200 avec canonical vers /, 404 réel sur URL inconnue.
14. [FAIT 18/09] lastmod honnête : 433 pages réellement quotidiennes datées (accueils,
    imminents) au lieu de 5 558 datées artificiellement chaque jour. V7 garantit
    que chaque URL du sitemap a son fichier.
15. [EN COURS 18/09] Diagnostic Search Console : 162 pages « en double, Google a choisi
    une autre canonique » = Google sert parfois une autre langue (la fiche arabe de
    Vogue World en tête des clics). Grappes hreflang vérifiées correctes ; remède
    posé : alternates hreflang émis dans le sitemap (5 447 URL). À mesurer au bilan
    du 2/10. [Reste : matrice intention vers URL unique pour Milan/PFW/Vogue World.]
16. [FAIT 18/09] 404 maison élégante (marque, liens radar/événements/entrer/favoris,
    bilingue) servie avec le vrai statut 404 ; les 61 redirections sont des sauts
    uniques, hors sitemap, et V6 interdit tout lien interne vers une ancienne adresse.

## P1 : robustesse fonctionnelle

17. [FAIT 18/09] Le radar principal se rend depuis les données embarquées (aucun
    réseau requis) ; la carte du moment reste cachée si son chargement échoue ;
    la recherche affiche désormais « momentanément indisponible » au lieu de se
    taire, et se retente à la frappe suivante.
18. [FAIT 18/09, vérifié] Toutes les lectures et écritures localStorage sont sous
    try/catch (fiches, accueil, page favoris) ; un slug disparu est simplement
    ignoré par la page favoris ; un échec de stockage n'empêche rien d'autre.
19. [À FAIRE] Recherche : accents, apostrophes typographiques, CJK/arabe/cyrillique,
    entrées longues, emojis, HTML échappé (jamais d'injection).
20. [À FAIRE] Dates et fuseaux : minuit, été/hiver, événement NY vu de Tokyo, 29 février ;
    définir et documenter le fuseau de référence d'« aujourd'hui ».

## P1 : mobile, performance, accessibilité, sécurité

21. [EN COURS 25/09] Poids de l'accueil divisé par trois (820 à 264 Ko transférés) :
    journaux d'enquête et séjours chargés au dépliage ; budget V11 au verrou. Rendu
    progressif des cartes posé le 25/09 (fil principal jamais bloqué au premier
    affichage). Mesure de repli en 3G simulée le 25/09 : DOM prêt 590 ms, chargement
    complet 886 ms, aucun décalage de mise en page. [Reste : LCP/INP/CLS exacts, bloqués
    par le quota PageSpeed ; JSON-LD en liste, écarté (gain jugé trop faible).]
22. [EN COURS 25/09 : 320/375/390, paysage, clavier ouvert et cibles tactiles propres]
    Petits écrans : 320/360/390 px, paysage (812×375) et clavier ouvert (hauteur réduite)
    contrôlés sans débordement horizontal ni élément fixe piégé. Cibles tactiles portées à
    44 px le 25/09 (bouton thème, sélecteur de langue, les deux champs de recherche, liens
    de catégories, bouton de filtres, crédit Instagram, flèche « voir plus ») par un cadre
    invisible élargi (padding + box-sizing), sans rien changer à l'apparence visible ;
    vérifié en ligne, mesuré et à l'écran (33 cibles sous 44 px avant, 21 après ; les
    restantes sont des puces de compte à rebours secondaires, volontairement laissées
    compactes pour ne pas surcharger visuellement une rangée serrée). Reste : le
    zoom 200 % à vérifier avec un vrai zoom (l'essai au zoom CSS simulé du 25/09 n'était
    pas fiable).
23. [EN COURS 25/09] Posé : lien d'évitement, landmark main, focus visible, aria-label sur
    les coeurs, reduced-motion (déjà). Audit structurel par arbre d'accessibilité le 25/09
    (accueil, pas un vrai passage VoiceOver/NVDA) : un seul h1, zéro image sans alt (le site
    n'utilise aucune balise img, la photo d'accueil est en fond CSS), landmarks propres
    (main, header, nav Catégories/Explorer/Filtres, footer), lien d'évitement fonctionnel.
    Un vrai défaut trouvé : le bouton coeur (♡, .fav-mini) est niché À L'INTÉRIEUR du titre
    (h1 à h6) sur les 217 cartes d'événements de l'accueil (et vraisemblablement sur les
    fiches et les listes, même patron) ; un lecteur d'écran qui saute de titre en titre
    risque d'annoncer « Favoris » à la suite du nom de l'événement. Correctif identifié
    (sortir le bouton du titre, l'en rendre frère) mais pas appliqué : le patron est
    répété sur des dizaines de gabarits (index-full.html et gen_pages.py), donc à traiter
    à part, pas dans cette passe. Signalé aussi : un saut de niveau de titre (h2 direct
    vers h4) sous Classement Prestige, mineur. Reste : contraste des deux thèmes, labels
    des selects, un vrai passage au lecteur d'écran, noms des symboles ◐ et →, correction
    du bouton coeur niché dans les titres.
24. [EN COURS 20/09, rendu vérifié à 375 et 320 px, bogue du lien d'évitement corrigé] RTL arabe (nombres/dates isolés, flèches, fil d'Ariane) et CJK
    (polices, coupures, pas de troncature au compte de caractères latins).
25. [À FAIRE] En-têtes HTTP : HSTS, CSP (en mode rapport d'abord), nosniff,
    Referrer-Policy, frame-ancestors. Limite : GitHub Pages ne permet pas tout,
    documenter ce qui est hors de portée.
26. [À FAIRE, samedi 20/09] Newsletter : double opt-in, anti-spam, erreurs visibles,
    SPF/DKIM/DMARC, désinscription, politique de confidentialité.
27. [FAIT 18/09 pour l'essentiel] Recherche : entrée jamais réinjectée, résultats
    échappés ; aucun secret dans le JS ; index-full.html confirmé hors ligne (404,
    gitignore) ; target=_blank avec rel noopener sur les gabarits contrôlés.

## P2 : confort

28. [FAIT 24/09] Graphies normalisées (Monte-Carlo, Saint-Tropez, Saint-Moritz, Saint-Barth,
    9 fiches renommées avec redirection). Tirets longs (– et —) interdits par Constance :
    purge exhaustive le 24/09, plus de 10 600 corrections retrouvées dans les traductions
    imbriquées et le bandeau d'interface (jamais couverts par les passes du 20-21/08, qui
    n'avaient traité que les titres) — 0 restant dans le contenu publié des 13 langues,
    vérifié en ligne. Reste, mineur : vocabulaire confirmé/probable/à vérifier, format des
    prix et des heures, à harmoniser si un nouveau signal le justifie.
29. [EN COURS 20/09 : favoris, recherche 13 langues, carte du moment] États vides : aucun favori, aucun résultat, fiche retirée, hors connexion.
30. [EN COURS 20/09 : og + cartes Twitter partout] Aperçus sociaux : og/twitter par page, rendu WhatsApp/iMessage/LinkedIn,
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
