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

### O1 · Fondations sans point faible (registre de l'audit croisé) · 78 %
- [100] Verrou de build bloquant sur les 7 876 pages, 13 langues
- [100] Compteurs réconciliés et expliqués
- [100] Redirections des anciennes adresses (lieux et fiches)
- [100] Français résiduel traduit dans les 12 langues
- [100] Métadonnées saisonnières purgées, titres « None » réparés
- [80]  Échappement et injection (recherche, favoris, JS)
- [30]  Cannibalisation entre langues (hreflang sitemap posé, matrice à faire)
- [70]  États vides : aucun favori (page), aucun résultat (recherche, 13 langues), carte
        du moment cachée si indisponible ; reste le mode hors connexion
- [60]  Aperçus sociaux : og et cartes Twitter/X sur toutes les pages ; reste le contrôle
        du rendu WhatsApp, iMessage, LinkedIn et une image par événement
- [100] JSON-LD Event recalibré le 20/09 : offre seulement si l'accès s'achète ou se
        réserve (237 fiches sur 320 au lieu de toutes), jamais d'InStock sur invitation,
        gratuité seulement si écrite, statut annulé ou reporté lu dans les textes
- [0]   Fraîcheur : dernière vérification distinguée du build quotidien
- [0]   Statuts des récurrents et saisons (EventCancelled, estimations)
- [100] Règle 403/429 des liens externes vérifiée le 20/09 (déjà juste dans la passe)
- [90]  Cohérence éditoriale : graphies normalisées (Monte-Carlo, Saint-Tropez, Saint-Moritz,
        Saint-Barth) ; tirets longs interdits purgés du site entier le 24/09 (plus de 10 600
        corrections, 13 langues, vérifié en ligne) ; reste le vocabulaire des doutes, mineur
- [93]  Accessibilité : lien d'évitement, <main>, focus visible, coeurs nommés, contrastes
        vérifiés, commandes symboliques (thème, langue, flèche) nommées en 13 langues
        (20/09) ; audit structurel par arbre d'accessibilité le 25/09 (1 seul h1, 0 image
        sans alt, landmarks propres) : un vrai défaut trouvé, corrigé le 25/09 (bouton
        favori sorti des 217 titres de cartes, rendu frère, testé au navigateur avant
        publication ; gen_pages.py vérifié indemne du même patron) ; contraste mesuré en
        direct le 25/09 (formule WCAG) : thème sombre 6,41 à 19,19, thème clair 5,78 à
        15,96, tout au-dessus du seuil de 4,5 pour 1 ; reste un vrai passage au lecteur
        d'écran et le saut de niveau de titre h2→h4 sous Prestige
