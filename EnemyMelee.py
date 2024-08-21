import random

import pygame

from Images import enemy_melee_img, enemy_melee_dash_img
from Settings import width, dt, height


class EnemyMelee(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy_melee_img
        self.rect = self.image.get_rect()
        self.rect.centery = -self.rect.height
        self.rect.centerx = random.randrange(self.rect.width, width - self.rect.width)
        self.speedx = 0
        self.speedy = 1 / 4
        self.last_spawn = pygame.time.get_ticks()
        self.spawn_delay = 4000
        self.hp = 3

    def update(self):
        self.rect.centerx += self.speedx * dt
        self.rect.centery += self.speedy * dt
        if self.rect.top > height:
            self.kill()

    def spawn(self, group1, group2):
        now = pygame.time.get_ticks()
        if now - self.last_spawn > self.spawn_delay:
            self.last_spawn = now
            enemy_melee = EnemyMelee()
            group1.add(enemy_melee)
            group2.add(enemy_melee)

    def get_hit(self):
        self.hp -= 1
        if self.hp <= 0:
            self.destroy()

    def destroy(self):
        self.kill()


class EnemyMeleeDash(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy_melee_dash_img
        self.rect = self.image.get_rect()
        self.rect.x = random.choice((-self.rect.width, width + self.rect.width))
        self.rect.y = random.randrange(0, height - self.rect.height * 3)
        self.speedy = 0
        self.speedx = 1
        self.hp = 20
        self.last_shot = pygame.time.get_ticks()
        self.spawn_delay = 5000
        self.last_spawn = pygame.time.get_ticks()

    def update(self):
        self.rect.x += self.speedx * dt
        self.rect.y += self.speedy * dt

        if self.rect.left <= 0:
            self.speedx *= -1.1
        elif self.rect.right >= width:
            self.speedx *= -1.1

        if self.rect.right > width:
            self.rect.right = width - self.rect.width
        if self.rect.left <= 0:
            self.rect.left = self.rect.width

        if self.rect.top > height:
            self.kill()

    def spawn(self, group1, group2):
        now = pygame.time.get_ticks()
        if now - self.last_spawn > self.spawn_delay:
            self.last_spawn = now
            enemy_ranged = EnemyMeleeDash()
            group1.add(enemy_ranged)
            group2.add(enemy_ranged)

    def get_hit(self):
        self.hp -= 1
        if self.hp <= 0:
            self.destroy()

    def destroy(self):
        self.kill()

    def left(self):
        self.speedx = -5

    def right(self):
        self.speedx = 5
