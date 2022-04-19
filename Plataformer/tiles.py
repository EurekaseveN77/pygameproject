import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, position, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill(('green'))
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def update(self, xShift):
        self.rect.x += xShift