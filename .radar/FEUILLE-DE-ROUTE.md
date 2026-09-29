# Feuille de route · un site de niveau mondial, prêt pour un million de visiteurs par jour

Commande de Constance du 18/09/2026. Document vivant : les taux d'avancement sont
tenus à jour à chaque publication. Source de vérité : ce fichier.

## L'ambition, dite honnêtement

Un million de visiteurs par jour, c'est l'audience d'un grand média mondial. La
technique peut y être prête, et c'est l'objet de cette feuille de route : que le
site tienne un million de visiteurs le jour où ils arrivent, sans ralentir, sans
casser, sans coûter une fortune. L'audience elle-même se gagne par paliers de dix
(100, 1 000, 10 000, 100 000, 1 000 000 par jour), et chaque palier se franchit
avec un moteur différent : le référencement porte jusqu'à quelques milliers ; au-delà,
ce sont la marque, la presse, les partenaires et les assistants d'intelligence
artificielle qui portent, leviers mis en pause à ta demande jusqu'à ce que le site
soit sans point faible. Aujourd'hui : palier 1 (35 à 100 visites par jour).

## DÉCISION DU 18/09/2026 : on reste chez GitHub Pages, comme maintenant

Constance a tranché après avis : pas de Cloudflare pour l'instant. Tout ce qui suit
est donc compatible avec un hébergement statique GitHub Pages. Les micro-objectifs
qui exigeaient Cloudflare sont marqués « hors périmètre » et ne comptent pas dans
les taux. Impératif posé le même jour : « un site très rapide sur mobile, Android
et iOS ». L'objectif O3 passe en priorité absolue.

## L'avis d'hébergement (rendu le 18/09, non retenu pour l'instant)

Constat au 18/09/2026 : 7 966 fichiers publiés (48 Mo), accueil de 2,5 Mo, 64
publications par semaine, aucun en-tête de sécurité servi, redirections faites par
pages de renvoi (pas de vrai 301), bande passante limitée en pratique à 100 Go par
mois chez GitHub Pages.

VERDICT :
1. AUJOURD'HUI, rester hébergé chez GitHub Pages (gratuit, fiable, déjà servi par
   un réseau mondial) : il tient largement jusqu'au palier 2 (1 000 par jour).
2. DÈS MAINTENANT, mettre Cloudflare DEVANT le site (offre gratuite) : le nom de
   domaine passe chez Cloudflare, qui se place entre le visiteur et GitHub Pages.
   Gains immédiats sans rien changer au site : en-têtes de sécurité (HSTS, CSP),
   vraies redirections 301 pour les 178 anciennes adresses, cache mondial plus
   agressif, HTTP/3 et Brotli, protection contre les attaques, statistiques sans
   cookie compatibles avec la promesse zéro donnée. Geste requis de Constance :
   créer le compte Cloudflare et changer les serveurs de noms chez le registrar
   du domaine (si c'est Gérald qui gère le domaine, c'est avec lui).
3. AVANT LE PALIER 3 (10 000 par jour), basculer l'hébergement sur Cloudflare
   Pages : bande passante illimitée, déploiement depuis le même dépôt GitHub (la
   chaîne de publication et les passes automatiques ne changent pas). Limites à
   connaître : 20 000 fichiers par déploiement (nous en avons 7 966 ; la limite
   sera atteinte vers 850 événements), 500 déploiements par mois en gratuit (nous
   en faisons environ 270).
4. R2 (stockage) : seulement le jour où le radar porte des photos par événement.
   Inutile aujourd'hui (une seule photo).
5. D1 (base de données) et Workers : seulement le jour d'un produit dynamique
   (Cercle, alertes personnalisées, API pour partenaires) ou pour dépasser la
   limite des 20 000 fichiers par un rendu à la volée. Ce n'est pas un besoin du
   radar tel qu'il est : c'est le socle du palier 4 et au-delà.

Coût : gratuit jusqu'au palier 3 ; de l'ordre de 25 dollars par mois au palier 3
(images, statistiques avancées) ; quelques centaines par mois au palier 5, ce qui
reste dérisoire pour un million de visiteurs par jour.

## Les objectifs et leurs micro-objectifs

Légende : [100] fait · [50] à moitié · [0] à faire. Le taux d'un objectif est la
moyenne de ses micro-objectifs.

