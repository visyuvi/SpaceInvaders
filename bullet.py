import pygame.sprite
from explosion import Explosion
from constants import *


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/bullet.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self, alien_group, explosion_group):
        self.rect.y -= 5
        if self.rect.bottom < 0:
            self.kill()
        if pygame.sprite.spritecollide(self, alien_group, True):
            self.kill()
            explosion_fx.play()
            explosion = Explosion(self.rect.centerx, self.rect.centery, 2)
            explosion_group.add(explosion)

