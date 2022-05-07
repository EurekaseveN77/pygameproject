import pygame
from settings import *


class Pause:
    def __init__(self,player):
        self.display_surface = pygame.display.get_surface()
        self.player = player
        
    def display(self):
        screen = pygame.display.set_mode((screen_width,screen_height))		
        screen.fill('black')
        #message_to_screen("Paused", black, -100, size="large")
        #message_to_screen("Press C to continue or Q to quit.", black, 25)
        #pygame.display.update()
        

