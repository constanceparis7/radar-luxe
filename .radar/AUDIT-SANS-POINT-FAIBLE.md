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
3. [FAIT 17/09 pour la description, scan FAIT le 26/09] Meta description FR de l'accueil
   encore estivale (avec un tiret long). Réécrite automne, 13 langues servies par la même
   page. Scan global des 5 890 fichiers générés (title/meta description/og) : 0 "None",
   "null", "undefined", "NaN", "[object Object]" hors balises &lt;script&gt; ; les 333+65+67
   occurrences de "été 2026"/"cet été"/"summer 2026" restantes sont toutes du contenu
   factuel légitime (nom ou sujet réel d'un événement/d'une programmation datée), aucune
   méta périmée trouvée dans les title/description des 14 pages qui en portaient — leur
   sujet même EST l'été 2026, pas une saison "courante" oubliée.
   [TROUVÉ ET CORRIGÉ 28/09] Un vrai résidu, hors de portée de V2 : la ligne de marque du
   bloc d'accueil (« International Luxury Events · Summer 2026 ») venait du JSON
   d'interface des 13 langues, que saison.py n'avait plus mis à jour (son motif de titre
   cherchait encore un tiret long disparu le 24/09) et qu'aucun contrôle ne lisait. Six
   jours après l'équinoxe, tout visiteur voyait « Summer 2026 » dans le bloc d'accueil.
   saison.py relancé et réparé ; verrou V13 : la saison du bandeau est contrôlée dans les
   13 langues à chaque publication.
4. [FAIT 17-18/09] Titres « None » corrigés ; garde bloquante V1 au verrou (title,
   description, og, h1). Search Console du 18/09 : les pages catégories étrangères
   avaient des centaines d'affichages et zéro clic, preuve de l'impact ; recrawl
   en cours, à mesurer au 2/10. [Reste : comparaison title servi vs attendu.]
5. [FAIT 27/09, sonde tenue 9 jours] Signal 502 vu par le navigateur d'audit : non
   reproduit. Sonde de disponibilité lancée le 18/09 et toujours en marche (5 adresses
   toutes les 20 minutes environ : accueil, /ar/, un lieu anglais, une fiche, le
   sitemap) : 525 mesures du 18 au 27/09, 480 réponses 200, ZÉRO 5xx, temps de
   réponse médian 0,20 s, 95 % sous 0,61 s, pire cas 2,61 s. Les 45 échecs restants
   sont des « connexion impossible » (code 000) dont 40 tombent par paquets de cinq
   à la même seconde, toutes adresses ensemble : c'est la machine qui sonde qui
   dormait ou perdait le réseau, pas le site (GitHub Pages ne tombe pas pour cinq
   adresses à la fois pendant une seconde). Conclusion honnête : aucune panne du
   site prouvée sur la période ; le 502 de l'audit venait de l'infrastructure de
   l'auditeur, comme envisagé. La sonde continue. Depuis le 28/09, une seconde sonde
   tourne chez GitHub toutes les 30 minutes, indépendante de cette machine (qui dort
   la nuit) : 5 adresses, 3 essais à 20 s d'écart, puis issue et courriel au propriétaire,
   refermée d'elle-même au retour ; premier passage vérifié vert.

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
9. [EN COURS 27/09, mécanique posée] Fraîcheur. Les trois dates sont désormais distinctes
   et honnêtes : la date de l'eyebrow de l'accueil est celle de la passe (avancée
   seulement quand une passe a vérifié quelque chose, règle de passe_automatique.py) ;
   le badge « ✓ Vérifié à la source le… » d'une fiche n'apparaît que si la date est
   écrite dans ses sources (gen_pages.date_verif, depuis le 26/08) ; et une file de
   revérification tient la différence entre les deux. Mesure du 27/09 : 219 fiches
   vivantes, 59 seulement avec une date écrite (âge médian 35 jours), 160 sans ; parmi
   les imminentes ou en cours, 109 sont à revérifier. Nouvel outil persisté
   `.radar/tools/reverification.py` → `.radar/reverification-prioritaire.json`, et
   étape 5bis de la doctrine : chaque passe de nuit en revérifie 3 à 5 à la source et
   écrit la date. Le 28/09, coup d'accélérateur : 40 fiches imminentes ou en cours
   confrontées à leur source officielle par 10 lots parallèles (règles : citation
   verbatim de la page officielle, site tiers refusé, « introuvable » au moindre doute).
   Résultat : 28 confirmées à l'identique et datées « vérifié le 28/09/2026 » ; 5 vrais
   écarts corrigés dans les 13 langues (Sphère 30 septembre au lieu du 28 ; Arqana 20-23
   octobre au lieu de 19-24 ; Sotheby's Hong Kong vente du soir le 28 et ventes de jour
   le 29 ; Global Gift Gala Paris le 5 novembre au Four Seasons George V, jusque-là
   « octobre, date non publiée » ; Journées Particulières LVMH 71 lieux dans 13 pays,
   45 Maisons, fiche renommée avec redirection et journal des renommages) ; 6
   introuvables laissées sans date (Bon Marché en 403, agrégateurs, saisons sans date de
   fin publiée). Mesure après : 214 vivantes, 71 datées, file de 106 à 72.
   Nuit du 28 au 29/09 : second lot de 62 fiches lancé (coupé par la limite de session,
   relancé) ; acquis : Ushuaïa et Blue Marlin confirmés, Splendido Mare corrigé (jusqu'au
   6 janvier 2027), 7 saisons sans date de fin publiée (Co(o)rniche, Westminster, Annabel's,
   Langosteria Paraggi, Covo di Nord-Est, La Gritta, Lío) laissées sans date, honnêtement.
   La passe de nuit du 29/09 a corrigé 5 dates de fin sur source et purgé 7 fiches
   terminées. Au 29/09 : 207 vivantes, 72 datées, 65 à revérifier.
   Troisième lot le 29/09 au matin (62 fiches, 13 lots parallèles) : 24 confirmées à la
   source et datées (Cheval Blanc, Marie Antoinette Style Yokohama, Scorpios, LUMA Arles,
   Cap-Ferrat, Pêcheurs, GAIA Bodrum…), Amanzoe corrigé (30 septembre et non 31 octobre),
   33 saisons sans date de fin publiée laissées sans date (Bâoli, Sass Café, La Guérite,
   Bagatelle Bodrum, terrasses des palaces parisiens, Lanterne Hermès…). Journal des
   preuves de l'ensemble (citation verbatim, source, verdict) :
   .radar/journal/reverification-sources-2026-09-28.json. Bilan des trois lots : 207
   vivantes, 90 datées, 43 à revérifier, presque toutes des saisons sans date de fin
   publiée par l'organisateur. Reste : les passes de nuit, 3 à 5 par nuit.
