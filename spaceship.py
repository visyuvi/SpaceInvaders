import pygame.sprite
from constants import *
from bullet import Bullet
from explosion import Explosion


class Spaceship(pygame.sprite.Sprite):
    def __init__(self, x, y, health):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/spaceship.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.health_start = health
        self.health_remaining = health
        self.last_shot = pygame.time.get_ticks()
        # update mask to ignore anything that is transparent
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, screen, bullet_group, explosion_group):
        # set movement speed
        speed = 8
        # set cooldown variable
        cooldown = 200  # in milliseconds
        gameover = 0
        # get key press
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= speed
        if key[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += speed

        # record current time
        time_now = pygame.time.get_ticks()
        # shoot
        if key[pygame.K_SPACE] and time_now - self.last_shot > cooldown:
            laser_fx.play( )
            bullet = Bullet(self.rect.centerx, self.rect.top)
            bullet_group.add(bullet)
            self.last_shot = pygame.time.get_ticks()

        # draw health bar
        pygame.draw.rect(screen, red, (self.rect.x, (self.rect.bottom + 10), self.rect.width, 15))
        if self.health_remaining > 0:
            pygame.draw.rect(screen, green,
                             (self.rect.x, (self.rect.bottom + 10),
                              self.rect.width * self.health_remaining / self.health_start, 15))
        elif self.health_remaining <= 0:
            explosion = Explosion(self.rect.centerx, self.rect.centery, 3)
            explosion_group.add(explosion)
            gameover = -1
            self.kill()
            return gameover

        return gameover
