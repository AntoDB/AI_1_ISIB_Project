# Nous gardons que les X meilleurs enfants (heuristiquement) après avoir analyser tous les enfants des X meilleurs parents (heuristiquement)
from datetime import datetime # Pour savoir le temps d'éxécution (vitesse)
from collections import deque
import heapq

# Station, station connectée avec temps de trajet et ligne(s) à laquelle elle appartient
metro_network = {
    # Ligne 5 (Début)
    'Erasme': {'Eddy Merckx': (1, ['5'])},
    'Eddy Merckx': {'Erasme': (1, ['5']), 'CERIA': (1, ['5'])},
    'CERIA': {'Eddy Merckx': (1, ['5']), 'La Roue': (1, ['5'])},
    'La Roue': {'CERIA': (1, ['5']), 'Bizet': (1, ['5'])},
    'Bizet': {'La Roue': (1, ['5']), 'Veeweyde': (1, ['5'])},
    'Veeweyde': {'Bizet': (1, ['5']), 'Saint-Guidon': (1, ['5'])},
    'Saint-Guidon': {'Veeweyde': (1, ['5']), 'Aumale': (1, ['5'])},
    'Aumale': {'Saint-Guidon': (1, ['5']), 'Jacques Brel': (1, ['5'])},
    'Jacques Brel': {'Aumale': (1, ['5']), 'Gare de l’Ouest': (1, ['5'])},
    # Ligne 1 & 5
    'Gare de l’Ouest': {'Jacques Brel': (1, ['5']), 'Beekkant': (1, ['1', '5', '2', '6']), 'Delacroix': (1, ['2', '6'])},
    'Beekkant': {'Gare de l’Ouest': (1, ['1', '5', '2', '6']), 'Etangs Noirs': (1, ['1', '5']), 'Osseghem': (1, ['2', '6'])},
    'Etangs Noirs': {'Beekkant': (1, ['1', '5', '2', '6']), 'Comte de Flandre': (1, ['1', '5'])},
    'Comte de Flandre': {'Etangs Noirs': (1, ['1', '5']), 'Sainte-Catherine': (1, ['1', '5'])},
    'Sainte-Catherine': {'Comte de Flandre': (1, ['1', '5']), 'De Brouckère': (45, ['1', '5'])}, # METRO BLOQUE
    'De Brouckère': {'Sainte-Catherine': (1, ['1', '5']), 'Gare Centrale': (1, ['1', '5']), 'Bourse': (1, ['3']), 'Rogier': (1, ['3'])},
    'Gare Centrale': {'De Brouckère': (1, ['1', '5']), 'Parc': (1, ['1', '5'])},
    'Parc': {'Gare Centrale': (1, ['1', '5']), 'Arts-Loi': (1, ['1', '5', '2', '6'])},
    'Arts-Loi': {'Parc': (1, ['1', '5']), 'Maelbeek': (1, ['1', '5']), 'Trône': (1, ['2', '6']), 'Madou': (1, ['2', '6'])},
    'Maelbeek': {'Arts-Loi': (1, ['1', '5']), 'Schuman': (1, ['1', '5'])},
    'Schuman': {'Maelbeek': (1, ['1', '5']), 'Merode': (1, ['1', '5'])},
    'Merode': {'Schuman': (1, ['1', '5']), 'Montgomery': (1, ['1']), 'Thieffry': (1, ['5'])},
    # Ligne 1 (suite tronc commun)
    'Montgomery': {'Merode': (2, ['1', '5']), 'Joséphine-Charlotte': (1, ['1'])},
    'Joséphine-Charlotte': {'Montgomery': (1, ['1']), 'Gribaumont': (1, ['1'])},
    'Gribaumont': {'Joséphine-Charlotte': (1, ['1']), 'Tomberg': (1, ['1'])},
    'Tomberg': {'Gribaumont': (1, ['1']), 'Roodebeek': (1, ['1'])},
    'Roodebeek': {'Tomberg': (1, ['1']), 'Vandervelde': (1, ['1'])},
    'Vandervelde': {'Roodebeek': (1, ['1']), 'Alma': (1, ['1'])},
    'Alma': {'Vandervelde': (1, ['1']), 'Crainhem': (1, ['1'])},
    'Crainhem': {'Alma': (1, ['1']), 'Stockel': (2, ['1'])},
    'Stockel': {'Crainhem': (2, ['1'])},
    # Ligne 5 (suite tronc commun)
    'Thieffry': {'Merode': (1, ['1', '5']), 'Pétillon': (1, ['5'])},
    'Pétillon': {'Thieffry': (1, ['5']), 'Hankar': (1, ['5'])},
    'Hankar': {'Pétillon': (1, ['5']), 'Delta': (1, ['5'])},
    'Delta': {'Hankar': (1, ['5']), 'Beaulieu': (1, ['5'])},
    'Beaulieu': {'Delta': (1, ['5']), 'Demey': (1, ['5'])},
    'Demey': {'Beaulieu': (1, ['5']), 'Herrmann-Debroux': (1, ['5'])},
    'Herrmann-Debroux': {'Demey': (1, ['5'])},
    # Ligne 6 (Début)
    'Roi Baudouin': {'Heysel': (1, ['6'])},
    'Heysel': {'Roi Baudouin': (1, ['6']), 'Houba-Brugmann': (1, ['6'])},
    'Houba-Brugmann': {'Heysel': (1, ['6']), 'Stuyvenbergh': (1, ['6'])},
    'Stuyvenbergh': {'Houba-Brugmann': (1, ['6']), 'Bockstael': (1, ['6'])},
    'Bockstael': {'Stuyvenbergh': (1, ['6']), 'Pannenhuis': (1, ['6'])},
    'Pannenhuis': {'Bockstael': (1, ['6']), 'Belgica': (1, ['6'])},
    'Belgica': {'Pannenhuis': (1, ['6']), 'Simonis': (1, ['2', '6'])},
    # Ligne 2 & 6
    'Simonis': {'Belgica': (1, ['6']), 'Osseghem': (1, ['2', '6']), 'Elisabeth': (4, ['2', '6']),  'Porte de Namur': (150, ['42'])}, # Ligne 42 fictive
    'Osseghem': {'Simonis': (1, ['2', '6']), 'Beekkant': (1, ['1', '5', '2', '6'])},
    # Beekkant & Gare de l'ouest déjà mis avant
    'Delacroix': {'Gare de l’Ouest': (1, ['1', '5', '2', '6']), 'Clemenceau': (1, ['2', '6'])},
    'Clemenceau': {'Delacroix': (1, ['2', '6']), 'Gare du Midi': (1, ['2', '6'])},
    'Gare du Midi': {'Clemenceau': (1, ['2', '6']), 'Porte de Hal': (1, ['2', '6']), 'Porte de Hal': (1, ['3']), 'Toots Thielemans': (1, ['3'])},
    'Porte de Hal': {'Gare du Midi': (1, ['2', '6']), 'Hôtel des Monnaies': (1, ['2', '6']), 'Parvis de Saint-Gilles': (1, ['3']), 'Gare du Midi': (1, ['3'])},
    'Hôtel des Monnaies': {'Porte de Hal': (1, ['2', '6']), 'Louise': (1, ['2', '6'])},
    'Louise': {'Hôtel des Monnaies': (1, ['2', '6']), 'Porte de Namur': (1, ['2', '6'])},
    'Porte de Namur': {'Louise': (1, ['2', '6']), 'Trône': (1, ['2', '6']), 'Simonis': (150, ['42'])}, # Ligne 42 fictive
    'Trône': {'Porte de Namur': (1, ['2', '6']), 'Arts-Loi': (1, ['1', '5', '2', '6'])},
    # Arts-Loi déjà mis avant
    'Madou': {'Arts-Loi': (1, ['1', '5', '2', '6']), 'Botanique': (1, ['2', '6'])},
    'Botanique': {'Madou': (1, ['2', '6']), 'Rogier': (1, ['2', '6'])},
    'Rogier': {'Botanique': (45, ['2', '6']), 'Yser': (1, ['2', '6']), 'De Brouckère': (1, ['3']), 'Gare du Nord': (1, ['3'])}, # METRO BLOQUE
    'Yser': {'Rogier': (1, ['2', '6']), 'Ribaucourt': (1, ['2', '6'])},
    'Ribaucourt': {'Yser': (1, ['2', '6']), 'Elisabeth': (1, ['2', '6'])},
    'Elisabeth': {'Ribaucourt': (1, ['2', '6']), 'Simonis': (4, ['2', '6'])},
    # Ligne 3
    'Albert': {'Horta': (1, ['3'])},
    'Horta': {'Albert': (1, ['3']), 'Parvis de Saint-Gilles': (1, ['3'])},
    'Parvis de Saint-Gilles': {'Horta': (1, ['3']), 'Porte de Hal': (1, ['3'])},
    # Porte de Hal & Gare du Midi mis avant
    'Toots Thielemans': {'Gare du Midi': (1, ['3']), 'Anneessens': (1, ['3'])},
    'Anneessens': {'Toots Thielemans': (1, ['3']), 'Bourse': (1, ['3'])},
    'Bourse': {'Anneessens': (1, ['3']), 'De Brouckère': (1, ['3'])},
    # De Brouckère
    'Rogier': {'De Brouckère': (1, ['3']), 'Gare du Nord': (1, ['3'])},
    'Gare du Nord': {'Rogier': (1, ['3']), 'Liedts': (1, ['3'])},
    'Liedts': {'Gare du Nord': (1, ['3']), 'Colignon': (1, ['3'])},
    'Colignon': {'Liedts': (1, ['3']), 'Verboekhoven': (1, ['3'])},
    'Verboekhoven': {'Colignon': (1, ['3']), 'Riga': (1, ['3'])},
    'Riga': {'Verboekhoven': (1, ['3']), 'Tilleul': (1, ['3'])},
    'Tilleul': {'Riga': (1, ['3']), 'Paix': (1, ['3'])},
    'Paix': {'Tilleul': (1, ['3']), 'Bordet': (1, ['3'])},
    'Bordet': {'Paix': (1, ['3'])}

    # Ligne 42 fictive entre Simonis et Porte de Namur (directe mais à coût hyper élevé, prévu pour montré l'effet BFS négatif)
}

