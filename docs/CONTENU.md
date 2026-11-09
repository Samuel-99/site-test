# Compléter le site

La source principale est `src/data/site.ts`. Il suffit de renseigner les tableaux correspondants puis de reconstruire le site. Les pages affichent automatiquement les contenus ajoutés.

## Livres

Chaque entrée de `books` possède `title`, `author`, `category`, `note` et, éventuellement, `url`. Rédiger une note personnelle et utiliser une URL HTTPS vérifiée si l’on souhaite un lien vers la source. Ne pas reproduire de passages protégés sans autorisation.

## Musiques

Chaque entrée de `tracks` possède `title`, `artist`, `note` et `url`. Le lien ouvre une plateforme externe ; aucun lecteur ni suivi tiers n’est chargé par la page.

## Études et articles

Chaque entrée de `articles` possède `title`, `source`, `category`, `note` et `url`. Privilégier la source originale ; distinguer son résultat du commentaire personnel et préciser ses limites dans la note.

## Programme

Chaque entrée de `proposals` possède `title`, `theme`, `summary` et `content`. Les propositions sont présentées sous forme de sections dépliables accessibles. `content` accepte des retours à la ligne, pas de HTML. Introduire objectifs, moyens, contexte et sources dans un langage clair. Les textes doivent être validés par Samuel avant publication ; aucune affiliation ou candidature ne doit être supposée.

## Éléments à confirmer avant publication

- La situation professionnelle et la formation actuelles : le CV fourni ne les établit pas à la date du site.
- Les convictions, le territoire politique, une éventuelle affiliation et les propositions.
- Les livres, artistes et ressources réellement sélectionnés.
- L’adresse de contact publique (`person.email`), les éventuels réseaux sociaux et la version du portrait.
- Le domaine de production et les mentions d’hébergement applicables.

L’historique ChatGPT complet n’est pas accessible depuis le projet. Les textes actuels utilisent uniquement cette conversation et le CV fourni. Ne pas présenter comme connus des éléments provenant d’échanges indisponibles.

## Vérifier

```sh
npm run check
npm run build
```

Puis vérifier les pages dans le navigateur, sur ordinateur et téléphone. Les liens des ressources doivent être testés avant leur publication. Ne pas copier le CV original dans `public/` : il contient des informations privées.
