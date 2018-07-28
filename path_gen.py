import numpy as np
import math

def generatePaths(room_arr, num_path, path_width, map_width, map_height):
    # loop through each room
    path_arr = []
    for i in range(0, room_arr.length):
        room_arr[i]['path'] = 1
        room_arr[i]['connected'] = True

        # check other rooms
        temp_room_arr = [x for j, x in enumerate(room_arr) if j!= i]
        minDist = map_width
        closestRoom = ({'x_pos' : 0, 'y_pos' : 0})
        for room_temp in temp_room_arr:
            tempDist = roomDist(room_arr[i]['x_loc'], room_arr[i]['y_loc'], closestRoom['x_pos'], closestRoom['y_pos'])
            # found a closer room
            if tempDist < minDist:
                minDist = tempDist
                closestRoom['x_pos'] = room_temp['x_loc']
                closestRoom['y_pos'] = room_temp['y_loc']

        # selected room x, y (center)
        # room_x = roomA['x_loc'] + (room['width'] // 2)
        # room_y = roomA['y_loc'] + (room['height'] // 2)
        path_arr.append(roomPath(room_arr[i], closestRoom))
    return path_arr

def roomDist(roomA_x, roomA_y, roomB_x, roomB_y):
    # calculate distance
    distX = math.pow(roomA_x - roomB_x, 2)
    distY = math.pow(roomA_y - roomB_y, 2)
    return math.sqrt(distX + distY)

def roomPath(roomA, roomB):
        path_arr = []
        
        # find start point for roomA
        roomA_middleX = roomA['x_loc'] + (roomA['width'] // 2)
        roomA_middleY = roomA['y_loc'] + (roomA['height'] // 2)
        # top
        a_top = roomDist(roomA_middleX, roomA['y_loc'], roomB['x_loc'], roomB['y_loc'])
        # bottom
        a_bottom = roomDist(roomA_middleX, roomA['y_loc'] - roomA['height'], roomB['x_loc'], roomB['y_loc'])
        # left
        a_left = roomDist(roomA['x_loc'], roomA_middleY, roomB['x_loc'], roomB['y_loc'])
        # right
        a_right = roomDist(roomA['x_loc'] + roomA['width'], roomA_middleY, roomB['x_loc'], roomB['y_loc'])
        if min(a_top, a_bottom, a_left, a_right) == a_top:
            # top is start point
            start_A = ({'x_loc' : roomA_middleX, 'y_loc' : roomA['y_loc']})
        elif min(a_top, a_bottom, a_left, a_right) == a_bottom:
            start_A = ({'x_loc' : roomA_middleX, 'y_loc' : roomA['y_loc'] - roomA['height']})
        elif min(a_top, a_bottom, a_left, a_right) == a_left:
            start_A = ({'x_loc' : roomA['x_loc'], 'y_loc' : roomA_middleY})
        elif min(a_top, a_bottom, a_left, a_right) == a_right:
            start_A = ({'x_loc' : roomA['x_loc'] + roomA['width'], 'y_loc' : roomA_middleY})


        # find start point for roomB
        roomB_middleX = roomB['x_loc'] + (roomB['width'] // 2)
        roomB_middleY = roomB['y_loc'] + (roomB['height'] // 2)
        # top
        b_top = roomDist(roomA['x_loc'], roomA['y_loc'], roomB_middleX, roomB['y_loc'])
        # bottom
        b_bottom = roomDist(roomA['x_loc'], roomA['y_loc'], roomB_middleX, roomB['y_loc'] - roomB['height'])
        # left
        b_left = roomDist(roomA['x_loc'], roomA['y_loc'], roomB['x_loc'], roomB_middleY)
        # right
        b_right = roomDist(roomA['x_loc'], roomA['y_loc'], roomB['x_loc'] + roomB['width'],  roomB_middleY)
        if min(b_top, b_bottom, b_left, b_right) == b_top:
            # top is start point
            start_B = ({'x_loc' : roomB_middleX, 'y_loc' : roomB['y_loc']})
        elif min(b_top, b_bottom, b_left, b_right) == b_bottom:
            start_B = ({'x_loc' : roomB_middleX, 'y_loc' : roomB['y_loc'] - roomB['height']})
        elif min(b_top, b_bottom, b_left, b_right) == b_left:
            start_B = ({'x_loc' : roomB['x_loc'], 'y_loc' : roomB_middleY})
        elif min(b_top, b_bottom, b_left, b_right) == b_right:
            start_B = ({'x_loc' : roomB['x_loc'] + roomB['width'], 'y_loc' : roomB_middleY}) 

        # find end point





