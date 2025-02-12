#Shay VanLandschoot
#2/12/25
#pygame template 1.0

import pygame , sys

#--- Constant ---#

width = 800
hight = 600
title = 'pygame template'

fps = 60

white= (255, 255, 255) #RGB triplet saved in a tuple

#--- Initialize pygame ---#

pygame.init()

#--- screen setup ---#

screen = pygame.display.set_mode((width, hight))
pygame.display.set_caption(title)

#--- clock setup ---#

clock = pygame.time.Clock()  #capital C is imporint

#--- game loop ---#

running = True
while running:
    #---listen for and handle events---#
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Type the QUIT in uppercase
            running = False

    #--- Game Logic ---#
    # (put all your game logic here)

    #--- Draw ---#

    screen.fill(white) # fills the backround with white

    # all drawing for the game gose here 

    pygame.display.flip()

    #--- Limit Fps ---#
    clock.tick(fps)
#--- Quit pygame and exit system module ---#
pygame.quit()
sys.exit()