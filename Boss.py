import pygame
from Images import boss_img
from Settings import dt, height, width


class Boss(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = boss_img
        self.rect = self.image.get_rect()
        self.rect.centerx = width // 2
        self.rect.centery = -self.rect.height
        self.speedy = 1
        self.speedx = 0
        self.count = 1
        self.hp = 1600
        self.is_alive = True

    def update(self):
        self.rect.centerx += self.speedx * dt
        self.rect.centery += self.speedy * dt

        if self.rect.centery >= height * 175 / 900:
            self.speedy = 0
            if self.count > 0:
                self.speedx = 1/2
            self.count -= 1

        if self.rect.x <= 0:
            self.speedx *= -1
        elif self.rect.x + self.rect.width >= width:
            self.speedx *= -1

    def get_hit(self):
        self.hp -= 1
        if self.hp <= 0:
            self.destroy()

    def destroy(self):
        self.is_alive = False
        self.kill()
