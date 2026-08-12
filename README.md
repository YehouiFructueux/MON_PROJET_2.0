
🏢 Gestion des réservations de salles

📌 Description

Ce projet est une application Python permettant de gérer les réservations de différentes salles.

L'application permet notamment de :

- 📅 Ajouter une réservation
- 👀 Consulter le planning d'une salle
- 🔍 Afficher les créneaux disponibles
- ❌ Annuler une réservation
- ✅ Vérifier qu'une salle existe
- ⏰ Vérifier les horaires et les conflits entre réservations
- 🗂️ Gérer les informations des réservations

🛠️ Technologies utilisées

- Python 3
- Module "datetime"
- Structures de données Python : listes et dictionnaires
- Fonctions
- Conditions et boucles

📂 Structure du projet

gestion-reservations/
│
├── main.py
├── README.md
└── ...

🚀 Installation

1. Cloner le dépôt

git clone https://github.com/YehouiFructueux/gestion-reservations.git

2. Accéder au projet

cd gestion-reservations

3. Lancer le programme

python main.py

⚙️ Fonctionnalités

Ajouter une réservation

L'utilisateur renseigne :

- La salle
- La date
- L'heure de début
- L'heure de fin
- Le responsable
- L'objet de la réservation

Le programme vérifie ensuite que la réservation est valide et qu'il n'existe pas déjà une réservation sur le même créneau.

Consulter le planning

L'utilisateur peut sélectionner une salle et une date afin d'afficher les réservations prévues.

Afficher les créneaux libres

Le programme analyse les réservations existantes et affiche les horaires encore disponibles dans la journée.

Annuler une réservation

L'utilisateur peut rechercher une réservation à partir de ses informations et la supprimer.

🕘 Horaires

Les réservations sont prévues dans la plage horaire suivante :

09h00 → 17h00

Les horaires sont convertis en minutes dans le programme afin de faciliter les comparaisons entre les différents créneaux.

📋 Exemple de réservation

{
    "salle": "Salle A",
    "date": "2026-08-10",
    "debut": 540,
    "fin": 600,
    "responsable": "Awa",
    "objet": "Reunion equipe"
}

Ici :

- "540" correspond à 09h00
- "600" correspond à 10h00

La réservation concerne donc la Salle A, de 09h00 à 10h00.

🎯 Objectif du projet

Ce projet a pour objectif de mettre en pratique les bases de la programmation Python, notamment :

- Les variables
- Les conditions
- Les boucles
- Les listes
- Les dictionnaires
- Les fonctions
- La gestion des dates et heures
- La validation des entrées utilisateur

👨‍💻 Auteur

YEHOUI Fructueux

Projet réalisé dans le cadre d'un apprentissage de la programmation Python.

📄 Licence

Ce projet est destiné à un usage pédagogique.
