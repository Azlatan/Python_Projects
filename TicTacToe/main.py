import pygame
import sys  
# NUMPY WILL HELP US CREATE ARE BOARD 
import numpy as np
 



# FUNCTION THAT DRAWS THE LINES ON THE SCREEN 
def draw_lines(): 
    # 1 HORIZONTAL LINE 
    pygame.draw.line(screen, LINES_COLOR, (0, 200), (600, 200), LINES_WIDTH)
    # 2 HORIZONTAL LINE 
    pygame.draw.line(screen, LINES_COLOR, (0, 400), (600, 400), LINES_WIDTH)
    # 1 VERTICAL LINE 
    pygame.draw.line(screen, LINES_COLOR, (200, 0), (200, 600), LINES_WIDTH)
    # 2 VERTICAL LINE 
    pygame.draw.line(screen, LINES_COLOR, (400, 0), (400, 600), LINES_WIDTH)

# FUNCTION THAT DRAWS THE SYMBOLS ON THE SCREEN WHEN I'TS CLICKED 
def draw_figures(): 
    for row in range(BOARD_ROWS): 
        for col in range(BOARD_COLUMS): 
            if board[row][col] == 1: 
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * 200 + 100), int(row * 200 + 100)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2: 
                pygame.draw.line(screen, CROSS_COLOR, (col * 200 + SPACE, row * 200 + 200 - SPACE), (col * 200 + 200 - SPACE, row * 200 + SPACE ), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * 200 + SPACE, row * 200 + SPACE), (col * 200 + 200 - SPACE, row * 200 + 200 - SPACE), CROSS_WIDTH)

# FUNCTION THAT MARKS ON THE SQUARES 
def mark_square(row, col, player): 
    board[row][col] = player

# FUNCTION THAT CHECKS IF A SQUARE ON THEE BOARD IS AVAILABLE 
def available_squares(row, col): 
    if board[row][col] == 0: 
        return True 
    else: 
        return False 

# FUNCTION THAT CHECKS IF THE BOARD IS FULL 
def is_board_full(): 
    for row in range(BOARD_ROWS): 
        for col in range(BOARD_COLUMS): 
            if board[row][col] == 0: 
                return False 
    return True 

def check_win(player): 
    # Vertical win check 
    for col in range(BOARD_COLUMS): 
        if board[0][col] == player and board[1][col] == player and board[2][col] == player: 
            draw_vertical_winning_line(col, player)
            return True 

    # Horizontal win check 
    for row in range(BOARD_ROWS): 
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row, player)
            return True 

    # asc diagonal win check 
    if board[2][0] == player and board[1][1] == player and board[0][2] == player: 
        draw_asc_diagonal(player)
        return True  
    
    # desc diagonal win check 
    if board[0][0] == player and board[1][1] == player and board[2][2] == player: 
        draw_desc_diagonal(player)
        return True  
    return False

def draw_vertical_winning_line(col, player): 
    posX = col * 200 + 100 
    if player == 1: 
        color = CIRCLE_COLOR
    elif player == 2: 
        color = CROSS_COLOR
    pygame.draw.line(screen, color, (posX, 15), (posX, HEIGHT - 15), 15)

def draw_horizontal_winning_line(row, player):
    posY = row * 200 + 100 
    if player == 1: 
        color = CIRCLE_COLOR
    elif player == 2: 
        color = CROSS_COLOR
    pygame.draw.line(screen, color, (15, posY), (WIDTH - 15, posY), 15)

def draw_asc_diagonal(player): 
    if player == 1: 
        color = CIRCLE_COLOR
    elif player == 2: 
        color = CROSS_COLOR
    pygame.draw.line(screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), 15)

def draw_desc_diagonal(player): 
    if player == 1: 
        color = CIRCLE_COLOR
    elif player == 2: 
        color = CROSS_COLOR
    pygame.draw.line(screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), 15) 

def restart(): 
    pass

# ALWAYS USED ON PYGAME 
pygame.init() 

WIDTH = 600 
HEIGHT = 600 
CIRCLE_RADIUS = 60 
CIRCLE_WIDTH = 15
CIRCLE_COLOR = (239, 231, 200) 
CROSS_WIDTH = 25 
SPACE = 55 
CROSS_COLOR = (66, 66, 66)
# RGB COLORS CREATION 
RED = (255, 0, 0)
# BACKGROUND COLOR THAT WE USED 
BG_COLOR = (28, 170, 156)
# LINES COLOR 
LINES_COLOR = (23, 145, 135)
# LINES WIDTH 
LINES_WIDTH = 15 

# BOARD ROWS AN COLUMNS 
BOARD_ROWS = 3
BOARD_COLUMS = 3 

screen = pygame.display.set_mode( (WIDTH, HEIGHT) ) 

# title for the game 
pygame.display.set_caption('TIC TAC TOE')

# Color To screen 
screen.fill(BG_COLOR)

# BOARD CREATION 
board = np.zeros( (BOARD_ROWS, BOARD_COLUMS) )


# CALLING FUNCTION FOR DRAW LINES 
draw_lines() 

player = 1 

# Main loop its same in all pygame projects keep window open 
while True: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            sys.exit() 
        # Checks if we clicking the screen 
        if event.type == pygame.MOUSEBUTTONDOWN: 

            mouseX = event.pos[0] # x
            mouseY = event.pos[1] # y 

            clicked_row = int(mouseY // 200) # Rounds up the number becase it goes up to 600 
            clicked_col = int(mouseX // 200) # Rounds up the number becase it goes up to 600 


            # Calls the functuion available squares if you clicked 
            if available_squares(clicked_row, clicked_col): 
                # Checks if the player is equal to 1
                if player == 1: 
                    # Marks the square to 1
                    mark_square(clicked_row, clicked_col, 1)
                    check_win(player)    
                    player = 2
                    draw_figures()
                # Checks if the player is equal to 2 
                elif player == 2: 
                    # Marks the square to 2 
                    mark_square(clicked_row, clicked_col, 2)
                    check_win(player) 
                    draw_figures()
                    player = 1
                # Checks if the board is full and terminates the program 
                if is_board_full(): 
                    print('End of game')
                    sys.exit() 

    # It updates the screen so the color and images can be showned 
    pygame.display.update() 
