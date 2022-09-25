**Connect-4-AI**

![AI2](https://user-images.githubusercontent.com/66219569/102391818-82815f80-3fd6-11eb-8bbc-d8c75014f19e.jpg)

**Description**

This program allows you to play a simple Connect-4 game against an AI in python. The AI is based on the minimax algorithm with a scoring system. A detailed explanation of the minimax alogrithm can be found here:  https://en.wikipedia.org/wiki/Minimax#Pseudocode. The code consists of the following 12 functions:

-def draw_text(text, color, surface, x, y,size): standard function to draw text in pygames

-def menu(): function to create a simple menu

-def game(): function that runs the game

-def circle(): function that draws the physical playing field including the grid

-def check_game_end(): function that checks if there are 4 discs vertically, horizontally or diagonally

-def animation(disc_number, mouse_pos_x = 0): function that checks the current mouseposition and drops the discs in the corresponding column

-def draw(position, disc_number,col): function that dynamically draws the dropped discs

-def possible_moves_func(): function that checks all possible moves

-def scoring(board_copy):function that evaluates and scores the current position

-def AI_opponent(board_copy, depth,alpha, beta, maximizingPlayer): function that creates our AI to play against

-def player_win(board):function that checks if the player has  4 discs vertically, horizontally or diagonally

-def opponent_win(board):function that checks if the opponent has  4 discs vertically, horizontally or diagonally


 

**Sources**:

https://pastebin.com/XDQyDZUd

https://en.wikipedia.org/wiki/Minimax#Pseudocode

https://github.com/KeithGalli/Connect4-Python/blob/master/connect4_with_ai.py
