import pygame
from tiles import AnimatedTile

class Enemy(AnimatedTile):
    def __init__(self,size,x,y):
        super().__init__(size,x,y,'Project/Real_Code/graphics/enemy/run')
        