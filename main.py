"""

Gang Related ~ 2015

Created by:
    Stephen Tam
    Gabriel de Lima-Mendonca
    Sean Wallach
    Andrew Bradley
    Nick Bann

"""

from __future__ import print_function
import pygame, sys, socket
pygame.init()
from pygame import *


###____________________________________Vars___________________________________________________####
infoObject = pygame.display.Info()
screenWidth, screenHeight = infoObject.current_w, infoObject.current_h
menuB = 0
Black = (0,0,0)
global mainCheck
mainCheck = True
buttonMainCheck = True
buttonPlayCheck = False


###____________________________________Import_________________________________________________####
#Backgrounds
startBack = pygame.image.load("img/StartScreenBackground.jpg")
startBack = pygame.transform.scale(startBack, (screenWidth, screenHeight))
#Main Screen Buttons
creditsBut = pygame.image.load("img/Credits_Button.png")
creditsRect = creditsBut.get_rect()
creditsButOH = pygame.image.load("img/Credits_Button_On_Hover.png")
settingsBut = pygame.image.load("img/Settings_Button.png")
settingsButOH = pygame.image.load("img/Settings_Button_On_Hover.png")
startBut = pygame.image.load("img/Start_Button.png")
startButOH = pygame.image.load("img/Start_Button_On_Hover.png")
title = pygame.image.load("img/Gang_Related_Title.png")
backBut = pygame.image.load("img/Back_Button.png")
backButOH = pygame.image.load("img/Back_Button_On_Hover.png")
quitBut = pygame.image.load("img/Quit_Button.png")
quitBut = pygame.transform.scale(quitBut, (269,92))
quitButOH = pygame.image.load("img/Quit_Button_On_Hover.png")
quitButOH = pygame.transform.scale(quitButOH, (269,92))
multiplayerBut = pygame.image.load("img/Multiplayer_Button.png")
multiplayerButOH = pygame.image.load("img/Multiplayer_Button_On_Hover.png")
singleplayerBut = pygame.image.load("img/Singleplayer_Button.png")
singleplayerButOH = pygame.image.load("img/Singleplayer_Button_On_Hover.png")
level1Floor = pygame.image.load("img/Floorplan_Basement.png")
level1Floor = pygame.transform.scale(level1Floor, (screenWidth,screenHeight))
creditsScreen = pygame.image.load("img/Credits_Screen.png")
creditsScreen = pygame.transform.scale(creditsScreen, (screenWidth,screenHeight))
redPlay = pygame.image.load("img/char/other/Color_Choose_Red_Original.png")
redPlay = pygame.transform.scale(redPlay, (500,500))
redPlayOH = pygame.image.load("img/char/other/Color_Choose_OnHover_Red_Original.png")
redPlayOH = pygame.transform.scale(redPlayOH, (500,500))
bluePlay = pygame.image.load("img/char/other/Color_Choose_Blue_Original.png")
bluePlay = pygame.transform.scale(bluePlay, (500,500))
bluePlayOH = pygame.image.load("img/char/other/Color_Choose_OnHover_Blue_Original.png")
bluePlayOH = pygame.transform.scale(bluePlayOH, (500,500))
#Music
menuMusic = "snd/Menu.ogg"
gameMusic = "snd/In_Game.ogg"
gameoverMusic = "snd/Credits.mp3"
###____________________________________Init___________________________________________________####
coords = pygame.mouse.get_pos()
screen = pygame.display.set_mode((screenWidth, screenHeight),pygame.FULLSCREEN, 32)
background = pygame.Surface(screen.get_size())
screen.blit(startBack,(0,0))
currentCred = creditsBut
currentSet = settingsBut
currentStr = startBut
currentBackB = backBut
currentQ = quitBut
currentMulti = multiplayerBut
currentSingle = singleplayerBut
mainMenu = True
pauseMenu = False
pygame.mouse.set_visible(True)
#Pygame clock 
clock = pygame.time.Clock()
FPS = 30 
playtime = 0.0
singleplayerCheck = False
creditsCheck = False
(playerX, playerY) = (200,200)
currentRedPlay = redPlay
currentBluePlay = bluePlay
singleplayerPlayerSelect = False
charColorSin = "null"
pygame.mixer.init()
allPressed = False
firstRun = True
menuSound = pygame.mixer.Sound(menuMusic)
menuSound.play(loops = -1)
defaultFont = pygame.font.Font("etc/fntf.otf", 75)
print(screenWidth, screenHeight)
wClicked = False
aClicked = False
sClicked = False
dClicked = False
mouseClicked = False
pauseMenu = False

###____________________________________Functions_______________________________________________####
def quitGame():
    pygame.quit()
    



