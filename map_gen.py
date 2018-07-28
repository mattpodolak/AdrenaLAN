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

def generateRooms(min_rooms, max_rooms, min_size, max_size, min_dist, mapWidth, mapHeight):
    
    # pick number of rooms
    print('Making map..')
    num_rooms = random.randint(min_rooms, max_rooms+1)

    # store room info
    room_data = []

    # generate rooms
    for i in range(0, num_rooms):
        print('Making: Room ', i)
        # pick width and height
        width = random.randint(min_size, max_size+1)
        height = random.randint(min_size, max_size+1)

        if i != 0:
            conflict = True
            loop_count = 0

            while conflict == True:
                conflict = False
                x_loc = random.randint(0, mapWidth-width)
                y_loc = random.randint(0, mapHeight-height)

                if loop_count == 5:
                    print('OH NO! making room smallest size')
                    width = min_size
                    height = min_size
                
                if loop_count == 10:
                    print('ITS NOT WORKING, making size 1 room')
                    width = 1
                    height = 1

                # check previous locations for conflicts
                for room in room_data:
                    if (room['x_loc']+room['width']+min_dist > x_loc || room['y_loc']+room['height']+min_dist > y_loc || x_loc+width+min_dist > room['x_loc'] || y_loc+height+min_dist > room['y_loc']):
                        print('Room overlap!')
                        conflict = True
                        break
                loop_count++

        else:
            x_loc = random.randint(0, mapWidth-width)
            y_loc = random.randint(0, mapHeight-height)

        # pick location with no conflicts, further than min dist away from nearest room
        # if conflicts make room smaller
        room_data.append({width})


