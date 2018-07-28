import numpy as np
import math

# generate all paths
def generatePaths(room_arr):
    # loop through each room
    path_arr = []

    for i in range(len(room_arr)):
        room_arr[i]['connected'] = True
        # check other rooms
        minDist = 1000
        closestRoom = ({'x_loc' : 0, 'y_loc' : 0, 'width' : 0, 'height' : 0})
        currentRoom = room_arr[i]
        if currentRoom != room_arr[-1]:
            temp_room_arr = [point for point in room_arr if point != currentRoom and point['connected'] == False]
        else:
            temp_room_arr = [point for point in room_arr if point != currentRoom]
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
                closestRoom['height'] = room_temp['height']
                closestRoom['width'] = room_temp['width']


        print('START POINT   X: ', room_arr[i]['x_loc'], ' Y: ', room_arr[i]['y_loc'], ' W: ', room_arr[i]['width'], 'H: ', room_arr[i]['height'])
        print('CLOSEST POINT X: ', closestRoom['x_loc'], ' Y: ', closestRoom['y_loc'], ' W: ', closestRoom['width'], 'H: ', closestRoom['height'])
        print('DISTANCE: ', minDist)
        path_arr.extend(roomPath(room_arr[i], closestRoom))
        print('______________________________________________')
    
    return path_arr

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
        a_bottom = roomDist(roomA_middleX, roomA['y_loc'] + roomA['height'], roomB['x_loc'], roomB['y_loc'])
        a_left = roomDist(roomA['x_loc'], roomA_middleY, roomB['x_loc'], roomB['y_loc'])
        a_right = roomDist(roomA['x_loc'] + roomA['width'], roomA_middleY, roomB['x_loc'], roomB['y_loc'])
        a_list = [a_top, a_bottom, a_left, a_right]
        if min(a_list) == a_top:
            start_A = {'x_loc' : roomA_middleX, 'y_loc' : roomA['y_loc']}
            A_direction = 'top'
        elif min(a_list) == a_bottom:
            start_A = {'x_loc' : roomA_middleX, 'y_loc' : roomA['y_loc'] + roomA['height']}
            A_direction = 'bottom'
        elif min(a_list) == a_left:
            start_A = {'x_loc' : roomA['x_loc'], 'y_loc' : roomA_middleY}
            A_direction = 'left'
        elif min(a_list) == a_right:
            start_A = {'x_loc' : roomA['x_loc'] + roomA['width'], 'y_loc' : roomA_middleY}
            A_direction = 'right'
        
        print('COORD_A (', start_A['x_loc'], ', ', start_A['y_loc'], ')')
        print('DIRECT_A: ', A_direction)

        # find END POINT for B
        roomB_middleX = roomB['x_loc'] + (roomB['width'] // 2)
        roomB_middleY = roomB['y_loc'] + (roomB['height'] // 2)
        b_top = roomDist(roomA['x_loc'], roomA['y_loc'], roomB_middleX, roomB['y_loc'])
        b_bottom = roomDist(roomA['x_loc'], roomA['y_loc'], roomB_middleX, roomB['y_loc'] + roomB['height'])
        b_left = roomDist(roomA['x_loc'], roomA['y_loc'], roomB['x_loc'], roomB_middleY)
        b_right = roomDist(roomA['x_loc'], roomA['y_loc'], roomB['x_loc'] + roomB['width'],  roomB_middleY)
        b_list = [b_top, b_bottom, b_left, b_right]
        if min(b_list) == b_top:
            start_B = {'x_loc' : roomB_middleX, 'y_loc' : roomB['y_loc']}
            B_direction = 'top'
        elif min(b_list) == b_bottom:
            start_B = {'x_loc' : roomB_middleX, 'y_loc' : roomB['y_loc'] + roomB['height']}
            B_direction = 'bottom'
        elif min(b_list) == b_left:
            start_B = {'x_loc' : roomB['x_loc'], 'y_loc' : roomB_middleY}
            B_direction = 'left'
        elif min(b_list) == b_right:
            start_B = {'x_loc' : roomB['x_loc'] + roomB['width'], 'y_loc' : roomB_middleY}
            B_direction = 'right' 

        print('COORD_B (', start_B['x_loc'], ', ', start_B['y_loc'], ')')
        print('DIRECT_B: ', B_direction)

        # X and Y VALUES
        x_val = abs(start_A['x_loc'] - start_B['x_loc'])
        y_val = abs(start_A['y_loc'] - start_B['y_loc'])
        print('BASE:', x_val)
        print('HEIGHT', y_val)

       # Connect A and B
        for i in range(x_val+1):
            # A is more left
            if(start_A['x_loc'] <= start_B['x_loc']):
                path_arr.append({'x_loc' : (start_A['x_loc'] + x_val - i), 'y_loc' : start_A['y_loc']})
                ini_starta = start_A['x_loc'] + x_val
                for j in range(y_val+1):
                    # A is higher
                    if(start_A['y_loc'] <= start_B['x_loc']):
                        path_arr.append({'x_loc' : ini_starta, 'y_loc' : start_B['y_loc'] - j})
                    else:
                        path_arr.append({'x_loc' : ini_starta, 'y_loc' : start_B['y_loc'] + j})
            # B is more left
            else: 
                path_arr.append({'x_loc' : (start_B['x_loc'] + x_val - i), 'y_loc' : start_B['y_loc']})
                ini_startb = start_B['x_loc'] + x_val
                for j in range(y_val+1):
                    # A is higher
                    if(start_A['y_loc'] <= start_B['x_loc']):
                        path_arr.append({'x_loc' : ini_startb, 'y_loc' : start_A['y_loc'] - j})
                    else:
                        path_arr.append({'x_loc' : ini_startb, 'y_loc' : start_A['y_loc'] + j})
       
        return path_arr




        






