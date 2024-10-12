import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60 # frame rate 
GRAVITY = 0.5
JUMP_STRENGTH = 10
PLAYER_SPEED = 5
BULLET_SPEED = 10
MAX_BULLETS = 3  # Max bullets per level

# Colors - in hex form 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
HEART_COLOR = (255, 20, 147)

# Setup the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Scrolling Platformer")

# Start game with player
reset_game()

# Game loop
clock = pygame.time.Clock()
camera_x = 0  # Camera offset
running = True
game_active = False  # The game will start in an inactive state
paused = False  # To track if the game is paused
on_start_screen = True  # Start with the start screen

def start_screen(): # use this sample here to figure out how to do the game over & pause screen 
    font = pygame.font.Font(None, 74)
    text = font.render("Press SPACE to Begin", True, BLACK)
    screen.fill(WHITE)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

def pause_screen():
    # add in a paused screen.blit here for paused 
    # have another screen.blit for quit 
    # feel free to customise this! :) 

def game_over():
    # game over screen.blit
    # restart by pressing space screen.blit

def draw_health(health):
    # a rectangle in pygame can be drawn like 
    # pygame.draw.rect(screen, HEART_COLOR, (10, 10, 30, 30))
    # create a function that draws heart-coloured boxes in the top left corner in the range of the input health
    # if you have time at the end, think about how you would use a heart image in the game instead of a rectangle: see https://www.pygame.org/docs/ref/image.html#pygame.image.load

pygame.quit()
