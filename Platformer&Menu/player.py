import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.Surface((32, 64))
        self.image.fill(('red'))
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        #vector2 is a list that contain an x and y value. A line is generated when connecting x origin and y end.

        #player movement
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 6
        self.gravity = 0.6
        self.jumpHeight = -13

    def getInput(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE]:
            self.jump()
    
    def applyGravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jumpHeight


    def update(self):
        self.getInput()