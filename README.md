# Tic Tac Toe Game

## Overview
This is a simple implementation of the Tic Tac Toe game in Python using the Tkinter library for the GUI. The game allows two players to play against each other or a player to play against a bot.

## Features
- Player vs Player mode: Two players can take turns to play the game.
- Player vs Bot mode: One player can play against a bot, which makes moves based on a simple strategy.
- Interactive GUI: The game features a graphical user interface built with Tkinter for a better user experience.
- Winning Detection: The game detects when a player wins or when the game ends in a draw.

## Notice
- if flip coin show any error clone coin_toss and paste it in the same directory(folder)

## How to Run
1. Make sure you have Python installed on your system.
2. Clone this repository or download the `tic_tac_toe.py` file.
3. Open a terminal or command prompt and navigate to the directory containing `tic_tac_toe.py`.
4. Run the command `python tic_tac_toe.py`.
5. The Tic Tac Toe game window will open, allowing you to play against another player or against the bot.

## How to Play
- When the game starts, you'll see a 3x3 grid representing the Tic Tac Toe board.
- Click on any empty cell to place your mark (X or O).
- The game alternates between players, with each player taking turns to make a move.
- The first player to get three of their marks in a row (horizontally, vertically, or diagonally) wins the game.
- If all cells are filled without any player achieving three in a row, the game ends in a draw.

## Additional Notes
- The bot's moves are based on a simple strategy: it first checks for immediate winning moves, then for immediate moves to block the opponent, and finally makes a random move if no winning moves are available.
- You can toggle between Player vs Player and Player vs Bot modes using the button provided in the game window.

Enjoy playing Tic Tac Toe!
