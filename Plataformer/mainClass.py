import pygame
from settings import *
from tiles import Tile
from level import Level

pygame.init()
screen = pygame.display.set_mode((screenW, screenH))
clock = pygame.time.Clock()
level = Level(levelMap, screen)

open = True 
while open:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Anything that happens inside game window is called an event
            open = False
    
    screen.fill('black')
    level.run()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()