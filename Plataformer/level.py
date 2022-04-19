import pygame
from tiles import Tile
from settings import tileSize, screenW
from player import Player

class Level:
    def __init__(self, levelData, surface):
        # level setup
        self.displaySurface = surface
        self.setupLevel(levelData)
        self.worldShift = 0
    
    def setupLevel(self,layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        for rowIndex,row in enumerate(layout):
            for colIndex,cell in enumerate(row):
                if cell == 'X':
                    x = colIndex * tileSize
                    y = rowIndex * tileSize
                    tile = Tile((x, y), tileSize)
                    self.tiles.add(tile)
                if cell == 'P':
                    x = colIndex * tileSize
                    y = rowIndex * tileSize
                    playerSprite = Player((x, y))
                    self.player.add(playerSprite)

    def scrollX(self):
        player = self.player.sprite
        playerX = player.rect.centerx
        directionX = player.direction.x

        if playerX < screenW and directionX < 0:
            self.worldShift = 6
            player.speed = 0
        elif playerX > screenW - (screenW * (3/4)) and directionX > 0:
            self.worldShift = -6
            player.speed = 0
        else:
            self.worldShift = 0
            player.speed = 6

    def horizontalMovementCollision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed   #horizontal movement

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):    #checks rectangles and player collition
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right  #placing player in correct side of collision
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
        
    def verticalMovementCollision(self):
        player = self.player.sprite
        player.applyGravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):    #checks rectangles and player collition
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top  #placing player in correct side of collision
                    player.direction.y = 0                #stops downward y movement which cancels out gravity
                elif player.direction.y < 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0

    def run(self):
        # level tiles
        self.tiles.update(self.worldShift)
        self.tiles.draw(self.displaySurface)
        self.scrollX()

        #player
        self.player.update()
        self.horizontalMovementCollision()
        self.verticalMovementCollision()
        self.player.draw(self.displaySurface)
        