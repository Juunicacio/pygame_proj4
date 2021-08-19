import pygame
import os

def draw_grid(window, color, tile_size, window_width, window_height):
    for line in range(0,25):
        pygame.draw.line(window, color, (0, line * tile_size), (window_width, line * tile_size))
        pygame.draw.line(window, color, (line * tile_size, 0), (line * tile_size, window_height))

# def buttonGetTime(button, buttonName):
#     button = pygame.time.get_ticks() - gameStartTime
#     # calculate the difference, i.e. the time elapsed
#     print(f"{buttonName} button was pressed for {button}")

def drawRectangle(window, color, xposition, yposition, width, height):
    # draw Rectangle not filled in, with 4 arg: x, y, w and h
    rect = pygame.draw.rect(window, color, (xposition, yposition, width, height), 1)
    return rect

def rectCollide(window, color, rect):
    # draw Rectangle not filled in, with rect arg
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

def createListOfAnimatedImgs(folderNameInAssetsFolder, action=None, fileNameInAssetsFolder=None, scaleImg='', newWidth='', newHeight=''):
    if action == None:
        image = pygame.image.load(os.path.join(folderNameInAssetsFolder, fileNameInAssetsFolder))
        #convert() optimizes the image format and makes drawing faster:
        image.convert()
        if scaleImg == '':                
                return image
        else:
            if newWidth != '' and newHeight != '':
                return pygame.transform.scale(image, (newWidth, newHeight))
            else:
                print('you need to assign a value for the new Width and Height of the scaled img')
    elif fileNameInAssetsFolder == None:
        i = 1
        listOfActionImgs = []
        #actionsCount = (len(os.listdir(folderNameInAssetsFolder)))
        while i <= len(os.listdir(folderNameInAssetsFolder)):        
            fileName = str(action) + str(i) + '.png'
            img = pygame.image.load(os.path.join(folderNameInAssetsFolder, fileName))
            #convert() optimizes the image format and makes drawing faster:
            img.convert()
            if scaleImg == '':
                listOfActionImgs.append(img)
                i+=1
            else:
                if newWidth != '' and newHeight != '':
                    listOfActionImgs.append(pygame.transform.scale(img, (newWidth, newHeight)))
                    i+=1
                else:
                    print('you need to assign a value for the new Width and Height of the scaled img')
                    break
        return listOfActionImgs