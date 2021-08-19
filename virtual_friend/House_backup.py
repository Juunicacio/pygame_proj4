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

        #self.doorHitBox = None

        self.imageRect = createListOfAnimatedImgs(House.PATH_FOR_ASSETS_FOLDER, None, self.houseName)
        self.hitBox = self.returnBoxCollider()
        self.doorHitBox = self.returnDoorBox()
        
        self.houseImg = createListOfAnimatedImgs(
            House.PATH_FOR_ASSETS_FOLDER, None, self.houseName)

    def drawHouse(self, window):
        window.blit(self.houseImg, (self.x, self.y))
        self.collide(window)
    
    #def drawRectangle(window, color, xposition, yposition, width, height):
        #rect = pygame.draw.rect(window, color, (xposition, yposition, width, height))
        #return rect
    
    def returnBoxCollider(self):
        hitBox = self.imageRect.get_rect()
        hitBox.x = self.x
        hitBox.y = self.y
        hitBox.width = 54
        hitBox.height = 59
        if self.houseKind == 1:
            hitBox.x = self.x + 8
            return hitBox
        if self.houseKind == 2:
            hitBox.x = self.x + 7
            hitBox.y = self.y + 10
            hitBox.width = 51
            hitBox.height = 48
            return hitBox
    
    def returnDoorBox(self):
        doorHitBox = self.imageRect.get_rect()
        if self.houseKind == 1:
            doorHitBox.x = self.x + 23
            doorHitBox.y = self.y + 45
            doorHitBox.width = 10
            doorHitBox.height = 13
            return doorHitBox
        if self.houseKind == 2:
            doorHitBox.x = self.x + 35
            doorHitBox.y = self.y + 45
            doorHitBox.width = 10
            doorHitBox.height = 13
            return doorHitBox

    def collide(self, window):
        rectCollide(window, (255, 255, 255), (self.doorHitBox))
        #drawRectangle(window, color, xposition, yposition, width, height)
        rectCollide(window, (255, 255, 255), (self.hitBox))
    
    def getHit(self):
        print('House hit')