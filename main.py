import pygame
from spaceship import Spaceship
from constants import *

# define fps
clock = pygame.time.Clock()
FPS = 60

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invaders")

# load image
bg = pygame.image.load("img/bg.png").convert_alpha()


def draw_bg():
    screen.blit(bg, (0, 0))


# create sprite groups
spaceship_group = pygame.sprite.Group()


# create player
spaceship = Spaceship(int(screen_width/2), screen_height - 100, 3)
spaceship_group.add(spaceship)


# game loop
run = True
while run:

    clock.tick(FPS)

    # draw background
    draw_bg()

    # event handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # update spaceship
    spaceship_group.update(screen)

    # update sprite groups
    spaceship_group.draw(screen)

    # update display
    pygame.display.update()

pygame.quit()
