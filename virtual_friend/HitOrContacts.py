from functions import *
class HitOrContacts:
    """Main hit class"""

    def __init__(self):
        pass

    def checkForContacts(self, obj2):
        # if the y coord of the character, is between the top and the bottom of the others objs rect
        # hitBox[1] = y coord | hitBox[3] = height | hitBox[0] = x coord | hitBox[2] = width
        # if are less than, we are above the bottom of the obj2 rect
        # and we need to check if we are also bellow the top of the obj2 rect (just the y coord)
        #if self.vel >= 0:
        if self.collided == False:
            if self.hitBox.y < obj2.hitBox.y + obj2.hitBox.height and  self.hitBox.y + self.hitBox.height > obj2.hitBox.y:
                # now we check if we are on the left side of the obj2 rect
                if self.hitBox.x + self.hitBox.width > obj2.hitBox.x and self.hitBox.x < obj2.hitBox.x + obj2.hitBox.width:
                    # this function will run what is inside it
                    obj2.getHit()
                    self.vel = -self.vel
                    self.collided = True
                    print(f'inside contact, vel: {self.vel}')