# Temps de déplacement de correspondance + temps d'attente d'un véhicule (2 min)
line_changes = {
    'Gare de l’Ouest': 4,
    'Beekkant': 4,
    'Arts-Loi': 4,
    'De Brouckère': 5,
    'Gare du Midi': 4,

    'Etangs Noirs': 3,
    'Comte de Flandre': 3,
    'Sainte-Catherine': 3,
    'Gare Centrale': 3,
    'Parc': 3,
    'Arts-Loi': 3,
    'Maelbeek': 3,
    'Schuman': 3,
    'Merode': 4,

    'Simonis': 3,
    'Osseghem': 3,
    'Delacroix': 3,
    'Clemenceau': 3,
    'Porte de Hal': 3,
    'Hôtel des Monnaies': 3,
    'Louise': 3,
    'Porte de Namur': 3,
    'Trône': 3,
    'Madou': 3,
    'Botanique': 3,
    'Rogier': 3,
    'Yser': 3,
    'Ribaucourt': 3,
    'Elisabeth': 3
}

def calculate_heuristics(graph, goal):
    """
    Calcule l'heuristique pour chaque station en utilisant un BFS à partir de la station d'arrivée.
    Ici, on utilise une heuristique simple : on suppose que chaque station restante ajoute 1 unité de coût. => Distance Manhattan, le nombre de station à atteindre avant d'arriver.
    Une meilleure heuristique pourrait utiliser des distances réelles entre stations et convertir ça en temps en fonction de la vitesse moyenne d'un métro.
    """
    heuristics = {station: float('inf') for station in graph}
    queue = deque([(goal, 0)])
    heuristics[goal] = 0

    while queue:
        current_station, distance = queue.popleft()

        for neighbor in graph[current_station]:
            if heuristics[neighbor] == float('inf'):  # Non visité
                heuristics[neighbor] = distance + 1
                queue.append((neighbor, distance + 1))
    
    return heuristics

