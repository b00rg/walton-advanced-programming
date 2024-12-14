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
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
platforms = pygame.sprite.Group()

# Create player
player = Player()
all_sprites.add(player)

# Create platforms for testing
platform1 = Platform(100, HEIGHT - 50, 400, 20)
platforms.add(platform1)
all_sprites.add(platform1)

platform2 = Platform(500, HEIGHT - 150, 200, 20)
platforms.add(platform2)
all_sprites.add(platform2)


# Main test loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update all sprites
    all_sprites.update()

    # Draw everything
    screen.fill(WHITE)
    all_sprites.draw(screen)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
