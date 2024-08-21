import pygame.time

width = 1600
height = 900

FPS = 120

display_dimensions = (width, height)
clock = pygame.time.Clock()

dt = clock.tick(FPS)

gold = (255,215,0)
red = (255, 0, 0)
orange = (255, 127, 0)
grey = (72, 72, 72)
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
bg_color = (0, 0, 30)
yellow = (255, 255, 0)

colors = [red, orange, grey]
