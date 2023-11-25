import pygame
import os
import sys 
import random
"""

Idea: 
* Space shooter type game where you are a triangle, and move around shooting different shapes like circles, squares, and more that are chasing you.
* You will have to survive waves of enemies, once a wave is over a new one starts. The goal is to survive 5 waves of enemies to win.
* You will be able to buy upgrades between waves.

Steps to create game idea:
1. Game window - [Done]
2. Make player character  - [Done]
3. Let the player move using WASD or Arrow keys - [Done]
4. Implement shooting mechanic  - [Done]
5. Implement max_health to player and enemy types - [Done]
6. Implement enemy and collision so that once an enemy is hit a certain amount of times they die  - [Done]
7. Implement wave system - [Done]

"""
pygame.init() 

class Ship:
    def __init__(self, x, y, health):
        self.x = x
        self.y = y
        self.health = health
        self.ship_image = None

    def draw(self, screen):
        screen.blit(self.ship_image, (self.x, self.y))
     
GREEN_SPACE_SHIP = pygame.transform.scale(pygame.image.load(os.path.join("Beginner_Projects", "assets", "player.png")), (80,80))
class Player(Ship):
    def __init__(self, x, y, health):
        super().__init__(x, y, health)
        self.ship_image = GREEN_SPACE_SHIP
        self.mask = pygame.mask.from_surface(self.ship_image)
        self.max_health = health
        self.lasers = []
        self.rect = self.ship_image.get_rect(topleft=(x, y))

PLAYER_LASER = pygame.transform.scale(pygame.image.load(os.path.join("Beginner_Projects", "assets", "laser.png")), (20,20))
class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)
        self.rect = self.img.get_rect(topleft=(self.x, self.y))

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))

    def move(self, y):
        self.y -= y
        self.rect.y = self.y

    def check_collision(self, enemies):
        for enemy in enemies:
            enemy_mask = pygame.mask.from_surface(enemy.ship_image)
            offset = (int(enemy.x - self.x), int(enemy.y - self.y))

            if self.mask.overlap(enemy_mask, offset):
                return enemy

        return None
    
BOSS_SPACE_SHIP = pygame.transform.scale(pygame.image.load(os.path.join("Beginner_Projects", "assets", "boss_enemy.png")), (200, 200)) 
TANK_SPACE_SHIP = pygame.transform.scale(pygame.image.load(os.path.join("Beginner_Projects", "assets", "tank_enemy.png")), (110,110)) 
NORMAL_SPACE_SHIP = pygame.transform.scale(pygame.image.load(os.path.join("Beginner_Projects", "assets", "normal_enemy.png")), (70,70)) 
FAST_SPACE_SHIP = pygame.transform.scale(pygame.image.load(os.path.join("Beginner_Projects", "assets", "fast_enemy.png")), (40,40))   
class Enemy(Ship):
    ENEMY_TYPES = {
        "boss": BOSS_SPACE_SHIP,
        "tank": TANK_SPACE_SHIP,
        "normal": NORMAL_SPACE_SHIP,
        "fast": FAST_SPACE_SHIP
    }

    ENEMY_SPEEDS = {
        "boss": 0.6,
        "tank": 1.6,    
        "normal": 1.8,
        "fast": 2
    }

    def __init__(self, x, y, health, enemy_type):
        super().__init__(x, y, health)
        self.ship_image = self.ENEMY_TYPES[enemy_type]
        self.mask = pygame.mask.from_surface(self.ship_image)
        self.rect = self.ship_image.get_rect(topleft=(self.x, self.y))
        self.speed = self.ENEMY_SPEEDS[enemy_type]

    def move(self):
        self.y += self.speed
        self.rect.y = self.y
    
    def take_damage(self, damage):
        self.health -= damage

    def is_dead(self):
        return self.health <= 0

