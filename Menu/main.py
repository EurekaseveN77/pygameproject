import pygame
from game import Game

gameInstance = Game()

while gameInstance.running:
    gameInstance.currentMenu.displayMenu()
    gameInstance.gameLoop()