10. [FAIT 27/09] Statuts : le JSON-LD de l'accueil déclarait « programmé » pour tous
    les événements, date estimée comprise. Désormais recalculé à chaque build comme
    sur les fiches : annulé → EventCancelled, reporté → EventPostponed, programmé
    SEULEMENT si la fiche est confirmée, sinon aucun statut affirmé (48 programmés,
    12 sans statut sur l'accueil du 27/09). Trouvé au passage et corrigé : le champ de
    confirmation lui-même avait cinq graphies (« confirme », « confirmé », « à
    vérifier », « a verifier », vide) et l'accueil n'en lisait que deux, donc 35 fiches
    confirmées s'affichaient « à vérifier » ; données ramenées à trois valeurs,
    normalisation à chaque build, avertissement au validateur, lecture tolérante côté
    navigateur (137 badges « confirmé » avant, 166 après, mesuré en ligne).
    « Année cohérente partout » contrôlé le 27/09 : sur les 319 fiches, 22 citent dans
    leur titre ou leur date écrite une année autre que celle de leurs dates machine, et
    les 22 sont légitimes (nom de collection « Printemps-Été 2027 » d'une Fashion Week
    de septembre 2026, fin de saison en 2027 d'une réouverture de décembre 2026, éditions
    précédentes citées comme référence, exposition ouverte en 2025). Aucune incohérence
    réelle ; le titre, la date écrite et le JSON-LD d'une même fiche sortent des mêmes
    champs d1/d2, donc ne peuvent pas diverger entre eux.

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
    du 2/10. [Matrice intention vers adresse unique POSÉE le 28/09
    (.radar/MATRICE-INTENTIONS.md) : par sujet, la fiche d'édition (13 langues, x-default
    vers le français), le guide permanent français et la page lieu, chacun avec son
    intention et son titre, liens réciproques guide ↔ fiche vérifiés. Reste : la mesure par
    requête au 2/10 ; si une mauvaise langue est encore servie, différencier les
    descriptions par langue plutôt que retirer des langues.]
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
19. [FAIT 25/09] Recherche testée en direct sur le site publié : injection HTML/script
    bloquée (img onerror, script, svg onload — aucune exécution, aucune balise brute
    dans le rendu) ; CJK, arabe, cyrillique, emojis et 6 000 caractères ne cassent rien
    (résultat vide, honnête, aucune erreur console). Un vrai défaut trouvé et corrigé le
    25/09 : la recherche était sensible aux accents (« Cote » ne trouvait pas « Côte »,
    15 résultats contre 0) ; normalisation Unicode NFD posée sur la requête et le texte
    cherché, vérifiée avant et après publication (Cote/COTE/Côte/cÔtE donnent maintenant
    tous 15). Apostrophes typographiques (’ ‘ ʼ) ramenées à l'apostrophe droite dans la
    requête et le texte cherché le 28/09 : « l’opéra », « l'opera » et « l’Opéra » donnent
    les mêmes 4 cartes, « d’hiver » et « d'hiver » les mêmes 8 (testé avant publication).
    Rien ne reste sur ce point.
