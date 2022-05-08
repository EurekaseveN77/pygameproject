import pygame, sys
from settings import *
from level import Level
from game_data import *

class Game:
    def __init__(self):
        self.status = 'level'
        self.create_level(0)
    
    def create_level(self,current_level):
        self.level = Level(current_level,screen)

    def run(self):
        self.level.run()

# Pygame setup
pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
#level = Level(level_0,screen)
game = Game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill('black')
    game.run()

    pygame.display.update()
    clock.tick(60)
