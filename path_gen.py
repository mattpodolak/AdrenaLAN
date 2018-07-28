import numpy as np
import math


myArr = [
    {
        'x_loc' : 100,
        'y_loc' : 100,
        'width' : 10,
        'height' : 10,
        'connected' : False
    },
    {
        'x_loc' : 170,
        'y_loc' : 150,
        'width' : 10,
        'height' : 10,
        'connected' : False
    },
    {
        'x_loc' : 300,
        'y_loc' : 300,
        'width' : 10,
        'height' : 10,
        'connected' : False
    },
    {
        'x_loc' : 250,
        'y_loc' : 250,
        'width' : 10,
        'height' : 10,
        'connected' : False
    },   
]

# generate all paths
def generatePaths(room_arr, map_width):
    # loop through each room
    path_arr = []

    for i in range(len(room_arr)):
        room_arr[i]['connected'] = True
        # check other rooms
        minDist = map_width
        closestRoom = ({'x_loc' : 0, 'y_loc' : 0})
        currentRoom = room_arr[i]
        temp_room_arr = [point for point in room_arr if point != currentRoom and point['connected'] == False]
        #print('CURRENT POINT: ', currentRoom)
        #print('OTHER POINTS', temp_room_arr)
        print(i+1)



        for room_temp in temp_room_arr:
            tempDist = roomDist(currentRoom['x_loc'], currentRoom['y_loc'], room_temp['x_loc'], room_temp['y_loc'])
            # found a closer room
            if tempDist < minDist:
                minDist = tempDist
                closestRoom['x_loc'] = room_temp['x_loc']
                closestRoom['y_loc'] = room_temp['y_loc']

        # selected room x, y (center)
        # room_x = roomA['x_loc'] + (room['width'] // 2)
        # room_y = roomA['y_loc'] + (room['height'] // 2)



        print('START POINT   X: ', room_arr[i]['x_loc'], ' Y: ', room_arr[i]['y_loc'])
        print('CLOSEST POINT X: ', closestRoom['x_loc'], ' Y: ', closestRoom['y_loc'])
        print('DISTANCE: ', minDist)
        print('______________________________')
        #path_arr.append(roomPath(room_arr[i], closestRoom))
    


    
    # return path_arr

# calculates distance between 2 points
def roomDist(roomA_x, roomA_y, roomB_x, roomB_y):
    distX = math.pow(roomA_x - roomB_x, 2)
    distY = math.pow(roomA_y - roomB_y, 2)
    
    return math.sqrt(distX + distY)


