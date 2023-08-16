import pygame.sprite


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/bullet.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self, alien_group):
        self.rect.y -= 5
        if self.rect.bottom < 0:
            self.kill()
        if pygame.sprite.spritecollide(self, alien_group, True):
            self.kill()
