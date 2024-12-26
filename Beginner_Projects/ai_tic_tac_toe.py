import pygame
import os

"""
Steps needed to created the game:

1. Draw the canvas/screen
2. Create player
3. Check for action: Left click = X, Ai = O
4. Check if: Win, Lost, Tie
5. Create intro screen - Play button to start game
6. Create lost screen - Check if player wants to Play again 
7. Crate AI player using minimax algorithm
8. Add sound
9. Extra: add difficulty, easy, medium, hard

"""

pygame.init()

def main():

    WIDTH, HEIGHT = 800, 800
    FPS = 60
    GRID_SIZE = 3
    CELL_SIZE = WIDTH // GRID_SIZE
    LINE_COLOR = (255, 215, 0)

    clock = pygame.time.Clock()

    pygame.display.set_caption("Tic-Tac-Toe")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    image_path = os.path.join("Beginner_Projects", "tictactoe_assets", "blackframe.jpg")
    BG_IMG = pygame.transform.scale(pygame.image.load(image_path), (WIDTH, HEIGHT))


    def draw_grid():
        # Drawing horizontal Lines
        for i in range(1, GRID_SIZE):
            pygame.draw.line(screen, LINE_COLOR, (90, i * CELL_SIZE), (710, i * CELL_SIZE), 3)
        # Drawing vertical lines
        for i in range(1, GRID_SIZE):
            pygame.draw.line(screen, LINE_COLOR, (i * CELL_SIZE, 90), (i * CELL_SIZE, 710), 3)

    def redraw_window(screen, bg_img):
        screen.blit(bg_img, (0, 0))
        draw_grid()

        pygame.display.update()


    running = True
    while running:
        clock.tick(FPS)
        redraw_window(screen, BG_IMG)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
    
main()