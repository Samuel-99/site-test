# Modifier mon site

Ce guide est le point de départ pour travailler dans VS Code. Le site garde son apparence et ses adresses ; les fichiers sont regroupés par rôle.

## 1. Quel fichier ouvrir ?

| Page | Adresse publique | Texte et structure | Style de la page |
| --- | --- | --- | --- |
| Accueil | `/` | `src/pages/index.astro` | `src/styles/pages/accueil.css` |
| Mon parcours | `/parcours/` | `src/pages/parcours.astro` | `src/styles/pages/parcours.css` |
| Programme | `/programme/` | `src/pages/programme.astro` | `src/styles/pages/programme.css` |
| Lectures | `/lectures/` | `src/pages/lectures.astro` | `src/styles/pages/lectures.css` |
| Musiques | `/musiques/` | `src/pages/musiques.astro` | `src/styles/pages/musiques.css` |
| Études et articles | `/regards/` | `src/pages/regards.astro` | `src/styles/pages/regards.css` |
| Contact | `/contact/` | `src/pages/contact.astro` | `src/styles/pages/contact.css` |
| Informations | `/informations/` | `src/pages/informations.astro` | `src/styles/pages/informations.css` |
| Erreur 404 | `/404.html` | `src/pages/404.astro` | `src/styles/pages/404.css` |

Les deux dossiers `pages` ont des rôles distincts : `src/pages` contient les pages Astro et `src/styles/pages` leur CSS. Il n’y a pas de dossier `ecrans`.

Chaque page commence par ses imports et ses éventuelles listes entre les deux lignes `---`. Ensuite vient le contenu affiché, avec un commentaire qui identifie la page et des commentaires pour ses sections. Les textes ordinaires restent directement dans cette page. Une balise `<h1>` est le grand titre, `<h2>` un titre de section, `<p>` un paragraphe et `<a href="...">` un lien.

Astro utilise le nom du fichier pour déterminer l’adresse : `index.astro` désigne l’accueil. Renommer un autre fichier de page change son adresse ; modifier son contenu ne la change pas.

## 2. Remplacer mon portrait

Le fichier actuel est :

```text
src/assets/images/commun/portrait.webp
```

1. Remplacer ce fichier par la nouvelle photo, avec **le même nom et le même format**.
2. Enregistrer : l’aperçu de développement actualise l’accueil et le parcours.
3. Vérifier le visage sur ordinateur et téléphone. Modifier au besoin le texte alternatif et le cadrage dans `src/configuration/images.ts`.

Les dimensions réelles sont détectées automatiquement par Astro. Il n’y a pas de nombres à mettre à jour dans les deux pages.

Pour connaître les dimensions d’un fichier avant de le remplacer, ouvrir l’image dans VS Code : son aperçu indique sa largeur et sa hauteur en pixels.

Le portrait actuel fait **728 × 688 pixels**. Pour conserver ses proportions, une photo de **1456 × 1376 pixels** convient également. Ce sont des dimensions recommandées, pas une obligation : le cadre de l’accueil recadre légèrement la photo.

Si la nouvelle photo est un JPEG ou un PNG, utiliser sa véritable extension et adapter l’import en haut de `src/configuration/images.ts`. Renommer un JPEG en `.webp` ne le convertit pas.

Le dossier `commun` contient les photos utilisées sur plusieurs pages. Les autres dossiers (`accueil`, `parcours`, `lectures`, `musiques`) accueillent les photos propres à ces rubriques. Les fichiers `.gitkeep` servent seulement à conserver les dossiers encore vides dans Git.

## 3. Comprendre le catalogue d’images

Dans `src/configuration/images.ts`, chaque image possède :

| Champ | Rôle |
| --- | --- |
| `fichier` | Image importée ; Astro en lit la largeur et la hauteur réelles. |
| `alt` | Description accessible de l’image, sans répéter « image de ». |
| `cadrage` | `centre`, `haut` ou `bas` : zone privilégiée si le cadre recadre l’image. |
| `conseil` | Dimensions recommandées et remarques pour la préparation du fichier. |
| `utilisations` | Liste des endroits où l’image est utilisée, à tenir à jour si on l’ajoute ailleurs. |

`conseil` et `utilisations` sont des indications pour toi : ils ne s’affichent pas sur le site et ne redimensionnent pas le fichier. Les dimensions et le cadrage appliqués au navigateur proviennent de `fichier` et `cadrage`.

**Dimensions du fichier ≠ dimensions à l’écran.** L’image peut faire 1456 pixels de large et être affichée sur 350 pixels. La largeur du cadre, son ratio et ses règles mobiles sont dans le CSS de la page (`.portrait-photo` pour l’accueil et `.bio-portrait` pour le parcours). Le catalogue choisit le point de cadrage ; le CSS choisit la place occupée par le cadre.

