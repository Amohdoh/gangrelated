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
#MAPS
level1Floor = pygame.image.load("img/Floorplan_Basement_Door_Open.png")
level1Floor = pygame.transform.scale(level1Floor, (screenWidth,screenHeight))
level2Surface = pygame.image.load("img/Floorplan_level2CLOSED.png")
level2Surface = pygame.transform.scale(level2Surface, (screenWidth, screenHeight))
level2SurfaceDoorOpen = pygame.image.load("img/Floorplan_level2.png")
level2SurfaceDoorOpen = pygame.transform.scale(level2SurfaceDoorOpen, (screenWidth, screenHeight))
level3Floor = pygame.image.load("img/Map_Skele_Original.png")
level3Floor = pygame.transform.scale(level3Floor, (screenWidth, screenHeight))
level3FloorOpen = pygame.image.load("img/Map_Skele_Door2_Open.png")
level3FloorOpen = pygame.transform.scale(level3FloorOpen, (screenWidth, screenHeight))
#MISC
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
#Consumables
drankImg = pygame.image.load("img/char/props/Drank.png")
drankImg = pygame.transform.scale(drankImg, (26, 56))
#Enemies
skeletonRight = pygame.image.load("img/char/enemies/skele_small_Right.png")
skeletonRight = pygame.transform.scale(skeletonRight, (99,171))
skelteonLeft = pygame.image.load("img/char/enemies/skele_small_Left.png")
skelteonLeft = pygame.transform.scale(skelteonLeft, (99,171))
skeletonRightOH = pygame.image.load("img/char/enemies/skele_small_Right_OnHit.png")
skeletonRightOH = pygame.transform.scale(skeletonRightOH, (99,171))
skelteonLeftOH = pygame.image.load("img/char/enemies/skele_small_OnHit_Left.png")
skelteonLeftOH = pygame.transform.scale(skelteonLeftOH, (99,171))
#Music
menuMusic = "snd/Menu.ogg"
gameMusic = "snd/In_Game.ogg"
gameoverMusic = "snd/Credits.mp3"
pistolShot = "snd/fx/weap/pistol.ogg"
sipLean = "snd/fx/etc/sip.ogg"
#Hearts
hearts3 = pygame.image.load("img/health/3hearts.png")
hearts3 = pygame.transform.scale(hearts3, (220,79))
hearts25 = pygame.image.load("img/health/25hearts.png")
hearts2 = pygame.image.load("img/health/2hearts.png")
hearts15 = pygame.image.load("img/health/15hearts.png")
hearts1 = pygame.image.load("img/health/1hearts.png")
hearts05 = pygame.image.load("img/health/05hearts.png")

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
FPS = 28 
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
firstRunStart = True
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
isShooting = False
checkTheTime = False
onFirst = False
level2Start = False
gamePlay = False
firstRunLevel2 = True
dranklvl2notHad = True
health = 3
textSample1 = "Enter empty door to Continue"
currentLevelBack = level1Floor
now = 0
change = 0
direction = ""
health = 12
level3Start = False
firstRunLevel3 = True
###____________________________________Functions_______________________________________________####
def quitGame():
    pygame.quit()
    



###____________________________________Loop__________________________________________________####
while mainMenu:
        
    #Clock___________________________________________
    if checkTheTime:
        if pygame.time.get_ticks() >= change:
           if direction == "Left":
                currentPlayer = PlayerLeft
                isShooting = False
                checkTheTime = False
           elif direction == "Right":
                currentPlayer = PlayerRight
                isShooting = False
                checkTheTime = False
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
    #Blit buttons____________________________________
        cred = screen.blit(currentCred,(screenWidth/2 -268.5,screenHeight-300))
        sets = screen.blit(currentSet,(screenWidth/2 -268.5,screenHeight-500))
        star = screen.blit(currentStr,(screenWidth/2 -268.5,screenHeight-700))
        quitb = screen.blit(currentQ,(screenWidth-280,screenHeight-150))
        
    if pauseMenu:
        singleplayerCheck = False

        

