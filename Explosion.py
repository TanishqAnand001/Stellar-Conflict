import pygame
from Images import explosion_img_list_enemy, explosion_img_list_player


class EnemyExplosion(pygame.sprite.Sprite):
    def __init__(self, centerx, centery):
        pygame.sprite.Sprite.__init__(self)
        self.sprite_shield = explosion_img_list_enemy
        self.current_sprite = 0
        self.image = self.sprite_shield[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.rect.centery = centery

    def update(self):
        self.current_sprite += 1 / 6
        if self.current_sprite >= len(self.sprite_shield):
            self.kill()
        self.image = self.sprite_shield[int(self.current_sprite) - 1]


class PlayerExplosion(pygame.sprite.Sprite):
    def __init__(self, centerx, centery):
        pygame.sprite.Sprite.__init__(self)
        self.sprite_shield = explosion_img_list_player
        self.current_sprite = 0
        self.image = self.sprite_shield[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.rect.centery = centery

    def update(self):
        self.current_sprite += 1 / 6
        if self.current_sprite >= len(self.sprite_shield):
            self.kill()
        self.image = self.sprite_shield[int(self.current_sprite) - 1]
