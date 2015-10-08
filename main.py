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
import pygame
pygame.init()



#Vars
infoObject = pygame.display.Info()
screenWidth, screenHeight = infoObject.current_w, infoObject.current_h
menuB = 0
#mpos = pygame.mouse.get_pos()
###Import####
#Backgrounds
startBack = pygame.image.load("img/StartScreenBackground.jpg")
startBack = pygame.transform.scale(startBack, (screenWidth, screenHeight))
#Main Screen Buttons
creditsBut = pygame.image.load("img/Credits_Button.png")
newcreditsBut = pygame.transform.scale(creditsBut, (600, 400))
creditsRect = newcreditsBut.get_rect()
creditsButOH = pygame.image.load("img/Credits_Button_On_Hover.png")
creditsButOH = pygame.transform.scale(creditsButOH, (600, 400))
settingsBut = pygame.image.load("img/Settings_Button.png")
settingsBut = pygame.transform.scale(settingsBut, (600, 400))
settingsButOH = pygame.image.load("img/Settings_Button_On_Hover.png")
settingsButOH = pygame.transform.scale(settingsButOH, (600, 400))
startBut = pygame.image.load("img/Start_Button.png")
startBut = pygame.transform.scale(startBut, (600, 400))
startButOH = pygame.image.load("img/Start_Button_On_Hover.png")
startButOH = pygame.transform.scale(startButOH, (600, 400))
coords = pygame.mouse.get_pos()
# init
screen = pygame.display.set_mode((screenWidth, screenHeight),pygame.FULLSCREEN, 32)
background = pygame.Surface(screen.get_size())
screen.blit(startBack,(0,0))
currentCred = newcreditsBut
currentSet = settingsBut
currentStr = startBut
mainMenu = True
pygame.mouse.set_visible(True)


# Pygame clock 
clock = pygame.time.Clock()


# Desired framerate in frames per second
FPS = 30

# How many seconds played
playtime = 0.0
 
 
while mainMenu:
    #Lock Framrate
    milliseconds = clock.tick(FPS)
    playtime += milliseconds / 1000.0
    creddy = screen.blit(currentCred,(screenWidth/2 -300,screenHeight-400))
    screen.blit(currentSet,(screenWidth/2 -300,screenHeight-600))
    screen.blit(currentStr,(screenWidth/2 -300,screenHeight-800))
    if creddy.collidepoint(pygame.mouse.get_pos()):
        currentCred = creditsButOH
    else:
        currentCred = newcreditsBut
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
           print(pygame.mouse.get_pos())
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
    FPS
    USERNAME (SAVE IN FILE)
    RES
    WASD OR ARROW KEYS?
    TURN MUSIC ON OR OFF
    TURN SOUND FX ON OR OFF
"""
 
