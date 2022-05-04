import pygame
import random   #needed for random enemy spawning
import math     #for math formulas needed for collisions 
from pygame import mixer

pygame.init()

# Create screen (width, height) or (x, y)
display = pygame.display.set_mode((1000, 600))
pygame.display.update()

# Background image
background = pygame.image.load('space.png')

# Background music
mixer.music.load('spaceGameSound.wav')
mixer.music.play(-1)  # -1 is put so it plays the sound continuously 

#Tittle and Icon
pygame.display.set_caption("Unknown Galaxies")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# Main Player 
mainP = pygame.image.load('aircraft.png') 
mainP_x = 500
mainP_y = 450
mainP_xChange = 0
mainP_yChange = 0

#Missile: loaded = missile cant be seen, fire = missile is moving
missile = pygame.image.load('missile.png')
missile_x = 0
missile_y = 0
missile_yChange = 0.5
missile_state = "loaded"

# Score: font type and its location

score = 0
font = pygame.font.Font('freesansbold.ttf', 32) #Other font types can be donwloaded and must be placed within project
fontX = 15                                      #font size is = 32
fontY = 15
Red = (255, 0, 0)
Lime = (0, 255, 0)

#GameOver font 

End_font = pygame.font.Font('freesansbold.ttf', 70)

# Enemy, and random spawning
Enemy = []
Enemy_x = []
Enemy_y = []
Enemy_xChange = []
Enemy_yChange = []
NumOfEnemies = 5

for i in range(NumOfEnemies):
    Enemy.append(pygame.image.load('alien.png'))
    #EnemyB = pygame.image.load('alien.png')
    Enemy_x.append(random.randint(0, 900)) # range of random numbers for x used for spawning coordinate
    Enemy_y.append(random.randint(0, 200))
    Enemy_xChange.append(0.4)
    Enemy_yChange.append(40) 

# Explosion replases alien
#Explosion = pygame.image.load("explosion.png")

def player(x, y):
    display.blit(mainP, (x, y))        # blit draws on the screen

def enemy(x, y, i):
    display.blit(Enemy[i], (x, y))

def fireMissile(x, y):
    global missile_state    # So missile_state variable can be accessed inside method
    missile_state = "fire"
    display.blit(missile, (x, y))
    display.blit(missile, (x + 45, y)) #second missile

def IsaHit(x, y, x2, y2):
    AB = math.sqrt((math.pow(x - x2, 2)) + (math.pow(y - y2, 2)))  #from the mathematical distance formula 
    if AB < 32:
        return True
    else:
        return False

#score board
def fontDisplayed(x, y):
    score_screen = font.render('Score :' + str(score), True, Lime)  #needs to be typed cast to string from integer
    display.blit(score_screen, (x, y))

def GameOver():
    End = End_font.render('GAME OVER', True, Red)      #(text you want, True, color you want)
    display.blit(End, (300, 300))

#Loops to close window
open = True
while open:

    #RGB (Red, Green, Blue) can input 0 - 255, Look at chart for precise colors
    display.fill((0, 0, 80))   #Placed here before other element calls because otherwise it hides/overlaps them. Also not needed here
    display.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Anything that happens inside game window is called an event
            open = False
    
    # <>^v arrow move properties, press down
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            mainP_xChange = -0.5
        if event.key == pygame.K_RIGHT:
            mainP_xChange = 0.5
        if event.key == pygame.K_UP:
            mainP_yChange = -0.5
        if event.key == pygame.K_DOWN:
            mainP_yChange = 0.5
        #shoot
        if event.key == pygame.K_z:
            if missile_state == "loaded":
                missile_Sound = mixer.Sound('missileLaunch.wav')
                missile_Sound.play()
                missile_x = mainP_x              #So it does not follow ship x movement 
                missile_y = mainP_y
                print("key has been pressed")
                fireMissile(missile_x, missile_y)
            

    # Release button
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            mainP_xChange = 0.0
        if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            mainP_yChange = 0.0

    mainP_x += mainP_xChange
    mainP_y += mainP_yChange

    # Keeping Main character within boundaries 
    if mainP_x <= 0:
        mainP_x = 0
    elif mainP_x >= 936:
        mainP_x = 936
    elif mainP_y <= 0:
        mainP_y = 0
    elif mainP_y >= 536:
        mainP_y = 536

    # Enemy movement on x and y directions
    for i in range(NumOfEnemies):

        # Game Over condition
        if Enemy_y[i] > 400:
            for j in range(NumOfEnemies):
                Enemy_y[j] = 2000
            GameOver()
            break

        # Movement 
        Enemy_x[i] += Enemy_xChange[i]
        if Enemy_x[i] <= 0:
            Enemy_xChange[i] = 0.4
            Enemy_y[i] += Enemy_yChange[i]
        elif Enemy_x[i] >= 936:
            Enemy_xChange[i] = -0.4
            Enemy_y[i] += Enemy_yChange[i]

        # Collision between Missile and alien 
        Hit = IsaHit(Enemy_x[i], Enemy_y[i], missile_x, missile_y)
        if Hit == True:
            Explosion_Sound = mixer.Sound('explosionSound.wav')
            Explosion_Sound.play()
            missile_y = mainP_y 
            missile_state = "loaded"
            score += 1
            #Enemy = Explosion
            #Enemy = EnemyB
            Enemy_x[i] = random.randint(0, 900) 
            Enemy_y[i] = random.randint(0, 200)

        enemy(Enemy_x[i], Enemy_y[i], i)

#Missile movement
    if missile_y <= 0:
        missile_y = mainP_y
        missile_state = "loaded"     #missile is being reused once it leaves the screen

    if missile_state is "fire":
        fireMissile(missile_x, missile_y)
        missile_y -= missile_yChange

    player(mainP_x, mainP_y)
    fontDisplayed(fontX, fontY)
    pygame.display.update()
 
pygame.quit()
quit()
