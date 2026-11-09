# Samuel Oliveira Condesso — site personnel

Site éditorial en français, construit avec **Astro** et exporté en HTML statique. Il peut être hébergé sur un hébergement Web Infomaniak sans serveur Node.js en production.

## Développer

Prérequis : Node.js **22.23.4 ou supérieur** (version testée : 24.22.1) et npm. Les commandes ci-dessous sont prévues pour Linux/macOS ou WSL.

```sh
cd /workspace/site-test
npm ci --cache /tmp/site-test-npm-cache
npm run dev
```

Le serveur de développement utilise le port **4321**. Pour travailler dans une autre copie du dépôt, adapter uniquement le répertoire. Utiliser le checkout existant ; chaque tâche Cloud est déjà isolée, aucun worktree supplémentaire n’est nécessaire.

```sh
npm run check
npm run build
npm run preview
```

`build` produit le répertoire `dist/`. `preview` permet de vérifier cet export ; aucun processus Node.js n’est nécessaire une fois les fichiers hébergés. Les commandes Astro désactivent sa télémétrie pour ne pas écrire de configuration hors du projet dans la machine Cloud.

## Pages et contenu

- `/` : présentation générale et portes d’entrée vers les rubriques.
- `/parcours/` : biographie, repères et engagements associatifs.
- `/programme/` : espace politique, explicitement en préparation.
- `/lectures/` : bibliothèque personnelle à compléter.
- `/musiques/` : pratique musicale et futur carnet d’écoute.
- `/regards/` : études et articles à compléter.
- `/contact/` : contact par courriel et copie de l’adresse.
- `/informations/` : informations et confidentialité.
- `/404.html` : page d’erreur.

Les faits biographiques, l’adresse de contact et les sélections sont centralisés dans **`src/data/site.ts`**. Les introductions et textes de présentation se trouvent dans `src/pages/`. Les styles et composants sont partagés ; le contenu est rendu au build, sans framework JavaScript côté visiteur.

Voir [le guide éditorial](docs/CONTENU.md) pour ajouter une référence ou une proposition. Les tableaux vides affichent une présentation « à venir », jamais de faux favoris ni de programme inventé.

Le CV fourni est une source non datée : ses indications « depuis » ne prouvent pas une fonction actuelle ou un diplôme obtenu. Le PDF original, l’adresse privée, la date de naissance et le téléphone **ne sont pas inclus** dans les fichiers publics. Seul le portrait a été extrait. L’adresse de courriel du CV est utilisée pour le contact ; la vérifier avant toute mise en ligne.

## Mise en ligne Infomaniak (manuelle)

1. Valider les contenus, le portrait, le courriel public et les textes d’information.
2. Exécuter `npm ci --cache /tmp/site-test-npm-cache`, `npm run check`, puis `npm run build`.
3. Sauvegarder le site existant avant de le remplacer.
4. Envoyer **le contenu** de `dist/` dans la racine Web du domaine choisie dans le Manager Infomaniak. Ne pas envoyer le dépôt, `node_modules`, le CV source ni des identifiants. Inclure le fichier caché `.htaccess`.
5. Activer/vérifier HTTPS dans le Manager, puis contrôler l’accueil, chaque URL directe, la navigation mobile et une URL inexistante. Vérifier les journaux Apache en cas d’erreur liée à une directive `.htaccess`.

Les chemins commencent par `/` : cette configuration vise un domaine ou sous-domaine dédié, pas un sous-répertoire. Le fichier `CNAME` existant, qui désigne `samuel-oliveira.ch`, est conservé à la racine et dans `public/` pour l’export. Aucun accès Infomaniak n’est configuré dans ce dépôt. Le fonctionnement local de l’export ne vérifie pas les réglages effectifs de l’hébergeur.

Le site de test précédent (`index.html`, `script.js`, `styles.css` à la racine) est remplacé par les sources Astro. Le serveur de production doit servir **l’export `dist/`**, et non la racine des sources. Si le domaine utilise GitHub Pages, il faudra configurer la construction et la publication de cet export avant de fusionner ; cette branche ne déclenche aucun déploiement.

Le site n’a ni formulaire serveur, ni mesure d’audience, ni lecteur tiers intégré. Le bouton « M’écrire » ouvre l’application de messagerie du visiteur. Les polices sont embarquées dans l’export. La copie du courriel nécessite un contexte sécurisé et propose une explication si le navigateur la refuse.

## Tests navigateur

Les scripts Python nécessitent Playwright (`python -m pip install -r tests/requirements.txt`) et Chromium. Ils utilisent `/usr/bin/chromium` par défaut ; adapter `CHROMIUM_PATH` si besoin.

Après avoir démarré `npm run preview` dans un autre terminal :

```sh
python tests/smoke.py
python tests/accessibility.py
```

`SITE_URL` permet de choisir l’adresse du serveur de test. Le test fonctionnel parcourt toutes les pages à 1440, 390 et 320 pixels, contrôle les liens internes, le menu mobile, les erreurs JavaScript et la copie du courriel. L’audit axe-core vérifie les règles WCAG A/AA disponibles sur ordinateur et mobile ; il ne remplace pas un examen manuel.

**Aucune commande de ce projet ne déploie ni ne publie le site.**
