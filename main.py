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
#Music
menuMusic = "snd/Menu.ogg"
gameMusic = "snd/In_Game.mp3"
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
pygame.mouse.set_visible(True)
#Pygame clock 
clock = pygame.time.Clock()
FPS = 30
playtime = 0.0
singleplayerCheck = False


pygame.mixer.init()
menuSound = pygame.mixer.Sound(menuMusic)
menuSound.play(loops = -1)


###____________________________________Functions_______________________________________________####
def quitGame():
    pygame.quit()
    



###____________________________________Loop__________________________________________________####
while mainMenu:
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
        

    if singleplayerCheck:
        print("worked")
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

        
    #Events______________________________________
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            
           if currentCred ==  creditsButOH:
               mainCheck = False
               screen.blit(startBack,(0,0))
               
           if currentSet == settingsButOH:
               mainCheck = False
               screen.blit(startBack, (0,0))
               
           if currentStr == startButOH:
               mainCheck = False
               buttonMainCheck = False
               buttonPlayCheck = True
               singleplayerCheck = False
               currentStr = startBut

           if currentBackB == backButOH:
               mainCheck = True
               buttonMainCheck = True
               buttonPlayCheck = False
               singleplayerCheck = False
               currentBackB = backBut

           if currentQ == quitButOH:
               quitGame()

           if currentSingle == singleplayerButOH:
               mainCheck = False
               buttonMainCheck = False
               buttonPlayCheck = False
               singleplayerCheck = True
               currentSingle = singleplayerButOH
        #Quit__________________________________
        if event.type == pygame.QUIT:
            mainloop = False
            
        elif event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_ESCAPE:
                mainloop = False
                
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