def main():
    WIDTH, HEIGHT = 1000, 800
    FPS = 60
    wave = 0
    enemies = []
    player_velocity = 8
    player_size = 80
    score = 0

    main_font = pygame.font.SysFont("comicsans", 30)
    score_font = pygame.font.SysFont("comicsans", 15)
    white_font_color = ((255,255,255))
    clock = pygame.time.Clock()

    # Player ship
    player_ship = Player(WIDTH / 2, HEIGHT - 60, 100)

    # Background Image
    pygame.display.set_caption("Space Invaders")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    image_path = os.path.join("Beginner_Projects", "assets", "nightsky.png")
    BG_IMG = pygame.transform.scale(pygame.image.load(image_path), (WIDTH, HEIGHT))

    def redraw_window(screen, bg_img):
        screen.blit(bg_img, (0, 0))

        # Game screen info 
        health_label = main_font.render(f"Health: {player_ship.health}", 1, white_font_color)
        wave_label = main_font.render(f"Wave: {wave}", 1, white_font_color)
        screen.blit(health_label, (10, 10))
        screen.blit(wave_label, (WIDTH - wave_label.get_width() - 10, 10))

        # Player starting position
        player_ship.draw(screen)

        #Updated and draw lasers
        for laser in player_ship.lasers[:]:
            laser.draw(screen)
            laser.move(10) 

            #Remove lasers that hit the top of the screen
            if laser.y < 0:
                player_ship.lasers.remove(laser)

        # Update and draw enemies
        for enemy in enemies[:]:
            enemy.draw(screen)
            enemy.move()

            #Player loss - remove everything from the screen
            if player_ship.health <= 0:
                enemies.remove(enemy)

            #Remove enemies that hit the bottom of the screen and take away health
            if enemy.y > HEIGHT:
                if enemy.ship_image == BOSS_SPACE_SHIP:
                    player_ship.health = 0
                    enemies.remove(enemy)
                else:
                    player_ship.health -= 10
                    enemies.remove(enemy)

        # Player Wins!
        if (len(enemies) == 0 and wave >= 5) and player_ship.health > 0:
            win_label = main_font.render("YOU WIN!", 1, white_font_color)
            score_label = score_font.render(f"Score: {score}", 1, white_font_color)
            screen.blit(win_label, ((WIDTH - win_label.get_width()) / 2, (HEIGHT - win_label.get_height()) / 2))
            screen.blit(score_label, ((WIDTH - win_label.get_width()) / 2 + 30, (HEIGHT - win_label.get_height()) / 2 + 60 )) 
        # Player Loss!
        elif player_ship.health <= 0:
            lost_label = main_font.render("GAME OVER!", 1, white_font_color)
            score_label = score_font.render(f"Score: {score}", 1, white_font_color)
            screen.blit(lost_label, ((WIDTH - lost_label.get_width()) / 2, (HEIGHT - lost_label.get_height()) / 2)) 
            screen.blit(score_label, ((WIDTH - lost_label.get_width()) / 2 + 50, (HEIGHT - lost_label.get_height()) / 2 + 50 )) 
             
        pygame.display.update()

    boss_spawned = False
    running = True
    while running:
        clock.tick(FPS)
        redraw_window(screen, BG_IMG)

        # Event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Player shoots a laser
                    player_laser = Laser(player_ship.x + player_ship.ship_image.get_width() / 2 - PLAYER_LASER.get_width() / 2, player_ship.y, PLAYER_LASER)
                    player_ship.lasers.append(player_laser)
       
       # Check for collision with enemies
        for laser in player_ship.lasers[:]:
            hit_enemy = laser.check_collision(enemies)
            if hit_enemy:
                score += 10
                hit_enemy.take_damage(40)
                player_ship.lasers.remove(laser)
                if hit_enemy.is_dead():
                    enemies.remove(hit_enemy)

        # Enemy Spawner
        if (len(enemies) == 0 and wave < 5) and player_ship.health > 0:
            wave += 1

            selectEnemy = ["tank", "normal", "fast"]
            for _ in range(wave * 5): 
                enemy_type = random.choice(selectEnemy)
                if enemy_type == "tank":
                    enemy_health = 120
                elif enemy_type == "normal":
                    enemy_health = 80
                elif enemy_type == "fast":
                    enemy_health = 40

                enemy = Enemy(random.randint(50, WIDTH - 100), random.randint(-1500, -100), enemy_health, enemy_type)
                enemies.append(enemy)
        elif wave == 5 and not boss_spawned and player_ship.health > 0:
            #Wave 5 boss
            enemy = Enemy(random.randint(50, WIDTH - 100), random.randint(-1500, -100), 3500, "boss")
            enemies.append(enemy)
            boss_spawned = True
            
        """
        The if statements checks both the keys pressed and the player's position. 
        For example, it verifies whether a key is pressed and checks if the player is out of bounds before allowing movement. 
        This approach enables the creation of a border or play area since we don't want the player to go beyond the screen.

        Player controls: WASD or Arrow keys
        Having this in the while loop allows continuous movement while the key is pressed.
        """
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and player_ship.x - player_velocity > 0:
            player_ship.x -= player_velocity
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and player_ship.x + player_velocity + player_size < WIDTH:
            player_ship.x += player_velocity
        if (keys[pygame.K_w] or keys[pygame.K_UP]) and player_ship.y - player_velocity - player_size > 0:
            player_ship.y -= player_velocity
        if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and player_ship.y + player_velocity + player_size < HEIGHT:
            player_ship.y += player_velocity

    pygame.quit() 

# Runs main
main()