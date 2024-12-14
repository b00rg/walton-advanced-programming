import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
GRAVITY = 0.5
JUMP_STRENGTH = 10
PLAYER_SPEED = 5
BULLET_SPEED = 10
MAX_BULLETS = 3  # Max bullets per level

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
HEART_COLOR = (255, 20, 147)

# Setup the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Scrolling Platformer")

def start_screen():
    font = pygame.font.Font(None, 74)
    text = font.render("Press SPACE to Begin", True, BLACK)
    screen.fill(WHITE)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))


def pause_screen():
    font = pygame.font.Font(None, 74)
    text = font.render("Paused", True, BLACK)
    screen.fill(WHITE)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

    font = pygame.font.Font(None, 36)
    quit_text = font.render("Press Q to Quit", True, BLACK)
    screen.blit(quit_text, (WIDTH // 2 - quit_text.get_width() // 2, HEIGHT // 2 + 50))

def game_over():
    font = pygame.font.Font(None, 74)
    text = font.render("Game Over", True, BLACK)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

    font = pygame.font.Font(None, 36)
    restart_text = font.render("Press SPACE to Restart", True, BLACK)
    screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 50))






class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(topleft=(x, y))


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = random.choice([1, 2])  # Random enemy speed

    def update(self):
        self.rect.x -= self.speed  # Move left
        # Respawn if it goes off screen
        if self.rect.right < 0:
            self.rect.x = random.randint(WIDTH, WIDTH + 100)
            self.rect.y = HEIGHT - 100  # Reset to ground level

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 5))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.rect.x += BULLET_SPEED
        if self.rect.left > WIDTH:  # Remove bullet if it goes off screen
            self.kill()


# Function to draw hearts
def draw_health(health):
    for i in range(health):
        pygame.draw.rect(screen, HEART_COLOR, (10 + i * 40, 10, 30, 30))  # Draw hearts in the top left




class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # create a rectangle for the player similar to the enemy class, but using the BLUE hex code constant (see exercise1.py)
        self.velocity_y = 0
        self.on_ground = False
        self.health = # set how many lives you want your player to have 
        self.hit_timer = 0   # A timer to manage the cooldown after the player gets hit.
        self.bullets_fired = 0 # Count how many bullets the player has fired in the current level.
        self.last_shot_time = 0 # Record the time when the last bullet was shot to manage shooting cooldown.
        self.shoot_cooldown = 500  # Define the cooldown time for shooting bullets in milliseconds.

    def update(self):
        self.handle_input()
        # Call methods to apply gravity, and check if on ground here
       
        # Manage hit cooldown
        if self.hit_timer > 0:
            self.hit_timer -= 1  # Decrement the timer

    def handle_input(self):
        keys = pygame.key.get_pressed()
        current_time = pygame.time.get_ticks()

        # Movement controls (Arrow keys)
        if keys[pygame.K_LEFT]:  # Move left
            self.rect.x -= PLAYER_SPEED # decrement the playerspeed 
        if keys[pygame.K_RIGHT]:  # Move right
            # increment the PLAYER_SPEED
        if keys[pygame.K_UP]:  # Jump
            if self.on_ground:  # Ensure the player can only jump if on the ground
                self.velocity_y = -JUMP_STRENGTH # change the velocity in the y direction by the JUMP_STRENGTH constant
                # set on_ground to false 

        # Shooting mechanism with cooldown
        if keys[pygame.K_d] and self.bullets_fired < MAX_BULLETS: # if we have shot less than the max bullets 
            if current_time - self.last_shot_time > self.shoot_cooldown: # if we are out of the bullet cooldown period
                bullet = Bullet(self.rect.centerx, self.rect.top)
                all_sprites.add(bullet) # add bullet to all_sprites (list of all sprites)
                # add bullet to bullets() 
                # increment bullets_fired += 1  
                # set last_shot_time to current_time to measure cooldown 

    def apply_gravity(self):
       # velocity_y is incremented by the GRAVITY constant 
       # rect.y is incremented by velocity_y
       
    def check_ground(self):
        # Reset the player's position if they're on the ground
       # if the rect.bottom is greater than the height: 
       # the rect.bottom is reset to the HEIGHT, the velocity_y is reset to 0 
       # and on_ground is set to True 

        # Check for collision with platforms
        for platform in platforms:
            if self.rect.colliderect(platform.rect) and self.velocity_y >= 0:
               # rect.bottom is equal to platform.rect.top (the bottom of the rectangle is equal to the top of the platform 
                self.rect.bottom = platform.rect.top
               # set velocity_y to 0
               # set on_ground to True 
                break  # Only check against the first platform colliding with
               
