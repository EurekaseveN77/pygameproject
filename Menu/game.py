from tkinter import OptionMenu
import pygame
from menu import *           #imports all classes

class Game():         # self is the reference to the Game class
    def __init__(self):          # below are all the values generated when creating an object of this class
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.displayW, self.displayH = 480, 270             #480*270 gives us the amount of pixels we can fit in the display
        self.display = pygame.Surface((self.displayW, self.displayH))
        self.window = pygame.display.set_mode(((self.displayW, self.displayH)))
        self.fontName = pygame.font.get_default_font()
        self.BLACK, self.CRIMSON = (0,0,0), (153,0,0)       #Red, Blue, Green the values given is like mixing colors in a canvas
        self.mainMenu = MainMenu(self)
        self.options = optionsMenu(self)
        self.credits = creditsMenu(self)
        self.currentMenu = self.mainMenu

    def gameLoop(self):
        while self.playing:
            self.registeredEvents()
            if self.START_KEY:
                self.playing = False
            self.display.fill(self.BLACK)           #along with update() resets the screen when a new pixel is drawn
            self.drawText('Game Starts', 20, self.displayW/2, self.displayH/2)
            self.window.blit(self.display, (0,0))   #0,0  aligns game window with the game's display
            pygame.display.update()
            self.resetKeys()

    def registeredEvents(self):
        for event in pygame.event.get():           #checks all actions done by player
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.currentMenu.runDisplay = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True   

    def resetKeys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def drawText(self, text, size, x, y):    #x, y is where the font would be located on the screen
        font = pygame.font.Font(self.fontName, size)
        textSurface = font.render(text, True, self.CRIMSON)
        textRect = textSurface.get_rect()
        textRect.center = (x,y)
        self.display.blit(textSurface,textRect)