###____________________________________Loop__________________________________________________####
while mainMenu:

    ###__________________________________Player Select____________________________________________####
    if singleplayerPlayerSelect:
        screen.blit(startBack,(0,0))
        redPlayBlit =  screen.blit(currentRedPlay,(screenWidth/2 -700,screenHeight-700))
        bluePlayBlit =  screen.blit(currentBluePlay,(screenWidth/2 +200,screenHeight-700))
    ###____________________________________Game Loop_______________________________________________####
    if buttonPlayCheck == True:
        screen.blit(startBack, (0,0))
        backB = screen.blit(currentBackB,(screenWidth/2 -268.5,screenHeight-300))
        multiB = screen.blit(currentMulti, (screenWidth/2 -268.5, screenHeight-500))
        singleB = screen.blit(currentSingle, (screenWidth/2 -268.5, screenHeight-700))
        
    #Framrate________________________________________
    milliseconds = clock.tick(FPS)
    playtime += milliseconds / 1000.0
    

    if mainCheck == True:
        
    #Title___________________________________________
        screen.blit(title,(screenWidth/2 -620,screenHeight-1000))
    #Blit buttons_____________________________________
        cred = screen.blit(currentCred,(screenWidth/2 -268.5,screenHeight-300))
        sets = screen.blit(currentSet,(screenWidth/2 -268.5,screenHeight-500))
        star = screen.blit(currentStr,(screenWidth/2 -268.5,screenHeight-700))
        quitb = screen.blit(currentQ,(screenWidth-280,screenHeight-150))
        
    if pauseMenu:
        singleplayerCheck = False

        
    if singleplayerCheck:
        if firstRun:
            menuSound.fadeout(1500)
            gameSound = pygame.mixer.Sound(gameMusic)
            gameSound.play(loops = -1)
            firstRun = False

        #Put level ground_____________________________
        screen.blit(level1Floor,(0,0))
        

        #Get and set vars_____________________________
        
        (mouseX, mouseY) = pygame.mouse.get_pos()
        #Import images__________________________________
        if charColorSin == "red":
            PlayerLeft = pygame.image.load("img/char/PlayerModel_Left_Glock_Original.png")
            PlayerLeft = pygame.transform.scale(PlayerLeft, (88,96))
            PlayerRight = pygame.image.load("img/char/PlayerModel_Right_Glock_Original.png")
            PlayerRight = pygame.transform.scale(PlayerRight, (88,96))
            currentPlayer = PlayerLeft
        elif charColorSin == "blue":
            PlayerLeft = pygame.image.load("img/char/2_PlayerModel_Left_Glock_Original.png")
            PlayerLeft = pygame.transform.scale(PlayerLeft, (88,96))
            PlayerRight = pygame.image.load("img/char/2_PlayerModel_Right_Glock_Original.png")
            PlayerRight = pygame.transform.scale(PlayerRight, (88,96))
            currentPlayer = PlayerLeft
            
        
        
        if mouseX > playerX + 88:
            currentPlayer = PlayerRight
            
        keys=pygame.key.get_pressed()
        if keys[K_w]:    
            playerY = playerY - 15
            wClicked = True
        if keys[K_a]:
            playerX = playerX - 15
            aClicked = True
        if keys[K_s]:    
            playerY = playerY + 15
            sClicked = True
        if keys[K_d]:    
            playerX = playerX + 15
            dClicked = True
        if keys[K_p]:
            print(playerX, playerY)

        if playerX >= screenWidth-230:
            playerX = screenWidth-230
        if playerX <= 150:
            playerX = 150
        if playerY <= 60:
            playerY = 60
        if playerY>=screenHeight-270:
            playerY = screenHeight-270
        playerSprite = screen.blit(currentPlayer,(playerX,playerY))
        if wClicked == True and aClicked == True and sClicked == True and dClicked == True:
            allPressed = True
        if allPressed == False:
            instructionB1 = defaultFont.render("Use 'WASD' to move", 1, (255,255,255))
            screen.blit(instructionB1, (screenWidth/2-350,screenHeight/2-250))
        if allPressed == True and mouseClicked == False:
            instructionB2 = defaultFont.render("Left click to shoot", 1, (255,255,255))
            screen.blit(instructionB2, (screenWidth/2-350,screenHeight/2-250))
        pygame.display.update()
        
    if creditsCheck:
        screen.blit(creditsScreen,(0,0))
        backB = screen.blit(currentBackB,(screenWidth/2 -268.5,screenHeight-300))
    #Hover detection__________________________________
    if buttonMainCheck == True:
        if cred.collidepoint(pygame.mouse.get_pos()):
            currentCred = creditsButOH
        else:
            currentCred = creditsBut
            
        if sets.collidepoint(pygame.mouse.get_pos()):
            currentSet = settingsButOH
        else:
            currentSet = settingsBut

        if star.collidepoint(pygame.mouse.get_pos()):
            currentStr = startButOH
        else:
            currentStr = startBut
            
        if quitb.collidepoint(pygame.mouse.get_pos()):
            currentQ = quitButOH
        else:
            currentQ = quitBut
            
    if buttonPlayCheck == True:
        if backB.collidepoint(pygame.mouse.get_pos()):
            currentBackB = backButOH
        else:
            currentBackB = backBut

        if multiB.collidepoint(pygame.mouse.get_pos()):
            currentMulti = multiplayerButOH
        else:
            currentMulti = multiplayerBut

        if singleB.collidepoint(pygame.mouse.get_pos()):
            currentSingle = singleplayerButOH
        else:
            currentSingle = singleplayerBut
            
    if singleplayerPlayerSelect:
        if bluePlayBlit.collidepoint(pygame.mouse.get_pos()):
            currentBluePlay = bluePlayOH
        else:
            currentBluePlay = bluePlay
            
        if redPlayBlit.collidepoint(pygame.mouse.get_pos()):
            currentRedPlay = redPlayOH
        else:
            currentRedPlay = redPlay
    if creditsCheck == True:
        if backB.collidepoint(pygame.mouse.get_pos()):
            currentBackB = backButOH
        else:
            currentBackB = backBut

        
    #Events______________________________________
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
           if singleplayerCheck == True: 
               mouseClicked = True
           if currentCred ==  creditsButOH:
               mainCheck = False
               buttonMainCheck = False
               buttonPlayCheck = False
               singleplayerCheck = False
               creditsCheck = True
               currentCred = creditsBut
               
               
           if currentSet == settingsButOH:
               mainCheck = False
               creditsCheck = False
               screen.blit(startBack, (0,0))
               
           if currentStr == startButOH:
               mainCheck = False
               buttonMainCheck = False
               buttonPlayCheck = True
               creditsCheck = False
               singleplayerCheck = False
               currentStr = startBut

           if currentBackB == backButOH:
               mainCheck = True
               buttonMainCheck = True
               buttonPlayCheck = False
               singleplayerCheck = False
               creditsCheck = False
               currentBackB = backBut
               screen.blit(startBack, (0,0))

           if currentQ == quitButOH:
               quitGame()

           if currentSingle == singleplayerButOH:
               mainCheck = False
               buttonMainCheck = False
               buttonPlayCheck = False
               creditsCheck = False
               singleplayerCheck = False
               singleplayerPlayerSelect = True
               currentSingle = singleplayerBut
               
           if currentBluePlay == bluePlayOH:
               charColorSin = "blue"
               mainCheck = False
               buttonMainCheck = False
               buttonPlayCheck = False
               creditsCheck = False
               singleplayerCheck = True
               singleplayerPlayerSelect = False
               currentBluePlay = bluePlay
               
           if currentRedPlay == redPlayOH:
               charColorSin = "red"
               mainCheck = False
               buttonMainCheck = False
               buttonPlayCheck = False
               creditsCheck = False
               singleplayerCheck = True
               singleplayerPlayerSelect = False
               currentBluePlay = bluePlay
        #Quit__________________________________
        if event.type == pygame.QUIT:
            mainloop = False
            
        elif event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_ESCAPE:
                if singleplayerCheck:
                    pauseMenu = True
                if pauseMenu:
                    singleplayerCheck = True
                    pauseMenu = False
                
            if event.key == pygame.K_UP:
                if menuB > 0: 
                    menuB = menuB - 1
                    print(menuB)
                    
            if event.key == pygame.K_DOWN:
                 if menuB < 3: 
                    menuB = menuB + 1
                    print(menuB)
 
    #Playtime: {1:.2f}".format(clock.get_fps(), playtime)
    
 
    #Update Pygame display.
    pygame.display.flip()

 
# Finish Pygame.
pygame.quit()



"""
Settings:
    FPS
    USERNAME (SAVE IN FILE)
    RES
    TURN MUSIC ON OR OFF
    TURN SOUND FX ON OR OFF
"""

##SPRITE IN CASE NEEDED LATER###
        #class playerSprite(pygame.sprite.Sprite):
            #image = None
            #def __init__(self,location):
                #if playerSprite.image is None:
                    #playerSprite.image = pygame.image.load("img/char/PlayerModel_Left_Glock_Original.png")
                    #playerSprite.image = pygame.transform.scale(playerSprite.image, (88,96))
                #self.image = playerSprite.image

                #self.rect = self.image.get_rect()
                #self.rect.topleft = location

        #playerSin1 = playerSprite([10,10])
        #screen.blit(playerSin1.image, playerSin1.rect)
