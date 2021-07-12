import pygame
import os

def drawRectangle(window, color, xposition, yposition, width, height):
    rect = pygame.draw.rect(window, color, (xposition, yposition, width, height))
    return rect

def checkForPlayerEvents(window, player):#, keyup=None):
    keys = pygame.key.get_pressed()
    if keys:
        try:
            # Moving
            if keys[pygame.K_a] and (player.x > player.vel):
                player.x -= player.vel               
                player.resting = False
                player.yesKnocking = False
                player.noKnocking = False
                player.sleeping = False
                player.goingLeft = True
                player.goingRight = False                    
                
            elif keys[pygame.K_d] and (player.x < window.get_width() - player.width - player.vel):
                player.x += player.vel
                player.resting = False
                player.yesKnocking = False
                player.noKnocking = False
                player.sleeping = False
                player.goingLeft = False
                player.goingRight = True
                
            elif keys[pygame.K_w] and (player.y > player.vel):
                player.y -= player.vel
                player.resting = False
                player.yesKnocking = False
                player.noKnocking = False
                player.sleeping = False
                player.goingLeft = False
                player.goingRight = False
                
            elif keys[pygame.K_s] and (player.y < window.get_height() - player.height - player.vel):
                player.y += player.vel
                player.resting = False
                player.yesKnocking = False
                player.noKnocking = False
                player.sleeping = False
                player.goingLeft = False
                player.goingRight = False
            
            # Standing                
            elif keys[pygame.K_p]:
                player.resting = False
                player.yesKnocking = False
                player.noKnocking = False
                player.sleeping = True
                player.goingLeft = False
                player.goingRight = False
            
            elif keys[pygame.K_y]:
                player.resting = False
                player.yesKnocking = True
                player.noKnocking = False
                player.sleeping = True
                player.goingLeft = False
                player.goingRight = False             
            
            elif keys[pygame.K_n]:
                player.resting = False
                player.yesKnocking = False
                player.noKnocking = True
                player.sleeping = False
                player.goingLeft = False
                player.goingRight = False        
        except:
            return False
    # if keyup != None:
    #     if keyup == pygame.K_a or keyup == pygame.K_d or keyup == pygame.K_w or keyup == pygame.K_s:
    #         player.resting = True
    #         player.yesKnocking = False
    #         player.noKnocking = False
    #         player.sleeping = False
    #         player.goingLeft = False
    #         player.goingRight = False
    else:
        # Breathing
        player.resting = True
        player.yesKnocking = False
        player.noKnocking = False
        player.sleeping = False
        player.goingLeft = False
        player.goingRight = False

def drawRestingAnimation(window, player):
    #if player.resting:
    #window.blit(player.restingImgs[player.idleCount//3], (player.x,player.y))
    window.blit(player.restingImgs[player.idleCount], (player.x,player.y))
    player.idleCount += 1
    if player.idleCount + 1 >= len(player.restingImgs):
        player.idleCount = 0

def drawYesKnockingAnimation(window, player):
    if player.yesKnocking:
        #window.blit(player.yesKnockingImgs[player.yesKnockCount//3], (player.x,player.y))
        window.blit(player.yesKnockingImgs[player.yesKnockCount], (player.x,player.y))
        player.yesKnockCount += 1
    if player.yesKnockCount + 1 >= len(player.yesKnockingImgs):
        player.yesKnockCount = 0

def drawNoKnockingAnimation(window, player):
    if player.noKnocking:
        #window.blit(player.noKnockingImgs[player.noKnockCount//3], (player.x,player.y))
        window.blit(player.noKnockingImgs[player.noKnockCount], (player.x,player.y))
        player.noKnockCount += 1
    if player.noKnockCount + 1 >= len(player.noKnockingImgs):
        player.noKnockCount = 0

def drawSleepingAnimation(window, player):
    if player.sleeping:
        #window.blit(player.sleepingImgs[player.sleepingCount//3], (player.x,player.y))
        window.blit(player.sleepingImgs[player.sleepingCount], (player.x,player.y))
        print(player.sleepingImgs[1])
        print(player.sleepingImgs[2])
        player.sleepingCount += 1
    if player.sleepingCount + 1 >= len(player.sleepingImgs):
        player.sleepingCount = 0

def drawGoingLeftAnimation(window, player):
    if player.goingLeft:
        #window.blit(player.goingLeftImgs[player.walkCount//3], (player.x,player.y))
        window.blit(player.goingLeftImgs[player.walkCount], (player.x,player.y))
        player.walkCount += 1
    if player.walkCount + 1 >= len(player.goingLeftImgs):
        player.walkCount = 0

def drawGoingRightAnimation(window, player):
    if player.goingRight:
        #window.blit(player.goingRightImgs[player.walkCount//3], (player.x,player.y))
        window.blit(player.goingRightImgs[player.walkCount], (player.x,player.y))
        player.walkCount += 1
    if player.walkCount + 1 >= len(player.goingRightImgs):
        player.walkCount = 0

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