from msilib.schema import SelfReg
from typing_extensions import Self
import pygame, sys
from settings import *
from level import Level
from UI import UI
#from Enemy import Enemy
pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(level_map, screen)
class Game:
        #game atributes
    def __init__(self):
        self.max_health = 100
        self.cur_health = 100

    #user interface
        self.UI = UI(screen)

    def creat_level(self, current_level):
        self.level = Level(current_level, screen,self.create_overworld, self.change_coins,self.change_health)
        self.status = 'level'


    def change_health(self, amount):
        self.cur_health += amount

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill('black')
        level.run()

        pygame.display.update()
        clock.tick(60)

    def run(self):
        if self.status == 'overworld':
            self.overworld.run()
        else:
            self.level.run()
            self.ui.show_health(50, 100)


