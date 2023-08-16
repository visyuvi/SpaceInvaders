import random

import pygame
from spaceship import Spaceship
from constants import *
from aliens import Aliens
from alien_bullets import AlienBullet
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
bullet_group = pygame.sprite.Group()
alien_group = pygame.sprite.Group()
alien_bullet_group = pygame.sprite.Group()


def create_aliens():
    # generate aliens
    for row in range(rows):
        for item in range(cols):
            alien = Aliens(100 + item * 100, 100 + row * 70)
            alien_group.add(alien)


# create aliens
create_aliens()

# create player
spaceship = Spaceship(int(screen_width / 2), screen_height - 100, 3)
spaceship_group.add(spaceship)

# game loop
run = True
while run:

    clock.tick(FPS)

    # draw background
    draw_bg()

    # create random alien bullets
    # record current time
    time_now = pygame.time.get_ticks()
    # shoot
    if time_now - last_alien_shot > bullet_cooldown and len(alien_bullet_group) < 5 and len(alien_group) > 0:
        attacking_alien = random.choice(alien_group.sprites())
        alien_bullet = AlienBullet(attacking_alien.rect.centerx, attacking_alien.rect.bottom)
        alien_bullet_group.add(alien_bullet)
        last_alien_shot = pygame.time.get_ticks()

    # event handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # update spaceship
    spaceship.update(screen, bullet_group)

    # update sprite groups
    bullet_group.update(alien_group)
    alien_group.update()
    alien_bullet_group.update(spaceship_group, spaceship)

    # draw sprite groups
    spaceship_group.draw(screen)
    bullet_group.draw(screen)
    alien_group.draw(screen)
    alien_bullet_group.draw(screen)

    # update display
    pygame.display.update()

pygame.quit()
