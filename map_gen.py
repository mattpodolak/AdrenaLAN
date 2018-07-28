import random
import numpy as np

def generateMap(min_width, max_width, min_height, max_height):
    # unit size converts width and height to pixels
    # min_dist, minimum distance between start and goal blocks

    # generate height and width
    print('Making map..')
    mapWidth = random.randint(min_width, max_width+1)
    mapHeight = random.randint(min_height, max_height+1)    

    # create array of 1s, dimensions equal map size (1 represents nothing, 0 is floor, 2 is wall)
    mapArr = np.ones((mapWidth, mapHeight), dtype=int)
    return mapArr 

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
        width = random.randint(min_size, max_size)
        height = random.randint(min_size, max_size)

        if i != 0:
            conflict = True
            loop_count = 0

            while conflict == True:
                conflict = False
                x_loc = random.randint(2, mapWidth-width-2)
                y_loc = random.randint(2, mapHeight-height-2)

                if loop_count == 5:
                    print('OH NO! making room smallest size')
                    width = min_size
                    height = min_size
                
                if loop_count == 10:
                    if(width != 1 and height != 1):
                        print('ITS NOT WORKING, making smaller')
                        width-=1
                        height-=1
                        # reset count
                        loop_count = 5
                    else:
                        print('CONFLICTED INTO SMALLEST ROOM')
                    

                # check previous locations for conflicts
                for room in room_data:
                    room_x = room['x_loc']+room['width']
                    room_y = room['y_loc']+room['height']
                    check_x = x_loc+width
                    check_y = y_loc+height
                    if ((room_x+min_dist > x_loc and room_x+min_dist < check_x ) 
                    or (room_y+min_dist > y_loc and room_y+min_dist < check_y) 
                    or (check_x+min_dist > room['x_loc'] and check_x+min_dist < room_x) 
                    or (check_y+min_dist > room['y_loc'] and check_y+min_dist < room_y)
                    or (room['x_loc'] < x_loc and room_x > check_x and room['y_loc'] > y_loc and room['y_loc'] < check_y)
                    or (room['y_loc'] < y_loc and room_y > check_y and room['x_loc'] > x_loc and room['x_loc'] < check_x)
                    or (room['x_loc'] > x_loc and room_x < check_x and room['y_loc'] < y_loc and room['y_loc'] > check_y)
                    or (room['y_loc'] > y_loc and room_y < check_y and room['x_loc'] < x_loc and room['x_loc'] > check_x)
                    ):
                        print('Room Conflict')
                        conflict = True
                        break
                loop_count+=1

        else:
            x_loc = random.randint(2, mapWidth-width-2)
            y_loc = random.randint(2, mapHeight-height-2)

        # store data
        print('width, height, x, y', width, height, x_loc, y_loc)
        room_data.append({'width': width, 'height': height, 'x_loc': x_loc, 'y_loc': y_loc, 'connected': False})
        print('Added room to data')
    return room_data


