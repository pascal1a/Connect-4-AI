#import the required libraries and functions (pygame library used for the interface)
import pygame, sys
import time
import random
import math
from pygame.locals import * 

#starttime=time.time()

global discs
discs = []

#initialize the imported pygame modules
pygame.init()
#set the ingame clock
global clock
clock = pygame.time.Clock()

#define all used colors
global light_grey,black,bg_color,red,yellow
light_grey = (200,200,200)
black = (0,0,0)
bg_color = (200,200,200)
red = (255,0,0)
yellow = (255,255,0)

#define the screen settings
screen_width = 800
screen_height = 600
global screen
screen = pygame.display.set_mode((screen_width,screen_height))

#set the caption, the playfield and discspeed
pygame.display.set_caption('Connect 4')
field = pygame.Rect(0, 0, 1200,330)
field2 = pygame.Rect(0, 0, 1200,330)

disc_speed_y = 8

#set the font
font = pygame.font.SysFont(None, 60)


#standard function to draw text in pygames (Source: https://pastebin.com/XDQyDZUd)
def draw_text(text, color, surface, x, y,size):

    font = pygame.font.SysFont(None, size)

    textobj = font.render(text, 1, color)

    textrect = textobj.get_rect()

    textrect.topleft = (x, y)

    surface.blit(textobj, textrect)

#function to create a simple menu (Source: https://pastebin.com/XDQyDZUd)
def menu():
    
    while True:
        screen.fill((0,0,0))      
      
        #get the current mouse position (x and y-axis)
        mx, my = pygame.mouse.get_pos()
        #create the play button 
        button_1 = pygame.Rect(310, 300, 200, 50)
        
        #create the game menu text
        draw_text('PLAY', (255, 255, 255), screen, 310, 300,80)

        #draw_text('INSTRUCTIONS',  (255, 255, 255), screen, 190, 400,80)

        draw_text('MENU', (255, 255, 255), screen, 300, 200,80) 
        #set click to False (to check later if the button was clicked)
        click = False
        #define the ingame events quit and mouseclick
        for event in pygame.event.get():

            if event.type == QUIT:

                pygame.quit()

                sys.exit()

            if event.type == MOUSEBUTTONDOWN:

                if event.button == 1:

                    click = True
        #check the current mouse position and if the button Play was clicked, if yes start the game  
        if button_1.collidepoint((mx, my)):

            if click:
                #draw the board (6x7 matrix) that is later used for the calculations
                global col1,col2,col3,col4,col5,col6,col7   
                col1,col2,col3,col4,col5,col6,col7  = [],[],[],[],[],[],[]
                global board
                board = [col1, col2, col3, col4, col5, col6, col7]       
                game()
        #update the screen
        pygame.display.update()
        #set framerate to max 60 fps
        clock.tick(60)

