import pygame

class board():
    def __init__(self, x, y):
        super.__init__()
        self.score = 0
        self.font = pygame.font.Font('freesansbold.ttf', 32) 
        self.x = 15                                      
        self.y = 15
        self.Red = (255, 0, 0)
        self.Lime = (0, 255, 0)
