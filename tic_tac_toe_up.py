import tkinter as tk
from tkinter import messagebox
from coin_toss import CoinToss  # Assuming you have coin_toss.py in the same directory
import random

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic-Tac-Toe")

        self.canvas = tk.Canvas(master, width=300, height=300, bg='white')
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.on_click)

        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.player = 'X'
        self.bot = 'O' if self.player == 'X' else 'X'
        self.is_bot_game = False

        self.player_toggle_button = tk.Button(master, text="Play against Bot", command=self.toggle_player_mode)
        self.player_toggle_button.pack()

        self.coin_button = tk.Button(master, text="Flip Coin", command=self.flip_coin)
        self.coin_button.pack()

        self.draw_board()

    def toggle_player_mode(self):
        self.is_bot_game = not self.is_bot_game
        if self.is_bot_game:
            self.player_toggle_button.config(text="Play against Person")
        else:
            self.player_toggle_button.config(text="Play against Bot")

    def draw_board(self):
        self.canvas.delete('all')
        for i in range(1, 3):
            self.canvas.create_line(i*100, 0, i*100, 300)
            self.canvas.create_line(0, i*100, 300, i*100)

        for i in range(3):
            for j in range(3):
                if self.board[i][j] != ' ':
                    x = j * 100 + 50
                    y = i * 100 + 50
                    self.canvas.create_text(x, y, text=self.board[i][j], font=('Arial', 50))

    def on_click(self, event):
        x = event.x // 100
        y = event.y // 100

        if self.board[y][x] == ' ':
            self.board[y][x] = self.player
            self.draw_board()
            if self.check_winner(self.player):
                winner = "Player " + self.player + " wins!"
                messagebox.showinfo("Winner", winner)
                self.reset_game()
            elif self.is_board_full():
                messagebox.showinfo("Draw", "It's a draw!")
                self.reset_game()
            else:
                self.switch_player()
                if self.is_bot_game and self.player == self.bot:  # Check if it's the bot's turn
                    self.bot_move()

    def switch_player(self):
        self.player = 'O' if self.player == 'X' else 'X'

    def bot_move(self):
        # Check for any immediate winning moves for the bot
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    self.board[i][j] = self.bot
                    if self.check_winner(self.bot):
                        self.draw_board()
                        winner = "Player " + self.bot + " wins!"
                        messagebox.showinfo("Winner", winner)
                        self.reset_game()
                        return
                    else:
                        self.board[i][j] = ' '  # Undo move if not a winning move for the bot

        # Check for any immediate winning moves for the opponent to block them
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    self.board[i][j] = self.player
                    if self.check_winner(self.player):
                        self.board[i][j] = self.bot
                        self.draw_board()
                        self.switch_player()  # Switch to the next player after the bot's move
                        return
                    else:
                        self.board[i][j] = ' '  # Undo move if not a winning move for the opponent

        # If no immediate winning moves are available, make a random move
        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == ' ']
        if empty_cells:
            cell = random.choice(empty_cells)
            self.board[cell[0]][cell[1]] = self.bot
            self.draw_board()
            if self.check_winner(self.bot):
                winner = "Player " + self.bot + " wins!"
                messagebox.showinfo("Winner", winner)
                self.reset_game()
            elif self.is_board_full():
                messagebox.showinfo("Draw", "It's a draw!")
                self.reset_game()
            else:
                self.switch_player()  # Switch to the next player after the bot's move

    def check_winner(self, player):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == player:
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == player:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True
        return False

    def is_board_full(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def reset_game(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.player = 'X'
        self.draw_board()

    def flip_coin(self):
        coin_toss_window = tk.Toplevel(self.master)
        coin_toss = CoinToss(coin_toss_window)

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
