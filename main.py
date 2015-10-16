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
mainCheck = True
mainGame = False

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

###____________________________________Init___________________________________________________####
coords = pygame.mouse.get_pos()
screen = pygame.display.set_mode((screenWidth, screenHeight),pygame.FULLSCREEN, 32)
background = pygame.Surface(screen.get_size())
screen.blit(startBack,(0,0))
currentCred = creditsBut
currentSet = settingsBut
currentStr = startBut
mainMenu = True
pygame.mouse.set_visible(True)
#Pygame clock 
clock = pygame.time.Clock()
FPS = 30
playtime = 0.0


###____________________________________Functions_______________________________________________####
def quit_game():
    pygame.quit()

###____________________________________Game Loop_______________________________________________####
while mainGame:
    star = screen.blit(currentStr,(screenWidth/2 -268.5,screenHeight-700))

###____________________________________Loop__________________________________________________####
while mainMenu:
    #Framrate________________________________________
    milliseconds = clock.tick(FPS)
    playtime += milliseconds / 1000.0
    #Blit buttons_____________________________________
    if mainCheck == True:
        cred = screen.blit(currentCred,(screenWidth/2 -268.5,screenHeight-300))
        sets = screen.blit(currentSet,(screenWidth/2 -268.5,screenHeight-500))
        star = screen.blit(currentStr,(screenWidth/2 -268.5,screenHeight-700))
    #Title___________________________________________
        screen.blit(title,(screenWidth/2 -620,screenHeight-1000))
    #Hover detection__________________________________
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
               mainMenu = False
               mainGame = True
               screen.blit(startBack, (0,0))
               
        # User presses QUIT-button.
        if event.type == pygame.QUIT:
            mainloop = False
        elif event.type == pygame.KEYDOWN:
            # User presses ESCAPE-Key
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
    FPSS
    USERNAME (SAVE IN FILE)
    RES
    WASD OR ARROW KEYS?
    TURN MUSIC ON OR OFF
    TURN SOUND FX ON OR OFF
"""
 
