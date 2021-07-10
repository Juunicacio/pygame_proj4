from functions import drawRectangle
import pygame
import os
from Character import Character
from functions import *
from palettes import colors_palette1, colors_palette2, colors_palette3
pygame.init()

chose_palette_game = colors_palette2

WIDTH, HEIGHT = 1000, 500

PATH_FOR_ASSETS_FOLDER = accessAssetsFolder()
# House - Scaled Backgrounds
FARM_HOUSE = pygame.image.load(os.path.join(PATH_FOR_ASSETS_FOLDER, 'farm_house.png'))

# make a window
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Virtual Friend")

def redrawGameWindow(win, man1):
    # we need to be changing this global variable
    global frameCount
    #----------- Fill BackScreen    
    # before drawing, fill the screen
    win.fill((colors_palette3["color2"]))
    # to use a background img, use #win.blit(yourbgimgnamehere, (wherex,wherey))
    #----------- All that will be on the screen
    # to show selected palette
    #showPalette(win, chose_palette_game)    
    ##### to draw player_rect on the screen
    #####drawRectangle(win, man1.color, man1.x, man1.y, man1.width, man1.height)
    # draw the actual player
    if man1.idleCount + 1 >= len(man1.restingImgs):
        man1.resetIdleCount(0)
    if man1.resting:
        win.blit(man1.restingImgs[man1.idleCount//3], (man1.x,man1.y))
        man1.updateIdleCount(1)
    
    if man1.sleepingCount + 1 >= len(man1.sleepingImgs):
        man1.resetSleepingCount(0)
    if man1.sleeping:
        win.blit(man1.sleepingImgs[man1.sleepingCount//3], (man1.x,man1.y))
        man1.updateSleepingCount(1)

    else:
        win.blit(man1.restingImgs[man1.idleCount//3], (man1.x,man1.y))
        man1.updateIdleCount(1)
        #drawRectangle(win, man1.color, man1.x, man1.y, man1.width, man1.height)
    #-----------
    pygame.display.update()

def mainWhileLoop():
    run = True
    while run:    
        pygame.time.delay(0)

        # Check events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False     

        man1 = Character(colors_palette2["color1"])

        #----------- Events    
        checkForPlayerEvents(man1, win)

        # The fillScreen, drawings and updates, is in another func
        redrawGameWindow(win, man1)
        

    pygame.quit()

mainWhileLoop()