def a_star_search(graph, start, goal, transfers):
    # Initialisation de la file de priorité avec le chemin de départ
    queue = [(0, [start], 0, None)]  # (heuristic cost, path, current cost, current line)
    visited = {}
    all_heuristics = calculate_heuristics(graph, goal)  # Calcule toutes les heuristiques des stations

    while queue:
        # Sort the queue by f = g + h (heapq ensures the smallest element is popped first)
        heapq.heapify(queue)
        heuristic_cost, path, current_cost, current_line = heapq.heappop(queue)
        current_station = path[-1]

        # Si la station actuelle est la destination, retournez le chemin et le coût total
        if current_station == goal:
            return path, current_cost

        # Si la station a déjà été visité avec un moindre coût alors on ignore le chemin. (Si trouve la station avec un meilleur coût on fait la suite de la boucle)
        if current_station in visited and visited[current_station] <= current_cost:
            continue
        # Marquer la station actuelle comme visitée avec le coût actuel
        visited[current_station] = current_cost
        print(f'Add visited station with cost: {visited}')

        # Explorer les stations adjacentes
        for neighbor, (travel_time, lines) in graph[current_station].items():
            for line in lines:
                # Calculer le coût total en ajoutant le temps de trajet et le temps de transfert en cas de changement de ligne
                additional_transfer_time = transfers.get(current_station, 0) if current_line and current_line != line else 0
                new_cost = current_cost + travel_time + additional_transfer_time
                new_path = path + [neighbor]

                # Calculer le coût réel avec l'ajout de l'heuristique estimé pour atteindre l'objectif depuis la station voisine
                heuristic_cost = new_cost + all_heuristics[neighbor]

                # Ajouter le nouveau chemin à la file si pas de boucle et moins coûteux
                if neighbor not in path:
                    heapq.heappush(queue, (heuristic_cost, new_path, new_cost, line))
                print(f'    New path: {new_path}, Heuristic_cost {heuristic_cost}')
        print(f'New queue: {queue}')
        print()    

    # Si aucune solution n'est trouvée
    return None, None

# Exemple d'utilisation (métro bloqué entre Sainte-Catherine et De Brouckère)
start_station = input()
goal_station = input()
started_time = datetime.now() # Pour savoir le temps d'exécution (vitesse)
path, total_cost = a_star_search(metro_network, start_station, goal_station, line_changes)
print(f"Chemin trouvé : {path}")
print(f"Coût total : {total_cost} minutes")
print(f'Temps d\'exécution/vitesse : {datetime.now() - started_time}')

"""
Travel cost above
Tested input for start and end station :

Stuyvenbergh
Roodebeek
"""
