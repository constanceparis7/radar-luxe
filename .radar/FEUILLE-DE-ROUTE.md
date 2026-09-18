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

## L'avis d'hébergement : GitHub Pages ou Cloudflare ?

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

### O1 · Fondations sans point faible (registre de l'audit croisé) · 53 %
- [100] Verrou de build bloquant sur les 7 876 pages, 13 langues
- [100] Compteurs réconciliés et expliqués
- [100] Redirections des anciennes adresses (lieux et fiches)
- [100] Français résiduel traduit dans les 12 langues
- [100] Métadonnées saisonnières purgées, titres « None » réparés
- [80]  Échappement et injection (recherche, favoris, JS)
- [30]  Cannibalisation entre langues (hreflang sitemap posé, matrice à faire)
- [30]  États vides (aucun favori, aucun résultat, hors connexion)
- [20]  Aperçus sociaux par page (og/twitter, rendu messageries)
- [0]   JSON-LD Event recalibré (url vers la fiche, offres réelles, statuts)
- [0]   Fraîcheur : dernière vérification distinguée du build quotidien
- [0]   Statuts des récurrents et saisons (EventCancelled, estimations)
- [0]   Règle 403/429 des liens externes vérifiée
- [0]   Cohérence éditoriale (graphies, formats de prix et de dates)
- [0]   Accessibilité (H1, landmarks, clavier, noms accessibles, contraste)
- [0]   Arabe de droite à gauche et langues CJK contrôlés à l'écran
- [0]   En-têtes de sécurité (dépend de Cloudflare devant)
- [0]   Newsletter : double opt-in, anti-spam, désinscription (samedi 20/09)

### O2 · Infrastructure de niveau mondial · 25 %
- [100] HTTPS forcé, http et www redirigés
- [100] Réseau de diffusion mondial (Fastly via GitHub Pages)
- [50]  Surveillance de disponibilité (sonde du matin ; sonde externe 24/7 à poser)
- [0]   Cloudflare devant le site (compte, DNS, proxy) : geste de Constance
- [0]   En-têtes HSTS, CSP, nosniff, Referrer-Policy, frame-ancestors
- [0]   Vraies redirections 301 (178 aujourd'hui en pages de renvoi)
- [0]   HTTP/3 et Brotli
- [0]   Cache immuable des ressources statiques (photo, JSON, index de recherche)
- [0]   Bascule d'hébergement sur Cloudflare Pages (avant le palier 3)
- [0]   R2 pour les médias (quand les photos arrivent)
- [0]   Workers, KV, D1 pour le rendu à la volée et l'API (palier 4)

### O3 · Performance et mobile · 20 %
- [100] Polices système (Didot, Avenir), aucune police téléchargée
- [50]  Photo d'accueil optimisée (296 Ko) ; WebP/AVIF et srcset à faire
- [0]   Accueil de 2,5 Mo ramené sous 300 Ko de HTML (données en JSON séparé
        et mis en cache, JSON-LD de l'accueil en liste plutôt qu'en 340 objets)
- [0]   Budget de poids par page inscrit au verrou
- [0]   LCP < 2,5 s, INP < 200 ms, CLS < 0,1 mesurés sur téléphone moyen, réseau lent
- [0]   Écrans de 320, 360 et 390 px, paysage, zoom 200 %, clavier ouvert
- [0]   Sitemap scindé par langue avec index (11 Mo aujourd'hui en un fichier)

### O4 · Données et contenu à l'échelle · 35 %
- [100] Passes de nuit (purge, liens, condensation)
- [100] Résorption hebdomadaire de tous les doutes, aux sources
- [100] Sentinelle des imminents (lundi)
- [100] Mémoire du radar (archives, changements)
- [34]  341 événements sur un palier de 1 000
- [0]   Photos par événement (R2)
- [0]   Rendu à la volée au-delà de 850 événements (limite des 20 000 fichiers)
- [0]   API publique JSON (partenaires, assistants d'IA, applications)

### O5 · Visibilité organique mondiale · 55 %
- [100] Titres en forme de requêtes, 13 langues, mois courant automatique
- [100] hreflang sur les pages et dans le sitemap
- [100] 88 pages Questions FR et EN, balisage FAQ
- [100] Search Console lue en entier et exploitée
- [50]  Résorption du cache Google (titres None, saison) : en cours
- [40]  JSON-LD Event propre (voir O1)
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

### O7 · Confiance, sécurité, conformité · 45 %
- [100] HTTPS, zéro cookie, zéro donnée collectée
- [100] Aucun fichier de travail en ligne, aucun secret dans le code
- [100] Sonde quotidienne du site en ligne
- [80]  Échappement et protection des liens externes
- [50]  Mentions légales (page existante, à compléter le 21/09)
- [0]   Politique de confidentialité
- [0]   Double opt-in, SPF, DKIM, DMARC pour la newsletter
- [0]   En-têtes de sécurité (Cloudflare)

### O8 · Observabilité et pilotage · 55 %
- [100] Compteur public GoatCounter
- [100] Search Console vérifiée, exports lus
- [100] Sonde du matin (quotidienne) et contrôle Google contre site (hebdomadaire)
- [100] Bilan observatoire du 2 octobre programmé
- [50]  Sonde de disponibilité 24 h (en cours) puis permanente
- [30]  Tableau de bord unique (tableau-de-bord.html à enrichir)
- [0]   Statistiques Cloudflare sans cookie
- [0]   Alertes automatiques en cas d'erreur (5xx, verrou en échec la nuit)

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

## L'ordre des prochaines semaines
1. Registre de l'audit jusqu'au bout (O1), en commençant par l'accueil de 2,5 Mo (O3).
2. Cloudflare devant le site (O2), dès que Constance a créé le compte.
3. Newsletter du 21/09 avec ses contrôles (O6, O7).
4. Bilan du 2/10 : mesure, puis décision de positionnement.
5. Bascule Cloudflare Pages quand le palier 2 est solide.