#Level 2_____________________________________________

    if level2Start:
        
        #Init________________________________________
        textSample1 = " "
        if firstRunLevel2:
            currentLevelBack = level2Surface
            health = 3
            playerX = 150
            isShooting = False
            singleplayerCheck = False
            firstRunLevel2 = False
            skeletonLvl21Health = 2
            skeletonLvl22Health = 2
            skeletonLvl23Health = 2
            skeletonLvl24Health = 2
            skeletonLvl21X = 590
            skeletonLvl22X = 830
            skeletonLvl23X = 1270
            skeletonLvl24X = 1540
            skeletonLvl21Y = 290
            skeletonLvl22Y = 670
            skeletonLvl23Y = 680
            skeletonLvl24Y = 300
        singleplayerCheck = False
        level1Floor = "dsadsa"        

        #Put level ground____________________________

        screen.blit(currentLevelBack,(0,0))

        #Drank health________________________________
        if dranklvl2notHad:
            if currentLevelBack == level2SurfaceDoorOpen:
                instructionA2 = defaultFont.render("Lean-Aid refills some health", 1, (255,255,255))
                screen.blit(instructionA2, (screenWidth/2-500,screenHeight/2-350))
            dranklvl2 = screen.blit(drankImg,(1405,745))
            dranklvl2.inflate(1000,1000)
        if dranklvl2.collidepoint(playerX, playerY):
            sip = pygame.mixer.Sound(sipLean)
            sip.play(0)
            dranklvl2notHad = False
        #Skeletons blit______________________________
        currentSideSkele21 = skelteonLeft
        currentSideSkele22 = skelteonLeft
        currentSideSkele23 = skelteonLeft
        currentSideSkele24 = skelteonLeft
        
        if skeletonLvl21Health > 0:
            skeletonLvl21 = screen.blit(currentSideSkele21,(skeletonLvl21X,skeletonLvl21Y))
##        else:
##            skeletonLvl21X = -4000
            
        if skeletonLvl22Health > 0:
            skeletonLvl22 = screen.blit(currentSideSkele22,(skeletonLvl22X,skeletonLvl22Y))
        else:
            skeletonLvl22X = -4000
        
        if skeletonLvl23Health > 0:
            skeletonLvl23 = screen.blit(currentSideSkele23,(skeletonLvl23X,skeletonLvl23Y))
##        else:
##            skeletonLvl23X = -4000
        
        if skeletonLvl24Health > 0:
            skeletonLvl24 = screen.blit(currentSideSkele24,(skeletonLvl24X,skeletonLvl24Y))
##        else:
##            skeletonLvl24X = -4000

        #Unlock Door_________________________________
        if skeletonLvl21Health <= 0 and skeletonLvl22Health <= 0 and skeletonLvl23Health <= 0 and skeletonLvl24Health <= 0:
            currentLevelBack = level2SurfaceDoorOpen
        #Skeletons AI________________________________

        #Get and set vars____________________________
        
        (mouseX, mouseY) = pygame.mouse.get_pos()
        
        
        if mouseX > playerX + 88 and isShooting == False:
            currentPlayer = PlayerRight
            direction = "Right"
        if mouseX < playerX and isShooting == False:
            currentPlayer = PlayerLeft
            direction = "Left"
            
        keys=pygame.key.get_pressed()
        if keys[K_w]:    
            playerY = playerY - 10
            wClicked = True
        if keys[K_a]:
            playerX = playerX - 10
            aClicked = True
        if keys[K_s]:    
            playerY = playerY + 10
            sClicked = True
        if keys[K_d]:    
            playerX = playerX + 10
            dClicked = True
        if keys[K_p]:
            print(playerX, playerY)

        if playerX >= screenWidth-230:
            playerX = screenWidth-230
        if playerX <= 150:
            playerX = 150
        if playerY <= 85:
            playerY = 85
        if playerY>=screenHeight-270:
            playerY = screenHeight-270

            
        if playerX == screenWidth - 230 and playerY == screenHeight - 580:
            level2Start = False
            singleplayerCheck = False
            level3Start = True
        if currentLevelBack == level2Surface and singleplayerCheck == False and level2Start == True:
            instructionA1 = defaultFont.render("Shoot enemies to kill them", 1, (255,255,255))
            screen.blit(instructionA1, (screenWidth/2-500,screenHeight/2-350))


        playerSprite = screen.blit(currentPlayer,(playerX,playerY))
        
        
        pygame.display.flip()