20. [FAIT 27/09] Dates et fuseaux. Fuseau de référence : Paris, via Intl (Europe/Paris)
    pour « aujourd'hui », « en cours » et les horloges, donc juste été comme hiver et
    pour un lecteur à New York ou Tokyo ; documenté sur la page La méthode depuis le
    18/09. Un vrai défaut trouvé et corrigé le 27/09 : le compte à rebours convertissait
    l'heure de Paris en UTC avec un « -2 » figé (heure d'été), faux d'une heure autour
    du passage à l'heure d'hiver (25/10/2026) ; les deux bornes sont désormais posées
    sur la même grille sans décalage supposé, valeurs identiques à la seconde près
    aujourd'hui, justes toute l'année. Minuit : le jour bascule quand Paris passe minuit
    (la fonction tick() le détecte et re-rend). 29 février : dates ISO manipulées par
    Date.UTC, qui gère les années bissextiles ; rien à faire.

## P1 : mobile, performance, accessibilité, sécurité

21. [FAIT 28/09 pour la mesure, un vrai défaut corrigé] Poids de l'accueil divisé par
    trois (820 à 264 Ko transférés) : journaux d'enquête et séjours chargés au dépliage ;
    budget V11 au verrou. Rendu progressif des cartes posé le 25/09. Mesure exacte le
    28/09 par le protocole DevTools de Chrome dans les conditions de Lighthouse mobile
    (412 px, 4G lent, CPU ralenti 4 fois ; outil `mesure_cdp.py`) : accueil LCP 0,43 à
    1,07 s, CLS 0,08, fiches LCP 0,34 à 0,67 s et CLS 0. Défaut trouvé : l'INP de
    l'accueil (réactivité aux interactions) atteignait 264 ms sur le bouton thème, et
    jusqu'à 3 s quand le clic tombait pendant le rendu des lots de cartes. Corrigé le
    même jour : jours hors écran rendus à la demande (content-visibility), frappe de
    recherche regroupée à 120 ms ; INP 88 à 120 ms mesuré en ligne, aucune erreur. CLS
    ramené de 0,08 à 0 le même jour : la cause (observée élément par élément) était le
    remplacement des libellés du bloc d'accueil par le script principal après le premier
    affichage (la barre de catégories gagnait une ligne et le bloc remontait de 51 px) ;
    libellés statiques alignés sur le français, bloc de langue généré par split_i18n à
    chaque build et placé juste après le bloc d'accueil, langue et sens de lecture posés
    dès l'en-tête ; mesuré en ligne à 0 en français, anglais, arabe et chinois. [Reste :
    la mesure PageSpeed officielle (quota) ; mesure hebdomadaire inscrite en doctrine.]