## 4. Ajouter une nouvelle image

Exemple : préparer `src/assets/images/lectures/mon-livre.webp`, puis dans `src/configuration/images.ts` :

```ts
// Ajouter cet import avec les autres, en haut du fichier.
import couverture from '../assets/images/lectures/mon-livre.webp';

// Ajouter cette entrée DANS l’objet « images », après « portrait ».
monLivre: {
  fichier: couverture,
  alt: 'Couverture du livre …',
  cadrage: 'centre',
  conseil: 'Image verticale, conserver les proportions de la couverture.',
  utilisations: ['Lectures'],
},
```

Dans la page où l’afficher, ajouter ces imports entre les `---` :

```astro
import ImageSite from '../composants/ImageSite.astro';
import { images } from '../configuration/images';
```

Puis placer ceci dans le contenu de la page, à l’endroit souhaité :

```astro
<ImageSite image={images.monLivre} />
```

Pour une photo principale visible dès l’ouverture, on peut ajouter `prioritaire`. La gestion commune des balises d’image est dans `src/composants/ImageSite.astro`.

Certaines illustrations actuelles (livres dessinés, disque, boussole, formes abstraites) sont réalisées en CSS, pas avec des fichiers photo. Leur dessin est dans le CSS de la page concernée. Les petites icônes sont dans `src/composants/Icone.astro`. Le favicon, affiché dans l’onglet du navigateur, reste dans `public/favicon.svg`.

## 5. Modifier les textes ou ajouter un livre

Ouvrir le fichier de la page indiquée dans le tableau. Chercher un passage avec `Ctrl+F`, puis modifier son texte en conservant les balises autour.

Les contenus répétés sont des listes au début de leur page : `books` dans Lectures, `tracks` dans Musiques, `articles` dans Études et articles, `proposals` dans Programme et `timeline` dans Parcours. L’accueil contient son introduction et les cartes des rubriques.

Exemple pour ajouter un livre dans `src/pages/lectures.astro` :

```ts
const books: Book[] = [
  {
    title: 'Titre du livre',
    author: 'Nom de l’auteur',
    category: 'Essai',
    note: 'Mon commentaire personnel sur cette lecture.',
    // url: 'https://…', // Facultatif : lien vers une référence vérifiée.
  },
];
```

Une liste vide (`[]`) affiche la présentation « à venir ». Une liste remplie affiche ses entrées. [Le guide éditorial](docs/CONTENU.md) détaille les champs des autres rubriques.

## 6. Modifier les couleurs, les boutons ou le menu

| Besoin | Fichier à modifier |
| --- | --- |
| Palette principale et choix des polices | `src/styles/theme.css` |
| Règles générales des titres, paragraphes et navigateur | `src/styles/base.css` |
| Boutons, menu, pied de page et présentations partagées | `src/styles/commun.css` |
| Mise en page d’une seule rubrique | Son fichier dans `src/styles/pages/` |
| Nom, courriel, localisation et liens du menu | `src/configuration/site.ts` |
| Structure du menu et comportement mobile | `src/composants/Entete.astro` |
| Contenu commun du pied de page | `src/composants/PiedDePage.astro` |
| Cadre HTML et métadonnées communes | `src/modeles/Page.astro` |

Tous les styles sont dans `src/styles/`. Chaque fichier comporte ses adaptations aux écrans sous le commentaire « AFFICHAGE MOBILE ET AUTRES ADAPTATIONS ». Les classes communes sont définies dans `commun.css`, les classes propres à l’accueil dans `accueil.css`, etc. Les couches CSS `reset`, `base`, `components`, `responsive` assurent l’ordre de priorité ; conserver leur déclaration dans `theme.css`.

## 7. Voir le résultat avant publication

Dans le terminal VS Code, à la racine du projet :

```sh
npm ci
npm run dev
```

Ouvrir l’adresse affichée par Astro (port 4321 par défaut). Enregistrer un fichier actualise l’aperçu ; `Ctrl+C` arrête le serveur. Sous Windows, utiliser WSL pour les scripts actuels ; ils sont également compatibles Linux/macOS.

Avant d’envoyer les changements :

```sh
npm run format
npm run check
npm run build
```

`format` réindente les fichiers pour les garder lisibles, sans publier. `check` vérifie les sources et `build` prépare `dist/`. Ne jamais modifier `dist/` à la main : son contenu est recréé à la construction.

Travailler sur une branche, envoyer les changements sur GitHub et les relire dans une pull request. **La fusion dans `main` déclenche la publication GitHub Pages.** L’aperçu local, un commit ou un envoi sur une autre branche ne publient pas le site.
