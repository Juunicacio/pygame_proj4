from functions import *
class Character:
    """Main Character class"""

    PATH_FOR_RESTING_FOLDER = accessAssetsFolder("resting")
    PATH_FOR_YESKNOCKING_FOLDER = accessAssetsFolder("yesKnocking")
    PATH_FOR_NOKNOCKING_FOLDER = accessAssetsFolder("noKnocking")
    PATH_FOR_SLEEPING_FOLDER = accessAssetsFolder("sleeping")
    PATH_FOR_GOING_LEFT_FOLDER = accessAssetsFolder("goingLeft")
    PATH_FOR_GOING_RIGHT_FOLDER = accessAssetsFolder("goingRight")

    def __init__(self, color):
        self.direction = [0,0]
        self.x = 150
        self.y = 150
        self.width = 64
        self.height = 64
        self.vel = 1
        self.color = color

        self.resting = False
        self.yesKnocking = False
        self.noKnocking = False
        self.sleeping = False
        self.goingLeft = False
        self.goingRight = False
        
        self.idleCount = 0   
        self.yesKnockCount = 0
        self.noKnockCount = 0
        self.sleepingCount = 0
        self.walkCount = 0
        

        # Player Animations
        self.restingImgs = createListOfAnimatedImgs(
            Character.PATH_FOR_RESTING_FOLDER, 'resting')
        self.yesKnockingImgs = createListOfAnimatedImgs(
            Character.PATH_FOR_YESKNOCKING_FOLDER, 'yesKnocking')
        self.noKnockingImgs = createListOfAnimatedImgs(
            Character.PATH_FOR_NOKNOCKING_FOLDER, 'noKnocking')
        self.sleepingImgs = createListOfAnimatedImgs(
            Character.PATH_FOR_SLEEPING_FOLDER, 'sleeping')
        self.goingLeftImgs = createListOfAnimatedImgs(
            Character.PATH_FOR_GOING_LEFT_FOLDER, 'goingLeft')
        self.goingRightImgs = createListOfAnimatedImgs(
            Character.PATH_FOR_GOING_RIGHT_FOLDER, 'goingRight')

    def setDirection(self,x,y):
        self.direction = [x,y]
        

    
    