#Level 2_____________________________________________

    elif level3Start:
        
        #Init________________________________________
##        textSample1 = " "
        if firstRunLevel3:
           currentLevelBack = level3Floor
##            health = 3
           playerX = 150
##            isShooting = False
##            singleplayerCheck = False
           firstRunLevel3 = False
        singleplayerCheck = False
##        level1Floor = "dsadsa"        

        #Put level ground____________________________

        screen.blit(currentLevelBack,(0,0))


        #Get and set vars____________________________
        
        (mouseX, mouseY) = pygame.mouse.get_pos()
        
        
        if mouseX > playerX + 88 and isShooting == False:
            currentPlayer = PlayerRight
            direction = "Right"
        if mouseX < playerX and isShooting == False:
            currentPlayer = PlayerLeft
            direction = "Left"
            
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
        if playerY <= 85:
            playerY = 85
        if playerY>=screenHeight-270:
            playerY = screenHeight-270

            
        if playerX == screenWidth - 230 and playerY == screenHeight - 580:
            level2Start = False
            singleplayerCheck = False
            level3Start = False


        playerSprite = screen.blit(currentPlayer,(playerX,playerY))
        
        
        pygame.display.flip()



#Level 1______________________________________________
    elif singleplayerCheck == True:
        
        gamePlay = True
        if firstRun and singleplayerCheck == True and level2Start == False:
            menuSound.fadeout(1500)
            gameSound = pygame.mixer.Sound(gameMusic)
            gameSound.play(loops = -1)
            firstRun = False
            health = 3

        #Put level ground____________________________

        screen.blit(currentLevelBack,(0,0))
        

        #Get and set vars____________________________

        (mouseX, mouseY) = pygame.mouse.get_pos()
        #Import images_______________________________

        if charColorSin == "red" and firstRunStart and singleplayerCheck == True and level2Start == False:

            PlayerLeft = pygame.image.load("img/char/PlayerModel_Left_Glock_Original.png")
            PlayerLeft = pygame.transform.scale(PlayerLeft, (88,96))
            PlayerLeftShooting = pygame.image.load("img/char/PlayerModel_Left_Glock_Firing.png")
            PlayerLeftShooting = pygame.transform.scale(PlayerLeftShooting, (88,96))
            PlayerRight = pygame.image.load("img/char/PlayerModel_Right_Glock_Original.png")
            PlayerRight = pygame.transform.scale(PlayerRight, (88,96))
            PlayerRightShooting = pygame.image.load("img/char/PlayerModel_Right_Glock_Firing.png")
            PlayerRightShooting = pygame.transform.scale(PlayerRightShooting, (88,96))
            currentPlayer = PlayerLeft
            firstRunStart = False

            
        elif charColorSin == "blue" and firstRunStart and singleplayerCheck == True and level2Start == False:
            PlayerLeft = pygame.image.load("img/char/2_PlayerModel_Left_Glock_Original.png")
            PlayerLeft = pygame.transform.scale(PlayerLeft, (88,96))
            PlayerLeftShooting = pygame.image.load("img/char/2_PlayerModel_Left_Glock_Firing.png")
            PlayerLeftShooting = pygame.transform.scale(PlayerLeftShooting, (88,96))
            PlayerRight = pygame.image.load("img/char/2_PlayerModel_Right_Glock_Firing.png")
            PlayerRight = pygame.transform.scale(PlayerRight, (88,96))
            PlayerRightShooting = pygame.image.load("img/char/2_PlayerModel_Right_Glock_Firing.png")
            PlayerRightShooting = pygame.transform.scale(PlayerRightShooting, (88,96))
            currentPlayer = PlayerLeft
            firstRunStart = False
        

        if mouseX > playerX + 88 and isShooting == False and singleplayerCheck == True and level2Start == False:
            currentPlayer = PlayerRight
            direction = "Right"
            
        if mouseX < playerX and isShooting == False and singleplayerCheck == True and level2Start == False:
            currentPlayer = PlayerLeft
            direction = "Left"
  
        keys=pygame.key.get_pressed()
        if keys[K_w] and singleplayerCheck == True and level2Start == False:
            playerY = playerY - 15
            wClicked = True
        if keys[K_a] and singleplayerCheck == True and level2Start == False:
            playerX = playerX - 15
            aClicked = True
        if keys[K_s] and singleplayerCheck == True and level2Start == False:    
            playerY = playerY + 15
            sClicked = True
        if keys[K_d] and singleplayerCheck == True and level2Start == False:    
            playerX = playerX + 15
            dClicked = True
        if keys[K_p] and singleplayerCheck == True and level2Start == False:
            print(playerX, playerY)

        if playerX >= screenWidth-230 and singleplayerCheck == True and level2Start == False:
            playerX = screenWidth-230
        if playerX <= 150 and singleplayerCheck == True and level2Start == False:
            playerX = 150
        if playerY <= 60 and singleplayerCheck == True and level2Start == False:
            playerY = 60
        if playerY>=screenHeight-270 and singleplayerCheck == True and level2Start == False:
            playerY = screenHeight-270
            

  
        playerSprite = screen.blit(currentPlayer,(playerX,playerY))

            
        if wClicked == True and aClicked == True and sClicked == True and dClicked == True and singleplayerCheck == True and level2Start == False:
            allPressed = True
        if allPressed == False and singleplayerCheck == True and level2Start == False:
            instructionB1 = defaultFont.render("Use 'WASD' to move", 1, (255,255,255))
            screen.blit(instructionB1, (screenWidth/2-350,screenHeight/2-250))
        if allPressed == True and mouseClicked == False and singleplayerCheck == True and level2Start == False:
            instructionB2 = defaultFont.render("Left click to shoot", 1, (255,255,255))
            screen.blit(instructionB2, (screenWidth/2-350,screenHeight/2-250))
        if allPressed == True and mouseClicked == True and onFirst and singleplayerCheck == True and level2Start == False:
            instructionB3 = defaultFont.render(textSample1, 1, (255,255,255))
            screen.blit(instructionB3, (screenWidth/2-550,screenHeight/2-250))
        if allPressed == True and mouseClicked == True and onFirst and playerX == screenWidth-230 and playerY == screenHeight - 550 and singleplayerCheck == True and level2Start == False:
            level2Start = True
            singleplayerCheck = False
            
        pygame.display.flip()


    #Health__________________________________________
    if health == 3:
        screen.blit(hearts3,(0,0))
    elif health == 2.5:
        screen.blit(hearts25,(5,5))
    elif health == 2:
        screen.blit(hearts2,(5,5))
    elif health == 1.5:
        screen.blit(hearts15,(5,5))
    elif health == 1:
        screen.blit(hearts1,(5,5))
    elif health == 0.5:
        screen.blit(hearts05,(5,5))
        
