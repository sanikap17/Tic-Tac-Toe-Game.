import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.configure(bg="violet")  # Set the background color

        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []

        # Add player name input fields
        self.player1_name = tk.StringVar(value="Player 1")
        self.player2_name = tk.StringVar(value="Player 2")
        self.create_ui()

    def create_ui(self):
        # Player name input labels and entry boxes
        tk.Label(self.root, text="Player X:", font=("Arial", 12), bg="violet").grid(row=0, column=0, sticky="e")
        tk.Entry(self.root, textvariable=self.player1_name, font=("Arial", 12)).grid(row=0, column=1, columnspan=2, sticky="w")

        tk.Label(self.root, text="Player O:", font=("Arial", 12), bg="violet").grid(row=1, column=0, sticky="e")
        tk.Entry(self.root, textvariable=self.player2_name, font=("Arial", 12)).grid(row=1, column=1, columnspan=2, sticky="w")

        # Create a 3x3 grid of buttons for the game
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.root, text="", font=("Arial", 24), width=5, height=2,
                                   bg="skyblue", command=lambda r=row, c=col: self.make_move(r, c))
                button.grid(row=row + 2, column=col)
                self.buttons.append(button)

        # Add a Reset button below the grid
        reset_button = tk.Button(self.root, text="Reset", font=("Arial", 16), bg="yellow", command=self.reset_game)
        reset_button.grid(row=5, column=0, columnspan=3, sticky="nsew")

    def make_move(self, row, col):
        index = row * 3 + col
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                winner = self.player1_name.get() if self.current_player == "X" else self.player2_name.get()
                messagebox.showinfo("Game Over", f"{winner} wins!")
                self.reset_game()
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
        else:
            messagebox.showwarning("Invalid Move", "This square is already taken!")

    def check_winner(self):
        # Define winning combinations
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
            [0, 4, 8], [2, 4, 6]              # Diagonal
        ]
        for combo in winning_combinations:
            if (self.board[combo[0]] == self.current_player and
                self.board[combo[1]] == self.current_player and
                self.board[combo[2]] == self.current_player):
                return True
        return False

    def reset_game(self):
        # Reset the board for a new game
        self.board = [""] * 9
        self.current_player = "X"
        for button in self.buttons:
            button.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
