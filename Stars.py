import pygame
import random
from Settings import *
from Images import star_image, star_image_big


class Stars(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = star_image
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(0, width)
        self.rect.centery = -self.rect.height
        self.speedx = 0
        self.speedy = 1
        self.last_spawn = pygame.time.get_ticks()
        self.spawn_delay = 100

    def update(self):
        self.rect.centery += self.speedy * dt

        if self.rect.centery > height:
            self.kill()

    def spawn(self, group):
        now = pygame.time.get_ticks()
        if now - self.last_spawn > self.spawn_delay:
            self.last_spawn = now
            star = Stars()
            group.add(star)


class BigStars(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = star_image_big
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(0, width)
        self.rect.centery = -self.rect.height
        self.speedx = 0
        self.speedy = 1/2
        self.last_spawn = pygame.time.get_ticks()
        self.spawn_delay = 1000

    def update(self):
        self.rect.centery += self.speedy * dt

        if self.rect.centery > height:
            self.kill()

    def spawn(self, group):
        now = pygame.time.get_ticks()
        if now - self.last_spawn > self.spawn_delay:
            self.last_spawn = now
            star = BigStars()
            group.add(star)
