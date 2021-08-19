import pygame
import os
import sys

from pygame.constants import KEYDOWN, K_ESCAPE, MOUSEBUTTONDOWN
#from functions import drawRectangle
from Character import Character
from House import House
from Npc import Npc
from GameTime import GameTime
from HitOrContacts import HitOrContacts
from World import World
from functions import *
from palettes import colors_palette1, colors_palette2, colors_palette3
pygame.font.init()
pygame.init()

chose_palette_game = colors_palette2

WIDTH, HEIGHT = 1000, 500
# define game variables
tile_size = 64
# 25 tiles on width and 13 tiles on height
# level data
world_data = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
]

PATH_FOR_ASSETS_FOLDER = accessAssetsFolder()
# House - Scaled Backgrounds
FARM_HOUSE = pygame.image.load(os.path.join(PATH_FOR_ASSETS_FOLDER, 'farm_house.png'))

# make a window
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Virtual Friend")

clock = pygame.time.Clock()
FPS = 60

# get the mouse position
mx, my = pygame.mouse.get_pos()

# fonts
mainFont = pygame.font.SysFont('Verdana', 30, bold=True)
#mainFont = pygame.font.SysFont('Raleway', 30, bold=True)
#mainFont = pygame.font.SysFont('arial', 35)
#mainFont = pygame.font.SysFont("comicsans", 35)

def redrawGameWindow(win, man1, house1, mainFont, house2, femaleNPC, world):
    #----------- Fill BackScreen    
    # before drawing, fill the screen
    win.fill((colors_palette3["color2"]))
    # to use a background img, use #win.blit(yourbgimgnamehere, (wherex,wherey))

    #----------- All that will be on the screen
    # to show selected palette
    #showPalette(win, chose_palette_game)

    # draw grid
    draw_grid(win, colors_palette1["color6"], tile_size, WIDTH, HEIGHT)
    
    # draw house
    house1.drawHouse(win)
    house2.drawHouse(win)

    # draw path
    world.drawPath(win)
    
    # to draw player_rect on the screen
    #drawRectangle(win, man1.color, man1.x, man1.y, man1.width, man1.height)
    # draw the actual player
    man1.drawActualPlayerWithAllAnimations(win)
    femaleNPC.drawNPCWithAllAnimations(win)
    # draw texts
    man1.drawtexts(win, mainFont, colors_palette1["color6"])

    
    
    

    #check for contacts between 2 objs
    HitOrContacts.checkForContacts(man1, house1)
    HitOrContacts.checkForContacts(man1, house2)
    HitOrContacts.checkForContacts(man1, femaleNPC)

    #----------- Key Pressed Events
    keys = pygame.key.get_pressed()    
    # change player coordinates
    man1.checkPressedKeys(win, keys)

    #-----------
    pygame.display.update()

def mainWhileLoop():
    run = True    
    man1 = Character(colors_palette2["color1"])
    house1 = House(450, 50, 64, 64, 'farm_house.png', True, 1)
    house2 = House(710, 50, 64, 64, 'farm_house2.png', False, 2)
    femaleNPC = Npc(800, 80)
    world = World(world_data, tile_size)

    while run:
        clock.tick(FPS)

        # if house1.collidepoint((mx, my)):
        #     if click:
        #         print("house 1 was clicked")
        #         # insideCharacterHouse()
        # if house2.collidepoint((mx, my)):
        #     if click:
        #         print("house 2 was clicked")
        
        # click = False
        #pygame.time.delay(40)
        # Check events
        for event in pygame.event.get():            
            if event.type == pygame.QUIT:
                run = False
            # if event.type == MOUSEBUTTONDOWN:
            #     if event.button == 1:
            #         click = True
            man1.checkForKeyUp(event)

        

        

        # starts also the time for the player rest
        GameTime.buttonGetTime(man1, 'sleeping', man1.sleeping)

        # The fillScreen, drawings and updates, is in this func 'redrawGameWindow'
        redrawGameWindow(win, man1, house1, mainFont, house2, femaleNPC, world)

    pygame.quit()


def redrawHouseWindow(win):
    #----------- Fill BackScreen 
    win.fill((colors_palette3["color3"]))

def insideCharacterHouse():
    inside = True
    while inside:
        for event in pygame.event.get():            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    inside = False
        
        redrawHouseWindow(win)

        clock.tick(FPS)
        pygame.display.update()


mainWhileLoop()