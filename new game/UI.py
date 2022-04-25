import pygame

class UI:
    def __init__(self, surface):
        #setup
        self.display_surface = surface

        #health
        self.healt_bar = pygame.image.load('../new game/Health Bar Asset Pack 2 by Adwit Rahman/Test1.png')
        
    def show_health(self,current,full):
        self.display_surface.blit(self.healt_bar,(20,10))
