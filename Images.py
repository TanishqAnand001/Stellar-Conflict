import pygame
from Settings import bg_color

player_img = pygame.image.load("player.png")


player_bullet_img = pygame.image.load("player bullet.png")
player_bullet_img = pygame.transform.scale(player_bullet_img, (15, 15))

player_shield_img = pygame.image.load("player shield.png")
player_shield_img = pygame.transform.scale(player_shield_img, (64, 64))

enemy_bullet_img_m = pygame.image.load("enemy bullet m.png")

enemy_melee_img = pygame.image.load("enemy melee.png")


enemy_ranged_img = pygame.image.load("ranged enemy.png")
enemy_ranged_img = pygame.transform.scale(enemy_ranged_img, (48, 48))

enemy_melee_dash_img = pygame.image.load("enemy melee dash.png")
enemy_melee_dash_img = pygame.transform.scale(enemy_melee_dash_img, (48, 48))

explosion_img_list_enemy = []
explosion_img_list_player = []

star_image = pygame.image.load("star_tiny.png")
star_image = pygame.transform.scale(star_image, (16, 16))
star_image.set_colorkey(bg_color)
star_image_big = pygame.transform.scale(star_image, (32, 32))

for i in range(6):
    filename = "explosion0{}.png".format(i)
    img = pygame.image.load(filename)
    img = pygame.transform.scale(img, (48, 48))
    explosion_img_list_enemy.append(img)

for i in range(6):
    filename = "explosion0{}.png".format(i)
    img = pygame.image.load(filename)
    img = pygame.transform.scale(img, (240, 240))
    explosion_img_list_player.append(img)

powerup_shield_img = pygame.image.load("shield_gold.png")

powerup_bullet_img = pygame.image.load("bolt_gold.png")

boss_img = pygame.image.load("boss img.png")
