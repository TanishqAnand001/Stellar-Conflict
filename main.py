import pygame.sprite

from EnemyMelee import EnemyMelee, EnemyMeleeDash
from EnemyRanged import EnemyRanged
from Explosion import EnemyExplosion, PlayerExplosion
from Functions import *
from Images import *
from Player import Player
from Powerups import PowerupShield, PowerupBullet
from Stars import Stars, BigStars
from Boss import Boss

# Initializing Pygame
pygame.init()

# Defining Display
display = pygame.display.set_mode(display_dimensions)
pygame.display.set_caption("Stellar COnflict")
pygame.display.set_icon(player_img)

# Defining Clock
clock = pygame.time.Clock()

# Defining Loop Variables
running = True

# Defining Objects
player = Player()
stars = Stars()
stars2 = BigStars()
enemy_melee = EnemyMelee()
enemy_ranged = EnemyRanged()
enemy_melee_dash = EnemyMeleeDash()

# Defining Groups
player_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
player_bullet_group = pygame.sprite.Group()
enemy_bullet_group = pygame.sprite.Group()
enemy_melee_group = pygame.sprite.Group()
enemy_ranged_group = pygame.sprite.Group()
powerups_shield_group = pygame.sprite.Group()
powerups_bullet_group = pygame.sprite.Group()
boss_group = pygame.sprite.Group()

# Adding Objects To Groups
player_group.add(player)

# Defining Stuff
particles = []
powerups_list = [PowerupBullet, PowerupShield]
countdown_is = True
countdown = 5
countdown_timer = pygame.time.get_ticks()
game_over = True
pause = True
boss_count = 1


# Defining Function
def shop_menu(events1, screen, c, fps, player1):
    global coins
    star_group = pygame.sprite.Group()
    star = Stars()
    pause1 = True
    for event in events1:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:
                while pause1:
                    screen.fill((0, 0, 30))
                    star.spawn(star_group)
                    star_group.draw(screen)
                    star_group.update()
                    draw_text(
                        screen, "Shop", 240, width // 2, height // 2 * 100 / 900, white
                    )
                    draw_text(
                        screen,
                        "Coins:",
                        120,
                        width * 425 / 900,
                        height // 2 * 25 / 900,
                        white,
                    )
                    draw_text(
                        screen,
                        str(coins),
                        120,
                        width * 550 / 900,
                        height // 2 * 25 / 900,
                        white,
                    )
                    draw_text(
                        screen,
                        "Press M To Buy 1 Max Shield [50 Coins]",
                        64,
                        width // 2,
                        height // 2 * 400 / 900,
                        white,
                    )
                    pygame.display.update()
                    c.tick(fps)
                    for eve in pygame.event.get():
                        if eve.type == pygame.KEYDOWN:
                            if eve.key == pygame.K_ESCAPE:
                                pygame.quit()
                                quit()
                            if eve.key == pygame.K_t:
                                pause1 = False
                            if eve.key == pygame.K_m:
                                if coins >= 50:
                                    player1.max_shield += 105
                                    player1.shield += 105
                                    coins -= 50


