import pygame
from Images import powerup_shield_img, powerup_bullet_img
from Settings import dt


class PowerupShield(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = powerup_shield_img
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speedy = 1 / 2

    def update(self):
        self.rect.centery += self.speedy * dt


class PowerupBullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = powerup_bullet_img
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speedy = 1 / 2

    def update(self):
        self.rect.centery += self.speedy * dt
