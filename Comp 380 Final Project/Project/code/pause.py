import pygame
from settings import *


class Pause:
    def __init__(self,player):
        self.display_surface = pygame.display.get_surface()
        self.player = player
        
        
    def display(self):
        screen = pygame.display.set_mode((screen_width,screen_height))	
        PauseText = font.render('Paused', True, white, black,)
        PauseOptions = font.render('press P to continue or ESC to exit', True, white, black)

        screen.fill('black')
        screen.blit(PauseText, (screen_width//2-50,screen_height-600))
        screen.blit(PauseOptions, (screen_width//2-250,screen_height-500))
        #message_to_screen("Paused", black, -100, size="large")
        #message_to_screen("Press C to continue or Q to quit.", black, 25)
        #pygame.display.update()
        

