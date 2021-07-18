from functions import *
class GameTime:
    """Main GameTime class"""
    gameStartTime = 0 # measures our time every frame
    # starting the stopwatch
    gameStartTime = pygame.time.get_ticks()/1000
    #print(gameStartTime)

    milliseconds = 0
    seconds = 0
    isSleeping = False
    sameButton = False

    def __init__(self):
        # self.milliseconds = 0
        # self.seconds = 0
        # self.isSleeping = False
        pass

    @staticmethod
    def buttonPressed(GameTime):
        if GameTime.isSleeping == True:
            # start counting time
            GameTime.milliseconds += 1
            if GameTime.milliseconds + 1 >= 17*3:
                GameTime.seconds += 1
                #print(GameTime.seconds)
                print(f"player is sleeping for {GameTime.seconds} seconds")
                GameTime.milliseconds = 0
                if GameTime.seconds == 300:
                    print(f"player is sleeping for 5 minutes")
                    GameTime.seconds = 0
                    print("5 minutes passed, full energy bar")
        else:
            # reset values
            GameTime.milliseconds = 0
            GameTime.seconds = 0
            #print(GameTime.milliseconds)
            #print(GameTime.seconds)

    def buttonGetTime(self, buttonName, playerAction):
        if playerAction == True:
            print(f"{self.buttonSpawnTimer} in")
            GameTime.isSleeping = True
            GameTime.buttonPressed(GameTime)            
            if GameTime.sameButton == False:
                self.buttonSpawnTimer = (pygame.time.get_ticks())
                print(self.buttonSpawnTimer) # this time when pressed button
                GameTime.sameButton = True
            print(f"{pygame.time.get_ticks() - self.buttonSpawnTimer} COUNT!")
            buttonSpawnFrequency = 60000 # milliseconds = 1 minute
            getfullBar = 0 # = 5 minutes
            if (pygame.time.get_ticks() - self.buttonSpawnTimer) >= buttonSpawnFrequency:
                print(f"{buttonSpawnFrequency} 1 minute has passed, + 10% of resting")
                getfullBar +=1
            while getfullBar < 5:
                print(f"{getfullBar} continue to sleep...")
                break
            else:
                print(f"{getfullBar} 5 minutes has passed, full bar")
            
        else:
            print(f"{self.buttonSpawnTimer} out")
            GameTime.isSleeping = False
            GameTime.buttonPressed(GameTime)
        