#create the function that runs the game
def game():
    
    print("Click on the column to drop the disc!")  
    #create the 42 discs and store them in a list
    global list_with_discs
    list_with_discs = []
    for i in range(0,43):
        list_with_discs.append(pygame.Rect(800, 700 , 7, 94))
        i=i+1

 
    #f checks if a wrong column was selected by the player
    global f
    f=0
    #t tracks the current disc
    global t
    t=0
    
    #define the players  (1 means coputer move and 0 means our move)
    global player
    player = False

    while True:
        
        #if all discs are used and there is no winner: end the game and print draw
        if t==42:

            print("Draw")
            screen.fill((0,0,0))
            draw_text('DRAW!',  (255, 255, 255), screen, 320, 300,60)
            pygame.display.flip()
            time.sleep(4)
            break    

        clock.tick(90)

 
        #defines the ingame events
        for event in pygame.event.get():
            #exit game
            if event.type == pygame.QUIT:

                pygame.quit()

                sys.exit()
            #click on the column to drop the disc
            elif event.type == pygame.MOUSEBUTTONDOWN:

                

                animation(t)
                #if the wrong column is selected, repeat the turn
                if f == 1:
                    t += 0
                #next turn
                else:            
                    t +=1
                    player = False

 
            #turn of the AI
            elif t%2 == 0:    
                player=True
                col, value = AI_opponent(board, 4, -math.inf, math.inf,False)
                
                animation(t, mouse_pos_x=col)
                
                
                t=t+1
        
             
        #draw the backgorund and playing field
        screen.fill(bg_color)
        pygame.draw.rect(screen,light_grey,field)                       

 
        #creates the yellow and red discs
        for i in range(0,43):
            if i % 2 == 1:
                pygame.draw.circle(screen,red,(list_with_discs[i][0],list_with_discs[i][1]),44)  

            else:
                pygame.draw.circle(screen,yellow,(list_with_discs[i][0],list_with_discs[i][1]),44)            
            i=i+1 


        #draws the grid and playing field
        circle()
        #scatter()     
        
        #if the game is over show the corresponding winning or losing screen 
        if check_game_end() == True:

            if player== True:  

                print("You lost !")

                screen.fill((0,0,0))

                draw_text('YOU LOST!',  (255, 255, 255), screen, 320, 300,60)

                pygame.display.flip()

                time.sleep(4)

 

            elif player== False:

                print("You won !")

                screen.fill((0,0,0))

                draw_text('YOU WON!',  (255, 255, 255), screen, 320, 300,60)

                pygame.display.flip()

                time.sleep(4)

            break

            

        # Updating the window to show whos turn it is

        if player ==True:

            draw_text('YOUR TURN',  (255, 255, 255), screen, 320, 5,40)

        else:

            draw_text('CALCULATING',  (255, 255, 255), screen, 320, 5,40) 
        
        pygame.display.flip()

#draws the physical playing field including the grid
def circle():
    #creates the black surface
    s = pygame.Surface((1200,600), pygame.SRCALPHA)   
    s.fill((0,0,0,255))  
    #draws 6 x 7 circles to create the grid                    
    x=-60
    y=-28
    for _ in range(7):
        x=x+115
        y=-28
        for _ in range(6):         
            y=y+95
            pygame.draw.circle(s,(255,255,255,0),(x,y),30)                         
    #draws our surface to the screen at the position 0,0
    screen.blit(s, (0,0))

#function that checks if there are 4 discs vertically, horizontally or diagonally, if that is the case the function returns True and the game is over
#-1  in the matrix stands for our discs and 1 for the opponents discs
def check_game_end():
  

    for x in range(6):

        for y in range(7):

            try:

                if (board[y][x] == -1 and board[y][x+1] == -1 and board[y][x+2] == -1 and board[y][x+3] == -1) or (board[y][x] == 1 and board[y][x+1] == 1 and board[y][x+2] == 1 and board[y][x+3] == 1):

                    return True

            except IndexError:

                next

    for x in range(6):

        for y in range(7):

            try:

                if (board[y][x] == -1 and board[y+1][x] == -1 and board[y+2][x] == -1 and board[y+3][x] == -1) or (board[y][x] == 1 and board[y+1][x] == 1 and board[y+2][x] == 1 and board[y+3][x] == 1):

                    return True

            except IndexError:

                next

    for x in range(6):

        for y in range(7):

            try:

                if (board[y][x] == -1 and board[y+1][x+1] == -1 and board[y+2][x+2] == -1 and board[y+3][x+3] == -1) or (board[y][x] == 1 and board[y+1][x+1] == 1 and board[y+2][x+2] == 1 and board[y+3][x+3] == 1):

                    return True

            except IndexError:

                next

    for x in range(6):

        for y in range(7):

            try:

                if (board[y][x] == -1 and board[y-1][x+1] == -1 and board[y-2][x+2] == -1 and board[y-3][x+3] == -1) or (board[y][x] == 1 and board[y-1][x+1] == 1 and board[y-2][x+2] == 1 and board[y-3][x+3] == 1):

                    return True

            except IndexError:

                next  
