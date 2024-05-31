<a href="https://github.com/AntoDB/AI_1_ISIB_Project/tree/main?tab=readme-ov-file#cours-he2b---isib-master-1-ia-intelligence-artificielle">[fr below/fr en dessous]</a>

# [HE2B - ISIB courses Master 1] AI (Artificial Intelligence)
## Course instructions
Choice of programming language: Python, Java, C++, etc. & Software of your choice: Matlab, Netbeans, Oracle, etc.
### Part 1: Basic, heuristic and optimal search
Implement, using the same language and software, 5 functions
o Basic: one for the BFS algorithm
o Basic: one for the Random Search algorithm
o Heuristic: one for the Greedy Search algorithm
o Heuristic: one for the Beam Search algorithm
o Optimal: one for the Estimated Extended Uniform Cost + Branch & Bound + Suppression = A* algorithm
### Part 2: Strategy game algorithms for 2 people
Using a language & software of your choice, implement a 2-person game.
Implement the selected game using the Min-Max algorithm plus alpha-beta optimisation.
### Part 3: Constraint programming
Using a language & software of your choice, implement a game or management problem from the following list, using the principles & algorithms seen in the Constraint Programming course:
Creation of a tool for creating lesson timetables (with teacher, room, time and group of students), Creation of a tool for managing teams (with equipment, machines, days of the week, group of workers, engineers), timetable and resource management. Set as many interesting constraints as possible.
You are allowed to use a ‘constraint programming’ package or dll.
Note: not Sudoku!

### Assessment criteria
• Meeting deadlines
• Precise and accurate algorithms
• Depth of work: you need to go as far as possible in your optimisation possibilities
• Understanding of the problem
• Interest in the application examples: you must apply your algos to concrete, real-life examples.
• Add a bibliography to your report if you have drawn inspiration from existing applications.

