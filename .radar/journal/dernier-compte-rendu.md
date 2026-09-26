# Compte rendu — passe du 26/09/2026

## Lu avant tout travail
`.radar/DOCTRINE.md` (intégral), `.radar/PASSATION.md`, `.radar/tools/lessons.md`
(intégral, 1246 lignes), puis `.radar/FEUILLE-DE-ROUTE.md`, `.radar/REGLE-ALPHA.md`,
`.radar/AUDIT-SANS-POINT-FAIBLE.md` (la RÈGLE ALPHA du 18/09 prime sur toute demande de
contenu et fait de ces trois derniers documents la référence de priorité active).

## Démarrage
Signature `radar-routine-claude` posée, trace `DEMARRAGE` poussée sur `main` avant tout
travail (push direct accepté, pas de repli de branche nécessaire). Dépôt shallow détecté
(`git rev-parse --is-shallow-repository` → true) : `git fetch --unshallow origin` fait
(2 branches `claude/*` non fusionnées découvertes en passant, non touchées — hors mandat
de cette passe). `index-full.html` reconstruit (absent, non versionné comme prévu).

## Priorité du prompt — condensation des voies d'invitation
Vérifiée à nouveau avec la même méthode que les 20/21/25/09 (lecture intégrale des champs
`iv.o`/`iv.g`/`iv.w` >1200 car. WARN + détecteur de motifs de dérive sur l'échantillon
>400 car. de la fenêtre live) : **0 dérive « journal d'enquête » trouvée**, troisième jour
consécutif. Les 11 champs encore au-dessus du seuil WARN et les ~104 encore au-dessus du
seuil-cible de 400 car. sont de la densité factuelle légitime (tarifs, horaires, plusieurs
contacts réels par fiche) — vérifié en lisant chacun des 11 en intégralité. Conformément à
la doctrine (« si tu n'as rien trouvé de digne, ne publie rien » transposé à la
condensation) : rien condensé aujourd'hui, pour ne pas réintroduire le risque connu
(URL abrégées, adresses déformées) sur du contenu déjà propre. Détail dans lessons.md.

## LOI DU SITE (iv + séjour + 13 langues)
`reste.py` : traductions 319/319 (100 %), voies d'invitation 319/319 (100 %), séjours
313/319 (reste 6, tous hors fenêtre live ou marginaux — non retraités aujourd'hui faute
de mandat prioritaire, la Règle Alpha plaçant l'audit technique au-dessus).

## Travail effectué — registre « aucun point faible » (Règle Alpha, priorité active)
1. **Scan global P0.3** (5 890 fichiers générés) : 0 occurrence de `None`/`null`/
   `undefined`/`NaN`/`[object Object]` hors balises `<script>`. Les occurrences de
   « été 2026 »/« cet été »/« summer 2026 » (333+65+67) sont toutes du contenu factuel
   légitime (le sujet réel d'un événement ou d'une programmation datée), y compris dans
   les 14 `<title>`/`<meta description>` qui en portent — aucune méta périmée. Item classé
   FAIT dans `AUDIT-SANS-POINT-FAIBLE.md`.
2. **Saut de niveau de titre h2→h4 corrigé** (item 23 du registre, ouvert depuis le 25/09) :
   deux occurrences trouvées (`renderPrestige()` sous « Classement Prestige », et
   `renderArchives()` sous « Archives »), toutes deux hors de la structure h2>h3>h4
   correcte de l'Agenda. Passées en h3 ; vérifié avant modification que le style visuel
   dépend uniquement de la classe CSS `.t`, jamais du nom de balise — aucun changement
   visuel. Diff de 2 lignes exactement dans `index.html`, `validate.py` et `perfcheck.py`
   relancés après coup, 0 régression.
3. **PageSpeed Insights** retesté pour LCP/INP/CLS (item 21) : quota toujours épuisé
   (429 `RESOURCE_EXHAUSTED`), rien de nouveau, à réessayer plus tard dans la semaine.
4. Reste ouvert, non traité aujourd'hui faute de temps : noms des symboles ◐ et →
   (priorité plus faible, le bouton thème a déjà un aria-label qui couvre ◐), vrai
   passage au lecteur d'écran, zoom 200 % avec un vrai zoom, matrice cannibalisation
   inter-langues, newsletter (bloquée sur le compte Brevo de Constance).

## Routine quotidienne
- `memoire.py changements` : 0 changement de date sur 7 jours.
- Bandeau « Ouvertures & délais » : 3 entrées, aucune expirée (2026-09-30, 2026-10-15,
  2027-01-31) — rien à retirer, rien de nouveau trouvé à ajouter aujourd'hui.
- Eyebrow mis à jour : « données collectées et vérifiées le 26 septembre 2026 »
  (remplacement vérifié unique avant application, piège du 18/09 évité).
- 2 AVERT W1 pré-existants et inchangés (Covo di Nord-Est, Nikki Beach Ibiza — dates
  écrites hors fenêtre saisonnière), non blocants, non traités aujourd'hui.

## Pipeline et publication
`split_i18n.py --apply` → `gen_seo.py 2026-09-26` → `gen_pages.py` → `validate.py`
(0 bloqueur, 2 avertissements inchangés) → `perfcheck.py` (0 régression) →
`.radar/session/publier.sh`. Diff final limité aux fichiers attendus (index.html,
sitemap, ld+json, pages e/* touchées par gen_seo/gen_pages, journaux).

## Non vérifié / laissé en l'état
- Les 6 séjours manquants (LOI DU SITE) n'ont pas été recomposés : à recroiser avec la
  fenêtre live à la prochaine passe avant de lancer une recherche.
- Aucun contrôle visuel au vrai navigateur (Playwright non installé dans cette session
  cloud) pour la correction h2→h3 : la garantie vient de l'analyse statique du CSS
  (styles par classe, jamais par balise), pas d'une capture d'écran.
- Feuille de route : le sous-item accessibilité d'O1 remonté de 93 à 95 ; le taux global
  d'O1 (82 %) n'a pas été recalculé — la méthode de pondération exacte de la moyenne
  n'est pas assez sûre pour être recalculée sans risquer un chiffre faux plutôt qu'un
  chiffre simplement pas encore rafraîchi.