#function that checks the current mouseposition and drops the dics in the corresponding column
def animation(disc_number, mouse_pos_x = 0):
    #f (failure) is set to 1 when a column that already contains 6 discs is clicked
    global f
    f = 0
    #checks if a cloumn was clicked
    global successful
    successful = False
    #if it is our turn get the current mouse position 
    if disc_number%2 == 1:
        mouse_pos_x=pygame.mouse.get_pos()
        mouse_pos_x= mouse_pos_x[0]
    else:
        pass
    #checks if the column contains less than 6 discs and dropps the disc in the corresponding column
    if mouse_pos_x <115 and len(col1) <6:

        draw(58,disc_number,col1)
        successful = True                          
          
    elif mouse_pos_x <230 and mouse_pos_x>115 and len(col2) <6:

        draw(173,disc_number,col2)
        successful = True
       
    elif mouse_pos_x <345 and mouse_pos_x>230 and len(col3) <6:

        draw(288,disc_number,col3)
        successful = True  

    elif mouse_pos_x <460 and mouse_pos_x>345 and len(col4) <6:

        draw(403,disc_number,col4)         
        successful = True

    elif mouse_pos_x <575 and mouse_pos_x>460 and len(col5) <6:

        draw(518,disc_number,col5)  
        successful = True

    elif mouse_pos_x <690 and mouse_pos_x>575 and len(col6) <6:

        draw(633,disc_number,col6)           
        successful = True

    elif mouse_pos_x <805 and mouse_pos_x>690 and len(col7) <6:

        draw(748,disc_number,col7)
        successful = True
    #sets the variable f (failure) to 1 if a column that already contains 6 discs was clicked
    else:
        f =1                 
        successful = True 

#function that dynamically draws  the dropped discs
def draw(position, disc_number,col):

    discs = list_with_discs[0:disc_number]
    #if a disc is dropped by the player a -1 is added to the board otherwise a 1 (used in other functions to check who won the game)
    if disc_number%2 == 1:    
        col.append(-1)
    else:
        col.append(1)
    #gets the current position form the disc
    list_with_discs[disc_number][0] = position
    #sets the y of the disc to zero as they are released from the top of the board
    list_with_discs[disc_number].y = 0 

    #while the disc has not reached the bottom
    while list_with_discs[disc_number].bottom < field.bottom+305:              
        #check for the first disc
        if disc_number >=1:
            #as long as the disc has not touched another disc y is increased 
            if  list_with_discs[disc_number].collidelist(discs) == -1:              
                pygame.draw.circle(screen,light_grey,(list_with_discs[disc_number][0],list_with_discs[disc_number][1]),50)    
                list_with_discs[disc_number].y += disc_speed_y

                #draws a red disc if its our turn and otherwise a yellow disc
                if disc_number % 2 ==1:              
                    pygame.draw.circle(screen,red,(list_with_discs[disc_number][0],list_with_discs[disc_number][1]),50) 
                    circle()
                else:
                    
                    pygame.draw.circle(screen,yellow,(list_with_discs[disc_number][0],list_with_discs[disc_number][1]),50) 
                    circle()                     
                pygame.display.flip()                                             
            #if the disc has touched another disc: break the loop and stop the disc at its current position
            else:
                
                list_with_discs[disc_number].y -= disc_speed_y                     
                break

        #for the first disc we only need to stop the drop when it reaches the bottom
        else:
            list_with_discs[disc_number][0] = position               
            pygame.draw.circle(screen,light_grey,(list_with_discs[disc_number][0],list_with_discs[disc_number][1]),50)    
            list_with_discs[disc_number].y += disc_speed_y
            pygame.draw.circle(screen,red,(list_with_discs[disc_number][0],list_with_discs[disc_number][1]) ,50)
            circle()
            pygame.display.flip()

