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

#Import
startBack = pygame.image.load("img/StartScreenBackground.jpg")


#Vars
infoObject = pygame.display.Info()
screenWidth, screenHeight = infoObject.current_w, infoObject.current_h
menuB = 0

# init
screen = pygame.display.set_mode((screenWidth, screenHeight), pygame.FULLSCREEN, 32)
background = pygame.Surface(screen.get_size())
screen.blit(startBack,(0,0))
mainMenu = True

# Pygame clock 
clock = pygame.time.Clock()
 

# Desired framerate in frames per second. Try out other values.
FPS = 30

# How many seconds played
playtime = 0.0
 
 
while mainMenu:
    # Do not go faster than this framerate.
    milliseconds = clock.tick(FPS)
    playtime += milliseconds / 1000.0
 
    for event in pygame.event.get():
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
 