# if you have finished this week's exercise, think about creating a new enemy that can attack the player in a different way
# again, you can add a different picture for the Player rect: # see https://www.geeksforgeeks.org/python-display-images-with-pygame/ and https://www.pygame.org/docs/ref/image.html#pygame.image.load
# you may use a tool like https://www.pixilart.com/draw to create your own artwork, if you would prefer

# here is another code to test your player code. Note that your platform & bullet classes must already work
# Groups

# Create sprite groups
all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

# Global variable for player
player = None

# Levels data
levels = [
    [(100, HEIGHT - 50, 400, 20), (600, HEIGHT - 150, 400, 20), (200, HEIGHT - 300, 600, 20)],  # Level 1 platforms
    [(100, HEIGHT - 50, 300, 20), (400, HEIGHT - 200, 300, 20), (300, HEIGHT - 350, 300, 20)],  # Level 2 platforms
    [(100, HEIGHT - 50, 200, 20), (500, HEIGHT - 250, 300, 20), (300, HEIGHT - 400, 300, 20)],  # Level 3 platforms
]

# Create enemies for each level
def create_enemies_for_level(level):
    enemies.empty()
    for _ in range(5):  # Increase the number of enemies
        enemy = Enemy(random.randint(WIDTH, WIDTH + 100), HEIGHT - 100)
        all_sprites.add(enemy)
        enemies.add(enemy)


# Global variable for current level
current_level = 0

# Function to reset the game
def reset_game():
    global player, current_level
    if player:  # Only create a new player if one does not already exist
        player.health = 3  # Reset health
        player.rect.topleft = (50, HEIGHT - 150)  # Reset position
        player.hit_timer = 0  # Reset hit timer
        player.bullets_fired = 0  # Reset bullet count
    else:
        player = Player()
        all_sprites.add(player)

    # Create platforms
    platforms.empty()
    for platform_data in levels[current_level]:
        platform = Platform(*platform_data)
        all_sprites.add(platform)
        platforms.add(platform)

    # Create enemies for the current level
    create_enemies_for_level(current_level)


# Start game with player
reset_game()

# Game loop
clock = pygame.time.Clock()
camera_x = 0  # Camera offset
running = True
game_active = False  # The game will start in an inactive state
paused = False  # To track if the game is paused
on_start_screen = True  # Start with the start screen

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if on_start_screen:  # If we're on the start screen, start the game
                    game_active = True
                    on_start_screen = False
                elif not game_active:  # Restart the game if it's over
                    game_active = True
                    current_level = 0
                    reset_game()
                else:  # Toggle pause
                    paused = not paused
            if event.key == pygame.K_q and paused:  # Press 'Q' to quit when paused
                running = False

    if on_start_screen:
        start_screen()

    elif game_active:
        if not paused:
            # Update game elements
            all_sprites.update()

            # Collision detection with enemies
            if pygame.sprite.spritecollide(player, enemies, False):
                if player.hit_timer == 0:  # Only lose a life if the hit timer is not active
                    player.health -= 1
                    player.hit_timer = 180  # Set cooldown for 3 seconds (180 frames)
                    if player.health <= 0:
                        game_active = False  # End the game if health is zero

            # Collision detection between bullets and enemies
            hits = pygame.sprite.groupcollide(bullets, enemies, True, True)
            for hit in hits:
                player.bullets_fired -= 1  # Decrement bullets fired on hit
                if not enemies:  # If all enemies are defeated, advance to the next level
                    current_level += 1
                    if current_level < len(levels):  # If there are more levels
                        reset_game()
                    else:  # If no more levels, end the game
                        game_active = False

            # Keep character within the screen
            if player.rect.x < 0:
                player.rect.x = 0
            elif player.rect.x > WIDTH - player.rect.width:
                player.rect.x = WIDTH - player.rect.width
            if player.rect.y > HEIGHT - player.rect.height:
                player.rect.y = HEIGHT - player.rect.height
                player.velocity_y = 0
                player.on_ground = True

            # Update camera offset to follow the player
            if player.rect.x > WIDTH // 2:  # If the player moves past the middle of the screen
                camera_x = player.rect.x - WIDTH // 2

            # Drawing
            screen.fill(WHITE)

            # Draw all sprites relative to the camera offset
            for sprite in all_sprites:
                screen.blit(sprite.image, sprite.rect.move(-camera_x, 0))

            # Draw health
            draw_health(player.health)

        else:  # If paused, show the pause screen
            pause_screen()

    else:
        # Display Game Over screen
        game_over()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
