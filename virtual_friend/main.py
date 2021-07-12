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
clock = pygame.time.Clock()

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
    if man1.resting:
        drawRestingAnimation(win, man1)

    elif man1.yesKnocking:
        drawYesKnockingAnimation(win, man1)

    elif man1.noKnocking:
        drawNoKnockingAnimation(win, man1)

    elif man1.sleeping:
        drawSleepingAnimation(win, man1)
    
    elif man1.goingLeft:
        drawGoingLeftAnimation(win, man1)
    
    elif man1.goingRight:
        drawGoingRightAnimation(win, man1)

    else:
        drawRestingAnimation(win, man1)
        #drawRectangle(win, man1.color, man1.x, man1.y, man1.width, man1.height)
    #-----------
    pygame.display.update()

def mainWhileLoop():
    run = True
    clock.tick(60)
    #releasedKeys = False
    man1 = Character(colors_palette2["color1"])

    while run:    
        pygame.time.delay(0)

        # Check events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYUP:
                #releasedEvent = event.key
                if event.key == pygame.K_w:
                    man1.resting = True
                    man1.yesKnocking = False
                    man1.noKnocking = False
                    man1.sleeping = False
                    man1.goingLeft = False
                    man1.goingRight = False
                if event.key == pygame.K_s:
                    man1.resting = True
                    man1.yesKnocking = False
                    man1.noKnocking = False
                    man1.sleeping = False
                    man1.goingLeft = False
                    man1.goingRight = False
                if event.key == pygame.K_a:
                    man1.resting = True
                    man1.yesKnocking = False
                    man1.noKnocking = False
                    man1.sleeping = False
                    man1.goingLeft = False
                    man1.goingRight = False
                if event.key == pygame.K_d:
                    man1.resting = True
                    man1.yesKnocking = False
                    man1.noKnocking = False
                    man1.sleeping = False
                    man1.goingLeft = False
                    man1.goingRight = False
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_w:
            #         #y-=1
            #     if event.key == pygame.K_s:
            #         #y+=1
            #     if event.key == pygame.K_a:
            #         #x-=1
            #     if event.key == pygame.K_d:
                    #x+=1

        #man1.setDirection(x,y)
        #----------- Events    
        checkForPlayerEvents(win, man1)

        # The fillScreen, drawings and updates, is in another func
        redrawGameWindow(win, man1)
        

    pygame.quit()

mainWhileLoop()