- [70]  Arabe de droite à gauche et langues CJK contrôlés à l'écran le 20/09 : rendu
        correct, et un vrai bogue attrapé (le lien d'évitement décalait toute la page
        arabe hors de l'écran) ; reste les flèches directionnelles et la ponctuation mixte
- [0]   En-têtes de sécurité (dépend de Cloudflare devant)
- [0]   Newsletter : double opt-in, anti-spam, désinscription (samedi 20/09)

### O2 · Infrastructure (périmètre GitHub Pages) · 68 %
- [100] HTTPS forcé, http et www redirigés
- [100] Réseau de diffusion mondial (Fastly via GitHub Pages, cache 10 minutes)
- [100] Redirections des anciennes adresses (178 pages de renvoi, le maximum possible ici)
- [50]  Surveillance de disponibilité (sonde du matin ; sonde 24 h en cours)
- [100] Équivalents statiques des en-têtes : CSP et referrer en balise meta sur toutes
        les pages (25/09), testés avant et après publication ; HSTS, nosniff et
        frame-ancestors restent hors de portée sans Cloudflare devant le site
- [0]   Empreintes de version sur les ressources (photo, JSON) pour un cache long côté navigateur
- [hors périmètre] Cloudflare devant, en-têtes HTTP, vrais 301, HTTP/3, Cloudflare Pages, R2, Workers, D1

### O3 · Vitesse mobile, Android et iOS (PRIORITÉ ABSOLUE) · 83 %
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
- [20]  LCP < 2,5 s, INP < 200 ms, CLS < 0,1 mesurés (PageSpeed mobile, chaque semaine ; le
        quota de l'API reste épuisé à chaque essai). Mesure de repli le 25/09, en conditions
        réelles 3G simulées dans le navigateur (TTFB 324 ms, DOM prêt 590 ms, chargement
        complet 886 ms, 267 Ko transférés pour l'accueil) : le décalage cumulé (CLS) mesuré
        est nul. Le LCP et l'INP exacts restent hors d'atteinte : l'outil de mesure du
        navigateur de cette session ne peuple pas ces deux entrées de performance ; seul
        PageSpeed les donnerait, et son quota reste bloqué.
- [100] Rendu progressif des cartes (25/09) : les deux premiers jours s'affichent aussitôt,
        le reste par lots hors du fil principal (requestIdleCallback, repli iOS/Safari),
        recherche toujours instantanée, vérifié sans doublon ni erreur
- [95]  Écrans de 320, 375 et 390 px contrôlés le 20/09 : plus aucun débordement horizontal
        (accueil, fiches, hubs, arabe compris) ; paysage (812×375) et clavier ouvert (hauteur
        réduite à 320 px) contrôlés le 25/09, propres l'un et l'autre ; cibles tactiles
        portées à 44 px le 25/09 (33 cibles sous la barre avant, 21 après, le reste des
        puces secondaires laissées compactes) ; le zoom 200 % reste
        à vérifier proprement, l'essai du 25/09 n'était pas fiable (le zoom CSS simulé fausse
        les unités vw, contrairement au vrai zoom d'un téléphone ou d'un navigateur)
- [100] Sitemap scindé par langue avec index (20/09) : 13 fichiers de 850 Ko au lieu d'un
        seul de 11 Mo ; le verrou lit l'index

### O4 · Données et contenu à l'échelle · 35 %
- [100] Passes de nuit (purge, liens, condensation)
- [100] Résorption hebdomadaire de tous les doutes, aux sources
- [100] Sentinelle des imminents (lundi)
- [100] Mémoire du radar (archives, changements)
- [34]  335 événements sur un palier de 1 000
- [0]   Photos par événement (R2)
- [0]   Rendu à la volée au-delà de 850 événements (limite des 20 000 fichiers)
- [0]   API publique JSON (partenaires, assistants d'IA, applications)

### O5 · Visibilité organique mondiale · 55 %
- [100] Titres en forme de requêtes, 13 langues, mois courant automatique
- [100] hreflang sur les pages et dans le sitemap
- [100] 88 pages Questions FR et EN, balisage FAQ
- [100] Search Console lue en entier et exploitée
- [50]  Résorption du cache Google (titres None, saison) : en cours
- [100] JSON-LD Event propre (recalibré le 20/09)
- [30]  Taux de clic des pages villes (mesure au bilan du 2/10)
- [0]   Pages Questions dans les 11 autres langues
- [0]   Matrice intention vers URL unique (Milan, PFW, Vogue World)
- [0]   Liens entrants (en pause volontaire ; liste de 20 relais prête)

### O6 · Produit et rétention · 35 %
- [100] Favoris partout, page Mes favoris, compteur
- [100] Moteur Comment entrer, Note du radar, Protocole, Questions
- [60]  Partage : aperçus og par page (à contrôler messagerie par messagerie)
- [0]   Newsletter hebdomadaire (dimanche 21/09)
- [0]   Alertes liées aux favoris
- [0]   Le Cercle (on ne peut pas acheter, on est choisi)
- [0]   Site installable et consultable hors connexion (PWA)
- [0]   Impression propre des fiches

### O7 · Confiance, sécurité, conformité · 60 %
- [100] HTTPS, zéro cookie, zéro donnée collectée
- [100] Aucun fichier de travail en ligne, aucun secret dans le code
- [100] Sonde quotidienne du site en ligne
- [80]  Échappement et protection des liens externes
- [50]  Mentions légales (page existante, à compléter le 21/09)
- [100] Politique de confidentialité : page dédiée publiée le 25/09, reprend et complète
        la section déjà écrite des mentions légales (la mention des favoris manquait),
        liée depuis le pied de page de tout le site ; vérifiée en ligne
- [0]   Double opt-in, SPF, DKIM, DMARC pour la newsletter
- [0]   En-têtes de sécurité (Cloudflare)

### O8 · Observabilité et pilotage · 62 %
- [100] Compteur public GoatCounter
- [100] Search Console vérifiée, exports lus
- [100] Sonde du matin (quotidienne) et contrôle Google contre site (hebdomadaire)
- [100] Bilan observatoire du 2 octobre programmé
- [50]  Sonde de disponibilité 24 h (en cours) puis permanente
- [30]  Tableau de bord unique (tableau-de-bord.html à enrichir)
- [0]   Statistiques Cloudflare sans cookie
- [60]  Alertes : la sonde du matin contrôle désormais que la passe de nuit a tourné et
        la relance sinon, mesure PageSpeed et tient un journal de vitesse (20/09) ;
        reste une alerte hors session (courriel) le jour où un canal existera

### O9 · Les paliers d'audience et leur prérequis technique
- [100] Palier 1, 100 par jour : atteint (35 à 100)
- [40]  Palier 2, 1 000 par jour : accueil allégé, Cloudflare devant, taux de clic
        corrigé, newsletter lancée
- [10]  Palier 3, 10 000 par jour : Cloudflare Pages, sitemaps scindés, budget de
        performance, alertes automatiques
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
