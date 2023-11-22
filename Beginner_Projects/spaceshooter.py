import pygame

"""

Idea: 
* Space shooter type game where you are a triangle, and move around shooting different shapes like circles, squares, and more that are chasing you.
* You will have to survive for a certain amount of time, once timer hits (00:00) a new wave starts. The goal is to survive 5 waves of enemies to win.
* You will be able to buy upgrades between waves.

Steps to create game idea:
1. Game window - Done
2. Make player character 
3. Let the player move using WASD or Arrow keys - Done 
4. Implement shooting mechanic
5. Implement health to player and enemy types
6. Implement enemy and collision so that once an enemy is hit a certain amount of times they die.
7. Implement timer and wave system
8. Implement upgrade system

"""

pygame.init()

HEIGHT, WIDTH = 800, 800 #Window
BACKGROUND_COLOR = ((0, 0, 0)) #Black
BASE_COLOR = ((255, 255, 255)) #White 
ENEMY_PROJECTILE_COLOR = ((255, 0, 0)) #Red

#Player position
player_x = (WIDTH)//2
player_y = (HEIGHT)//2
velocity = 3

# Key states
key_states = {
    #Arrow keys
    pygame.K_LEFT: False,
    pygame.K_RIGHT: False,
    pygame.K_UP: False,
    pygame.K_DOWN: False,

    #WASD
    pygame.K_a: False,
    pygame.K_d: False,
    pygame.K_w: False,
    pygame.K_s: False
}

pygame.display.set_caption("Space Shooter")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def player():
    pygame.draw.circle(screen, BASE_COLOR, (player_x, player_y), 20, width=0)   

running = True
while running:
    
    screen.fill((BACKGROUND_COLOR))
    keys = pygame.key.get_pressed()

    #Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False
        elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if event.key in key_states:
                key_states[event.key] = event.type == pygame.KEYDOWN

    #Keys being pressed
    player_x -= velocity * ((key_states[pygame.K_LEFT] or key_states[pygame.K_a]) and not (key_states[pygame.K_RIGHT] or key_states[pygame.K_d]))
    player_x += velocity * ((key_states[pygame.K_RIGHT] or key_states[pygame.K_d]) and not (key_states[pygame.K_LEFT] or key_states[pygame.K_a]))
    player_y -= velocity * ((key_states[pygame.K_UP] or key_states[pygame.K_w]) and not (key_states[pygame.K_DOWN] or key_states[pygame.K_s]))
    player_y += velocity * ((key_states[pygame.K_DOWN] or key_states[pygame.K_s]) and not (key_states[pygame.K_UP] or key_states[pygame.K_w]))
    
    player()
    pygame.display.update()
pygame.quit()