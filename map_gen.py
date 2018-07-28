import random
import numpy as np

def generateMap(min_width, max_width, min_height, max_height):
    # unit size converts width and height to pixels
    # min_dist, minimum distance between start and goal blocks

    # generate height and width
    print('Making map..')
    mapWidth = random.randint(min_width, max_width+1)
    mapHeight = random.randint(min_height, max_height+1)    

    # create array of 1s, dimensions equal map size (1 represents wall, 0 is floor, 2 is start, 3 is goal)
    return mapArr = np.ones((mapWidth, mapHeight), dtype=int)

def generateRooms(min_rooms, max_rooms, min_size, max_size, min_dist):
    
    # pick number of rooms
    print('Making map..')

def Room(room_x, room_y, maxWidth, maxHeight, minmax):
    # plus or minus minmax 
    plus_x =   random.randint(0, minmax+1)
    minus_x =   random.randint(0, minmax+1)
    plus_y =   random.randint(0, minmax+1)
    minus_y =   random.randint(0, minmax+1)

    # make sure room doesn't go off the map
    # calculate x room variables
    if(room_x + plus_x > maxWidth-1):
        room_x2 = maxWidth - 1
    else:
        room_x2 = room_x + plus_x
    
    if(room_x - minus_x < 0):
        room_x1 = 0
    else:
        room_x1 = room_x - minus_x

    # calculate y room variables
    if(room_y + plus_y > maxHeight-1):
        room_y2 = maxHeight - 1
    else:
        room_y2 = room_y + plus_y
    if(room_y - minus_y < 0):
        room_y1 = 0
    else:
        room_y1 = room_y - minus_y

    return room_x1, room_x2, room_y1, room_y2