## Part 1: Selection of a (most) optimised route between 2 STIB-MIVB metro stations
The aim of this project is to develop an algorithm to find the optimal path between two stations in a metro network. The optimisation aims to minimise the total journey time, taking into account not only travel times between stations, but also connection times when line changes are necessary. To find out which algorithm provides the best optimisation, we are testing several: BFS (Beam-first Search), Random Search, Greedy Search, Beam Search, A*.
For the sake of the experiment, I have added the future line 3 as well as a fictitious line between Simonis and Porte de Namur with an abusive cost (150).
![Metro map with line 3](https://raw.githubusercontent.com/AntoDB/AI_1_ISIB_Project/main/readme_files/M3planmetro.png)
*Metro map with future line 3

You can see the latest versions of these codes with the 5 algorithms [here, in this folder](https://github.com/AntoDB/AI_1_ISIB_Project/tree/main/Projet%201%20-%20Algo.%20de%20recherche/).

## Partie 2 : Power 8 game
The game chosen is a Power 8. As in Power 4, you have to align your pieces horizontally, vertically and/or diagonally. In this version, you don't need to line up four checkers but eight to complete the game. The grid is therefore not 6x7 but 10x13 to allow the eight pieces to be aligned.

For this project, I went back to [the grid and the counters](https://github.com/AntoDB/AI_1_ISIB_Project/tree/main/Projet%202%20-%20Algo.%20jeu%20-%20Puissance%208/Puissance_8/Images/) even though I didn't take the time to implement the images of the counters.
You can admire the graphics [in this directory](https://github.com/AntoDB/AI_1_ISIB_Project/tree/main/Projet%202%20-%20Algo.%20jeu%20-%20Puissance%208/Puissance_8/Images/).

You can see the latest versions of the code with just min-max (minimax) and the one with min-max (minimax) with alpha-beta optimisation [here, in this folder](https://github.com/AntoDB/AI_1_ISIB_Project/tree/main/Projet%202%20-%20Algo.%20jeu%20-%20Puissance%208/).

## Part 3: Agenda for April 2024
To create a coherent schedule for my diary for April 2024, taking into account the priorities and constraints of the various activities. This is a common problem of planning and organisation based on non-overlap and priority constraints.

As I have a huge number of activities, it's often complicated to find solutions so that all my activities fit together.
That's why I thought I'd use AI with constraint-based programming to create a coherent diary/schedule for the month of April 2024.
I chose this month because of the high workload and the fact that I sometimes have several activities on the same day.
To do this, the algorithm has to be able to assign me as many activities as possible without having any at the same time (overlap).

The diary for April has been reduced here to keep only the essentials.

### Package(s)/Library(ies) used
The main package used for the implementation is `docplex.cp.model` from IBM's DOcplex library. DOcplex is a Python package for constraint programming and mathematical programming, part of the IBM Decision Optimization suite. It allows you to create, manipulate and solve optimisation models with the IBM ILOG CPLEX Optimization Studio solver (to be [downloaded and installed](https://www.ibm.com/products/ilog-cplex-optimization-studio) when using the Python code).

Steps to follow:
1. Download and install:
    * Go to the IBM website and download CPLEX Optimization Studio: IBM ILOG CPLEX Optimization Studio
    * Follow the instructions to install the software on your system.
    (That was enough for me, I didn't have to do the rest. I just did step 3.)

2. Add cpoptimizer.exe to the PATH:
    * Search for "Change environment variables" in the Start menu.
    * In the environment variables window, find the PATH variable in the system variables and click on "Edit".
    * Add the full path to the directory containing cpoptimizer.exe (for example, C:\Program Files\IBM\ILOG\CPLEX_Studio\cpoptimizer\bin\x64_win64).

3. Restart your IDE:
    * Be sure to close and reopen your IDE or terminal to apply the changes.

You can see the latest versions of the code [here, in this folder](https://github.com/AntoDB/AI_1_ISIB_Project/tree/main/Projet%203%20-%20Algo.%20contrainte%20-%20Agenda%20avril%202024).

## Report
As part of the course, I had to do a [report (in French)](https://github.com/AntoDB/AI_1_ISIB_Project/blob/main/Compte%20rendu%20projets%20Intelligence%20Articielle%20-%20Juin%202024%20-%20Antonin%20v3.pdf) which is available [here, on this GitHub](https://github.com/AntoDB/AI_1_ISIB_Project/blob/main/Compte%20rendu%20projets%20Intelligence%20Articielle%20-%20Juin%202024%20-%20Antonin%20v3.pdf).

## Contact
For all enquiries: <a href="mailto:contact@antodb.be">contact@antodb.be</a>


# [Cours HE2B - ISIB Master 1] IA (Intelligence Artificielle)
## Consigne du cours
Langage de programmation au choix : Python, Java, C++ … & Logiciels de votre choix : Matlab, Netbeans, Oracle …
### Partie 1 : Recherche basique, heuristique et optimale
Implémenter, avec le même langage et logiciel, 5 fonctions
o Basique : une pour l’algorithme BFS
o Basique : une pour l’algorithme Random Search
o Heuristique : une pour l’algorithme Greedy Search
o Heuristique : une pour l’algorithme Beam Search
o Optimale : une pour l’algorithme Estimated Extended Uniform Cost + Branch & Bound + Suppression = A*
### Partie 2 : Algorithmes de jeux de stratégie pour 2 personnes
Avec un langage & logiciel au choix, implémenter un jeu de 2 personnes.
Implémenter le jeu sélectionné avec l’algorithme Min-Max complété de l’optimisation alpha-beta.
### Partie 3 : Programmation par contraintes
Avec un langage & logiciel au choix, implémenter un jeu ou un problème de gestion au choix dans la liste suivante, au moyen des principes & algorithmes vus au cours de programmation par contraintes :
Création d’un outil de création d’horaires de cours (avec professeur, local, heure et groupe d’étudiants), Création d’un outil de gestion d’équipes (avec matériel, machines, jours de semaines, groupe d’ouvriers, ingénieurs), gestion de l’emploi du temps et de ressources. Mettre un maximum de contraintes intéressantes.
Il est permis d’utiliser un package ou une dll de « programmation par contraintes ».
Remarque : pas Sudoku !

### Critères d’évaluation
• Respect des deadlines
• Précision et justesse des algorithmes
• Profondeur du travail : vous devez aller le plus loin possible dans vos possibilités d’optimisation
• Compréhension du problème
• Intérêt des exemples applicatifs : vous devez appliquer vos algos sur des exemples concrets & réels.
• Rajoutez une bibliographie à votre rapport si vous vous êtes inspirés d’applications existantes 

## Partie 1 : Sélection d'un trajet (le plus) optimisé entre 2 stations de métro STIB-MIVB
L'objectif de ce projet est de développer un algorithme pour trouver le chemin optimal entre deux stations dans un réseau de métro. L'optimisation vise à minimiser le temps de trajet total, en prenant en compte non seulement les temps de déplacement entre les stations, mais aussi les temps de correspondance lorsque des changements de ligne sont nécessaires. Afin de savoir quel algorithme permet une meilleure optimisation, nous en testons plusieurs : BFS (Beam-first Search), Random Search, Greedy Search, Beam Search, A*.
Pour le bien de l’expérience, j’ai rajouté la future ligne 3 ainsi qu’une ligne fictive entre Simonis et Porte de Namur avec un coût abusif (150).
![Metro map with line 3](https://raw.githubusercontent.com/AntoDB/AI_1_ISIB_Project/main/readme_files/M3planmetro.png)
*Plan de métro avec la future ligne 3*

Vous pouvez voir les dernières versions de ces codes avec les 5 algorithmes [ici, dans ce dossier](https://github.com/AntoDB/AI_1_ISIB_Project/tree/main/Projet%201%20-%20Algo.%20de%20recherche/).

## Partie 2 : Jeu Puissance 8
Le jeu choisi est un Puissance 8. Comme le Puissance 4, il faut aligner des pions horizontalement, verticalement et/ou diagonalement. Dans cette version, il ne faut pas aligner quatre pions mais huit pour réussir la partie. La grille ne fait donc pas 6x7 mais 10x13 pour permettre la réalisation de l’alignement des huit palets.

Pour ce projet, j'ai redeigné [la grille et les pions](https://github.com/AntoDB/AI_1_ISIB_Project/tree/main/Projet%202%20-%20Algo.%20jeu%20-%20Puissance%208/Puissance_8/Images/) même si finalement je n'ai pas pris le temps d'implémenter les images des pions.
Vous pouvez admirer les graphismes [dans ce répertoire](https://github.com/AntoDB/AI_1_ISIB_Project/tree/main/Projet%202%20-%20Algo.%20jeu%20-%20Puissance%208/Puissance_8/Images/).

Vous pouvez voir les dernières versions du code avec juste min-max (minimax) et celle avec min-max (minimax) avec l'optimisation alpha-beta [ici, dans ce dossier](https://github.com/AntoDB/AI_1_ISIB_Project/tree/main/Projet%202%20-%20Algo.%20jeu%20-%20Puissance%208/).

## Partie 3 : Agenda du mois d'avril 2024
Création d’un planning cohérent de mon agenda du mois d’avril 2024 en tenant compte des priorités et des contraintes des différentes activités. C’est un problème courant de planification et d’organisation en fonction de contraintes de non-chevauchement et de priorité.

Ayant énormément d’activités, c’est souvent compliqué de trouver des solutions pour que toutes mes activités concordent.
C’est pourquoi j’ai pensé utiliser l’IA avec une programmation par contrainte afin de me faire un agenda/planning cohérent pour le mois d’avril 2024.
J’ai choisi ce mois due à la charge élevée et avec parfois plusieurs activités le même jour.
Pour ce faire, l’algorithme doit pouvoir m’assigner un maximum d’activités sans en avoir au même moment (chevauchement).

L'agenda de ce mois d'avril a été diminué ici pour ne garder que l'essentiel.

### Package(s)/Librairie(s) utilisé(s)
Le principal package utilisé pour l'implémentation est `docplex.cp.model` de la bibliothèque DOcplex d'IBM. DOcplex est un package Python pour la programmation par contraintes et la programmation mathématique, qui fait partie de l'IBM Decision Optimization suite. Il permet de créer, manipuler et résoudre des modèles d'optimisation avec le solveur IBM ILOG CPLEX Optimization Studio (à [télécharger et installer](https://www.ibm.com/products/ilog-cplex-optimization-studio) lors de l’utilisation du code Python).

Etapes à suivre :
1. Télécharger et installer :
    * Allez sur le site web d'IBM et téléchargez CPLEX Optimization Studio : IBM ILOG CPLEX Optimization Studio
    * Suivez les instructions pour installer le logiciel sur votre système.
    (C'était suffisant pour moi, je n'ai pas du faire la suite. J'ai juste fait l'étape 3.)

2. Ajoutez cpoptimizer.exe au PATH :
    * Recherchez « Modifier les variables d'environnement » dans le menu Démarrer.
    * Dans la fenêtre des variables d'environnement, trouvez la variable PATH dans les variables système et cliquez sur « Modifier ».
    * Ajoutez le chemin complet vers le répertoire contenant cpoptimizer.exe. (par exemple, C:\Program Files\IBM\ILOG\CPLEX_Studio\cpoptimizer\bin\x64_win64).

3. Redémarrer l'IDE :
    * Assurez-vous de fermer et de rouvrir votre IDE ou votre terminal pour appliquer les changements.

Vous pouvez voir les dernières versions du code [ici, dans ce dossier](https://github.com/AntoDB/AI_1_ISIB_Project/tree/main/Projet%203%20-%20Algo.%20contrainte%20-%20Agenda%20avril%202024).

## Rapport
Dans le cadre du cours, j'ai du faire un [rapport](https://github.com/AntoDB/AI_1_ISIB_Project/blob/main/Compte%20rendu%20projets%20Intelligence%20Articielle%20-%20Juin%202024%20-%20Antonin%20v3.pdf) qui est disponible [ici, sur ce GitHub](https://github.com/AntoDB/AI_1_ISIB_Project/blob/main/Compte%20rendu%20projets%20Intelligence%20Articielle%20-%20Juin%202024%20-%20Antonin%20v3.pdf).

## Contact
Pour toute demande : <a href="mailto:contact@antodb.be">contact@antodb.be</a>
