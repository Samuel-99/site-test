/** CATALOGUE DES IMAGES
 * Remplacer le fichier importé suffit pour actualiser tous ses usages.
 * La largeur et la hauteur réelles sont détectées par Astro (ne pas les recopier).
 */
import portrait from '../assets/images/commun/portrait.webp';
import type { ImageMetadata } from 'astro';

export type ImageDuSite = {
  fichier: ImageMetadata;
  alt: string;
  cadrage: 'centre' | 'haut' | 'bas';
  conseil: string;
  utilisations: string[];
};

export const images = {
  portrait: {
    fichier: portrait,
    alt: 'Portrait de Samuel Oliveira Condesso, souriant, avec des lunettes et un t-shirt noir',
    cadrage: 'centre',
    conseil:
      'Format actuel : 728 × 688 px. Conseillé : 1456 × 1376 px, même proportion. Le cadre de l’accueil recadre légèrement la photo.',
    utilisations: ['Accueil : présentation principale', 'Parcours : portrait biographique'],
  },
} satisfies Record<string, ImageDuSite>;
