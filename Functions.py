import pygame
from pygame import BLEND_RGB_ADD
from Stars import Stars
from Settings import *
import random


def check_quit_event(events):
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quit()


def pause_game(events, screen, c, fps):
    star_group = pygame.sprite.Group()
    star = Stars()
    pause = True
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                while pause:
                    screen.fill((0, 0, 30))
                    star.spawn(star_group)
                    star_group.draw(screen)
                    star_group.update()
                    draw_text(screen, "Paused", 480, width // 2, height // 2 - height // 4, white)
                    pygame.display.update()
                    c.tick(fps)
                    for eve in pygame.event.get():
                        if eve.type == pygame.KEYDOWN:
                            if eve.key == pygame.K_ESCAPE:
                                pygame.quit()
                                quit()
                            if eve.key == pygame.K_p:
                                pause = False


def circle_surf(radius, color):
    surf = pygame.Surface((radius * 2, radius * 2))
    pygame.draw.circle(surf, color, (radius, radius), radius)
    surf.set_colorkey((0, 0, 0))
    return surf


def draw_flames(screen, particles):
    mx, my = pygame.mouse.get_pos()
    particles.append([[mx, my], [random.randint(0, 10) / 10 - 1, -10], random.randint(4, 5)])

    for particle in particles:
        particle[0][0] -= particle[1][0]
        particle[0][1] -= particle[1][1]
        particle[2] -= 0.2
        pygame.draw.circle(screen, random.choice(colors), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))

        radius = particle[2] * 2
        screen.blit(circle_surf(radius, random.choice(colors)),
                    (int(particle[0][0] - radius), int(particle[0][1] - radius)),
                    special_flags=BLEND_RGB_ADD)

        if particle[2] <= 0:
            particles.remove(particle)


def draw_text(surf, text, size, x, y, color):
    font = pygame.font.Font('visitor2.ttf', size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def draw_shield_color(surf, x, y, pct, color, player):
    length = width
    health_height = 20
    fill = (pct / player.max_shield) * length
    outline_rect = pygame.Rect(x, y, length, health_height)
    fill_Rect = pygame.Rect(x, y, fill, health_height)
    pygame.draw.rect(surf, color, fill_Rect)
    pygame.draw.rect(surf, white, outline_rect, 2)


def draw_shield(surf, x, y, pct):
    if pct < 0:
        pct = 0
    if 1065 <= pct <= 1600:
        color = green
    elif 530 <= pct <= 1065:
        color = yellow
    elif 0 <= pct <= 530:
        color = red
    length = width
    health_height = 20
    fill = (pct / 1600) * length
    outline_rect = pygame.Rect(x, y, length, health_height)
    fill_Rect = pygame.Rect(x, y, fill, health_height)
    pygame.draw.rect(surf, color, fill_Rect)
    pygame.draw.rect(surf, white, outline_rect, 2)


def game_over_1(display, group, stars):
    display.fill((0, 0, 30))
    draw_text(display, "Stellar COnflict", 125, (width // 2), (height // 2 * 0.44), white)
    draw_text(display, "Press Q To Play", 64, (width // 2), (height // 2), white)
    group.add(stars)
    stars.spawn(group)
    group.draw(display)
    group.update()
    waiting = True

    while waiting:
        for ev in pygame.event.get():
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if ev.key == pygame.K_q:
                    waiting = False
        pygame.display.update()
        clock.tick(FPS)


def timer(display, countdown, countdown_is_1, countdown_timer_1):
    while countdown_is_1:
        now = pygame.time.get_ticks()
        display.fill((0, 0, 30))
        draw_text(display, str(countdown), 128, (width // 2), (height // 2 - 30), white)
        if now - countdown_timer_1 >= 900:
            countdown -= 1
            countdown_timer_1 = now
        if countdown <= 0:
            countdown_is_1 = False
        pygame.display.update()
        clock.tick(FPS)


def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)
    target.blit(temp, location)


def spawn_powerup(powerup, hit, group1, group2):
    powerup_chance = random.random()
    if powerup_chance > 0.9:
        powerup = powerup(hit.rect.centerx, hit.rect.centery)
        group1.add(powerup)
        group2.add(powerup)


def end_screen(screen):
    screen.fill((0, 0, 30))
    draw_text(screen, "Game Over", 128, width // 2, height // 2 - 50, white)
    draw_text(screen, "Press Esc To Quit", 64, width // 2, height // 2 + 75, white)
