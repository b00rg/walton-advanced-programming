import pygame
import sys
import random
pygame.init()
WIDTH, HEIGHT = 800, 600
FPS = 60 
GRAVITY = 0.5
JUMP_STRENGTH = 10
PLAYER_SPEED = 5
BULLET_SPEED = 10
MAX_BULLETS = 3  
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
HEART_COLOR = (255, 20, 147)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Scrolling Platformer")
reset_game()
clock = pygame.time.Clock()
camera_x = 0  
running = True
game_active = False  
paused = False  
on_start_screen = True  

def start_screen(): # see exercise 1

def pause_screen(): # see exercise 1

def game_over(): # see exercise 1

def draw_health(health): # see exercise 1
   
class Enemy(pygame.sprite.Sprite): # see exercise 1
    def __init__(self, x, y):
    def update(self):

class Platform(pygame.sprite.Sprite): # looking at the enemy sprite from exercise 1, try and create a platform given a width and height 
    def __init__(self, x, y, width, height): # use Surface, fill, and get_rect. You can colour this using the GREEN constant
        super().__init__()

class Bullet(pygame.sprite.Sprite): # again, looking at the enemy sprite from exercise 2, try and create a bullet sprite given an x and y
    def __init__(self, x, y): # use Surface, fill, and get_rect. You can colour this using the BLACK constant
        super().__init__()

    def update(self): # have the self.rext.x be increased by the constant BULLET_SPEED
        self.rect.x += BULLET_SPEED
       # If self.rect.left is greater than the WIDTH constant : 
            self.kill() # remove the bullet 
      
# if you have finished this week's exercise, try and figure out how to get images for the bullets and platforms instead of rectangles
# see https://www.pygame.org/docs/ref/image.html#pygame.image.load
# think about adding zapping noises for the bullets: see https://www.pygame.org/docs/ref/mixer.html and https://pythonprogramming.net/adding-sounds-music-pygame/
# code below tests the platform and enemy code. think about how you can test the bullet code. 
# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Test")

# Create sprite groups
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()


# Create enemies
for _ in range(5):
    enemy = Enemy(random.randint(WIDTH, WIDTH + 100), HEIGHT - 100)
    all_sprites.add(enemy,)
    enemies.add(enemy)

# Create platform
platform = Platform(100, HEIGHT - 50, 600, 20)
all_sprites.add(platform)


# Main game loop
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 
    all_sprites.update()

    # Fill the screen with white
    screen.fill(WHITE)
    
    # Draw all sprites
    all_sprites.draw(screen)

    # Refresh the display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
