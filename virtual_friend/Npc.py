from functions import *
class Npc:
    """Main NPC class"""
    PATH_FOR_RESTING_NPC_FOLDER = accessAssetsFolder("restingNPC")

    def __init__(self, x, y):
        #self.direction = [0,0]
        self.x = x
        self.y = y
        self.width = 64
        self.height = 64

        self.resting = False

        self.idleCount = 0

        self.spritesDelay = 5

        # Player Animations
        self.restingNPCImgs = createListOfAnimatedImgs(
            Npc.PATH_FOR_RESTING_NPC_FOLDER, 'restingNPC')
    
    #------------ Each Animation Per Time -----------------------------------------
    def drawRestingNPCAnimation(self, window):
        #if self.resting:
        window.blit(self.restingNPCImgs[self.idleCount//self.spritesDelay], (self.x,self.y))
        #window.blit(self.restingImgs[self.idleCount], (self.x,self.y))
        self.collide(window, self.restingNPCImgs, self.idleCount, self.spritesDelay)
        self.idleCount += 1
        # I've 17 imgs in my folder, multiplying it for 3 = 51, each img is running at 51 fps
        #but instead of multiplying it per 3, I've used 100
        if self.idleCount + 1 >= len(self.restingNPCImgs)*self.spritesDelay:
            self.idleCount = 0
    
    def drawNPCWithAllAnimations(self, window):
        if self.resting:
            self.drawRestingNPCAnimation(window)
        else:
            self.drawRestingNPCAnimation(window)
    
    def collide(self, window, imgFolder, count, spritesDelay):
        self.imageRect = imgFolder[count//spritesDelay]
        self.hitBox = self.imageRect.get_rect()
        self.hitBox.x = self.x + 21
        self.hitBox.y = self.y + 14
        self.hitBox.width = 22
        self.hitBox.height = 22
        rectCollide(window, (255, 255, 255), (self.hitBox))
    
    def getHit(self):
        print('hit')