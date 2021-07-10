import pygame
import os

def drawRectangle(window, color, xposition, yposition, width, height):
    rect = pygame.draw.rect(window, color, (xposition, yposition, width, height))
    return rect

def checkForPlayerEvents(player, window):
    keys = pygame.key.get_pressed()
    if keys:
        try:
            if keys[pygame.K_a] and (player.x > player.vel):
                player.updateX(-player.vel)
                #player.update(x, -player.vel)
                #player.x -= player.vel
                player.updateSleeping(False)
                #player.sleeping = False
                player.updateResting(False)
                #player.resting = False
                player.resetSleepingCount(0)
                #player.sleepingCount = 0
                player.resetIdleCount(0)
                #player.idleCount = 0        
                
            elif keys[pygame.K_d] and (player.x < window.get_width() - player.width - player.vel):
                player.updateX(player.vel)
                #player.update(x, player.vel)
                #player.x += player.vel
                player.updateSleeping(False)
                player.updateResting(False)
                player.resetSleepingCount(0)
                player.resetIdleCount(0)
                
            elif keys[pygame.K_w] and (player.y > player.vel):
                player.updateY(-player.vel)
                #player.update(y, -player.vel)
                #player.y -= player.vel
                player.updateSleeping(False)
                player.updateResting(False)
                player.resetSleepingCount(0)
                player.resetIdleCount(0)
                
            elif keys[pygame.K_s] and (player.y < window.get_height() - player.height - player.vel):
                player.updateY(player.vel)
                #player.update(y, player.vel)
                #player.y += player.vel
                player.updateSleeping(False)
                player.updateResting(False)
                player.resetSleepingCount(0)
                player.resetIdleCount(0)
                
            elif keys[pygame.K_p]:
                player.updateSleeping(True)
                player.resetWalkCount(0)
        
        except:
            return False
    else:
        player.updateResting(True)
        player.resetWalkCount(0)

def showPalette(window, chose_palette):
    # to draw palette colors on the screen
    x = 50
    y = 50
    w = 40
    h = 60
    i = 0
    for colors in chose_palette:
        drawRectangle(window, chose_palette[colors], x+w*i, y, w, h)
        i+=1

def accessAssetsFolder(folderName=''):
    ASSETS_FOLDER = os.path.join('virtual_friend', 'assets')
    FOLDER_INSIDE_ASSETS_FOLDER = os.path.join(ASSETS_FOLDER, folderName)
    if folderName == '':
        return ASSETS_FOLDER
    elif folderName != '':
        return FOLDER_INSIDE_ASSETS_FOLDER

def createListOfAnimatedImgs(folderNameInAssetsFolder, action):
    #print(len([name for name in os.listdir(folderNameInAssetsFolder)]))
    i = 1
    listOfActionImgs = []
    #actionsCount = (len(os.listdir(folderNameInAssetsFolder)))
    while i <= len(os.listdir(folderNameInAssetsFolder)):        
        fileName = str(action) + str(i) + '.png'
        listOfActionImgs.append(pygame.image.load(
                os.path.join(
                    folderNameInAssetsFolder, fileName
                )
            ))
        i+=1
    return listOfActionImgs