22. [FAIT 28/09 : zoom 200 % et 400 % vérifiés avec de vraies largeurs de 640 et 320 px
    sur cinq pages, aucun débordement ; le reste ci-dessous était déjà fait le 25/09]
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
    [CORRIGÉ 25/09] Un vrai défaut trouvé : le bouton coeur (♡, .fav-mini) était niché
    À L'INTÉRIEUR du titre (h1 à h6) sur les 217 cartes d'événements de l'accueil
    (evCard() et renderPrestige(), les deux dans index-full.html) ; un lecteur d'écran
    qui saute de titre en titre risquait d'annoncer « Favoris » à la suite du nom de
    l'événement. Corrigé : bouton sorti du titre, rendu frère juste après la balise
    fermante (<h4 class="t">Titre</h4> <button class="fav-mini">…), CSS .ev .t passé en
    display:inline-block pour garder le coeur visuellement à côté du titre (même ligne,
    ou juste après si le titre est long) — rendu, bascule favoris/défavoris et absence
    d'erreur console vérifiés au navigateur avant publication (217 → 0 occurrences
    nichées). Vérification faite sur gen_pages.py (fiches individuelles, pages de liste,
    accueils par langue) : PAS le même patron, le bouton y est déjà frère de l'ancre du
    titre plutôt qu'enfant d'un h1-h6 — aucune correction nécessaire là, fausse piste de
    l'audit initial écartée. Signalé aussi : un saut de niveau de titre (h2 direct
    vers h4) sous Classement Prestige [CORRIGÉ 26/09, voir plus bas]. Contraste des deux thèmes
    mesuré en direct le 25/09 (formule WCAG, texte réel sur fond réel) : thème sombre
    6,41 à 19,19 pour 1, thème clair 5,78 à 15,96 pour 1 ; largement au-dessus du seuil de
    4,5 pour 1 partout testé. Vérifié aussi le 25/09 : le seul select de l'accueil (langue)
    porte déjà un aria-label (« Langue ») ; rien à corriger là.
    [CORRIGÉ 26/09] Saut de niveau de titre h2→h4 : deux occurrences, toutes deux hors de
    la structure h2>h3>h4 correcte de l'Agenda (qui groupe par jour en h3 avant chaque
    carte en h4). Sous « Classement Prestige » (h2) et sous « Archives » (h2), les cartes
    rendaient directement en h4 (renderPrestige(), renderArchives()) — les deux passées en
    h3 (le style visuel dépend uniquement de la classe CSS .t, jamais du nom de balise,
    vérifié par grep des règles CSS avant modification : aucun changement visuel). Diff de
    2 lignes dans index.html, validate.py et perfcheck.py relancés, 0 régression. Symboles :
    le bouton thème porte un aria-label qui couvre ◐ ; les flèches → décoratives des liens
    sont masquées aux lecteurs d'écran depuis le 28/09 (aria-hidden, toutes les pages
    générées). Audit automatisé axe-core le 28/09 (WCAG 2.1 A/AA et bonnes pratiques,
    injecté par DevTools sur le site en ligne, rien de modifié) : accueil 0 violation ;
    fiches et page favoris : 1 violation sérieuse, réelle (liens du fil d'Ariane et de la
    ligne de métadonnées distingués par la couleur seule) ; corrigée par un soulignement
    fin sur toutes les pages générées, 0 violation après. Validité HTML (W3C Nu) le même
    jour : toutes les fiches portaient une erreur de structure (un <style> dans le corps de
    page, après le titre), corrigée ; pages générées à 0 erreur et 0 avertissement ;
    verrou V14 posé. Reste : un vrai passage au lecteur d'écran.
