import pygame
import os
import sys 
import math
import random
"""

Idea: 
* Space shooter type game where you are a triangle, and move around shooting different shapes like circles, squares, and more that are chasing you.
* You will have to survive waves of enemies, once a wave is over a new one starts. The goal is to survive 5 waves of enemies to win.
* You will be able to buy upgrades between waves.

Steps to create game idea:
1. Game window - [Done] 
2. Make player character - [Done] 
3. Let the player move using WASD or Arrow keys - [Done]
4. Implement shooting mechanic - 
5. Implement max_health to player and enemy types - [Done]
6. Implement enemy and collision so that once an enemy is hit a certain amount of times they die.
7. Implement wave system - [Done]
8. Implement upgrade system

"""

pygame.init()

#Draw the player
def player():
    pygame.draw.polygon(screen, BASE_COLOR, 
        [(player_x, player_y),
        (player_x + PLAYER_SIZE, player_y),
        (player_x + PLAYER_SIZE // 2, player_y - PLAYER_SIZE)]
    )

#Tank type
def circle_enemy(enemy_x, enemy_y):
    pygame.draw.circle(screen, (255,140,100), (enemy_x, enemy_y), 30, 5)

#Normal type
def rect_enemy(enemy_x, enemy_y):
    pygame.draw.rect(screen, (255,100,255), (enemy_x, enemy_y, 30, 30), 5)

#Fast type
def line_enemy(enemy_x, enemy_y):
    pygame.draw.rect(screen, (25,25,25), (enemy_x, enemy_y, 10, 40))  

def gameover():
    lost_label = lost_font.render("GAME OVER", 1, BASE_COLOR)
    screen.blit(lost_label, ((WIDTH - lost_label.get_width()) // 2, (HEIGHT - lost_label.get_height()) // 2))
    pygame.display.flip()

def win():
    win_label = win_font.render("YOU WIN!", 1, BASE_COLOR)
    screen.blit(win_label, ((WIDTH - win_label.get_width()) // 2, (HEIGHT - win_label.get_height()) // 2))
    pygame.display.flip()

#Window
WIDTH, HEIGHT = 1000, 800
pygame.display.set_caption("Space Shooter")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND_IMG = pygame.transform.scale(pygame.image.load(os.path.join("Beginner_Projects", "assets", "nightsky.png")), (WIDTH, HEIGHT))

#Player Attributes
PLAYER_SIZE = 20
PLAYER_VELOCITY = 5
BASE_COLOR = ((255, 255, 255)) #White
PLAYER_PROJECTILE_COLOR = ((49, 136, 195)) #Blue
FPS = 60
max_health = 100
wave = 1

#Player position
player_x = (WIDTH - PLAYER_SIZE)//2
player_y = (HEIGHT - PLAYER_SIZE)//1

#Enemy Attributes
ENEMY_PLAYER_VELOCITY = {
    circle_enemy: 5,
    rect_enemy: 5,   
    line_enemy: 5
} 

def wave_spawner(wave):
    level = 5
    new_enemy_list = []
    for _ in range(wave * level):
        new_enemy_list.append([random.choice([circle_enemy, rect_enemy, line_enemy]), random.randint(50, WIDTH - 100), random.randint(-1500, -100)])
    return new_enemy_list

clock = pygame.time.Clock()
main_font = pygame.font.SysFont("comicsans", 30)
lost_font = pygame.font.SysFont("comicsans", 40)
win_font = pygame.font.SysFont("comicsans", 50)

running = True
enemy_list = wave_spawner(wave)
while running:
    clock.tick(FPS)
    screen.blit(BACKGROUND_IMG, (0, 0))

    #Screen info
    max_health_label = main_font.render(f"Health: {max_health}", 1, BASE_COLOR)
    wave_label = main_font.render(f"Wave: {wave}", 1, BASE_COLOR)
    screen.blit(max_health_label, (10,10))
    screen.blit(wave_label, (WIDTH - wave_label.get_width() - 10, 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    enemy_list = [enemy for enemy in enemy_list if enemy[2] <= HEIGHT]
    for enemy in enemy_list:
        """
        Enemy spawner: 
        enemy[0] is the function representing the enemy type.
        enemy[1] is the x-coordinate.
        enemy[2] is the y-coordinate.
        """
        enemy[2] += ENEMY_PLAYER_VELOCITY[enemy[0]]
        enemy_rect = pygame.Rect(enemy[1], enemy[2], 30, 30)
        enemy[0](enemy[1], enemy[2])

        #Check bottom collision
        if enemy_rect.bottom >= HEIGHT:
            max_health -= 1
            enemy_list.remove(enemy)

        if max_health <= 0:
            gameover()
            pygame.time.delay(4000) 
            pygame.quit()
            sys.exit()

        if len(enemy_list) == 0:
            if wave < 5:
                wave += 1
                enemy_list = wave_spawner(wave)
            else:
                win()
                pygame.time.delay(4000) 
                pygame.quit()
                sys.exit()

    #Check player collision and take away health
    player_rect = pygame.Rect(player_x, player_y, PLAYER_SIZE, PLAYER_SIZE)
    for enemy in enemy_list:
        enemy_rect = pygame.Rect(enemy[1], enemy[2], 30, 30)
        if player_rect.colliderect(enemy_rect):
            max_health -= 1

    """
    The if statements checks both the keys pressed and the player's position. 
    For example, it verifies whether a key is pressed and checks if the player is out of bounds before allowing movement. 
    This approach enables the creation of a border or play area since we don't want the player to go beyond the screen.

    Player controls: WASD or Arrow keys
    """
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and player_x - PLAYER_VELOCITY > 0:
        player_x -= PLAYER_VELOCITY
    if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and player_x + PLAYER_VELOCITY + PLAYER_SIZE < WIDTH:
        player_x += PLAYER_VELOCITY
    if (keys[pygame.K_w] or keys[pygame.K_UP]) and player_y - PLAYER_VELOCITY - PLAYER_SIZE > 0:
        player_y -= PLAYER_VELOCITY
    if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and player_y + PLAYER_VELOCITY + PLAYER_SIZE < HEIGHT:
        player_y += PLAYER_VELOCITY
            
    player()
    pygame.display.flip()

pygame.quit()