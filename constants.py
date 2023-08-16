# screen parameters
import pygame.time

screen_width = 600
screen_height = 800

# define game variables
rows = 5
cols = 5
bullet_cooldown = 1000 # bullet cool down in milliseconds
last_alien_shot = pygame.time.get_ticks()

# define colours
red = (255, 0, 0)
green = (0, 255, 0)
