import sys, pygame, map_gen
import numpy as np
import pygame.surfarray as surfarray

#pylint shows as an errror
pygame.init()

'''

GENERATION VARIABLES

'''
map_min_width = 60
map_max_width = 70
map_min_height = 60
map_max_height = 70
min_rooms = 5
max_rooms = 8
min_size = 4
max_size = 8
min_dist_bw_rooms = 2

'''

DISPLAY VARIABLES

'''
# pixels in a unit
unit_size = 32

white = 1, 1, 1
black = 0, 0, 0

# window location
window_x_units = 0
window_y_units = 0

# window size with pixels and units
window_width_units = 40
window_height_units = 20
window_width = window_width_units * unit_size
window_height = window_height_units * unit_size

# window size
size = window_width, window_height


mapArr = map_gen.generateMap(map_min_width, map_max_width, map_min_height, map_max_height)
mapWidth, mapHeight = mapArr.shape

print('Height, Width', mapWidth, mapHeight)
rooms = map_gen.generateRooms(min_rooms, max_rooms, min_size, max_size, min_dist_bw_rooms, mapWidth, mapHeight)

# add rooms
print('Loading rooms onto map')
for room in rooms:
    x = room['x_loc']
    x2 = x+room['width']
    y = room['y_loc']
    y2 = y+room['height']
    print('Passed room vars (x, x2, y, y2): ', x, x2, y, y2)
    # 2 is wall surrounding a floor
    mapArr[x-1:x2+1, y-1:y2+1] = 2
    # 0 is floor
    mapArr[x:x2, y:y2] = 0

# Create graphical window
screen = pygame.display.set_mode(size)
screen.fill(white)

wall = pygame.image.load("assets/wall/default-wall.bmp")
floor = pygame.image.load("assets/floor/default-floor.bmp")

def renderMap():
    #Clear screen
    screen.fill(black)
    # create rectangles
    for x in range(window_x_units, window_width_units+window_x_units):
        for y in range(window_y_units, window_height_units+window_y_units):
            # shift graphics depending on window location
            new_x = x-window_x_units
            new_y = y-window_y_units
            if(mapArr[x, y] == 2):
                #print('Drawing wall')
                screen.blit(wall, (new_x*unit_size, new_y*unit_size, unit_size, unit_size))
            elif(mapArr[x, y] == 0):
                #print('Drawing floor')
                screen.blit(floor, (new_x*unit_size, new_y*unit_size, unit_size, unit_size))

renderMap()

def moveScreen(keyWASD):
    global window_x_units
    global window_y_units

    if(keyWASD == 'w'):
        # check if move is possible
        if(window_y_units > 0):
            window_y_units-=1
            renderMap()
        else:
            print('Cant move that direction')

    elif(keyWASD == 'a'):
        # check if move is possible
        if(window_x_units > 0):
            window_x_units-=1
            renderMap()
        else:
            print('Cant move that direction')

    elif(keyWASD == 's'):
        # check if move is possible
        if(window_y_units + window_height_units < mapHeight):
            window_y_units+=1
            renderMap()
        else:
            print('Cant move that direction')

    elif(keyWASD == 'd'):
        # check if move is possible
        if(window_x_units + window_width_units < mapWidth):
            window_x_units+=1
            renderMap()
        else:
            print('Cant move that direction')





# runs the game
while 1:
    for event in pygame.event.get():
        #pylint shows as an error
        if event.type == pygame.QUIT: 
            print('Exiting..')
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # button is being pressed
            if event.key == pygame.K_w:
                print('Pressed w')
                moveScreen('w')
            elif event.key == pygame.K_s:
                print('Pressed s')
                moveScreen('s') 
            elif event.key == pygame.K_a:
                print('Pressed a')
                moveScreen('a') 
            elif event.key == pygame.K_d:
                print('Pressed d')
                moveScreen('d') 
    
    #Make drawn items appear
    pygame.display.flip()