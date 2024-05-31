import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox # Pour annoncer le(s) vainqueur(s)
from tkinter import simpledialog # Pour sélection joueur début
import os

class StartDialog(simpledialog.Dialog):
    def body(self, master):
        tk.Label(master, text="Choisissez le joueur qui commence:").pack()
        self.player_var = tk.IntVar()
        self.player_var.set(1)
        tk.Radiobutton(master, text="Joueur 1 (Vous)", variable=self.player_var, value=1).pack(anchor=tk.W)
        tk.Radiobutton(master, text="Joueur 2 (IA)", variable=self.player_var, value=2).pack(anchor=tk.W)
        return None

    def apply(self):
        self.result = self.player_var.get()

class Puissance8(tk.Tk):
    def __init__(self, starting_player):
        super().__init__()
        self.title("Puissance 8")
        self.geometry("800x600")  # Taille de la fenêtre adaptée à la grille 13x10
        
        self.canvas = tk.Canvas(self, width=800, height=600)
        self.canvas.pack()

        # Charger l'image de la grille
        self.image_path = os.path.join(os.getcwd(), "Puissance_8", "Images", "Grille_10x13.png")
        print(self.image_path)
        self.image = Image.open(self.image_path)
        self.image = self.image.resize((800, 600))
        self.grille_image = ImageTk.PhotoImage(self.image)  # Convertir l'image PIL en PhotoImage
        
        self.canvas.create_image(0, 0, anchor="nw", image=self.grille_image)

        self.canvas.bind("<Button-1>", self.get_x_click)
        
        self.grid_size = (10, 13)  # Taille de la grille avec 10 lignes et 13 colonnes
        self.grid_spacing = 57
        self.x_ofset = 30
        self.y_ofset = 15
        self.token_radius = 22
        #self.current_player = 1
        self.current_player = starting_player
        self.grid = [[0] * self.grid_size[1] for _ in range(self.grid_size[0])]
        self.max_depth = 2  # Profondeur maximale pour l'algorithme Minimax

        print(f'START: {self.grid}')
        if self.current_player == 2:
            self.ai_move()

    def get_x_click(self, event):
        x_grid = event.x
        print(f'Event: {x_grid}')
        column = (x_grid - self.x_ofset) // self.grid_spacing # Sélection de la colonne en fonction de la position en X
        self.place_token(column)
        print(f'Wins possibilities: {self.check_win_possibility(self.get_empty_row(column), column, 1)}')

    def place_token(self, column):        
        print(f'Colonne: {column}')
        if column > -1 and column < 13:
            row = self.get_empty_row(column)
            if row is not None:
                self.draw_token(row, column)
                self.grid[row][column] = self.current_player
                print(f'New token: {self.grid}')
                winner = self.check_winner(row, column)
                if winner:
                    messagebox.showinfo("Fin de partie", f"Le joueur {winner} ({'vous' if winner == 1 else 'IA'}) a gagné !")
                    self.reset_game()
                elif self.check_full():
                    messagebox.showinfo("Fin de partie", f"Ex aequo ! La grille est remplie, pas de gagnant donc !")
                    self.reset_game()
                else:
                    self.current_player = 3 - self.current_player  # Switch player
                    if self.current_player == 2:
                        self.ai_move()

    def get_empty_row(self, column):
        for row in range(self.grid_size[0]-1, -1, -1):  # Parcourt les lignes de bas en haut
            if self.grid[row][column] == 0:
                return row
        return None

    def draw_token(self, row, column):
        x = (column + 0.5) * self.grid_spacing + self.x_ofset
        y = (row + 0.5) * self.grid_spacing + self.y_ofset
        color = "red" if self.current_player == 1 else "yellow"
        self.canvas.create_oval(x - self.token_radius, y - self.token_radius,
                                x + self.token_radius, y + self.token_radius,
                                fill=color)

    def check_winner(self, row, column):
        player = self.grid[row][column]
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]  # Vecteurs de direction pour vérifier les lignes, colonnes et diagonales

        for dr, dc in directions:
            count = 1  # Nombre de jetons alignés dans la direction actuelle
            
            # Vérifier vers la droite
            r, c = row, column
            while True:
                r, c = r + dr, c + dc
                if 0 <= r < self.grid_size[0] and 0 <= c < self.grid_size[1] and self.grid[r][c] == player:
                    count += 1
                else:
                    break
            
            # Vérifier vers la gauche (direction opposée)
            r, c = row, column
            while True:
                r, c = r - dr, c - dc
                if 0 <= r < self.grid_size[0] and 0 <= c < self.grid_size[1] and self.grid[r][c] == player:
                    count += 1
                else:
                    break
            
            if count >= 8:
                return player  # Le joueur actuel a gagné
        
        return None  # Pas de gagnant
    
    def check_full(self):
        for row in range(self.grid_size[0]):
            for col in range(self.grid_size[1]):
                if self.grid[row][col] == 0:
                    return False
        return True
    
    def reset_game(self):
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor="nw", image=self.grille_image)
        self.grid = [[0] * self.grid_size[1] for _ in range(self.grid_size[0])]
        #self.current_player = 1
        self.current_player = 3 - self.current_player
        if self.current_player == 2:
            self.ai_move()

    #================================================== AI Part ==================================================#

    # Check les toutes les possibilités gagnantes pour chaque position de pions
    # Check s'il y a moyen de gagner
    # Check si c'est vide ou si un pion du joueur sur le même axe que celui à check
    
    def check_win_possibility(self, row, column, player = -1):
        if player == -1:
            player = self.grid[row][column]
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]  # Vecteurs de direction pour vérifier les lignes, colonnes et diagonales
        nbr_reussite = 0

        for dr, dc in directions:
            count = 1  # Nombre de jetons alignés dans la direction actuelle
            
            # Vérifier vers la droite
            r, c = row, column
            while True:
                r, c = r + dr, c + dc
                if 0 <= r < self.grid_size[0] and 0 <= c < self.grid_size[1] and (self.grid[r][c] == 0 or self.grid[r][c] == player):
                    count += 1
                else:
                    break
            
            # Vérifier vers la gauche (direction opposée)
            r, c = row, column
            while True:
                r, c = r - dr, c - dc
                if 0 <= r < self.grid_size[0] and 0 <= c < self.grid_size[1] and self.grid[r][c] == 0:
                    count += 1
                else:
                    break
            
            if count >= 8:
                #print(f'Counts : {count}')
                nbr_reussite += count - 7  # Rajout du nombre de réussites pour la direction (et son opposée)
        """        
        if nbr_reussite >= 1:
            return nbr_reussite  # Nombre de réussites
        
        return 0  # Pas de réussite possible
        """
        return count
        """
    def check_win_possibility(self, row, column, player):
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        win_count = 0
        for dr, dc in directions:
            count = 1
            for direction in [1, -1]:
                r, c = row, column
                while True:
                    r += dr * direction
                    c += dc * direction
                    if 0 <= r < self.grid_size[0] and 0 <= c < self.grid_size[1] and self.grid[r][c] in [0, player]:
                        count += 1
                    else:
                        break
            if count >= 8:
                win_count += 1
        return win_count
        """

    def evaluate_board(self, maximizing_player):
        score = 0
        for col in range(self.grid_size[1]):
            row = self.get_empty_row(col)
            if row is not None:
                #score += self.check_win_possibility(row, col, 2) if maximizing_player else -self.check_win_possibility(row, col, 1)
                # Évaluation pour l'IA
                score += self.check_win_possibility(row, col, 2) * (1 if maximizing_player else -1)
                # Évaluation pour le joueur humain
                score -= self.check_win_possibility(row, col, 1) * (1 if not maximizing_player else -1)
        return score

    def minimax(self, depth, maximizing_player):
        if depth == self.max_depth:
            return self.evaluate_board(maximizing_player)
            #return self.evaluate_board()

        if maximizing_player:
            max_eval = float('-inf')
            for col in range(self.grid_size[1]):
                row = self.get_empty_row(col)
                if row is not None:
                    self.grid[row][col] = 2  # Simulate AI move
                    eval = self.minimax(depth + 1, False)
                    self.grid[row][col] = 0  # Undo move
                    max_eval = max(max_eval, eval)
                    print(f'MAX eval : {max_eval}')
            return max_eval
        else:
            min_eval = float('inf')
            for col in range(self.grid_size[1]):
                row = self.get_empty_row(col)
                if row is not None:
                    self.grid[row][col] = 1  # Simulate opponent move
                    eval = self.minimax(depth + 1, True)
                    self.grid[row][col] = 0  # Undo move
                    min_eval = min(min_eval, eval)
                    print(f'MIN eval : {min_eval}')
            return min_eval

    def ai_move(self):
        best_score = float('-inf')
        best_col = None
        for col in range(self.grid_size[1]):
            row = self.get_empty_row(col)
            if row is not None:
                self.grid[row][col] = 2  # Simulate AI move
                score = self.minimax(0, False)
                self.grid[row][col] = 0  # Undo move
                if score > best_score:
                    best_score = score
                    best_col = col
        if best_col is not None:
            print(f'IA win possibility : {self.check_win_possibility(self.get_empty_row(best_col),best_col,2)}')
            self.place_token(best_col)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Cache la fenêtre de sélection de joeuur
    start_dialog = StartDialog(root)
    starting_player = start_dialog.result
    root.destroy()  # Supprime la fenêtre de sélection de joeuur
    if starting_player is not None:
        app = Puissance8(starting_player)
        app.mainloop()