### O1 · Fondations sans point faible (registre de l'audit croisé) · 86 %
- [100] Verrou de build bloquant sur les 7 876 pages, 13 langues
- [100] Compteurs réconciliés et expliqués
- [100] Redirections des anciennes adresses (lieux et fiches)
- [100] Français résiduel traduit dans les 12 langues
- [100] Métadonnées saisonnières purgées, titres « None » réparés ; défaut trouvé le 28/09 :
        la ligne de marque du bloc d'accueil affichait encore « Summer 2026 » dans les 13
        langues (JSON d'interface, jamais lu par le contrôle V2) ; corrigé (saison.py
        relancé, motif du titre réparé) et verrou V13 posé (saison du bandeau contrôlée
        à chaque publication)
- [100] Échappement et injection (recherche, favoris, JS) : testé en direct le 25/09,
        injection HTML/script bloquée, script CJK/arabe/cyrillique/emoji/entrées très
        longues sans casse ; défaut trouvé et corrigé (recherche insensible aux accents
        depuis le 25/09, « Cote » trouve « Côte ») ; apostrophes typographiques ramenées à
        l'apostrophe droite le 28/09 (« l’opéra » et « l'opera » donnent les mêmes 4
        cartes, testé avant publication)
- [60]  Cannibalisation entre langues : hreflang dans le sitemap posé ; matrice intention
        vers adresse unique posée le 28/09 (.radar/MATRICE-INTENTIONS.md : fiche d'édition,
        guide permanent français, page lieu, rôles et titres distincts, liens réciproques
        vérifiés, x-default vers le français) ; reste la mesure par requête au bilan du
        2/10 et, si Google sert encore une mauvaise langue, la différenciation des
        descriptions par langue
- [100] États vides : aucun favori (page), aucun résultat (recherche, 13 langues), carte
        du moment cachée si indisponible ; mode hors connexion posé le 28/09 (service
        worker, page « Hors connexion », pages visitées consultables sans réseau, testé
        serveur coupé puis vérifié en ligne)
- [88]  Aperçus sociaux : og et cartes Twitter/X sur toutes les pages ; dimensions et
        texte alternatif de l'image ajoutés le 28/09 ; nom du site et langue de la page
        (og:site_name, og:locale par langue) ajoutés le 29/09 ; image d'aperçu de 37 Ko,
        sous les limites des messageries ; reste le contrôle visuel WhatsApp, iMessage,
        LinkedIn et une image par événement
- [100] JSON-LD Event recalibré le 20/09 : offre seulement si l'accès s'achète ou se
        réserve (237 fiches sur 320 au lieu de toutes), jamais d'InStock sur invitation,
        gratuité seulement si écrite, statut annulé ou reporté lu dans les textes
