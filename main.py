from __future__ import print_function
import pygame

 
pygame.init()
#Vars
infoObject = pygame.display.Info()
screenWidth, screenHeight = infoObject.current_w, infoObject.current_h


# init
screen = pygame.display.set_mode((screenWidth, screenHeight), pygame.FULLSCREEN, 32)
background = pygame.Surface(screen.get_size())
background.fill((255, 255, 255))
background = background.convert()
screen.blit(background, (0,0))
screen.blit(background, (50,50))
mainloop = True

# Pygame clock 
clock = pygame.time.Clock()
 

# Desired framerate in frames per second. Try out other values.
FPS = 30

# How many seconds played
playtime = 0.0
 
 
while mainloop:
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
            if event.key == pygame.K_r:
                text = " OMG this Works!"
 
    #Playtime: {1:.2f}".format(clock.get_fps(), playtime)
    
 
    #Update Pygame display.
    pygame.display.flip()
 
# Finish Pygame.
pygame.quit()
 
