**Connect-4-AI**

**Description**

This program allows you to play a simple Connect-4 game against an AI in python. The AI is based on the minimax algorithm with a scoring system. A detailed explanation of the minimax alogrithm can be found here:  https://en.wikipedia.org/wiki/Minimax#Pseudocode. The AI with a depth of 4 calculates different possibilities of the next four moves in advance and tries to choose the best one.  The code consists of the following 12 functions:

-def draw_text(text, color, surface, x, y,size):

-def menu():

-def circle():

-def check_game_end():

-def animation(disc_number, mouse_pos_x = 0):

-def draw(position, disc_number,col):

-def possible_moves_func():

-def scoring(board_copy):

-def AI_opponent(board_copy, depth,alpha, beta, maximizingPlayer):

-def player_win(board):

-def opponent_win(board):




The A detailed description of the individual steps can be found as as comments in the code.

**Instructions**

The program can be  executed online or locally on python. For the online version use the following link:              .
To run it locally the following steps are required:

      1. Make sure the following packages are avaiable: time, math, random and sys
      
      2.Install the pygame package (pip install pygame)
      
      3.Download the file Connect4.py and execute it
      
  




![AI2](https://user-images.githubusercontent.com/66219569/102391818-82815f80-3fd6-11eb-8bbc-d8c75014f19e.jpg)

**Sources**:

https://pastebin.com/XDQyDZUd

https://en.wikipedia.org/wiki/Minimax#Pseudocode

https://github.com/KeithGalli/Connect4-Python/blob/master/connect4_with_ai.py
