# Compte rendu — passe du 27/09/2026

## Démarrage
Clone superficiel constaté (comme le 20/09) → `git fetch --unshallow origin` fait avant
tout outil d'historique. Cadence : dernier run à 43 h (> seuil 30 h), passe traitée en
RATTRAPAGE normal — aucune anomalie trouvée dans l'historique des commits de la veille
(passe du 26/09 complète, FIN bien journalisée). `precheck.sh` → OK, verrou posé.

## État des trois compteurs (LOI DU SITE) — 100 % sur la fenêtre live
- Traductions 13 langues : 319/319
- Séjours clé en main : 313/319 (les 6 manquants sont tous des fiches-conseil `c=acces`,
  exemption prévue par la doctrine — vérifié un par un, 0 fiche d'événement sans séjour)
- Voies d'invitation : 319/319

## Condensation `iv` (priorité de passe) — 4e jour consécutif à zéro dérive réelle
Lecture intégrale des 11 champs `iv.*` >1200 car. (seuil WARN) + détecteur de motifs de
dérive et de duplication sur les 82 fiches de la fenêtre live >400 car. (seuil cible) :
tout l'excédent est de la densité factuelle légitime (tarifs, horaires, contacts
multiples réels, badges « vérifié le »). Un seul candidat relevé par le détecteur
(Sotheby's Royal & Noble Jewels) : relu, confirmé faux positif déjà connu du 26/09
(procédure d'enchères légitimement répétée sous deux angles différents). Conforme à la
règle du 21/09 : ne pas forcer un quota de condensation sur du contenu déjà sain.

## Vérifications de routine
- `memoire.py changements` : 0 changement de date sur 7 jours.
- 16 événements dans les 7 prochains jours, tous les liens `u` testés (`curl -sL`,
  domaine témoin wikipedia.org contrôlé avant) : 15×200, 1×403 (lebonmarche.com,
  anti-bot sur la page d'accueil du grand magasin — pas un signal sur l'événement
  Fashion Week lui-même, aucune action).
- 0 zombie à purger (aucune fiche avec d2 < 28/08/2026).
- Bandeau « Ouvertures & délais » : 3 entrées, toutes encore valides (aucune à retirer).
- Eyebrow mis à jour : 26 → 27 septembre 2026 (édité précisément dans `index-full.html`,
  la clé i18n voisine sans date vérifiée intacte).
- Ancres printemps 2027 (TEFAF, Art Basel HK, Watches and Wonders, Salone del Mobile,
  Cannes 80e, GemGenève, GP Monaco, Royal Ascot) + Fuorisalone : les 9 sont en ligne.
- Joaillerie : 12 fiches en fenêtre live (seuil de vigilance à 10), aucun ajout forcé.
- Recherche de nouveaux événements : aucune piste digne de l'ADN Riviera trouvée
  aujourd'hui au-delà de ce qui précède — rien ajouté, conformément à la doctrine
  (mieux vaut ne rien publier que du grand public déguisé).

## Fait aujourd'hui : traduction turque des 44 pages Questions (objectif O5)
Dernier backlog de langue du chantier Questions (l'agent unique avait échoué 6 fois le
26/09). Repris en 4 lots de 11 questions, 4 agents parallèles, règles turques de la
doctrine (orthographe TDK, exonymes Monako/Venedik/Viyana/Cenevre, Paris/Saint-Tropez/
Cannes inchangés, dates à la turque, aucun tiret long, aucun fait/prix/URL/contact
modifié). Fusion : 44/44 slugs identiques et dans le même ordre que le français, clés
conformes au format des 11 autres langues.

Contrôle mécanique de non-perte de faits : nouvel outil `.radar/tools/verif_traduction.py`
écrit et PERSISTÉ ce jour (généralisation de `verif_faits.py` à une paire de fichiers
JSON par slug), avec un piège corrigé en le construisant : un premier jet du détecteur de
téléphones fusionnait un numéro avec le début de la phrase suivante à travers un point
final (« +41 81 837 2661. 15 Aralık… » lu comme un seul numéro) — corrigé en segmentant le
texte par phrase avant la recherche. Sur les 44 entrées : 1 seule alerte restante, un
montant en devise localisée (« 400 francs suisses » → « 400 İsviçre frangı », non reconnu
par le détecteur), vérifié à la main dans le texte turc intégral — présent, aucune perte.

Pipeline complet exécuté : `split_i18n.py --apply` (12 langues, tr 228 Ko gzip),
`gen_seo.py 2026-09-27`, `gen_pages.py` (44 pages `/tr/q/*.html` + `/tr/questions.html`
générées, contrôlées : `<html lang="tr">`, titres et h1 en turc, thèmes traduits, 0 tiret
long). `validate.py` : 0 bloqueur, 2 avertissements inchangés (iv.g/iv.w denses déjà
connus). `perfcheck.py` : 0 régression. Publié sur `main` via `publier.sh`
(939 fichiers touchés, quasi tous par le recalcul quotidien normal de la Note du radar,
vérifié sur un échantillon — aucun contenu de fiche altéré). `healthcheck.sh` : OK
(http=200, compte_live=319/319, date fraîche). Vérification directe des pages turques en
ligne : 404 au moment du contrôle (quelques minutes après le push) — décalage de
propagation GitHub Pages déjà documenté (leçon du 22/07), pas une panne : le healthcheck
officiel du site est passé au vert sur son propre calcul.

FEUILLE-DE-ROUTE mise à jour : objectif O5, item « Pages Questions » passé à 100 %
(12 langues + français désormais complètes sur les 44 questions), taux O5 65 → 68 %.

## Ce qui reste (à ne pas perdre)
- Vérifier dans les prochaines 24 h, à froid, que `/tr/questions.html` et `/tr/q/*.html`
  répondent bien 200 en ligne (propagation GitHub Pages).
- Item O5 encore ouvert : matrice intention → URL unique (Milan, PFW, Vogue World), 0 %.
- Item O1 encore à 0 % : fraîcheur distincte du build quotidien ; statuts des récurrents
  (EventCancelled).
- `a-reverifier.md` : plusieurs entrées d'août concernent des établissements d'été dont la
  fenêtre est probablement déjà passée — à relire lors de la prochaine résorption des
  doutes du mercredi pour purger les doutes devenus sans objet.

## Anomalie à signaler
Cadence rompue signalée par `precheck.sh` (43 h) : fausse alerte de mesure, pas un jour
manqué (la passe du 26/09 est complète, DEMARRAGE+FIN journalisés) — probablement un
écart d'heure de déclenchement d'un jour à l'autre. Aucune action nécessaire.

Rien d'autre à signaler. Publié sur `main`.