# Defining Loops
while running:
    global coins
    if game_over:
        game_over_1(display, all_sprites, stars)
        score = 0
        coins = 0

    if game_over:
        timer(display, countdown, countdown_is, countdown_timer)

    # Defining Variables
    game_over = False
    restart = False

    # Updating Display
    clock.tick(FPS)
    pygame.display.update()
    pygame.mouse.set_visible(False)

    # Checking For Events
    events = pygame.event.get()
    check_quit_event(events)

    # Shop Menu
    shop_menu(events, display, clock, FPS, player)

    pause_game(events, display, clock, FPS)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        player.shoot(all_sprites, player_bullet_group)

    # Clearing Display
    display.fill(bg_color)

    # Checking Collisions
    hits1 = pygame.sprite.groupcollide(
        player_bullet_group, enemy_melee_group, True, False
    )
    for hit, enemy in hits1.items():

        chance = random.choice([1, 2])
        if chance == 1:
            spawn_powerup(PowerupShield, hit, all_sprites, powerups_shield_group)
        elif chance == 2:
            spawn_powerup(PowerupBullet, hit, all_sprites, powerups_bullet_group)
        score += 100
        coins += 2
        expl = EnemyExplosion(hit.rect.centerx, hit.rect.centery)
        all_sprites.add(expl)
        for enemy1 in enemy:
            enemy1.get_hit()

    hits2 = pygame.sprite.groupcollide(
        player_bullet_group, enemy_ranged_group, True, False
    )
    for hit, enemy in hits2.items():

        chance = random.choice([1, 2])
        if chance == 1:
            spawn_powerup(PowerupShield, hit, all_sprites, powerups_shield_group)
        elif chance == 2:
            spawn_powerup(PowerupBullet, hit, all_sprites, powerups_bullet_group)
        score += 100
        coins += 2
        expl = EnemyExplosion(hit.rect.centerx, hit.rect.centery)
        all_sprites.add(expl)
        for enemy1 in enemy:
            enemy1.get_hit()

    hits3 = pygame.sprite.groupcollide(player_group, enemy_melee_group, False, True)
    if hits3:
        player.get_hit()
        expl = PlayerExplosion(player.rect.centerx, player.rect.centery)
        all_sprites.add(expl)

    hits4 = pygame.sprite.groupcollide(player_group, enemy_bullet_group, False, True)
    if hits4:
        player.get_hit()
        expl = PlayerExplosion(player.rect.centerx, player.rect.centery)
        all_sprites.add(expl)

    hits5 = pygame.sprite.groupcollide(player_group, enemy_ranged_group, False, True)
    if hits5:
        player.get_hit()
        expl = PlayerExplosion(player.rect.centerx, player.rect.centery)
        all_sprites.add(expl)

    hits6 = pygame.sprite.groupcollide(player_group, powerups_shield_group, False, True)
    for hit in hits6:
        player.shield += 105
        if player.shield > player.max_shield:
            player.shield = player.max_shield

    hits7 = pygame.sprite.groupcollide(player_group, powerups_bullet_group, False, True)
    for hit in hits7:
        player.power += 1
        if player.power > player.max_power:
            player.power = player.max_power

    hit8 = pygame.sprite.groupcollide(player_bullet_group, boss_group, True, False)
    for hit in hit8:
        chance = random.choice([1, 2])
        if chance == 1:
            spawn_powerup(PowerupShield, hit, all_sprites, powerups_shield_group)
        elif chance == 2:
            spawn_powerup(PowerupBullet, hit, all_sprites, powerups_bullet_group)
        score += 100
        coins += 2
        expl = EnemyExplosion(hit.rect.centerx, hit.rect.centery)
        all_sprites.add(expl)
        for enemy1 in boss_group:
            enemy1.get_hit()
    hit9 = pygame.sprite.groupcollide(player_group, boss_group, False, False)
    if hit9:
        player.get_hit()
        expl = PlayerExplosion(player.rect.centerx, player.rect.centery)
        all_sprites.add(expl)

    # Displaying Groups
    all_sprites.draw(display)
    if player.is_alive:
        draw_flames(display, particles)
    player_group.draw(display)
    draw_shield(display, 0, height - height * 20 / 900, player.hp)
    draw_shield_color(
        display, 0, height - height * 40 / 900, player.shield, blue, player
    )

    # Drawing Text
    draw_text(display, str(score), 32, width // 2, height * 20 / 900, white)
    draw_text(display, str(coins), 32, width * 25 / 900, height * 20 / 900, white)
    draw_text(
        display,
        str(int(clock.get_fps())),
        32,
        width * 1568 / 1600,
        height * 20 / 900,
        white,
    )

    # Updating Groups
    all_sprites.update()
    player_group.update()

    # End Screen
    if not player.is_alive:
        end_screen(display)

    # Spawning Objects
    if player.shield > 0:
        blit_alpha(
            display,
            player_shield_img,
            (player.rect.centerx - 32, player.rect.centery - 32),
            100,
        )
    stars.spawn(all_sprites)
    stars2.spawn(all_sprites)
    enemy_melee.spawn(all_sprites, enemy_melee_group)
    enemy_ranged.spawn(all_sprites, enemy_ranged_group)
    enemy_melee_dash.spawn(all_sprites, enemy_melee_group)

    # Boss Spawning Stuff
    if boss_count > 0:
        boss = Boss()
        all_sprites.add(boss)
        boss_group.add(boss)
        boss_count = 0
    if boss.is_alive:
        draw_shield(display, 0, height * 1 / 900, boss.hp)

    # Shooting Objects
    enemy_ranged.shoot(all_sprites, enemy_bullet_group, enemy_ranged_group)

    # Level System
