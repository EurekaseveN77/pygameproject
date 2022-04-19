import pygame, sys
from settings import *
from level import Level
#from Enemy import Enemy
pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(level_map, screen)

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


