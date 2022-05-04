import pygame

class Menu():
    def __init__(self, game):
        self.game = game
        self.midW, self.midH = self.game.displayW / 2, self.game.displayH / 2
        self.runDisplay = True
        self.cursorRect = pygame.Rect(0, 0, 20, 20)   #square cursor, then you can put any image inside it
        self.offset = -100

    def drawCursor(self):
        self.game.drawText('->', 15, self.cursorRect.x, self.cursorRect.y)

    def blitScreen(self):
        self.game.window.blit(self.game.display, (0,0)) 
        pygame.display.update()
        self.game.resetKeys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startX, self.startY = self.midW, self.midH + 30
        self.optionsX, self.optionsY = self.midW, self.midH + 50
        self.creditsX, self.creditsY = self.midW, self.midH + 70
        self.cursorRect.midtop = (self.startX + self.offset, self.startY)

    def displayMenu(self):
        self.runDisplay = True
        while self.runDisplay:
            self.game.registeredEvents()
            self.checkInput()
            self.game.display.fill(self.game.BLACK)
            self.game.drawText('Main Menu', 20, self.game.displayW/2, self.game.displayH/2 - 20)
            self.game.drawText("Start Game", 20, self.startX, self.startY)
            self.game.drawText("Options", 20, self.optionsX, self.optionsY)
            self.game.drawText("Credits", 20, self.creditsX, self.creditsY)
            self.drawCursor()
            self.blitScreen()

    def moveCursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursorRect.midtop = (self.optionsX + self.offset, self.optionsY)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursorRect.midtop = (self.creditsX + self.offset, self.creditsY)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursorRect.midtop = (self.startX + self.offset, self.startY)
                self.state = 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursorRect.midtop = (self.creditsX + self.offset, self.creditsY)
                self.state = 'Credits'
            elif self.state == 'Options':
                self.cursorRect.midtop = (self.startX + self.offset, self.startY)
                self.state = 'Start'
            elif self.state == 'Credits':
                self.cursorRect.midtop = (self.optionsX + self.offset, self.optionsY)
                self.state = 'Options'

    def checkInput(self):
        self.moveCursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Options':
                self.game.currentMenu = self.game.options
            elif self.state == 'Credits':
                self.game.currentMenu = self.game.credits
            self.runDisplay = False

class optionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Volume'
        self.volX, self.volY = self.midW, self.midH + 20
        self.controlsX, self.controlsY = self.midW, self.midH + 40
        self.cursorRect.midtop = (self.volX + self.offset, self.volY)   #cursor is alligned to start with volume option

    def displayMenu(self):    #Name must match name under init above
        self.runDisplay = True
        while self.runDisplay:
            self.game.registeredEvents()
            self.checkInput()
            self.game.display.fill(self.game.BLACK)
            self.game.drawText('Options', 20, self.game.displayW/2, self.game.displayH/2 - 30)
            self.game.drawText("Volume", 15, self.volX, self.volY)
            self.game.drawText("Controls", 15, self.controlsX, self.controlsY)
            self.drawCursor()
            self.blitScreen()

    def checkInput(self):
        if self.game.BACK_KEY:
            self.game.currentMenu = self.game.mainMenu
            self.runDisplay = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Volume':
                self.state = 'Controls'
                self.cursorRect.midtop = (self.controlsX + self.offset, self.controlsY)
            elif self.state == 'Controls':
                self.state = 'Volume'
                self.cursorRect.midtop = (self.volX + self.offset, self.volY)
            elif self.game.START_KEY:
                pass

class creditsMenu(Menu):
     def __init__(self, game):
        Menu.__init__(self, game)

     def displayMenu(self):  
        self.runDisplay = True
        while self.runDisplay:
            self.game.registeredEvents()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.currentMenu = self.game.mainMenu
                self.runDisplay = False
            self.game.display.fill(self.game.BLACK)
            self.game.drawText('Designed By:', 20, self.game.displayW/2, self.game.displayH/2 - 50)
            self.game.drawText('Andres Esparza', 15, self.game.displayW/2, self.game.displayH/2)
            self.game.drawText('Andrew Howard', 15, self.game.displayW/2, self.game.displayH/2+20)
            self.game.drawText('Carlos A Morales Sierra', 15, self.game.displayW/2, self.game.displayH/2+40)
            self.game.drawText('James Carton', 15, self.game.displayW/2, self.game.displayH/2+60)
            self.game.drawText('Luis Hernandez', 15, self.game.displayW/2, self.game.displayH/2+80)
            self.game.drawText('Tommy Ibrahimi', 15, self.game.displayW/2, self.game.displayH/2+100)

            self.blitScreen()