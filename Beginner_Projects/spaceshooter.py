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

Disclaimer: The sound effects and music are not mine, I optain them from (Pixabay.com) all the credit goes to the authors that created them.  
"""

pygame.init() 
pygame.mixer.init()

class Ship:
    def __init__(self, x, y, health):
        self.x = x
        self.y = y
        self.health = health
        self.ship_image = None

    def draw(self, screen):
        screen.blit(self.ship_image, (self.x, self.y))
     
GREEN_SPACE_SHIP = pygame.transform.scale(pygame.image.load(os.path.join("beginner_projects", "spaceshooter_assets", "player.png")), (80,80))
class Player(Ship):
    def __init__(self, x, y, health):
        super().__init__(x, y, health)
        self.ship_image = GREEN_SPACE_SHIP
        self.mask = pygame.mask.from_surface(self.ship_image)
        self.max_health = health
        self.lasers = []
        self.rect = self.ship_image.get_rect(topleft=(x, y))

PLAYER_LASER = pygame.transform.scale(pygame.image.load(os.path.join("beginner_projects", "spaceshooter_assets", "laser.png")), (20,20))
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
    
BOSS_SPACE_SHIP = pygame.transform.scale(pygame.image.load(os.path.join("beginner_projects", "spaceshooter_assets", "boss_enemy.png")), (200, 200)) 
TANK_SPACE_SHIP = pygame.transform.scale(pygame.image.load(os.path.join("beginner_projects", "spaceshooter_assets", "tank_enemy.png")), (110,110)) 
NORMAL_SPACE_SHIP = pygame.transform.scale(pygame.image.load(os.path.join("beginner_projects", "spaceshooter_assets", "normal_enemy.png")), (70,70)) 
FAST_SPACE_SHIP = pygame.transform.scale(pygame.image.load(os.path.join("beginner_projects", "spaceshooter_assets", "fast_enemy.png")), (40,40))   
class Enemy(Ship):
    ENEMY_TYPES = {
        "boss": BOSS_SPACE_SHIP,
        "tank": TANK_SPACE_SHIP,
        "normal": NORMAL_SPACE_SHIP,
        "fast": FAST_SPACE_SHIP
    }

    ENEMY_SPEEDS = {
        "boss": 0.4,
        "tank": 1,    
        "normal": 1.2,
        "fast": 1.5
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

    LASER_SOUND_FILE = "beginner_projects/spaceshooter_assets/laser_sound.mp3"
    BOSS_BATTLE_SOUND_FILE = "beginner_projects/spaceshooter_assets/boss_sound.mp3"
    BACKGROUND_SOUND_FILE = "beginner_projects/spaceshooter_assets/background_sound.mp3"
    BOSS_SPAWN_SOUND_FILE = "beginner_projects/spaceshooter_assets/boss-spawn_sound.mp3" 
    GAME_WON_SOUND = "beginner_projects/spaceshooter_assets/game-won_sound.mp3"
    GAME_LOST_SOUND = "beginner_projects/spaceshooter_assets/game-over_sound.mp3"

    def play_sound(sound_file, volume=1.0):
        sound = pygame.mixer.Sound(sound_file)
        sound.set_volume(volume)
        sound.play()

    WIDTH, HEIGHT = 1000, 800
    FPS = 60
    wave = 0
    enemies = []
    player_velocity = 8
    player_size = 80
    score = 0

    main_font = pygame.font.SysFont("comicsans", 30)
    wave_font = pygame.font.SysFont("comicsans", 50)
    white_font_color = ((255,255,255))
    clock = pygame.time.Clock()

    # Player ship
    player_ship = Player(WIDTH / 2, HEIGHT - 60, 100)

    # Background Image
    pygame.display.set_caption("Space Invaders")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    image_path = os.path.join("beginner_projects", "spaceshooter_assets", "nightsky.png")
    BG_IMG = pygame.transform.scale(pygame.image.load(image_path), (WIDTH, HEIGHT))
    
    def redraw_window(screen, bg_img):
        screen.blit(bg_img, (0, 0))

        #Wave label fade after 3 seconds
        wave_label = wave_font.render(f"Wave {wave}", 1, white_font_color)
        current_time = pygame.time.get_ticks()
    
        if wave == 1 and (current_time - start_time <= 3000):
            screen.blit(wave_label, ((WIDTH - wave_label.get_width()) // 2, (HEIGHT - wave_label.get_height()) // 2))
        elif wave == 2 and (current_time - start_time <= 3000):
            screen.blit(wave_label, ((WIDTH - wave_label.get_width()) // 2, (HEIGHT - wave_label.get_height()) // 2))
        elif wave == 3 and (current_time - start_time <= 3000):
            screen.blit(wave_label, ((WIDTH - wave_label.get_width()) // 2, (HEIGHT - wave_label.get_height()) // 2))
        elif wave == 4 and (current_time - start_time <= 3000):
            screen.blit(wave_label, ((WIDTH - wave_label.get_width()) // 2, (HEIGHT - wave_label.get_height()) // 2))
        elif wave == 5 and (current_time - start_time <= 3000):
            screen.blit(wave_label, ((WIDTH - wave_label.get_width()) // 2, (HEIGHT - wave_label.get_height()) // 2))

        # Game screen info 
        health_label = main_font.render(f"Health: {player_ship.health}", 1, white_font_color)
        score_label = main_font.render(f"Score: {score}", 1, white_font_color)
        screen.blit(health_label, (10, 10))
        screen.blit(score_label, (WIDTH - score_label.get_width() - 10, 10))

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
                    player_ship.health -= 5
                    enemies.remove(enemy)

        # Player Win! Draw
        if (len(enemies) == 0 and wave >= 5) and player_ship.health > 0:
                win_label = main_font.render("YOU WIN!", 1, white_font_color)
                screen.blit(win_label, ((WIDTH - win_label.get_width()) // 2, (HEIGHT - win_label.get_height()) // 2))
        # Player Loss! Draw
        elif player_ship.health <= 0:
                lost_label = main_font.render("GAME OVER!", 1, white_font_color)
                screen.blit(lost_label, ((WIDTH - lost_label.get_width()) // 2, (HEIGHT - lost_label.get_height()) // 2)) 

        pygame.display.update()

    boss_spawned = False   
    running = True
    switch_music = True
    start_time = pygame.time.get_ticks()
    stop_sound = True
    while running:
        clock.tick(FPS)
        current_time = pygame.time.get_ticks()
        redraw_window(screen, BG_IMG)

        # Event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Player shoots a laser
                    play_sound(LASER_SOUND_FILE, 0.2)
                    player_laser = Laser(player_ship.x + player_ship.ship_image.get_width() // 2 - PLAYER_LASER.get_width() // 2, player_ship.y, PLAYER_LASER)
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
            start_time = current_time

            #Background music switch
            if wave <= 4 and switch_music:
                switch_music = False
                pygame.mixer.music.load(BACKGROUND_SOUND_FILE)
                pygame.mixer.music.set_volume(0.5)
                pygame.mixer.music.play(-1)
            elif wave >= 5:
                pygame.mixer.music.load(BOSS_BATTLE_SOUND_FILE)
                pygame.mixer.music.set_volume(0.5)
                pygame.mixer.music.play(-1)
                
            selectEnemy = ["tank", "normal", "fast"]
            for _ in range(wave * 8):
                enemy_type = random.choice(selectEnemy)
                if enemy_type == "tank":
                    enemy_health = 120
                elif enemy_type == "normal":
                    enemy_health = 80
                elif enemy_type == "fast":
                    enemy_health = 40

                enemy = Enemy(random.randint(50, WIDTH - 100), random.randint(-1500, -100), enemy_health, enemy_type)
                enemies.append(enemy)
        elif wave >= 5 and not boss_spawned and player_ship.health > 0:
            #Wave 5 boss
            play_sound(BOSS_SPAWN_SOUND_FILE, 1.0)
            enemy = Enemy(random.randint(50, WIDTH - 100), random.randint(-1500, -100), 4000, "boss")
            enemies.append(enemy)
            boss_spawned = True
            
        # Player Wins! Sound
        if (len(enemies) == 0 and wave >= 5) and (player_ship.health > 0) and stop_sound:
            pygame.mixer.music.stop()
            play_sound(GAME_WON_SOUND, 1.0)
            stop_sound = False
        # Player Loss! Sound
        elif player_ship.health <= 0 and stop_sound:
            pygame.mixer.music.stop()
            play_sound(GAME_LOST_SOUND, 1.0)
            stop_sound = False
                  
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