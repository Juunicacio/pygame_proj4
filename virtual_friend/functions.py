import pygame
import os

# def buttonGetTime(button, buttonName):
#     button = pygame.time.get_ticks() - gameStartTime
#     # calculate the difference, i.e. the time elapsed
#     print(f"{buttonName} button was pressed for {button}")

def drawRectangle(window, color, xposition, yposition, width, height):
    # draw Rectangle not filled in
    rect = pygame.draw.rect(window, color, (xposition, yposition, width, height), 1)
    return rect

def rectCollide(window, color, rect):
    # draw Rectangle not filled in
    rect = pygame.draw.rect(window, color, (rect.x, rect.y, rect.width, rect.height), 1)
    return rect

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

def createListOfAnimatedImgs(folderNameInAssetsFolder, action=None, fileNameInAssetsFolder=''):
    if action == None:
        image = pygame.image.load(os.path.join(folderNameInAssetsFolder, fileNameInAssetsFolder))
        return image    
    elif fileNameInAssetsFolder == '':
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