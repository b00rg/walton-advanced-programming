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
        super().__init__()
    def update(self):

class Platform(pygame.sprite.Sprite): # see exercise 2
    def __init__(self, x, y, width, height): 
        super().__init__()

class Bullet(pygame.sprite.Sprite): # see exercise 2
    def __init__(self, x, y): 
        super().__init__()
    def update(self): 
      

pygame.quit()
