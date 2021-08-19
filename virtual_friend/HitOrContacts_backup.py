#from functions import *
class HitOrContacts:
    """Main hit class"""

    def __init__(self):
        pass

    def checkForContacts(self, obj2):
        # if the y coord of the character, is between the top and the bottom of the others objs rect
        # hitBox[1] = y coord | hitBox[3] = height | hitBox[0] = x coord | hitBox[2] = width
        # if are less than, we are above the bottom of the obj2 rect
        # and we need to check if we are also bellow the top of the obj2 rect (just the y coord)
        if self.y - self.hitBox.width < obj2.hitBox.y + obj2.hitBox.height and  self.y + self.hitBox.width > obj2.hitBox.y:
            # now we check if we are on the left side of the obj2 rect
            if self.x + self.hitBox.width > obj2.hitBox.x and self.x - self.hitBox.width < obj2.hitBox.x + obj2.hitBox.width:
                # this function will run what is inside it
                obj2.getHit()