#Credits______________________________________________
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
            
    elif buttonPlayCheck == True:
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
            
    elif singleplayerPlayerSelect:
        if bluePlayBlit.collidepoint(pygame.mouse.get_pos()):
            currentBluePlay = bluePlayOH
        else:
            currentBluePlay = bluePlay
            
        if redPlayBlit.collidepoint(pygame.mouse.get_pos()):
            currentRedPlay = redPlayOH
        else:
            currentRedPlay = redPlay
    elif creditsCheck == True:
        if backB.collidepoint(pygame.mouse.get_pos()):
            currentBackB = backButOH
        else:
            currentBackB = backBut

        
    #Events______________________________________
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
           if singleplayerCheck == True: 
               mouseClicked = True
               onFirst = True
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



           if level2Start:
               pistolBang = pygame.mixer.Sound(pistolShot)
               pistolBang.play(0)
               checkTimeNow = True
               if checkTimeNow:
                    now = pygame.time.get_ticks()
                    change = now + 200
                    checkTimeNow = False
               if direction == "Left":
                    isShooting = True
                    currentPlayer = PlayerLeftShooting
                    checkTheTime = True
               elif direction == "Right":
                    isShooting = True
                    currentPlayer = PlayerRightShooting
                    checkTheTime = True
                    
               if playerY > skeletonLvl21Y and playerY+96 < skeletonLvl21Y+171:
#                   if skeletonLvl21Health > 0 and skeletonLvl21X + playerX < skeletonLvl22X + playerX:
                   if skeletonLvl21X > playerX and direction == "Right":
                       skeletonLvl21Health = skeletonLvl21Health - 1
                   elif skeletonLvl21X < playerX and direction == "Left":
                       skeletonLvl21Health = skeletonLvl21Health - 1

               if playerY > skeletonLvl22Y and playerY+96 < skeletonLvl22Y+171:
#                   if skeletonLvl22Health > 0 and skeletonLvl22X + playerX < skeletonLvl21X + playerX:
                   if skeletonLvl22X > playerX and direction == "Right":
                       skeletonLvl22Health = skeletonLvl22Health - 1
                   elif skeletonLvl22X < playerX and direction == "Left":
                       skeletonLvl22Health = skeletonLvl22Health - 1

               if playerY > skeletonLvl23Y and playerY+96 < skeletonLvl23Y+171:
#                   if skeletonLvl23Health > 0 and skeletonLvl23X + playerX < skeletonLvl24X + playerX:
                   if skeletonLvl23X > playerX and direction == "Right":
                       skeletonLvl23Health = skeletonLvl23Health - 1
                   elif skeletonLvl23X < playerX and direction == "Left":
                       skeletonLvl23Health = skeletonLvl23Health - 1

               if playerY > skeletonLvl24Y and playerY+96 < skeletonLvl24Y+171:
#                   if skeletonLvl24Health > 0 and skeletonLvl24X + playerX < skeletonLvl23X + playerX:
                   if skeletonLvl24X > playerX and direction == "Right":
                       skeletonLvl24Health = skeletonLvl24Health - 1
                   elif skeletonLvl24X < playerX and direction == "Left":
                       skeletonLvl24Health = skeletonLvl24Health - 1
                       

                    
           elif singleplayerCheck == True:
               pistolBang = pygame.mixer.Sound(pistolShot)
               pistolBang.play(0)
               checkTimeNow = True
               if checkTimeNow:
                    now = pygame.time.get_ticks()
                    change = now + 200
                    checkTimeNow = False
               if direction == "Left":
                    isShooting = True
                    currentPlayer = PlayerLeftShooting
                    checkTheTime = True
               elif direction == "Right":
                    isShooting = True
                    currentPlayer = PlayerRightShooting
                    checkTheTime = True
##                        currentPlayer = PlayerRight

        #Quit___________________________
        if event.type == pygame.QUIT:
            mainloop = False
            
        elif event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_ESCAPE:
                """if singleplayerCheck:
                    pauseMenu = True
                if pauseMenu:
                    singleplayerCheck = True
                    pauseMenu = False"""
                
            elif event.key == pygame.K_UP:
                if menuB > 0: 
                    menuB = menuB - 1
                    print(menuB)
                    
            elif event.key == pygame.K_DOWN:
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

Instructions Level 2:
    - Shoot at enemies to kill them
    - Lean-Aid Refills Some Health
    - Kill all enemies to get door key

    
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
