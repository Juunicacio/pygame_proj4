from functions import * # import accessAssetsFolder
import pygame

class World():
    """Main World class"""

    PATH_FOR_ASSETS_FOLDER = accessAssetsFolder()

    def __init__(self, data, tile_size):
        self.tile_size = tile_size
        self.path_img_filename = 'path9.png'
        self.path_img = createListOfAnimatedImgs(World.PATH_FOR_ASSETS_FOLDER, None, self.path_img_filename)

        self.grass_img_filename = 'grass1.png'
        self.grass_img = createListOfAnimatedImgs(World.PATH_FOR_ASSETS_FOLDER, None, self.grass_img_filename)
        
        self.tile_list = []

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    # if I want to scale it the same size of the grid I use:
                    # that is just the picture
                    ###img = pygame.transform.scale(self.path_img, ((self.tile_size)*2, self.tile_size))
                    # or
                    img = self.path_img
                    # to know where put it on the screen, I need the x and y coord
                    # that's when our rectangle come in:
                    img_rect = img.get_rect()
                    # the x has to be defined where I'm on this list of tiles
                    # I can get where I'm because of the 'for tile in row', so I add a count on it
                    ####### after having the counts, I can use to know where I am on the screen
                    ####### the x is gonna increase with the column, and the y with the rows
                    ####### the next column will the the width of the tile_size, so:
                    img_rect.x = col_count * self.tile_size #-20 # to go to the beginning of the screen
                    img_rect.y = row_count * self.tile_size
                    # add these values to my tile_list, I have 2 values to store, the img and the img_rect
                    # so I add these on tuples
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                # as I iterate I increase the value +1 of the column, to know where I'm
                col_count += 1
                # When I'm done with the columns, I need to know where I am in the rows as well, 
                # so for 'row in data' I also add a count
            row_count += 1    

    def drawPath(self, window):
        # example:
        # window.blit(self.path_img, (self.tile_size, self.tile_size))
        # self.drawCollider(window, self.houseImg)

        # I need to draw the tiles in the list
        # I have a tuple with 2 values, the first is the img and the second is the rect position
        for tile in self.tile_list:
            window.blit(tile[0], tile[1])
