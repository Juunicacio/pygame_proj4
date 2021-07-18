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
        self.x = 150
        self.y = 150
        self.width = 64
        self.height = 64
        self.vel = 2
        self.color = color

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
        self.goingDownImgs = createListOfAnimatedImgs(
            Character.PATH_FOR_GOING_DOWN_FOLDER, 'goingDown')
        self.goingUpImgs = createListOfAnimatedImgs(
            Character.PATH_FOR_GOING_UP_FOLDER, 'goingUp')
    
    #------------ Each Animation Per Time -----------------------------------------
    def drawRestingAnimation(self, window):
        #if self.resting:
        window.blit(self.restingImgs[self.idleCount//self.spritesDelay], (self.x,self.y))
        #window.blit(self.restingImgs[self.idleCount], (self.x,self.y))
        self.collide(window, self.restingImgs, self.idleCount, self.spritesDelay)
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
            self.collide(window, self.yesKnockingImgs, self.yesKnockCount, self.spritesDelay)
            self.yesKnockCount += 1
        if self.yesKnockCount + 1 >= len(self.yesKnockingImgs)*self.spritesDelay:
            self.yesKnockCount = 0

    def drawNoKnockingAnimation(self, window):
        if self.noKnocking:
            window.blit(self.noKnockingImgs[self.noKnockCount//self.spritesDelay], (self.x,self.y))
            #window.blit(self.noKnockingImgs[self.noKnockCount], (self.x,self.y))
            self.collide(window, self.noKnockingImgs, self.noKnockCount, self.spritesDelay)
            self.noKnockCount += 1
        if self.noKnockCount + 1 >= len(self.noKnockingImgs)*self.spritesDelay:
            self.noKnockCount = 0

    def drawSleepingAnimation(self, window):
        if self.sleeping:
            # draw
            window.blit(self.sleepingImgs[self.sleepingCount//self.spritesDelay], (self.x,self.y))
            #window.blit(self.sleepingImgs[self.sleepingCount], (self.x,self.y))
            self.collide(window, self.sleepingImgs, self.sleepingCount, self.spritesDelay)
            self.sleepingCount += 1
        if self.sleepingCount + 1 >= len(self.sleepingImgs)*self.spritesDelay:
            self.sleepingCount = 0

    def drawGoingLeftAnimation(self, window):
        if self.goingLeft:
            window.blit(self.goingLeftImgs[self.walkCount//self.spritesDelay], (self.x,self.y))
            #window.blit(self.goingLeftImgs[self.walkCount], (self.x,self.y))
            self.collide(window, self.goingLeftImgs, self.walkCount, self.spritesDelay)
            self.walkCount += 1
        if self.walkCount + 1 >= len(self.goingLeftImgs)*self.spritesDelay:
            self.walkCount = 0

    def drawGoingRightAnimation(self, window):
        if self.goingRight:
            window.blit(self.goingRightImgs[self.walkCount//self.spritesDelay], (self.x,self.y))
            #window.blit(self.goingRightImgs[self.walkCount], (self.x,self.y))
            self.collide(window, self.goingRightImgs, self.walkCount, self.spritesDelay)
            self.walkCount += 1
        if self.walkCount + 1 >= len(self.goingRightImgs)*self.spritesDelay:
            self.walkCount = 0
    
    def drawGoingDownAnimation(self, window):
        if self.goingDown:
            window.blit(self.goingDownImgs[self.walkCount//self.spritesDelay], (self.x,self.y))
            #window.blit(self.goingRightImgs[self.walkCount], (self.x,self.y))
            self.collide(window, self.goingDownImgs, self.walkCount, self.spritesDelay)
            self.walkCount += 1
        if self.walkCount + 1 >= len(self.goingDownImgs)*self.spritesDelay:
            self.walkCount = 0

    def drawGoingUpAnimation(self, window):
        if self.goingUp:
            window.blit(self.goingUpImgs[self.walkCount//self.spritesDelay], (self.x,self.y))
            #window.blit(self.goingRightImgs[self.walkCount], (self.x,self.y))
            self.collide(window, self.goingUpImgs, self.walkCount, self.spritesDelay)
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
            if event.key == pygame.K_d:
                self.resting = True
                self.yesKnocking = False
                self.noKnocking = False
                self.sleeping = False
                self.goingLeft = False
                self.goingRight = False
                self.goingDown = False
                self.goingUp = False
            if event.key == pygame.K_w:
                self.resting = True
                self.yesKnocking = False
                self.noKnocking = False
                self.sleeping = False
                self.goingLeft = False
                self.goingRight = False
                self.goingDown = False
                self.goingUp = False
            if event.key == pygame.K_s:
                self.resting = True
                self.yesKnocking = False
                self.noKnocking = False
                self.sleeping = False
                self.goingLeft = False
                self.goingRight = False
                self.goingDown = False
                self.goingUp = False
    
    def checkPressedKeys(self, window, keys):
        #keys = pygame.key.get_pressed()
        if keys:
            try:
                # Moving
                if keys[pygame.K_a] and (self.x > self.vel):
                    self.x -= self.vel               
                    self.resting = False
                    self.yesKnocking = False
                    self.noKnocking = False
                    self.sleeping = False
                    self.goingLeft = True
                    self.goingRight = False
                    self.goingDown = False
                    self.goingUp = False              
                    
                elif keys[pygame.K_d] and (self.x < window.get_width() - self.width - self.vel):
                    self.x += self.vel
                    self.resting = False
                    self.yesKnocking = False
                    self.noKnocking = False
                    self.sleeping = False
                    self.goingLeft = False
                    self.goingRight = True
                    self.goingDown = False
                    self.goingUp = False
                    
                elif keys[pygame.K_w] and (self.y > self.vel):
                    self.y -= self.vel
                    self.resting = False
                    self.yesKnocking = False
                    self.noKnocking = False
                    self.sleeping = False
                    self.goingLeft = False
                    self.goingRight = False
                    self.goingDown = False
                    self.goingUp = True
                    
                elif keys[pygame.K_s] and (self.y < window.get_height() - self.height - self.vel):
                    self.y += self.vel
                    self.resting = False
                    self.yesKnocking = False
                    self.noKnocking = False
                    self.sleeping = False
                    self.goingLeft = False
                    self.goingRight = False
                    self.goingDown = True
                    self.goingUp = False
                
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
                
                elif keys[pygame.K_y]:
                    self.resting = False
                    self.yesKnocking = True
                    self.noKnocking = False
                    self.sleeping = False
                    self.goingLeft = False
                    self.goingRight = False
                    self.goingDown = False
                    self.goingUp = False          
                
                elif keys[pygame.K_n]:
                    self.resting = False
                    self.yesKnocking = False
                    self.noKnocking = True
                    self.sleeping = False
                    self.goingLeft = False
                    self.goingRight = False
                    self.goingDown = False
                    self.goingUp = False     
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
    
    def drawtexts(self, window, mainFont, color):
        self.energyLevel = mainFont.render(f"Energy: {self.energy}", 1, color)
        window.blit(self.energyLevel, (window.get_width() - self.energyLevel.get_width() - 10, 10))
    
    def collide(self, window, imgFolder, count, spritesDelay):
        self.imageRect = imgFolder[count//spritesDelay]
        self.hitBox = self.imageRect.get_rect()
        self.hitBox.x = self.x + 21
        self.hitBox.y = self.y + 14
        self.hitBox.width = 22
        self.hitBox.height = 22
        if imgFolder == self.goingRightImgs:
            self.hitBox.x = self.x + 25
        rectCollide(window, (255, 255, 255), (self.hitBox))