#function that checks all possible moves and removes the moves that lead to a win for the player in the next move
def possible_moves_func():
    moves=[]
    for i in range(7):
        if len(board[i]) < 6:
            moves.append(i)
    
    for i in range(7):
        if len(moves) >1:
            if len(board[i]) < 6:
                board[i].append(1)
                board[i].append(-1)
                if player_win(board) == True:
                    del board[i][-1]
                    del board[i][-1]
                    moves.remove(i)               
                else:
                    del board[i][-1]
                    del board[i][-1]
            

    return moves

#function that evaluates and scores all simulated positions by the minimax function:
#Connect 3 (vertically, horizontally or diagonally): +5
#Middle column: +20
#Opponent connects 3: -10
#Connect 2 (vertically, horizontally or diagonally): +3
#Some combinations of Connect 3 with gaps in between: +5

def scoring(board_copy):
    scoring = 0
    try:
        for x in range(6):
            if (board_copy[3][x] ==1):
                scoring+=20
    except IndexError:
            next

    for x in range(6):
        for y in range(7):
            try:
                if (board[y][x] == 1 and board[y][x+1] == 1 and board[y][x+2] == 1):
                    scoring+=5
                if (board[y][x] == 1 and board[y+1][x] == 1 and board[y+2][x] == 1):
                    scoring+=5
                if (board[y][x] == 1 and board[y+1][x+1] == 1 and board[y+2][x+2] == 1):
                    scoring+=5   
                if (board[y][x] ==1 and board[y-1][x+1] ==1 and board[y-2][x+2] == 1):
                    scoring+=5
                if (board[y][x] == 1 and board[y][x+1] == 1  and board[y][x+3] == 1):
                    scoring+=5
                if (board[y][x] == 1 and board[y+1][x] == 1 and board[y+3][x] == 1):
                    scoring+=5
                if (board[y][x] == 1 and board[y+1][x+1] == 1  and board[y+3][x+3] == 1):
                    scoring+=5   
                if (board[y][x] ==1 and board[y-1][x+1] ==1  and board[y-3][x+3] == 1):
                    scoring+=5
                if (board[y][x] == 1  and board[y][x+2] == 1 and board[y][x+3] == 1):
                    scoring+=5
                if (board[y][x] == 1  and board[y+2][x] == 1 and board[y+3][x] == 1):
                    scoring+=5
                if (board[y][x] == 1  and board[y+2][x+2] ==1 and board[y+3][x+3] == 1):
                    scoring+=5    
                if (board[y][x] ==1  and board[y-2][x+2] == 1 and board[y-3][x+3] == 1):
                    scoring+=5
                if (board[y][x] == 1 and board[y][x+1] == 1):
                   scoring+=3
                if (board[y][x] == 1 and board[y+1][x] == 1):
                    scoring+=3
                if (board[y][x] == 1 and board[y+1][x+1] == 1):
                    scoring+=3
                if (board[y][x] ==1 and board[y-1][x+1] ==1):
                    scoring+=3
                if (board[y][x] == -1 and board[y][x+1] == -1 and board[y][x+2] == -1):
                    scoring-=10
                if (board[y][x] == -1 and board[y+1][x] == -1 and board[y+2][x] == -1):
                    scoring-=10
                if (board[y][x] == -1 and board[y+1][x+1] == -1 and board[y+2][x+2] == -1):
                    scoring-=10   
                if (board[y][x] ==-1 and board[y-1][x+1] ==-1 and board[y-2][x+2] == -1):
                    scoring-=10
            except IndexError:
                next
    
    return scoring




