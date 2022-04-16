import pygame
pygame.init()

win = pygame.display.set_mode((600,600)) #this is to setr the screen


#lets the eneymey walk in both directions
WalkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png')]
WalkLeft  = [pygame.image.load('L1.png'), pygame.image.load('L2.png')]

class enemy(object):
    WalkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png')]
    WalkLeft  = [pygame.image.load('L1.png'), pygame.image.load('L2.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width  = width 
        self.height = height
        self.path = [x, end] #here we defined were the enemy starts and ends

        self.WalkCount = 0
        self.vel = 3

    def draw(self, win):
        self.move()
        if self.walkCount + 1 >= 38: # Since we have 11 images for each animtion our upper bound is 33. 
                                        # We will show each image for 3 frames. 3 x 11 = 33.
                self.walkCount = 0
                
        if self.vel > 0: # If we are moving to the right we will display our walkRight images
                win.blit(self.walkRight[self.walkCount//4], (self.x,self.y))
                self.walkCount += 1
        
        else: 
         # Otherwise we will display the walkLeft images
            win.blit(self.walkLeft[self.walkCount//4], (self.x,self.y))
        self.walkCount += 1




    def move(self):
        if self.vel > 0:
            if self.x < self.path[1]+self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.WalkCount = 0
        else:
            if self.x > self.path[0] - self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
            self.x += self.vel
            self.WalkCount = 0