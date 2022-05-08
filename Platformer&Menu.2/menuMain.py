import pygame
from game import Game
from pygame import mixer

mixer.music.load('EpicBattle.wav')
mixer.music.play(-1)  # -1 is put so it plays the sound continuously 

gameInstance = Game()

while gameInstance.running:
    gameInstance.currentMenu.displayMenu()
    gameInstance.gameLoop()