#function that creates our AI to play against
def AI_opponent(board, depth,alpha, beta, maximizingPlayer):
    #z is the x-axis value and refers to the column in which we drop the disc
    
    #Check1: Check whether we can connect 4 and drop the disc in that column (simulate our 7 possible moves and use the check_game_end function)
    z =100
    for i in range(7):
        if len(board[i]) < 6:
            board[i].append(1)
            if check_game_end() == True:
                del board[i][-1]          
                return z,0             
            else:
                del board[i][-1]
        z+=115 

    #Check2: Check whether the opponent can connect 4 and prevent that if possible (simulate the opponents 7 possible moves and use the check_game_end function)
    z =100
    for i in range(7):
        if len(board[i]) < 6:
            board[i].append(-1)
            if check_game_end() == True:
                del board[i][-1]
                return z,0               
            else:
                del board[i][-1]
        z+=115
        
  
    
    #implementation of the minimax algorithm acording to https://en.wikipedia.org/wiki/Minimax#Pseudocode and ps://github.com/KeithGalli/Connect4-Python/blob/master/connect4_with_ai.py
    columns_x_values =[100,200,300,400,500,600,700]
    possible_moves = possible_moves_func()
    if depth == 0 or check_game_end()==True: 
        if check_game_end()==True:
            if opponent_win(board)==True:
                return (None,10000000000)
            elif player_win(board) == True:
                return (None,-1000000)
            else:
                
                return (random.choice(possible_moves),0)
            #return (None,0)
        else:
            
            return (None,scoring(board))
            

    if maximizingPlayer==False:
        value = -math.inf
        column = random.choice(possible_moves)
        for col in possible_moves:
            board2 = board.copy()
            board2[col].append(1)
            new_score = AI_opponent(board2, depth-1,alpha, beta, True)[1]
            
            if new_score > value:
                value= new_score
                column=col
            del board2 [col][-1]
            alpha = max(alpha, value)
            if alpha >= beta:
                break
             
        return columns_x_values[column],value
    else:
        value = math.inf
        column = random.choice(possible_moves)
        for col in possible_moves:
            board2 = board.copy()
            board2[col].append(-1)
            new_score = AI_opponent(board2, depth-1,alpha,beta, False)[1]
            
            if new_score < value:
                value= new_score
                column=col
            del board2 [col][-1]
            beta = min(beta, value)
            if alpha >= beta:
                break 
            
        
        return columns_x_values[column],value
         

#function that checks if the player has  4 discs vertically, horizontally or diagonally; if that is the case the function returns True and the game is over
def opponent_win(board):

    for x in range(6):
        for y in range(7):
            try:
                if (board[y][x] == 1 and board[y][x+1] == 1 and board[y][x+2] == 1 and board[y][x+3] == 1):
                    return True

            except IndexError:
                next

    for x in range(6):
        for y in range(7):
            try:
                if (board[y][x] == 1 and board[y+1][x] == 1 and board[y+2][x] == 1 and board[y+3][x] == 1):
                    return True

            except IndexError:
                next

    for x in range(6):
        for y in range(7):
            try:
                if (board[y][x] == 1 and board[y+1][x+1] == 1 and board[y+2][x+2] == 1 and board[y+3][x+3] == 1):
                    return True

            except IndexError:
                next

    for x in range(6):

        for y in range(7):
            try:
                if (board[y][x] ==1 and board[y-1][x+1] ==1 and board[y-2][x+2] == 1 and board[y-3][x+3] == 1):
                    return True

            except IndexError:
                next

#function that checks if the opponent has  4 discs vertically, horizontally or diagonally; if that is the case the function returns True and the game is over
def player_win(board):

    for x in range(6):
        for y in range(7):
            try:
                if (board[y][x] == -1 and board[y][x+1] == -1 and board[y][x+2] == -1 and board[y][x+3] == -1):
                    return True
                    

            except IndexError:
                next

    for x in range(6):
        for y in range(7):
            try:
                if (board[y][x] == -1 and board[y+1][x] == -1 and board[y+2][x] == -1 and board[y+3][x] == -1):
                    return True
                    

            except IndexError:
                next

    for x in range(6):
        for y in range(7):
            try:
                if (board[y][x] == -1 and board[y+1][x+1] == -1 and board[y+2][x+2] == -1 and board[y+3][x+3] == -1):
                    return True
                    

            except IndexError:
                next

    for x in range(6):

        for y in range(7):
            try:
                if (board[y][x] ==-1 and board[y-1][x+1] ==-1 and board[y-2][x+2] == -1 and board[y-3][x+3] == -1):
                    return True
                    

            except IndexError:
                next



#runs the game by calling the menu function
menu()