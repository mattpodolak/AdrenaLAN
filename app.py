import sys, pygame, map_gen
import numpy as np

#pylint shows as an errror
pygame.init()

# window size
size = width, height = 320, 240

'''
GENERATION VARIABLES

'''
unit_size = 5
map_min_width = 400
map_max_width = 500
map_min_height = 400
map_max_height = 500
min_rooms = 3
max_rooms = 6
min_size = 3
max_size = 7
min_dist_bw_rooms = 2



mapArr = map_gen.generateMap(map_min_width, map_max_width, map_min_height, map_max_height)
mapWidth, mapHeight = mapArr.shape
print('Height, Width', mapWidth, mapHeight)
print(mapArr)
rooms = map_gen.generateRooms(min_rooms, max_rooms, min_size, max_size, min_dist_bw_rooms, mapWidth, mapHeight)

# Create graphical window
# screen = pygame.display.set_mode(size)