# creates the shortest path between roomA and roomB
def roomPath(roomA, roomB):
        path_arr = []
        A_direction = ''
        B_direction = ''

        # find START POINT for A
        roomA_middleX = roomA['x_loc'] + (roomA['width'] // 2)
        roomA_middleY = roomA['y_loc'] + (roomA['height'] // 2)
        a_top = roomDist(roomA_middleX, roomA['y_loc'], roomB['x_loc'], roomB['y_loc'])
        a_bottom = roomDist(roomA_middleX, roomA['y_loc'] - roomA['height'], roomB['x_loc'], roomB['y_loc'])
        a_left = roomDist(roomA['x_loc'], roomA_middleY, roomB['x_loc'], roomB['y_loc'])
        a_right = roomDist(roomA['x_loc'] + roomA['width'], roomA_middleY, roomB['x_loc'], roomB['y_loc'])
        if min(a_top, a_bottom, a_left, a_right) == a_top:
            start_A = [{'x_loc' : roomA_middleX, 'y_loc' : roomA['y_loc']}]
            A_direction = 'top'
        elif min(a_top, a_bottom, a_left, a_right) == a_bottom:
            start_A = [{'x_loc' : roomA_middleX, 'y_loc' : roomA['y_loc'] - roomA['height']}]
            A_direction = 'bottom'
        elif min(a_top, a_bottom, a_left, a_right) == a_left:
            start_A = [{'x_loc' : roomA['x_loc'], 'y_loc' : roomA_middleY}]
            A_direction = 'left'
        elif min(a_top, a_bottom, a_left, a_right) == a_right:
            start_A = [{'x_loc' : roomA['x_loc'] + roomA['width'], 'y_loc' : roomA_middleY}]
            A_direction = 'right'

        # find END POINT for B
        roomB_middleX = roomB['x_loc'] + (roomB['width'] // 2)
        roomB_middleY = roomB['y_loc'] + (roomB['height'] // 2)
        b_top = roomDist(roomA['x_loc'], roomA['y_loc'], roomB_middleX, roomB['y_loc'])
        b_bottom = roomDist(roomA['x_loc'], roomA['y_loc'], roomB_middleX, roomB['y_loc'] - roomB['height'])
        b_left = roomDist(roomA['x_loc'], roomA['y_loc'], roomB['x_loc'], roomB_middleY)
        b_right = roomDist(roomA['x_loc'], roomA['y_loc'], roomB['x_loc'] + roomB['width'],  roomB_middleY)
        if min(b_top, b_bottom, b_left, b_right) == b_top:
            start_B = [{'x_loc' : roomB_middleX, 'y_loc' : roomB['y_loc']}]
            B_direction = 'top'
        elif min(b_top, b_bottom, b_left, b_right) == b_bottom:
            start_B = [{'x_loc' : roomB_middleX, 'y_loc' : roomB['y_loc'] - roomB['height']}]
            B_direction = 'bottom'
        elif min(b_top, b_bottom, b_left, b_right) == b_left:
            start_B = [{'x_loc' : roomB['x_loc'], 'y_loc' : roomB_middleY}]
            B_direction = 'left'
        elif min(b_top, b_bottom, b_left, b_right) == b_right:
            start_B = [{'x_loc' : roomB['x_loc'] + roomB['width'], 'y_loc' : roomB_middleY}]
            B_direction = 'right' 

        # X and Y VALUES
        x_val = abs(start_A['x_loc'] - start_B['x_loc'])
        y_val = abs(start_A['y_loc'] - start_B['y_loc'])

        # CONNECT A TO MIDDLE
        if (A_direction == 'top' or A_direction == 'bottom'):
            for i in range(0, y_val + 1):
                if A_direction == 'top':
                    path_arr.append({'x_loc' : start_A['x_loc'], 'y_loc' : start_A['y_loc'] + i})
                elif A_direction == 'bottom':
                    path_arr.append({'x_loc' : start_A['x_loc'], 'y_loc' : start_A['y_loc'] - i})
        elif (A_direction == 'left' or A_direction == 'right'):
            for i in range(0, x_val + 1):
                if A_direction == 'left':
                    path_arr.append({'x_loc' : start_A['x_loc'] - i, 'y_loc' : start_A['y_loc']})
                elif A_direction == 'right':
                    path_arr.append({'x_loc' : start_A['x_loc'] + i, 'y_loc' : start_A['y_loc']})

        # CONNECT B TO MIDDLE
        if (B_direction == 'top' or B_direction == 'bottom'):
            for i in range(0, y_val + 1):
                if B_direction == 'top':
                    path_arr.append({'x_loc' : start_B['x_loc'], 'y_loc' : start_B['y_loc'] + i})
                elif B_direction == 'bottom':
                    path_arr.append({'x_loc' : start_B['x_loc'], 'y_loc' : start_B['y_loc'] - i})
        elif (B_direction == 'left' or B_direction == 'right'):
            for i in range(0, x_val + 1):
                if B_direction == 'left':
                    path_arr.append({'x_loc' : start_B['x_loc'] - i, 'y_loc' : start_B['y_loc']})
                elif B_direction == 'right':
                    path_arr.append({'x_loc' : start_B['x_loc'] + i, 'y_loc' : start_B['y_loc']})

        
        # print statements
        print('A  X: ', start_A['x_loc'], ' Y: ', start_A['y_loc'])
        print('B  X: ', start_B['x_loc'], ' Y: ', start_B['y_loc'])

        return path_arr



print('generating paths...')
generatePaths(myArr, 1000)
print('wow no errors')
# print(myArr)
       



        






