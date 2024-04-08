import tkinter as tk
import random

class CoinToss:
    def __init__(self, master):
        self.master = master
        self.master.title("Coin Toss")

        self.canvas = tk.Canvas(master, width=200, height=200, bg='white')
        self.canvas.pack()

        self.button = tk.Button(master, text="Flip Coin", command=self.flip_coin)
        self.button.pack()

    def flip_coin(self):
        self.canvas.delete('all')
        result = random.choice(['Heads', 'Tails'])
        self.canvas.create_text(100, 100, text=result, font=('Arial', 20, 'bold'))

if __name__ == "__main__":
    root = tk.Tk()
    coin_toss = CoinToss(root)
    root.mainloop()
