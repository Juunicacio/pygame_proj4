from functions import *
class House:
    """Main House class"""
    
    PATH_FOR_ASSETS_FOLDER = accessAssetsFolder()
    
    def __init__(self, x, y, width, height, fileName, playersHouse=False, houseKind=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.houseName = fileName
        self.playersHouse = False
        self.houseKind = houseKind
        
        self.houseImg = createListOfAnimatedImgs(
            House.PATH_FOR_ASSETS_FOLDER, None, self.houseName)

    def drawHouse(self, window):
        window.blit(self.houseImg, (self.x, self.y))
        self.collide(window, self.houseImg)
    
    #def drawRectangle(window, color, xposition, yposition, width, height):
        #rect = pygame.draw.rect(window, color, (xposition, yposition, width, height))
        #return rect

    def collide(self, window, img):
        self.imageRect = img
        self.hitBox = self.imageRect.get_rect()
        self.hitBox.x = self.x
        self.hitBox.y = self.y
        self.hitBox.width = 54
        self.hitBox.height = 59
        self.doorHitBox = self.imageRect.get_rect()
        if self.houseKind == 1:
            self.hitBox.x = self.x + 8
            self.doorHitBox.x = self.x + 23
            self.doorHitBox.y = self.y + 45
            self.doorHitBox.width = 10
            self.doorHitBox.height = 13
            rectCollide(window, (255, 255, 255), (self.doorHitBox))
            #drawRectangle(window, color, xposition, yposition, width, height)
            rectCollide(window, (255, 255, 255), (self.hitBox))
        if self.houseKind == 2:
            self.hitBox.x = self.x + 7
            self.hitBox.y = self.y + 10
            self.hitBox.width = 51
            self.hitBox.height = 48
            self.doorHitBox.x = self.x + 35
            self.doorHitBox.y = self.y + 45
            self.doorHitBox.width = 10
            self.doorHitBox.height = 13
            rectCollide(window, (255, 255, 255), (self.doorHitBox))
            #drawRectangle(window, color, xposition, yposition, width, height)
            rectCollide(window, (255, 255, 255), (self.hitBox))