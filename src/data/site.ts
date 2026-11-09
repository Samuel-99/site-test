/** Contenu éditorial : les faits biographiques proviennent du CV fourni.
 * Les sélections et le programme restent vides tant qu'ils ne sont pas validés.
 * Ne pas déduire une fonction actuelle des mentions « depuis » du CV.
 */
export const person = {
  name: 'Samuel Oliveira Condesso',
  shortName: 'Samuel Oliveira',
  location: 'Vuadens · Fribourg',
  email: 'samuelcondesso@live.fr',
  introduction: 'Mon parcours relie l’électronique, la transmission et la vie associative. J’aime comprendre comment les choses fonctionnent, créer et faire avancer des projets à plusieurs.',
};

export const navigation = [
  { label: 'Accueil', href: '/' },
  { label: 'Mon parcours', href: '/parcours/' },
  { label: 'Programme', href: '/programme/' },
  { label: 'Lectures', href: '/lectures/' },
  { label: 'Musiques', href: '/musiques/' },
  { label: 'Études & articles', href: '/regards/' },
];

export const timeline = [
  { date: '2015 — 2019', title: 'Un parcours bilingue', place: 'Gymnase de Bulle', text: 'Une formation en français et en allemand, après le cycle d’orientation à La Tour-de-Trême.' },
  { date: '2016', title: 'La musique, un engagement collectif', place: 'Fanfare de Vuadens', text: 'Un engagement au comité de la fanfare, en parallèle de la pratique du baryton.' },
  { date: '2017 — 2019', title: 'Le goût de transmettre', place: 'Cours d’appui', text: 'L’accompagnement d’une quinzaine d’élèves du cycle d’orientation et du gymnase.' },
  { date: '2019 — 2021', title: 'Explorer la technique', place: 'EPFL · HEIA-FR · Wago Contact SA', text: 'Un semestre en informatique à l’EPFL, puis une année passerelle à la HEIA-FR, avec une expérience pratique chez Wago Contact SA.' },
  { date: '2021', title: 'L’électronique comme fil conducteur', place: 'HEIA-FR', text: 'Le début d’un parcours de bachelor en électronique, dans une classe bilingue français–allemand.' },
  { date: '2022 — 2023', title: 'Une année à Munich', place: 'Hochschule München', text: 'Une année d’échange en Allemagne pendant la deuxième année de bachelor.' },
  { date: '2023', title: 'L’Automate solidaire', place: 'Vie associative', text: 'La cofondation de l’association, sa présidence au démarrage et une contribution au développement électronique.' },
];

export type Book = { title: string; author: string; category: string; note: string; url?: string };
export type Track = { title: string; artist: string; note: string; url: string };
export type Article = { title: string; source: string; category: string; note: string; url: string };
export type Proposal = { title: string; theme: string; summary: string; content: string };

// Ajouter ici uniquement les contenus choisis par Samuel.
export const books: Book[] = [];
export const tracks: Track[] = [];
export const articles: Article[] = [];
export const proposals: Proposal[] = [];
