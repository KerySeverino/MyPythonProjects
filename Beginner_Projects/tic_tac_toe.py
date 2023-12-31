import pygame

"""
Steps needed to created the game:

1. Draw the canvas/screen
2. Create a Grid for the game
3. Create players
4. Check for action: Left click = O, Right click = X
5. Check if: Win, Lost, Tie
6. Check if player wants to: Play again
"""

pygame.init()

# Constants
HEIGHT, WIDTH = 600, 600
GRID_SIZE = 3
CELL_SIZE = WIDTH // GRID_SIZE

# Colors
BACKGROUND_COLOR = (255, 253, 208)
LINE_COLOR = (0, 0, 0)
HOVER_COLOR = (185, 177, 167)

# Display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")
quit = False #Pressing (red - X) on top-right of screen

# 0 = Empty, 1 = X / Left-click, 3 = O / Right-click
board = [[0, 0, 0], 
         [0, 0, 0], 
         [0, 0, 0]]  

# Font
font = pygame.font.SysFont(None, 100)
rules_font =  pygame.font.SysFont(None, 30)

def draw_grid():
    # Drawing horizontal Lines
    for i in range(1, GRID_SIZE):
        pygame.draw.line(screen, LINE_COLOR, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), 3)
    # Drawing vertical lines
    for i in range(1, GRID_SIZE):
        pygame.draw.line(screen, LINE_COLOR, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), 3)

def draw_player():
    for row in range(GRID_SIZE):
        for column in range(GRID_SIZE):
            if board[row][column] == 1:  # X / Left-click
                x_pos = column * CELL_SIZE + CELL_SIZE // 4
                y_pos = row * CELL_SIZE + CELL_SIZE // 4

                pygame.draw.line(screen, LINE_COLOR, (x_pos, y_pos), (x_pos + CELL_SIZE // 2, y_pos + CELL_SIZE // 2), 5)
                pygame.draw.line(screen, LINE_COLOR, (x_pos, y_pos + CELL_SIZE // 2), (x_pos + CELL_SIZE // 2, y_pos), 5)
            elif board[row][column] == 3:  # O / Right-click
                x_pos = column * CELL_SIZE + CELL_SIZE // 4
                y_pos = row * CELL_SIZE + CELL_SIZE // 4

                pygame.draw.circle(screen, LINE_COLOR, (x_pos + CELL_SIZE // 4, y_pos + CELL_SIZE // 4), CELL_SIZE // 4, 5)

def check_winner():
    for i in range(GRID_SIZE):
        """
        If:
        Checks if all elements in the current row are equal and not equal to 0. 
        If true, it means a player has won in that row.

        Elif:
        Checks if all elements in the current column are equal and not equal to 0. 
        If true, it means a player has won in that column.
        """
        if board[i][0] == board[i][1] == board[i][2] != 0:
            return board[i][0]  # Return the winning player
        elif board[0][i] == board[1][i] == board[2][i] != 0:
            return board[0][i]  # Return the winning player

    """
    If:
    Checks if all elements in the diagonal direction are equal and not equal to 0. 
    If true, it means a player has won diagonally from top-left to bottom-right.

    Elif:
    Checks if all elements in the other diagonal direction are equal and not equal to 0. 
    If true, it means a player has won diagonally from top-right to bottom-left.
    """
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return board[0][0]  # Return the winning player
    elif board[0][2] == board[1][1] == board[2][0] != 0:
        return board[0][2]  # Return the winning player

    return 0  # No winner yet

def check_tie():
    # Check if the board is full
    for row in range(GRID_SIZE):
        for column in range(GRID_SIZE):
            if board[row][column] == 0:
                return False  # There is an empty space, game is not a tie
    return True  # All spaces are filled, game is a tie

#Play again / Result Menu
def display_result(result):
    text = font.render(result, True, LINE_COLOR)
    screen.blit(text, (WIDTH // 4, HEIGHT // 3))

def display_playagain_text(text):
    text = font.render(text, True, LINE_COLOR)
    screen.blit(text, (WIDTH // 6, HEIGHT // 2))

def display_playagain_border(hover):
    pygame.draw.rect(screen, hover, pygame.Rect(WIDTH // 6, HEIGHT // 2, 390, 70))
    
def game_rules(text):
    text = rules_font.render(text, True, LINE_COLOR)
    screen.blit(text, (WIDTH // 8, HEIGHT // 6))
    
# Game loop
while not quit:
    screen.fill(BACKGROUND_COLOR)
    play_again_rect = pygame.Rect(WIDTH // 6, HEIGHT // 2, 390, 50)
    start_rect = pygame.Rect(WIDTH // 3, HEIGHT // 4, 180, 70)

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = pygame.mouse.get_pos()
            clicked_row = mouseY // CELL_SIZE
            clicked_col = mouseX // CELL_SIZE

            if event.button == 1 and board[clicked_row][clicked_col] == 0:  # Left click
                board[clicked_row][clicked_col] = 1
            elif event.button == 3 and board[clicked_row][clicked_col] == 0:  # Right click
                board[clicked_row][clicked_col] = 3

            #Result menu
            if check_winner() or check_tie():
                if event.button == 1 and play_again_rect.collidepoint(mouseX, mouseY):
                    board = [[0, 0, 0], 
                             [0, 0, 0], 
                             [0, 0, 0]]

    #Color changes when mouse is near it
    hover_color = HOVER_COLOR if play_again_rect.collidepoint(pygame.mouse.get_pos()) else BACKGROUND_COLOR
 
    screen.fill(BACKGROUND_COLOR)
    draw_grid()
    draw_player()
       
    # Check for game result
    if check_winner() == 1:
            screen.fill((BACKGROUND_COLOR))
            display_result("X wins !")
            display_playagain_border(hover_color)
            display_playagain_text("Play again?")
            game_rules("Rules: A line horizontally, vertically, or diagonally")
                
    elif check_winner() == 3:
            screen.fill((BACKGROUND_COLOR))
            display_result("O wins !")
            display_playagain_border(hover_color)
            display_playagain_text("Play again?")
            game_rules("Rules: A line horizontally, vertically, or diagonally")

    elif check_tie():
            screen.fill((BACKGROUND_COLOR))
            display_result("It's a tie!")
            display_playagain_border(hover_color)
            display_playagain_text("Play again?")
            game_rules("Rules: A line horizontally, vertically, or diagonally")

    # Update game state
    pygame.display.update()