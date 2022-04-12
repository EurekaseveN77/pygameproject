import pygame, sys
from settings import *
from level import Level

# !!! TUTORIAL STOPPED AT 27:31 -- need to input 'P' into the level_map to denote player spawn

# Pygame setup
pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(level_map,screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill('black')
    level.run()

    pygame.display.update()
    clock.tick(60)
