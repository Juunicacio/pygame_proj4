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

        self.defaultImg = 'restingNPC1.png'
        self.imageRect = createListOfAnimatedImgs(Npc.PATH_FOR_RESTING_NPC_FOLDER, None, self.defaultImg)
        self.hitBox = self.imageRect.get_rect()

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
        self.drawCollider(window, self.restingNPCImgs, self.idleCount, self.spritesDelay)
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
    
    def drawCollider(self, window, imgFolder, count, spritesDelay):
        self.imageRect = imgFolder[count//spritesDelay]
        self.hitBox = self.imageRect.get_rect()
        self.hitBox.center = self.width//2, self.height//2
        # self.hitBox.x = self.x + 21
        # self.hitBox.y = self.y + 14
        # self.hitBox.width = 22
        # self.hitBox.height = 22       
        
        #if imgFolder == self.goingRightImgs:
            ##self.hitBox.x = self.x + (self.hitBox.center[0]/.95)
            #self.hitBox.x = self.x + (self.hitBox.width/2.4)
        #else:
        self.hitBox.x = self.x + (self.hitBox.width/2.8)        
        self.hitBox.y = self.y + (self.hitBox.height/4.3)
        
        self.hitBox.width = (self.hitBox.width/3)
        self.hitBox.height = (self.hitBox.height/3)
        rectCollide(window, (255, 255, 255), (self.hitBox))
    
    def getHit(self):
        print('Npc hit')