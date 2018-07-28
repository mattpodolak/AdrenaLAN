import numpy as np
import math

def generatePath(room_arr, num_path, path_width, map_width, map_height):
    # loop through each room
    path_arr = []
    for i in range(0, room_arr.length):
        room_arr[i]['path'] = 1
        room_arr[i]['connected'] = True

        # selected room x, y (center)
        # room_x = roomA['x_loc'] + (room['width'] // 2)
        # room_y = roomA['y_loc'] + (room['height'] // 2)

        # find the closest room
        temp_room_arr = [x for j, x in enumerate(room_arr) if j!= i]
        minDist = map_width
        closestRoom = ({'x_pos' : 0, 'y_pos' : 0})
        for room_temp in temp_room_arr:
            tempDist = roomDist(room_arr[i], room_temp)
            # found a closer room
            if tempDist < minDist:
                minDist = tempDist
                closestRoom['x_pos'] = room_temp['x_loc']
                closestRoom['y_pos'] = room_temp['y_loc']

        # draw path from room to closest room
    return path_arr


def roomDist(roomA, roomB):
    # room A
    roomA_x = roomA['x_loc']
    roomA_y = roomA['y_loc']
    # room B
    roomB_x = roomB['x_loc']
    roomB_y = roomB['y_loc']
    # calculate distance
    distX = math.pow(roomA_x - roomB_x, 2)
    distY = math.pow(roomA_y - roomB_y, 2)
    return math.sqrt(distX + distY)













