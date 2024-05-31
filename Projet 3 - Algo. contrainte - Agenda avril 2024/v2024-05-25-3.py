# -*- coding: utf-8 -*-
"""
Find an agenda 😅

Version 7

1st version:
Created on Thursday April 11 2024 at 01:32:43
Stopped on Saturday May 25 2024 at 18:33:50

Authors : 
Antonin De Breuck (Computer engineer - 1st Master)

Helped by :
ChatGPT
"""
# The CP Optimizer solver is not found. -> To solve this problem, you need to install IBM ILOG CPLEX Optimization Studio, which includes CP Optimizer.
"""
Example of configuration on Windows :
1. Download and install :
    * Go to the IBM website and download CPLEX Optimization Studio: IBM ILOG CPLEX Optimization Studio
    * Follow the instructions to install the software on your system. (good enough for me)

2. Add cpoptimizer.exe to the PATH:
    * Search for "Change environment variables" in the Start menu.
    * In the environment variables window, find the PATH variable in the system variables and click on "Edit".
    * Add the full path to the directory containing cpoptimizer.exe (for example, C:\Program Files\IBM\ILOG\CPLEX_Studio\cpoptimizer\bin\x64_win64).

3. Restart your IDE:
    * Be sure to close and reopen your IDE or terminal to apply the changes.
"""

#=========================================================================================================#

                        #-------------------- Modules imported --------------------#

#=========================================================================================================#

from docplex.cp.model import CpoModel
from datetime import datetime, timedelta

# Fonction utilitaire pour convertir les heures en minutes
def to_minutes(day, hour, minute=0):
    return (day - 1) * 24 * 60 + hour * 60 + minute

# Fonction utilitaire pour convertir les minutes en une date lisible
def from_minutes(minutes):
    base_date = datetime(2024, 4, 1)  # 1er avril 2024
    actual_date = base_date + timedelta(minutes=minutes)
    return actual_date.strftime("%A %d %B %Y at %H:%M")

#=========================================================================================================#

        #-------------------- (Un)Mofiable/(Un)Changeable variables | Options --------------------#

#=========================================================================================================#

# Création du modèle
mdl = CpoModel()

# Création des activités fixes
courses = [
    (to_minutes(3, 8), to_minutes(3, 12, 30), "Exo ingé. logiciel"),
    (to_minutes(3, 13, 40), to_minutes(3, 18), "Analyse & visualisation de data"),
    (to_minutes(4, 8), to_minutes(4, 12, 30), "Développement d'app réseau"),
    (to_minutes(4, 13, 40), to_minutes(4, 18), "IA"),
    (to_minutes(26, 8), to_minutes(26, 12, 30), "Ergonomie des logiciels")
]

# Création des variables pour chaque cours
courses_activities = []
for start, end, name in courses:
    interval = mdl.interval_var(start=start, end=end, name=name)
    courses_activities.append(interval)

# Concours de robotique (Priorité maximale)
concours_robotique = mdl.interval_var(start=to_minutes(20, 0), end=to_minutes(21, 23, 59), name="Concours de robotique")

# Autres activités le 20 avril
concert_chorale = mdl.interval_var(start=to_minutes(20, 16, 30), end=to_minutes(20, 20), optional=True, name="Concert avec la chorale")
rave_rebels = mdl.interval_var(start=to_minutes(20, 20), end=to_minutes(21, 10), optional=True, name="Rave Rebels")
repas_famille_20 = mdl.interval_var(start=to_minutes(20, 19, 30), end=to_minutes(20, 23), optional=True, name="Repas de famille 20 avril")
repres_theatre = mdl.interval_var(start=to_minutes(20, 20, 30), end=to_minutes(20, 23), optional=True, name="Représentation théâtrale")

# Anniversaire d'un cousin (optionnel)
anniversaire_florian = mdl.interval_var(start=to_minutes(26, 20, 30), end=to_minutes(27, 5), optional=True, name="Anniversaire 25 ans Florian")

# Repas de famille le 27 avril (optionnel si 20 avril)
repas_famille_27 = mdl.interval_var(start=to_minutes(27, 19, 30), end=to_minutes(27, 23), optional=True, name="Repas de famille 27 avril")

# Chorale tous les samedis
chorales = [
    mdl.interval_var(start=to_minutes(s, 15, 15), end=to_minutes(s, 17, 30), optional=True, name=f"Chorale {s}")
    for s in range(6, 30, 7) if s != 20
]

#=========================================================================================================#

                #-------------------- Main part - Treatment & output --------------------#

#=========================================================================================================#

# Ajouter les contraintes de non-chevauchement
all_intervals = courses_activities + [concours_robotique, concert_chorale, rave_rebels, repas_famille_20, repres_theatre, anniversaire_florian, repas_famille_27] + chorales
mdl.add(mdl.no_overlap(all_intervals))

# Ajouter les contraintes de priorité (le concours de robotique exclut toutes les autres activités du 20 avril)
mdl.add(mdl.if_then(mdl.presence_of(concours_robotique), mdl.logical_not(mdl.presence_of(concert_chorale))))
mdl.add(mdl.if_then(mdl.presence_of(concours_robotique), mdl.logical_not(mdl.presence_of(rave_rebels))))
mdl.add(mdl.if_then(mdl.presence_of(concours_robotique), mdl.logical_not(mdl.presence_of(repas_famille_20))))
mdl.add(mdl.if_then(mdl.presence_of(concours_robotique), mdl.logical_not(mdl.presence_of(repres_theatre))))

# Ajouter des contraintes d'exclusivité entre les activités optionnelles du 20 avril
mdl.add(mdl.if_then(mdl.presence_of(repas_famille_20), mdl.logical_not(mdl.presence_of(repres_theatre))))

# Ajouter une contrainte de minimisation pour encourager la présence des activités optionnelles
#mdl.add(mdl.maximize(sum(mdl.presence_of(var) for var in [anniversaire_florian, repas_famille_27] + chorales)))
mdl.add(mdl.maximize(sum(mdl.presence_of(var) for var in all_intervals)))

# Résolution du problème
solution = mdl.solve()

# Collecter les résultats dans une liste
results = []

# Affichage des résultats
if solution:
    for v in all_intervals:
        interval_solution = solution.get_var_solution(v)
        start = interval_solution.start
        end = interval_solution.end
        if start is not None and end is not None:
            results.append((v.get_name(), start, end))

    # Trier les résultats par heure de début
    results.sort(key=lambda x: x[1])

    # Afficher les résultats triés
    for name, start, end in results:
        print(f"{name}: {from_minutes(start)} - {from_minutes(end)}")
else:
    print("Aucune solution trouvée")
