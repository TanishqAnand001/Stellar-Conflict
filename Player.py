import pygame
from Images import player_img
from Settings import *
from Bullet import PlayerBullet


class Player(pygame.sprite.Sprite):
    def __init__(self):
        mx, my = pygame.mouse.get_pos()
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.centerx = mx
        self.rect.centery = my
        self.speedx = 0
        self.speedy = 0
        self.hp = 1600
        self.shield = 315
        self.max_shield = 315
        self.shoot_delay = 100
        self.last_shot = pygame.time.get_ticks()
        self.is_alive = True
        self.power = 1
        self.max_power = 5

    def update(self):
        mx, my = pygame.mouse.get_pos()
        self.rect.centerx = mx
        self.rect.centery = my

        if self.rect.right > width:
            self.rect.right = width
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > height - height * 40 / 900:
            self.rect.bottom = height - height * 40 / 900
        if self.rect.top < 0:
            self.rect.top = 0

    def shoot(self, group1, group2):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            if self.power == 1:
                player_bullet = PlayerBullet(self.rect.centerx, self.rect.centery, 0, 1.5)
                group1.add(player_bullet)
                group2.add(player_bullet)
            if self.power == 2:
                player_bullet1 = PlayerBullet(self.rect.centerx - 15, self.rect.centery, 0, 1.5)
                group1.add(player_bullet1)
                group2.add(player_bullet1)

                player_bullet2 = PlayerBullet(self.rect.centerx + 15, self.rect.centery, 0, 1.5)
                group1.add(player_bullet2)
                group2.add(player_bullet2)

            if self.power == 3:
                player_bullet1 = PlayerBullet(self.rect.left, self.rect.centery, 0, 1.5)
                group1.add(player_bullet1)
                group2.add(player_bullet1)

                player_bullet2 = PlayerBullet(self.rect.right, self.rect.centery, 0, 1.5)
                group1.add(player_bullet2)
                group2.add(player_bullet2)

                player_bullet3 = PlayerBullet(self.rect.centerx, self.rect.top, 0, 1.5)
                group1.add(player_bullet3)
                group2.add(player_bullet3)

            if self.power > 3:
                player_bullet1 = PlayerBullet(self.rect.left, self.rect.centery, 0, 1.5)
                group1.add(player_bullet1)
                group2.add(player_bullet1)

                self.shoot_delay = 1

    def get_hit(self):
        self.shield -= 105
        if self.shield < 0:
            self.shield = 0
            self.hp -= 105
        if self.hp <= 0:
            self.destroy()

    def destroy(self):
        self.is_alive = False
        self.kill()
