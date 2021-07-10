from functions import *
class Character:
    """Main Character class"""

    PATH_FOR_RESTING_FOLDER = accessAssetsFolder("resting")
    PATH_FOR_YESKNOCKHEAD_FOLDER = accessAssetsFolder("yesKnockHead")
    PATH_FOR_NOKNOCKHEAD_FOLDER = accessAssetsFolder("noKnockHead")
    PATH_FOR_SLEEPING_FOLDER = accessAssetsFolder("sleeping")
    startXPosition = 150
    startYPosition = 150
    startVel = 10

    resting = False
    yesKnockHead = False
    noKnockHead = False
    sleeping = False
    walkCount = 0
    idleCount = 0
    sleepingCount = 0

    @classmethod
    def updateX(cls, value):
        cls.startXPosition += value

    @classmethod
    def updateY(cls, value):
        cls.startYPosition += value
    
    @classmethod
    def nextLevel(cls, newSpeed):
        cls.startVel += newSpeed
    
    @classmethod
    def updateResting(cls, bool):
        cls.resting = bool
    
    @classmethod
    def updateYesKnockHead(cls, bool):
        cls.yesKnockHead = bool
    
    @classmethod
    def updateNoKnockHead(cls, bool):
        cls.noKnockHead = bool
    
    @classmethod
    def updateSleeping(cls, bool):
        cls.sleeping = bool
    
    @classmethod
    def updateWalkCount(cls, value):
        cls.walkCount += value
    
    @classmethod
    def resetWalkCount(cls, value):
        cls.walkCount = value
    
    @classmethod
    def updateIdleCount(cls, value):
        cls.idleCount += value
    
    @classmethod
    def resetIdleCount(cls, value):
        cls.idleCount = value
    
    @classmethod
    def updateSleepingCount(cls, value):
        cls.sleepingCount += value
    
    @classmethod
    def resetSleepingCount(cls, value):
        cls.sleepingCount = value

    def __init__(self, color):
        self.x = Character.startXPosition
        self.y = Character.startYPosition
        self.width = 64
        self.height = 64
        self.vel = Character.startVel
        self.color = color

        self.resting = Character.resting
        self.yesKnockHead = Character.yesKnockHead
        self.noKnockHead = Character.noKnockHead
        self.sleeping = Character.sleeping
        self.walkCount = Character.walkCount
        self.idleCount = Character.idleCount
        self.sleepingCount = Character.sleepingCount

        # Player Animations
        self.restingImgs = createListOfAnimatedImgs(Character.PATH_FOR_RESTING_FOLDER, 'resting')
        self.yesKnockHeadImgs = createListOfAnimatedImgs(Character.PATH_FOR_YESKNOCKHEAD_FOLDER, 'yesKnockHead')
        self.noKnockHeadImgs = createListOfAnimatedImgs(Character.PATH_FOR_NOKNOCKHEAD_FOLDER, 'noKnockHead')
        self.sleepingImgs = createListOfAnimatedImgs(Character.PATH_FOR_SLEEPING_FOLDER, 'sleeping')

    
    