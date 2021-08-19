from functions import *
class Character:
    """Main Character class"""

    PATH_FOR_RESTING_FOLDER = accessAssetsFolder("resting")
    PATH_FOR_YESKNOCKING_FOLDER = accessAssetsFolder("yesKnocking")
    PATH_FOR_NOKNOCKING_FOLDER = accessAssetsFolder("noKnocking")
    PATH_FOR_SLEEPING_FOLDER = accessAssetsFolder("sleeping")
    PATH_FOR_GOING_LEFT_FOLDER = accessAssetsFolder("goingLeft")
    PATH_FOR_GOING_RIGHT_FOLDER = accessAssetsFolder("goingRight")
    PATH_FOR_GOING_DOWN_FOLDER = accessAssetsFolder("goingDown")
    PATH_FOR_GOING_UP_FOLDER = accessAssetsFolder("goingUp")

    def __init__(self, color):
        #self.direction = [0,0]
        # dx and dy to change player direction
        self.dx = 0
        self.dy = 0
        self.x = 150
        self.y = 150
        self.width = 64
        self.height = 64
        self.vel = 2

        #self.negativeDirection = 1
        #self.go = self.negativeDirection
        
        #self.speed = 1
        #self.vel = 1 + self.speed

        self.color = color

        self.defaultImg = 'resting1.png'
        # self.imageRect = <surface(64x64x32 SW)> # pygame.image.load() returns a pygame.Surface()
        self.image = createListOfAnimatedImgs(Character.PATH_FOR_RESTING_FOLDER, None, self.defaultImg, 'yes', 80, 80)
        # self.hitBox = <rect(171, 164, 22, 22)>
        self.hitBox = self.image.get_rect()
        # self.hitBox.x = self.x + 21
        # self.hitBox.y = self.y + 14
        # self.hitBox.width = 22
        # self.hitBox.height = 22
        self.collided = False

        self.energy = 100

        self.buttonSpawnTimer = 0
        self.buttonSpawnFrequency = 60000 # milliseconds = 1 minute # increase 10% of bar
        self.frequencyAchievement = 60000 # this updates inside the loop of a function
        self.stepsToFullBar = 1 # 5 steps = full bar

        self.resting = False
        self.yesKnocking = False
        self.noKnocking = False
        self.sleeping = False
        self.goingLeft = False
        self.goingRight = False
        self.goingDown = False
        self.goingUp = False
        
        self.idleCount = 0   
        self.yesKnockCount = 0
        self.noKnockCount = 0
        self.sleepingCount = 0
        self.walkCount = 0

        self.spritesDelay = 3    

        # Player Animations
        self.restingImgs = createListOfAnimatedImgs(
            Character.PATH_FOR_RESTING_FOLDER, 'resting', None, 'yes', 80, 80)
        self.yesKnockingImgs = createListOfAnimatedImgs(
            Character.PATH_FOR_YESKNOCKING_FOLDER, 'yesKnocking', None, 'yes', 80, 80)
        self.noKnockingImgs = createListOfAnimatedImgs(
            Character.PATH_FOR_NOKNOCKING_FOLDER, 'noKnocking', None, 'yes', 80, 80)
        self.sleepingImgs = createListOfAnimatedImgs(
            Character.PATH_FOR_SLEEPING_FOLDER, 'sleeping', None, 'yes', 80, 80)
        self.goingLeftImgs = createListOfAnimatedImgs(
            Character.PATH_FOR_GOING_LEFT_FOLDER, 'goingLeft', None, 'yes', 80, 80)
        self.goingRightImgs = createListOfAnimatedImgs(
            Character.PATH_FOR_GOING_RIGHT_FOLDER, 'goingRight', None, 'yes', 80, 80)
        self.goingDownImgs = createListOfAnimatedImgs(
            Character.PATH_FOR_GOING_DOWN_FOLDER, 'goingDown', None, 'yes', 80, 80)
        self.goingUpImgs = createListOfAnimatedImgs(
            Character.PATH_FOR_GOING_UP_FOLDER, 'goingUp', None, 'yes', 80, 80)
    
    #------------ Each Animation Per Time -----------------------------------------
    def drawRestingAnimation(self, window):
        #if self.resting:
        window.blit(self.restingImgs[self.idleCount//self.spritesDelay], (self.x,self.y))
        #window.blit(self.restingImgs[self.idleCount], (self.x,self.y))
        self.drawCollider(window, self.restingImgs, self.idleCount, self.spritesDelay)
        #self.rect.x = self.x
        #self.rect.y = self.y
        #print(self.rect)
        #rectCollide(window, (255, 255, 255), self.rect)
        self.idleCount += 1
        # I've 17 imgs in my folder, multiplying it for 3 = 51, each img is running at 51 fps
        #but instead of multiplying it per 3, I've used 100
        if self.idleCount + 1 >= len(self.restingImgs)*self.spritesDelay:
            self.idleCount = 0

    def drawYesKnockingAnimation(self, window):
        if self.yesKnocking:
            window.blit(self.yesKnockingImgs[self.yesKnockCount//self.spritesDelay], (self.x,self.y))
            #window.blit(self.yesKnockingImgs[self.yesKnockCount], (self.x,self.y))
            self.drawCollider(window, self.yesKnockingImgs, self.yesKnockCount, self.spritesDelay)
            self.yesKnockCount += 1
        if self.yesKnockCount + 1 >= len(self.yesKnockingImgs)*self.spritesDelay:
            self.yesKnockCount = 0

    def drawNoKnockingAnimation(self, window):
        if self.noKnocking:
            window.blit(self.noKnockingImgs[self.noKnockCount//self.spritesDelay], (self.x,self.y))
            #window.blit(self.noKnockingImgs[self.noKnockCount], (self.x,self.y))
            self.drawCollider(window, self.noKnockingImgs, self.noKnockCount, self.spritesDelay)
            self.noKnockCount += 1
        if self.noKnockCount + 1 >= len(self.noKnockingImgs)*self.spritesDelay:
            self.noKnockCount = 0

    def drawSleepingAnimation(self, window):
        if self.sleeping:
            # draw
            window.blit(self.sleepingImgs[self.sleepingCount//self.spritesDelay], (self.x,self.y))
            #window.blit(self.sleepingImgs[self.sleepingCount], (self.x,self.y))
            self.drawCollider(window, self.sleepingImgs, self.sleepingCount, self.spritesDelay)
            self.sleepingCount += 1
        if self.sleepingCount + 1 >= len(self.sleepingImgs)*self.spritesDelay:
            self.sleepingCount = 0

    def drawGoingLeftAnimation(self, window):
        if self.goingLeft:
            window.blit(self.goingLeftImgs[self.walkCount//self.spritesDelay], (self.x,self.y))
            #window.blit(self.goingLeftImgs[self.walkCount], (self.x,self.y))
            self.drawCollider(window, self.goingLeftImgs, self.walkCount, self.spritesDelay)
            self.walkCount += 1
        if self.walkCount + 1 >= len(self.goingLeftImgs)*self.spritesDelay:
            self.walkCount = 0

    def drawGoingRightAnimation(self, window):
        if self.goingRight:
            window.blit(self.goingRightImgs[self.walkCount//self.spritesDelay], (self.x,self.y))
            #window.blit(self.goingRightImgs[self.walkCount], (self.x,self.y))
            self.drawCollider(window, self.goingRightImgs, self.walkCount, self.spritesDelay)
            self.walkCount += 1
        if self.walkCount + 1 >= len(self.goingRightImgs)*self.spritesDelay:
            self.walkCount = 0
    
    def drawGoingDownAnimation(self, window):
        if self.goingDown:
            window.blit(self.goingDownImgs[self.walkCount//self.spritesDelay], (self.x,self.y))
            #window.blit(self.goingRightImgs[self.walkCount], (self.x,self.y))
            self.drawCollider(window, self.goingDownImgs, self.walkCount, self.spritesDelay)
            self.walkCount += 1
        if self.walkCount + 1 >= len(self.goingDownImgs)*self.spritesDelay:
            self.walkCount = 0

    def drawGoingUpAnimation(self, window):
        if self.goingUp:
            window.blit(self.goingUpImgs[self.walkCount//self.spritesDelay], (self.x,self.y))
            #window.blit(self.goingRightImgs[self.walkCount], (self.x,self.y))
            self.drawCollider(window, self.goingUpImgs, self.walkCount, self.spritesDelay)
            self.walkCount += 1
        if self.walkCount + 1 >= len(self.goingUpImgs)*self.spritesDelay:
            self.walkCount = 0
    #-------------------------------------------------------------------
    def drawActualPlayerWithAllAnimations(self, window):
        if self.resting:
            self.drawRestingAnimation(window)
        elif self.yesKnocking:
            self.drawYesKnockingAnimation(window)
        elif self.noKnocking:
            self.drawNoKnockingAnimation(window)
        elif self.sleeping:
            self.drawSleepingAnimation(window) 
        elif self.goingLeft:
            self.drawGoingLeftAnimation(window)    
        elif self.goingRight:
            self.drawGoingRightAnimation(window)
        elif self.goingDown:
            self.drawGoingDownAnimation(window)
        elif self.goingUp:
            self.drawGoingUpAnimation(window)
        else:
            self.drawRestingAnimation(window)
    
    def checkForKeyUp(self, event):
        self.returnVelAfterHit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                self.resting = True
                self.yesKnocking = False
                self.noKnocking = False
                self.sleeping = False
                self.goingLeft = False
                self.goingRight = False
                self.goingDown = False
                self.goingUp = False
                self.returnVelAfterHit()

            if event.key == pygame.K_d:
                self.resting = True
                self.yesKnocking = False
                self.noKnocking = False
                self.sleeping = False
                self.goingLeft = False
                self.goingRight = False
                self.goingDown = False
                self.goingUp = False
                self.returnVelAfterHit()

            if event.key == pygame.K_w:
                self.resting = True
                self.yesKnocking = False
                self.noKnocking = False
                self.sleeping = False
                self.goingLeft = False
                self.goingRight = False
                self.goingDown = False
                self.goingUp = False
                self.returnVelAfterHit()

            if event.key == pygame.K_s:
                self.resting = True
                self.yesKnocking = False
                self.noKnocking = False
                self.sleeping = False
                self.goingLeft = False
                self.goingRight = False
                self.goingDown = False
                self.goingUp = False
                self.returnVelAfterHit()


    # to press 2 keys at the same time, we need to use, 2 separated methods
    #https://www.youtube.com/watch?v=yKv02lq7JHs
    
    def checkPressedKeys(self, window, keys):
        if keys:
            try:
                # Moving
                if keys[pygame.K_a] and (self.x > self.vel):
                    print(f'keys a, vel:{self.vel}')   
                    #self.x -= self.vel
                    self.dx -= self.vel
                    # check for player collision and then move him
                    self.resting = False
                    self.yesKnocking = False
                    self.noKnocking = False
                    self.sleeping = False
                    self.goingLeft = True
                    self.goingRight = False
                    self.goingDown = False
                    self.goingUp = False
                    self.returnVelAfterHit() 
                    
                elif keys[pygame.K_d] and (self.x < window.get_width() - self.width - self.vel):
                    print(f'keys d, vel: {self.vel}')         
                    #self.x += self.vel
                    self.dx += self.vel
                    self.resting = False
                    self.yesKnocking = False
                    self.noKnocking = False
                    self.sleeping = False
                    self.goingLeft = False
                    self.goingRight = True
                    self.goingDown = False
                    self.goingUp = False
                    self.returnVelAfterHit()
                    
                elif keys[pygame.K_w] and (self.y > self.vel):
                    print(f'keys w, vel: {self.vel}')   
                    #self.y -= self.vel
                    self.dy -= self.vel
                    self.resting = False
                    self.yesKnocking = False
                    self.noKnocking = False
                    self.sleeping = False
                    self.goingLeft = False
                    self.goingRight = False
                    self.goingDown = False
                    self.goingUp = True
                    self.returnVelAfterHit()
                    
                elif keys[pygame.K_s] and (self.y < window.get_height() - self.height - self.vel):
                    print(f'keys s, vel: {self.vel}')        
                    #self.y += self.vel
                    self.dy += self.vel
                    self.resting = False
                    self.yesKnocking = False
                    self.noKnocking = False
                    self.sleeping = False
                    self.goingLeft = False
                    self.goingRight = False
                    self.goingDown = True
                    self.goingUp = False
                    self.returnVelAfterHit()
                
                # Standing                
                elif keys[pygame.K_p]:
                    self.resting = False
                    self.yesKnocking = False
                    self.noKnocking = False
                    self.sleeping = True
                    self.goingLeft = False
                    self.goingRight = False
                    self.goingDown = False
                    self.goingUp = False
                    self.returnVelAfterHit()
                
                elif keys[pygame.K_y]:
                    self.resting = False
                    self.yesKnocking = True
                    self.noKnocking = False
                    self.sleeping = False
                    self.goingLeft = False
                    self.goingRight = False
                    self.goingDown = False
                    self.goingUp = False
                    self.returnVelAfterHit()       
                
                elif keys[pygame.K_n]:
                    self.resting = False
                    self.yesKnocking = False
                    self.noKnocking = True
                    self.sleeping = False
                    self.goingLeft = False
                    self.goingRight = False
                    self.goingDown = False
                    self.goingUp = False
                    self.returnVelAfterHit()     
            except:
                return False
        else:
            # Breathing
            self.resting = True
            self.yesKnocking = False
            self.noKnocking = False
            self.sleeping = False
            self.goingLeft = False
            self.goingRight = False
            self.goingDown = False
            self.goingUp = False
            self.returnVelAfterHit()
    
    def drawtexts(self, window, mainFont, color):
        self.energyLevel = mainFont.render(f"Energy: {self.energy}", 1, color)
        #self.imageRect = mainFont.render(f"imageRect: {self.imageRect}", 1, color)
        #self.hitBox = mainFont.render(f"hitBox: {self.hitBox}", 1, color)
        window.blit(self.energyLevel, (window.get_width() - self.energyLevel.get_width() - 10, 10))
        #window.blit(self.imageRect, (window.get_width() - self.imageRect.get_width() - 10, 10))
        #window.blit(self.hitBox, (window.get_width() - self.hitBox.get_width() - 10, 10))
    
    def drawCollider(self, window, imgFolder, count, spritesDelay):
        self.imageRect = imgFolder[count//spritesDelay]
        self.hitBox = self.imageRect.get_rect()
        self.hitBox.center = self.width//2, self.height//2
        # self.hitBox.x = self.x + 21
        # self.hitBox.y = self.y + 14
        # self.hitBox.width = 22
        # self.hitBox.height = 22       
        
        if imgFolder == self.goingRightImgs:
            #self.hitBox.x = self.x + (self.hitBox.center[0]/.95)
            self.hitBox.x = self.x + (self.hitBox.width/2.4)

        else:
            #self.hitBox.x = self.x + (self.hitBox.center[0]/1.15)
            self.hitBox.x = self.x + (self.hitBox.width/2.8)
        
        #self.hitBox.y = self.y + (self.hitBox.center[1]/1.7)     
        self.hitBox.y = self.y + (self.hitBox.height/4.3)       
        self.hitBox.width = (self.hitBox.width/3)
        self.hitBox.height = (self.hitBox.height/3)

        rectCollide(window, (255, 255, 255), (self.hitBox))
    
    def getHit(self):
        print('Character hit')
    
    # def checkForContacts(self, window, house1, house2, femaleNPC):
    #     # if the y coord of the character, is between the top and the bottom of the others objs rect
    #     if self.y - radius <

    def returnVelAfterHit(self):
        if self.vel == -2:
            self.vel = 2
            self.collided = False