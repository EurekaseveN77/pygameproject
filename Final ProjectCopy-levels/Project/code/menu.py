import pygame

class Menu():
    def __init__(self, game):
        self.game = game
        self.midW, self.midH = self.game.displayW / 2, self.game.displayH / 2
        self.runDisplay = True
        self.cursorRect = pygame.Rect(0, 0, 20, 20)   #square cursor, then you can put any image inside it
        self.offset = -150                             #where arrow appears on x axis
        self.background = pygame.image.load('Castle2.png') #new

    def drawCursor(self):
        self.game.drawText('->', 70, self.cursorRect.x, self.cursorRect.y)

    def blitScreen(self):
        self.game.window.blit(self.game.display, (0,0)) 
        pygame.display.update()
        self.game.resetKeys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startX, self.startY = self.midW, self.midH + 50            
        self.optionsX, self.optionsY = self.midW, self.midH + 110         
        self.creditsX, self.creditsY = self.midW, self.midH + 170
        self.cursorRect.midtop = (self.startX + self.offset, self.startY)

    def displayMenu(self):
        self.runDisplay = True
        while self.runDisplay:
            self.game.registeredEvents()
            self.checkInput()
            self.game.display.fill(self.game.BLACK)
            self.game.display.blit(self.background, (0,0)) #new
            self.game.drawText('Knightmare', 100, self.game.displayW/2, self.game.displayH/2 - 50)
            self.game.drawText("Start Game", 60, self.startX, self.startY)
            self.game.drawText("Options", 60, self.optionsX, self.optionsY)
            self.game.drawText("Credits", 60, self.creditsX, self.creditsY)
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
        self.volX, self.volY = self.midW, self.midH + 40
        self.LevelsX, self.LevelsY = self.midW, self.midH + 100
        self.cursorRect.midtop = (self.volX + self.offset, self.volY)   #cursor is alligned to start with volume option

    def displayMenu(self):    #Name must match name under init above
        self.runDisplay = True
        while self.runDisplay:
            self.game.registeredEvents()
            self.checkInput()
            self.game.display.fill(self.game.BLACK)
            self.game.display.blit(self.background, (0,0))
            self.game.drawText('Options', 80, self.game.displayW/2, self.game.displayH/2 - 60)
            self.game.drawText("Volume", 60, self.volX, self.volY)
            self.game.drawText("Levels", 60, self.LevelsX, self.LevelsY)
            self.drawCursor()
            self.blitScreen()

    def checkInput(self):
        if self.game.BACK_KEY:
            self.game.currentMenu = self.game.mainMenu
            self.runDisplay = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Volume':
                self.state = 'Levels'
                self.cursorRect.midtop = (self.LevelsX + self.offset, self.LevelsY)
            elif self.state == 'Levels':
                self.state = 'Volume'
                self.cursorRect.midtop = (self.volX + self.offset, self.volY)
        elif self.game.START_KEY:
            if self.state == 'Levels':
                self.game.currentMenu = self.game.levels
            self.runDisplay = False

class levelsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'level1'
        self.level1X, self.level1Y = self.midW, self.midH + 40
        self.level2X, self.level2Y = self.midW, self.midH + 100
        self.cursorRect.midtop = (self.level1X + self.offset, self.level1Y)   #cursor is alligned to start with volume option
    
    def displayMenu(self):
        self.runDisplay = True
        while self.runDisplay:
            self.game.registeredEvents()
            self.checkInput()
            self.game.display.fill(self.game.BLACK)
            self.game.display.blit(self.background, (0,0))
            self.game.drawText('Levels', 80, self.game.displayW/2, self.game.displayH/2 - 60)
            self.game.drawText("level A", 65, self.level1X, self.level1Y)
            self.game.drawText("level B", 65, self.level2X, self.level2Y)
            self.drawCursor()
            self.blitScreen()

    def checkInput(self):
        if self.game.BACK_KEY:
            self.game.currentMenu = self.game.options
            self.runDisplay = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'level1':
                self.state = 'level2'
                self.cursorRect.midtop = (self.level2X + self.offset, self.level2Y)
            elif self.state == 'level2':
                self.state = 'level1'
                self.cursorRect.midtop = (self.level1X + self.offset, self.level1Y)
            elif self.game.START_KEY:
                pass
        elif self.game.START_KEY:
            if self.state == 'level1':
                pass                      # Andrew place level 1 here or call game from level 1
            elif self.state == 'level2':
                pass                      #level 2 here or call game from level 2
            self.runDisplay = False

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
            self.game.display.blit(self.background, (0,0))
            self.game.drawText('Designed By:', 80, self.game.displayW/2, self.game.displayH/2 - 150)
            self.game.drawText('Andres Esparza', 60, self.game.displayW/2, self.game.displayH/2-50)
            self.game.drawText('Andrew Howard', 60, self.game.displayW/2, self.game.displayH/2 +10)
            self.game.drawText('Carlos A Morales Sierra', 60, self.game.displayW/2, self.game.displayH/2+70)
            self.game.drawText('James Carton', 60, self.game.displayW/2, self.game.displayH/2+130)
            self.game.drawText('Luis Hernandez', 60, self.game.displayW/2, self.game.displayH/2+190)
            self.game.drawText('Tommy Ibrahimi', 60, self.game.displayW/2, self.game.displayH/2+250)

            self.blitScreen()