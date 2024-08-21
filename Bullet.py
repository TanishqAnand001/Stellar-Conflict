
import pygame
from Images import player_bullet_img, enemy_bullet_img_m
from Settings import dt


class PlayerBullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speedx, speedy):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_bullet_img
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speedx = speedx
        self.speedy = speedy

    def update(self):
        self.rect.centery -= self.speedy * dt
        self.rect.centerx -= self.speedx * dt

        if self.rect.centery < -50:
            self.kill()


class EnemyBulletM(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy_bullet_img_m
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speedx = 0
        self.speedy = 1.5

    def update(self):
        self.rect.centery += self.speedy * dt
        self.rect.centerx -= self.speedx * dt

        if self.rect.centery < 0:
            self.kill()


class EnemyBulletR(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy_bullet_img_m
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speedx = 1.5
        self.speedy = 1.5

    def update(self):
        self.rect.centery += self.speedy * dt
        self.rect.centerx -= self.speedx * dt

        if self.rect.centery < 0:
            self.kill()


class EnemyBulletL(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy_bullet_img_m
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speedx = -1.5
        self.speedy = 1.5

    def update(self):
        self.rect.centery += self.speedy * dt
        self.rect.centerx -= self.speedx * dt

        if self.rect.centery < 0:
            self.kill()