- [95]  Fraîcheur : trois dates distinctes et honnêtes (passe, fiche, file de
        revérification) ; outil reverification.py et étape 5bis de la doctrine posés le
        27/09. Le 28/09, la passe de nuit a revérifié 2 fiches (Fondazione Prada, Villa
        Carmignac) et maintenu 1 doute avec preuve (Gaïo Saint-Tropez, aucune date de fin
        publiée) ; puis 40 fiches imminentes ou en cours ont été confrontées à leur source
        officielle par 10 lots parallèles (citation verbatim exigée, site tiers refusé) :
        28 confirmées à l'identique et datées, 5 corrigées (Sphère ouvre le 30 septembre
        et non le 28 ; Arqana du 20 au 23 octobre ; Sotheby's Hong Kong vente du soir le
        28 et ventes de jour le 29 ; Global Gift Gala Paris le 5 novembre au Four Seasons
        George V et non « octobre, date inconnue » ; Journées Particulières LVMH 71 lieux
        dans 13 pays, fiche renommée avec redirection), 6 introuvables laissées sans date
        (sites en 403 ou sans date publiée) ; toutes les corrections traduites dans les
        13 langues. Second lot dans la nuit du 28 au 29/09 (62 fiches, coupé par la limite
        de session, relancé) : Ushuaïa et Blue Marlin confirmés (fins de saison), Splendido
        Mare corrigé (ouvert jusqu'au 6 janvier 2027, source Belmond), 7 saisons sans date
        de fin publiée laissées sans date ; la passe de nuit du 29/09 a corrigé 5 dates de
        fin sur source et purgé 7 fiches terminées. Troisième lot le 29/09 au matin (62
        fiches, 13 lots) : 24 fins de saison ou dates confirmées à la source et datées,
        Amanzoe corrigé (jusqu'au 30 septembre et non 31 octobre, 13 langues), 33 saisons
        sans date de fin publiée laissées sans date. Journal des preuves (citation, source,
        verdict de chaque vérification) dans .radar/journal. Mesure au 29/09 après ces
        trois lots : 207 fiches vivantes, 90 datées « vérifié à la source », file de
        revérification de 106 à 43. Le 29/09, honnêteté sur ces 43 : les 36 saisons dont
        l'organisateur ne publie aucune date de fin portent désormais la mention « source
        relue le 28/09/2026, fin estimée par le radar » (sans badge), et 21 d'entre elles
        passent de « confirmé » à « probable » ; 4 sources inaccessibles notées à retenter ;
        file ramenée à 5. Reste : les passes de nuit, et un badge qui ne s'affiche que sur
        une date réellement confirmée.
- [100] Statuts des récurrents et saisons : JSON-LD de l'accueil recalculé à chaque
        build depuis le 27/09 (annulé, reporté, programmé seulement si confirmé, sinon
        aucun statut affirmé) ; champ de confirmation ramené à trois valeurs, 35 fiches
        confirmées qui s'affichaient « à vérifier » réparées ; années contrôlées sur les
        319 fiches le 27/09 (22 mentions d'une autre année, toutes légitimes)
- [100] Règle 403/429 des liens externes vérifiée le 20/09 (déjà juste dans la passe)
- [100] Cohérence éditoriale : graphies normalisées (Monte-Carlo, Saint-Tropez, Saint-Moritz,
        Saint-Barth) ; tirets longs interdits purgés du site entier le 24/09 (plus de 10 600
        corrections, 13 langues, vérifié en ligne) ; vocabulaire des doutes unifié le 27/09
        (confirmé / probable / à vérifier, trois valeurs et pas cinq graphies) ; découverte
        du 28/09 : deux lignes du générateur de pages republiaient chaque nuit près de
        22 000 tirets sur les hubs et les séjours des 12 langues étrangères, invisibles aux
        purges qui ne lisaient que les données ; corrigées à la source, 45 tirets corrigés à
        la main dans la page Note traduite, 1 dans la mémoire du radar, 7 dans le tableau de
        bord public ; contrôle bloquant V12 au verrou sur le texte visible de toute page
        publiée (8 166 pages, 0 restant, vérifié en ligne)
- [97]  Accessibilité : lien d'évitement, <main>, focus visible, coeurs nommés, contrastes
        vérifiés, commandes symboliques (thème, langue, flèche) nommées en 13 langues
        (20/09) ; audit structurel par arbre d'accessibilité le 25/09 (1 seul h1, 0 image
        sans alt, landmarks propres) : un vrai défaut trouvé, corrigé le 25/09 (bouton
        favori sorti des 217 titres de cartes, rendu frère, testé au navigateur avant
        publication ; gen_pages.py vérifié indemne du même patron) ; contraste mesuré en
        direct le 25/09 (formule WCAG) : thème sombre 6,41 à 19,19, thème clair 5,78 à
        15,96, tout au-dessus du seuil de 4,5 pour 1 ; saut de niveau de titre h2→h4
        corrigé le 26/09 (Classement Prestige et Archives, passés en h3, aucun changement
        visuel, style porté par la classe CSS, pas la balise) ; flèches décoratives des
        liens masquées aux lecteurs d'écran le 28/09 (aria-hidden, toutes les pages) ; audit
        automatisé axe-core (WCAG 2.1 AA et bonnes pratiques) le 28/09 sur accueil, fiche,
        fiche arabe, hub et favoris : un vrai défaut trouvé et corrigé (liens des fils
        d'Ariane et des lignes de métadonnées distingués par la couleur seule ; soulignés
        d'un trait fin sur toutes les pages), 0 violation après correction ; reste un vrai
        passage au lecteur d'écran
- [95]  Validité HTML (validateur W3C, 28/09) : une erreur de structure sur toutes les
        fiches corrigée (bloc de style dans le corps de page, déplacé dans l'en-tête),
        adresse du script de mesure explicitée, cinq blocs de l'accueil sans titre passés
        en div ; pages générées à 0 erreur et 0 avertissement ; l'accueil ne garde que
        deux faux positifs (syntaxe image-set avec type(), que le validateur ne connaît
        pas encore) ; verrou V14 : plus jamais de style dans le corps d'une page
- [95]  Arabe de droite à gauche et langues CJK contrôlés à l'écran le 20/09 : rendu
        correct, et un vrai bogue attrapé (le lien d'évitement décalait toute la page
        arabe hors de l'écran) ; flèches directionnelles retournées le 25/09 (page
        arabe et accueil basculé en arabe, testé dans les deux sens) ; ponctuation mixte
        contrôlée à l'écran le 28/09 sur une fiche arabe (heures, note 86/100, noms de
        lieux latins dans une phrase arabe : tout se lit dans l'ordre) ; un vrai défaut
        trouvé et corrigé le 28/09 : un titre latin commençant par un nombre
        (« 104. Jägerball… ») se lisait « Jägerball… .104 » sur la page arabe ; titres
        des fiches et des listes en dir=auto sur toutes les pages, vérifié à l'écran ;
        langue et sens de lecture mémorisés appliqués dès l'en-tête de l'accueil (plus
        de bascule après le premier affichage)
- [0]   En-têtes de sécurité (dépend de Cloudflare devant)
- [0]   Newsletter : double opt-in, anti-spam, désinscription (samedi 20/09)

### O2 · Infrastructure (périmètre GitHub Pages) · 100 %
- [100] HTTPS forcé, http et www redirigés
- [100] Réseau de diffusion mondial (Fastly via GitHub Pages, cache 10 minutes)
- [100] Redirections des anciennes adresses (178 pages de renvoi, le maximum possible ici)
- [100] Surveillance de disponibilité : sonde du matin, sonde continue locale depuis le
        18/09 (5 adresses, 525 mesures en 9 jours au 27/09 : zéro 5xx, médiane 0,20 s,
        95 % sous 0,61 s ; les seuls échecs sont des coupures de la machine qui sonde,
        toutes adresses à la même seconde) et, depuis le 28/09, sonde GitHub indépendante
        de toute machine toutes les 30 minutes (5 adresses, 3 essais à 20 s d'écart avant
        alerte) : alerte par issue et courriel GitHub, fermeture automatique au retour ;
        premier passage vérifié vert (5 fois 200, 0,16 à 0,35 s)
- [100] Équivalents statiques des en-têtes : CSP et referrer en balise meta sur toutes
        les pages (25/09), testés avant et après publication ; HSTS, nosniff et
        frame-ancestors restent hors de portée sans Cloudflare devant le site
- [hors périmètre, vérifié 25/09] Empreintes de version pour un cache long côté
        navigateur : GitHub Pages impose `cache-control: max-age=600` (10 minutes) sur
        TOUT, y compris la photo d'accueil, sans aucun moyen de le changer par fichier
        ou par balise ; un nom de fichier à empreinte recevrait le même en-tête. La
        technique n'apporte donc rien ici (vérifié par une requête réelle sur la photo,
        moment.json et un fichier i18n-data) ; les ETags présents limitent déjà le coût
        au strict minimum (304 Non modifié) après les 10 minutes. À revoir seulement
        si Cloudflare passe devant le site
- [hors périmètre] Cloudflare devant, en-têtes HTTP, vrais 301, HTTP/3, Cloudflare Pages, R2, Workers, D1

### O3 · Vitesse mobile, Android et iOS (PRIORITÉ ABSOLUE) · 100 %
Mesure de référence du 18/09/2026 : un téléphone reçoit 820 Ko pour l'accueil
(2 547 Ko bruts), plus 294 Ko de photo et 43 Ko d'index de recherche, soit environ
1,15 Mo. Le poids vient de deux champs embarqués inutiles au premier affichage :
les textes de séjour (1 088 Ko) et les journaux d'enquête (619 Ko). Une fiche
événement ne pèse que 4 Ko transférés : les fiches sont déjà rapides.
- [100] Polices système (Didot, Avenir), aucune police téléchargée
- [100] Mesure de référence établie (poids par bloc, transfert réel)
- [100] Photo d'accueil en AVIF/WebP par largeur d'écran : 34 Ko sur téléphone, 67 Ko sur
        ordinateur, au lieu de 294 Ko (20/09) ; JPEG conservé pour les vieux navigateurs
- [100] Séjours et journaux d'enquête sortis de l'accueil, chargés à la demande
        (18/09 : accueil de 2 547 Ko à 868 Ko bruts, de 820 Ko à 264 Ko transférés,
        trois fois plus léger ; sections conservées, contenu chargé au dépliage)
- [écarté 20/09] JSON-LD de l'accueil en liste : gain mesuré de 8 Ko compressés seulement,
        contre la règle « gen_pages ne modifie jamais index.html » ; pas rentable
- [100] Budget de poids au verrou (V11 : accueil sous 1 000 Ko bruts, fiche sous 60 Ko)
- [95]  LCP < 2,5 s, INP < 200 ms, CLS < 0,1 : mesurés le 28/09 par le protocole DevTools
        de Chrome dans les conditions de Lighthouse mobile (écran 412 px, 4G lent 1,6 Mbit/s
        et 150 ms, CPU ralenti 4 fois), outil persisté. Accueil : LCP 0,43 à 1,07 s, CLS
        0,08, INP 264 ms (et jusqu'à 3 s quand le clic tombait pendant le rendu des cartes)
        AVANT correction ; corrigé le même jour (rendu différé des jours hors écran par
        content-visibility, frappe de recherche regroupée à 120 ms) : INP 88 à 120 ms en
        ligne, aucune erreur. Fiches : LCP 0,34 à 0,67 s, CLS 0, 4 à 6 Ko transférés. CLS
        de l'accueil ramené de 0,08 à 0 le même jour : le décalage venait des libellés du
        bloc d'accueil remplacés après le premier affichage (barre de catégories sur une
        ligne de plus) ; libellés statiques alignés, bloc de langue généré à chaque build et
        placé avant le reste de la page ; mesuré en ligne à 0 en français, anglais, arabe et
        chinois (LCP 0,43 à 0,90 s). Reste la mesure PageSpeed officielle (quota toujours
        épuisé) ; la mesure hebdomadaire du lundi est inscrite à la doctrine (5ter) et
        automatisée le 29/09 sur la machine de travail (launchd, lundi 9 h 40 : vitesse,
        validateur W3C, axe-core, journalisés et poussés).
- [100] Rendu progressif des cartes (25/09) : les deux premiers jours s'affichent aussitôt,
        le reste par lots hors du fil principal (requestIdleCallback, repli iOS/Safari),
        recherche toujours instantanée, vérifié sans doublon ni erreur
- [100] Écrans de 320, 375 et 390 px contrôlés le 20/09 : plus aucun débordement horizontal
        (accueil, fiches, hubs, arabe compris) ; paysage (812×375) et clavier ouvert (hauteur
        réduite à 320 px) contrôlés le 25/09, propres l'un et l'autre ; cibles tactiles
        portées à 44 px le 25/09 (33 cibles sous la barre avant, 21 après, le reste des
        puces secondaires laissées compactes) ; zoom 200 % et 400 % vérifiés le 28/09 avec
        de vraies largeurs de 640 et 320 px CSS (accueil, fiche, arabe, lieu anglais, page
        hors connexion) : aucun débordement
- [100] Sitemap scindé par langue avec index (20/09) : 13 fichiers de 850 Ko au lieu d'un
        seul de 11 Mo ; le verrou lit l'index

### O4 · Données et contenu à l'échelle · 63 %
- [100] Passes de nuit (purge, liens, condensation)
- [100] Résorption hebdomadaire de tous les doutes, aux sources
- [100] Sentinelle des imminents (lundi)
- [100] Mémoire du radar (archives, changements)
- [31]  309 événements vivants sur un palier de 1 000 (au 29/09, après purge des saisons
        terminées ; le radar grossit par les passes de nuit)
- [0]   Photos par événement (R2)
- [0]   Rendu à la volée au-delà de 850 événements (limite des 20 000 fichiers)
- [70]  API publique JSON (partenaires, assistants d'IA, applications) : /api/evenements.json
        publié le 29/09 (tous les événements : dates, lieu, catégorie, accès, degré de
        confirmation, source officielle, date de vérification, note, fiche en 13 langues,
        fichier calendrier), régénéré à chaque publication, CORS ouvert, page /api/ avec les
        champs et les conditions (attribution libre, usage commercial sur accord), llms.txt
        complété ; reste un premier partenaire ou assistant qui le consomme

### O5 · Visibilité organique mondiale · 75 %
- [100] Titres en forme de requêtes, 13 langues, mois courant automatique
- [100] hreflang sur les pages et dans le sitemap
- [100] 88 pages Questions FR et EN, balisage FAQ
- [100] Search Console lue en entier et exploitée
- [50]  Résorption du cache Google (titres None, saison) : en cours
- [100] JSON-LD Event propre (recalibré le 20/09)
- [30]  Taux de clic des pages villes (mesure au bilan du 2/10)
- [100] Pages Questions dans les 12 langues : les 11 publiées le 26/09 (allemand,
        espagnol, italien, portugais, russe, arabe, chinois, japonais, coréen, hindi)
        et le TURC le 27/09 (44 questions, 4 lots parallèles), qui avait échoué
        6 fois auparavant. Contrôle factuel mécanique (`.radar/tools/verif_traduction.py`,
        nouvel outil persisté ce jour, contacts/URLs/tarifs comparés au français) :
        1 seule alerte sur 44, une localisation de devise (« 400 francs suisses » →
        « 400 İsviçre frangı ») non reconnue par le détecteur, vérifiée à la main,
        aucune perte réelle. Zéro tiret long. Les 12 langues + le français sont
        désormais complètes sur les 44 questions.
- [70]  Matrice intention vers adresse unique (Milan, Paris Fashion Week, Vogue World)
        posée le 28/09 : trois familles de pages par sujet, chacune avec son intention,
        son titre et ses liens vers les deux autres (vérifiés) ; reste la mesure au 2/10
- [0]   Liens entrants (en pause volontaire ; liste de 20 relais prête)

### O6 · Produit et rétention · 68 %
- [100] Favoris partout, page Mes favoris, compteur
- [100] Moteur Comment entrer, Note du radar, Protocole, Questions
- [75]  Partage : aperçus og par page, dimensions et texte alternatif de l'image depuis le
        28/09 (à contrôler messagerie par messagerie)
- [0]   Newsletter hebdomadaire (dimanche 21/09)
- [65]  Alertes liées aux favoris : « Ajouter à mon agenda » sur chaque fiche le 28/09
        (fichier calendrier .ics, journée entière, français ou anglais selon la langue) ;
        page Mes favoris refaite le 29/09 : favoris triés par date, mention « dans N jours »,
        « en cours » ou « terminé », ligne « Prochain favori », ajout au calendrier par
        événement et « Tout ajouter à mon agenda » en un seul fichier construit dans le
        navigateur (rien ne quitte l'appareil), testé avant publication (tri, états, fichier
        de 3 événements, retrait) ; reste l'alerte automatique, qui exige un canal (courriel
        ou notification)
- [0]   Le Cercle (on ne peut pas acheter, on est choisi)
- [100] Site installable et consultable hors connexion (28/09) : manifeste, icônes (onglet,
        écran d'accueil iOS et Android, monogramme C7 en Didot), service worker réseau
        d'abord avec copie de secours des pages visitées (90 entrées au plus, jamais de
        ressource tierce), page « Hors connexion » dédiée ; testé serveur coupé en local
        (accueil avec 116 cartes, fiche visitée, page inconnue vers la page de secours,
        zéro erreur) puis vérifié en ligne (worker actif, 6 entrées en cache, manifeste
        lu avec ses 3 icônes)
- [100] Impression propre des fiches (25/09) : feuille d'impression dédiée sur toutes
        les pages générées, navigation et favoris masqués, adresses des liens utiles
        affichées en clair, fond blanc ; n'affecte jamais l'écran, vérifié en ligne

### O7 · Confiance, sécurité, conformité · 71 %
- [100] HTTPS, zéro cookie, zéro donnée collectée
- [100] Aucun fichier de travail en ligne, aucun secret dans le code
- [100] Sonde quotidienne du site en ligne
- [100] Échappement et protection des liens externes : contrôle du 28/09 sur les 3 904
        pages qui portent un lien externe, zéro lien ouvert dans un nouvel onglet sans
        rel=noopener, zéro lien externe sans attribut rel
- [70]  Mentions légales : page complète pour le site tel qu'il est (éditrice non
        professionnelle et anonymat LCEN, hébergeur, domaine, propriété intellectuelle,
        données personnelles, GoatCounter, mémoire des favoris, droits RGPD, liens
        sortants, droit applicable) ; reste la mention du prestataire de newsletter le
        jour où elle existe
- [100] Politique de confidentialité : page dédiée publiée le 25/09, reprend et complète
        la section déjà écrite des mentions légales (la mention des favoris manquait),
        liée depuis le pied de page de tout le site ; vérifiée en ligne
- [0]   Double opt-in, SPF, DKIM, DMARC pour la newsletter
- [0]   En-têtes de sécurité (Cloudflare)

### O8 · Observabilité et pilotage · 84 %
- [100] Compteur public GoatCounter
- [100] Search Console vérifiée, exports lus
- [100] Sonde du matin (quotidienne) et contrôle Google contre site (hebdomadaire)
- [100] Bilan observatoire du 2 octobre programmé
- [100] Sonde de disponibilité : locale sans interruption depuis le 18/09 (zéro 5xx), et
        depuis le 28/09 chez GitHub toutes les 30 minutes, indépendante de la machine (plus
        rien à relancer si elle redémarre)
- [85]  Tableau de bord unique : générateur .radar/tools/tableau_de_bord.py posé le 28/09,
        qui lit les journaux existants (visiteurs par jour, vitesse mobile LCP/INP/CLS,
        fraîcheur et file de revérification, taux de la feuille de route, dernières
        publications et passes) et produit une page privée, publiée à Constance en artefact
        « Pilotage ConstanceParis7 » ; régénéré chaque matin par le plancher GitHub depuis
        le 29/09 (étape de passe-quotidienne.yml, jamais bloquante) ; le tableau public des
        visites reste tel quel (ses 7 tirets purgés le 28/09) ; reste à republier
        l'artefact à chaque session de travail
- [0]   Statistiques Cloudflare sans cookie
- [85]  Alertes : la sonde du matin contrôle que la passe de nuit a tourné et la relance
        sinon, mesure PageSpeed et tient un journal de vitesse (20/09) ; alerte hors
        session en place : issue GitHub et courriel au propriétaire, pour un site figé
        (surveillance.yml, deux fois par jour) et pour une adresse qui ne répond plus
        (disponibilite.yml, toutes les 30 minutes depuis le 28/09) ; reste PageSpeed
        (quota)

### O9 · Les paliers d'audience et leur prérequis technique
- [100] Palier 1, 100 par jour : atteint (35 à 100)
- [55]  Palier 2, 1 000 par jour : accueil allégé (fait), vitesse mobile mesurée dans le
        vert (fait), surveillance et alertes indépendantes (fait), site installable et hors
        connexion (fait) ; reste Cloudflare devant, le taux de clic (bilan du 2/10) et la
        newsletter
- [45]  Palier 3, 10 000 par jour : sitemaps scindés (fait), budget de performance au
        verrou (fait), alertes automatiques (fait), API publique (fait) ; reste Cloudflare
        Pages pour la bande passante, décision à rouvrir le moment venu
- [0]   Palier 4, 100 000 par jour : rendu à la volée (Workers, KV), R2, API,
        cache agressif, contenu à 1 000 événements et plus
- [0]   Palier 5, 1 000 000 par jour : architecture edge complète, D1, tests de
        charge, plan de reprise, coûts maîtrisés ; et la distribution mondiale
        (marque, presse, partenaires, assistants d'IA)

## La durée du travail, honnêtement

- Semaine 1 (19 au 26 septembre) : vitesse mobile de l'accueil (O3, cible trois fois
  plus léger), newsletter du 21, fin des points critiques du registre.
- Semaines 2 et 3 (jusqu'au 10 octobre) : accessibilité, arabe et langues asiatiques
  à l'écran, JSON-LD, états vides, aperçus sociaux ; bilan du 2 octobre.
- Semaines 4 à 6 (jusqu'à fin octobre) : pages Questions en 11 langues, matrice
  d'intentions, sitemaps scindés, alertes automatiques, tableau de bord unique.
- Ensuite, en continu : le radar grossit (palier 1 000 événements), les routines
  tiennent la qualité, les mesures pilotent. Sur GitHub Pages, le plafond technique
  se situe autour du palier 3 (10 000 par jour) à cause de la bande passante ; au-delà,
  la question de l'hébergement se rouvrira, à ta main.

## L'ordre des prochaines semaines
1. Registre de l'audit jusqu'au bout (O1), en commençant par l'accueil de 2,5 Mo (O3).
2. Équivalents statiques des en-têtes et empreintes de version (O2).
3. Newsletter du 21/09 avec ses contrôles (O6, O7).
4. Bilan du 2/10 : mesure, puis décision de positionnement.
5. Mesure PageSpeed hebdomadaire jusqu'au vert sur les trois indicateurs.
