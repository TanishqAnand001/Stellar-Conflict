import pygame
from Images import enemy_ranged_img
import random
from Settings import width, height, dt
from Bullet import EnemyBulletM, EnemyBulletL, EnemyBulletR


class EnemyRanged(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy_ranged_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, width - self.rect.width)
        self.rect.y = -self.rect.height
        self.frame_length = 3
        self.speedy = 1
        self.speedx = 0
        self.hp = 1
        self.last_shot = pygame.time.get_ticks()
        self.states = {"FLY_DOWN": "FLY_DOWN",
                       "ATTACK": "ATTACK"}
        self.state = self.states["FLY_DOWN"]
        self.init_state = True
        self.shoot_delay = 1000
        self.spawn_delay = 4000
        self.last_spawn = pygame.time.get_ticks()
        self.last_shot = pygame.time.get_ticks()

    def update(self):
        if self.state == "FLY_DOWN":
            self.state_fly_down()
        elif self.state == "ATTACK":
            self.state_attack()
        self.rect.x += self.speedx * dt
        self.rect.y += self.speedy * dt
        if ((self.rect.top > height + 10) or (self.rect.right < -25) or
                (self.rect.left > width + 25)):
            self.kill()

    def spawn(self, group1, group2):
        now = pygame.time.get_ticks()
        if now - self.last_spawn > self.spawn_delay:
            self.last_spawn = now
            enemy_ranged = EnemyRanged()
            group1.add(enemy_ranged)
            group2.add(enemy_ranged)

    def get_hit(self):
        self.hp -= 1
        if self.hp <= 0:
            self.destroy()

    def destroy(self):
        self.kill()

    def shoot(self, group1, group2, group3):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            for enemy in group3:
                enemy_bullet1 = EnemyBulletM(enemy.rect.centerx, enemy.rect.bottom)
                group1.add(enemy_bullet1)
                group2.add(enemy_bullet1)

                enemy_bullet1 = EnemyBulletL(enemy.rect.centerx, enemy.rect.bottom)
                group1.add(enemy_bullet1)
                group2.add(enemy_bullet1)

                enemy_bullet1 = EnemyBulletR(enemy.rect.centerx, enemy.rect.bottom)
                group1.add(enemy_bullet1)
                group2.add(enemy_bullet1)

    def state_fly_down(self):
        if self.init_state:
            self.init_state = False
        if self.rect.y >= width / 32:
            self.state = self.states["ATTACK"]
            self.init_state = True

    def state_attack(self):
        if self.init_state:
            self.speedy = 0
            while self.speedx == 0:
                self.speedx = random.choice((0.25, -0.25))
            self.init_state = False
        if self.rect.x <= 0:
            self.speedx *= -1
        elif self.rect.x + self.rect.width >= width:
            self.speedx *= -1
