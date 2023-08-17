from pygame import mixer
import pygame.time
pygame.init()

# screen parameters
screen_width = 600
screen_height = 800

# define fonts
font_30 = pygame.font.SysFont('Constantia', 30)
font_40 = pygame.font.SysFont('Constantia', 40)

pygame.mixer.pre_init(44100, -16, 2, 512)  # don't know usage / meaning of this line
mixer.init()

# load sounds
explosion_fx = pygame.mixer.Sound("img/explosion.wav")
explosion_fx.set_volume(0.25)

explosion2_fx = pygame.mixer.Sound("img/explosion2.wav")
explosion2_fx.set_volume(0.25)

laser_fx = pygame.mixer.Sound("img/laser.wav")
laser_fx.set_volume(0.25)

# define game variables
rows = 5
cols = 5
bullet_cooldown = 1000  # bullet cool down in milliseconds
last_alien_shot = pygame.time.get_ticks()
countdown = 3
last_count = pygame.time.get_ticks()
game_over = 0  # 0 is no game over, 1 means player has won, -1 means player has lost

# define colours
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