24. [EN COURS 25/09, flèches directionnelles corrigées] RTL arabe (nombres/dates
    isolés, fil d'Ariane) et CJK (polices, coupures, pas de troncature au compte de
    caractères latins) : rendu vérifié à 375 et 320 px le 20/09, bogue du lien
    d'évitement corrigé. Trouvé et corrigé le 25/09 : la flèche « → » restait orientée
    de gauche à droite sur les pages arabes et sur l'accueil basculé en arabe, malgré
    la lecture de droite à gauche ; retournée en CSS (toutes les pages générées et
    l'accueil), testée avant et après publication dans les deux sens de bascule.
    Ponctuation mixte contrôlée à l'écran le 28/09 sur une fiche arabe (heures
    « 20:00، 21:00 », note « 86/100 », noms de lieux latins dans la phrase) : tout se lit
    dans l'ordre. Un vrai défaut trouvé au passage et corrigé le 28/09 : le titre latin
    « 104. Jägerball, Ball vom Grünen Kreuz » se lisait « Jägerball، Ball vom Grünen .104
    Kreuz » (le nombre en tête d'un titre latin dans un paragraphe arabe) ; titres des
    fiches et des listes en dir="auto" sur toutes les pages générées, vérifié à l'écran
    après publication. Reste : rien d'identifié ; à réobserver quand de nouvelles fiches
    arabes arrivent.
25. [FAIT 25/09, dans la limite du possible sans Cloudflare] En-têtes de sécurité :
    Content-Security-Policy et Referrer-Policy posées en balise <meta> sur toutes les
    pages (le site n'a aucun en-tête HTTP configurable sur GitHub Pages). La CSP
    restreint script/style/police/image/appel réseau aux origines nécessaires (le site
    lui-même et GoatCounter) ; script-src et style-src gardent 'unsafe-inline' car tout
    le site est un fichier autonome sans serveur pour générer un nonce par page — gain
    réel malgré tout : bloque le chargement de toute ressource distante non listée.
    Testé avant publication sur un serveur local propre (recherche, filtres, thème,
    favoris, changement de langue, page arabe) : aucune violation, aucune erreur
    console ; revérifié en direct sur constanceparis7.com après publication.
    HORS DE PORTÉE sans Cloudflare devant le site (balise <meta> ignorée par la
    spec pour ces cas) : HSTS, nosniff (X-Content-Type-Options), frame-ancestors
    (protection anti-clickjacking), un CSP en vrai mode rapport (report-only), des
    nonces par page. Ne pas les croire posés tant que Cloudflare n'est pas devant.
26. [Politique de confidentialité FAITE le 25/09, reste la newsletter] Politique de
    confidentialité publiée en page dédiée le 25/09 (reprend et complète la section déjà
    écrite des mentions légales), liée depuis le pied de page de tout le site. Reste,
    bloqué sur le compte Brevo de Constance : double opt-in, anti-spam, erreurs visibles,
    SPF/DKIM/DMARC, désinscription de la newsletter elle-même.
27. [FAIT 18/09 pour l'essentiel] Recherche : entrée jamais réinjectée, résultats
    échappés ; aucun secret dans le JS ; index-full.html confirmé hors ligne (404,
    gitignore) ; target=_blank avec rel noopener sur les gabarits contrôlés.

## P2 : confort

28. [FAIT 24/09] Graphies normalisées (Monte-Carlo, Saint-Tropez, Saint-Moritz, Saint-Barth,
    9 fiches renommées avec redirection). Tirets longs (– et —) interdits par Constance :
    purge exhaustive le 24/09, plus de 10 600 corrections retrouvées dans les traductions
    imbriquées et le bandeau d'interface (jamais couverts par les passes du 20-21/08, qui
    n'avaient traité que les titres) — 0 restant dans le contenu publié des 13 langues,
    vérifié en ligne. Vocabulaire des doutes unifié le 27/09 (confirmé / probable / à
    vérifier : trois valeurs canoniques dans les données, normalisées à chaque build, voir
    le point 10). DÉCOUVERTE DU 28/09 : la purge du 24/09 avait nettoyé les données, mais
    deux lignes du générateur de pages (l'en-tête des hubs et la ligne d'hôtel des séjours)
    réécrivaient un tiret long à chaque génération : près de 22 000 tirets republiés
    chaque nuit sur 4 898 pages des 12 langues étrangères, sans qu'aucun contrôle ne
    regarde les pages produites. Corrigé à la source ; 45 tirets corrigés à la main dans
    les traductions de la page Note (règles par langue, relus), 1 dans la mémoire du radar,
    7 dans le tableau de bord public. Verrou V12 posé : tiret long dans le texte visible de
    n'importe quelle page publiée = publication refusée (8 166 pages, 0 restant, vérifié
    en ligne). Leçon : une règle éditoriale se contrôle sur ce qui est PUBLIÉ, pas sur ce
    qui est stocké. Reste, mineur : format des prix et des heures.
29. [FAIT 28/09] États vides : aucun favori, aucun résultat (13 langues), carte du moment
    cachée si indisponible, fiche retirée (404 maison, favoris ignorent un slug disparu) ;
    hors connexion posé le 28/09 : manifeste et icônes (le site s'installe sur l'écran
    d'accueil), service worker réseau d'abord avec copie de secours des pages visitées,
    page « Hors connexion » dédiée ; testé serveur coupé en local (accueil 116 cartes,
    fiche, page inconnue), vérifié en ligne (worker actif, 6 entrées en cache).
30. [EN COURS 28/09 : og + cartes Twitter partout, dimensions et alt de l'image] Aperçus
    sociaux : og/twitter par page ; og:image:width, height et alt sur toutes les pages
    depuis le 28/09 ; impression propre des fiches faite le 25/09. Reste : le rendu
    WhatsApp/iMessage/LinkedIn à contrôler, et une image par événement.

## LE VERROU : le validateur de build bloquant

[EN SERVICE depuis le 17/09 au soir] .radar/tools/verrou.py, branché dans validate.py :
toute publication échoue sur V1 champs empoisonnés (None/null/undefined/NaN/[object
Object]) dans title/description/og/h1, V2 saison périmée dans les métadonnées de
structure, V3 page sans title/description/canonical, V4 d2 < d1, V5 compteurs
divergents, V6 lien interne cassé, V7 URL de sitemap sans fichier, V8 JSON-LD
illisible, V9 hreflang vers fichier absent, V10 grappes hreflang réciproques, V11 budget
de poids, V12 tiret long dans le texte visible d'une page publiée (28/09), V13 saison
du bandeau dans le JSON d'interface des 13 langues (28/09). En avertissement (promotion
à venir) : W1 date écrite hors fenêtre machine, W2 page sans h1. 8 179 pages contrôlées
au 28/09.
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
