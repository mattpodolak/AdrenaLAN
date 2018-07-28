import numpy as np
import math
import random

def path(rooms):
    pathArr = []
    for room in rooms:
        print('room')
        x = room['x_loc']
        y = room['y_loc']
        width = room['width']
        height = room['height']
        num_paths = random.randint(1, 3)
        # find 1 or 2 closest rooms
        near_rooms = minDist(room, rooms)

        for near_room in near_rooms:
            x2 = near_room['x_loc']
            y2 = near_room['y_loc']
            width2 = near_room['width']
            height2 = near_room['height']

            # pick side to start path
            delt_x = x2-x
            delt_y = y2-y

            if(abs(delt_y) < abs(delt_x)):
                print('hello')
                if(delt_y > 0):
                    # start on bottom, pick pixel to start at
                    start_pt_x = random.randint(x+1, x-1+width)
                    start_pt_y = y+height
                    if delt_x > 0:
                        # land on left of block 2
                        end_pt_x = x2
                        end_pt_y = random.randint(y2+1, y2+height2-1)
                        pathArr = createPath(pathArr, 'bottom', start_pt_x, start_pt_y, end_pt_x, end_pt_y)
                    else:
                        # land on right
                        end_pt_x = x2+width2-1
                        end_pt_y = random.randint(y2+1, y2+height2-1)
                        pathArr = createPath(pathArr, 'bottom', start_pt_x, start_pt_y, end_pt_x, end_pt_y)
                else:
                    # start on top, pick pixel to start at
                    start_pt_x = random.randint(x+1, x-1+width)
                    start_pt_y = y
                    if delt_x > 0:
                        # land on left of block 2
                        end_pt_x = x2
                        end_pt_y = random.randint(y2+1, y2+height2-1)
                        pathArr = createPath(pathArr, 'top', start_pt_x, start_pt_y, end_pt_x, end_pt_y)
                    else:
                        # land on right
                        end_pt_x = x2+width2-1
                        end_pt_y = random.randint(y2+1, y2+height2-1)
                        pathArr = createPath(pathArr, 'top', start_pt_x, start_pt_y, end_pt_x, end_pt_y)
            else:
                print('Hello')
                if(delt_x > 0):
                    # start on right, pick pixel to start at
                    start_pt_y = random.randint(y+1, y+height-1)
                    start_pt_x = x+width-1
                    if delt_y > 0:
                        # land on top of block 2
                        end_pt_y = y2
                        end_pt_x = random.randint(x2+1, x2+width2-1)
                    else:
                        # land on bottom
                        end_pt_y = y2+height2-1
                        end_pt_x = random.randint(x2+1, x2+width2-1)
                    pathArr = createPath(pathArr, 'right', start_pt_x, start_pt_y, end_pt_x, end_pt_y)
                else:
                    # start on left, pick pixel to start at
                    start_pt_y = random.randint(y+1, y-1+height)
                    start_pt_x = x
                    if delt_y > 0:
                        # land on top of block 2
                        end_pt_y = y2
                        end_pt_x = random.randint(x2+1, x2+width2-1)
                    else:
                        # land on bottom
                        end_pt_y = y2-1+height2
                        end_pt_x = random.randint(x2+1, x2+width2-1)
                    pathArr = createPath(pathArr, 'left', start_pt_x, start_pt_y, end_pt_x, end_pt_y)
            
            if num_paths == 1:
                break

    return pathArr


# calculates distance between 2 points
def minDist(room, rooms):
    max_dist1 = 0
    min_dist2 = 20000
    max_room1 = room
    min_room2 = room
    x = room['x_loc']
    y = room['y_loc']
    width = room['width']
    height = room['height']
    for i in range(0, len(rooms)):
        if rooms[i] != room:
            x2 = rooms[i]['x_loc']
            y2 = rooms[i]['y_loc']
            width2 = rooms[i]['width']
            height2 = rooms[i]['height']
            # calculate distance
            distX = math.pow((x - x2), 2)
            distY = math.pow((y - y2), 2)
            dist = math.sqrt(distX + distY)

            # update variables
            if dist > max_dist1:
                max_dist1 = dist
                max_room1 = rooms[i]
            if dist < min_dist2:
                min_dist2 = dist
                min_room2 = rooms[i]
    near_rooms = []
    near_rooms.append(max_room1)
    near_rooms.append(min_room2)
    return near_rooms

def createPath(pathArr, startSide, start_x, start_y, end_x, end_y):
    # create path between
    if startSide == 'top':
        for i in range(0, start_y-end_y):
            var = end_y+i
            pathArr.append({'x_loc': start_x, 'y_loc':var})
        if end_x > start_x:
            for i in range(0, end_x-start_x):
                var = start_x+i
                pathArr.append({'x_loc': var, 'y_loc':end_y})
        else:
            for i in range(0, start_x-end_x):
                var = end_x+i
                pathArr.append({'x_loc': var, 'y_loc':end_y})

    elif startSide == 'bottom':
        for i in range(0, end_y-start_y):
            var = start_y+i
            pathArr.append({'x_loc': start_x, 'y_loc':var})
        if end_x > start_x:
            for i in range(0, end_x-start_x):
                var = start_x+i
                pathArr.append({'x_loc': var, 'y_loc':end_y})
        else:
            for i in range(0, start_x-end_x):
                var = start_x-i
                pathArr.append({'x_loc': var, 'y_loc':end_y})

    elif startSide == 'right':
        for i in range(0, end_x-start_x):
            var = end_x-i
            pathArr.append({'x_loc': var, 'y_loc':start_y})
        if end_y > start_y:
            for i in range(0, end_y-start_y):
                var = start_y+i
                pathArr.append({'x_loc': end_x, 'y_loc':var})
        else:
            for i in range(0, start_y-end_y):
                var = end_y+i
                pathArr.append({'x_loc': end_x, 'y_loc':var})

    elif startSide == 'left':
        for i in range(0, start_x-end_x):
            var = end_x+i
            pathArr.append({'x_loc': var, 'y_loc':start_y})
        if end_y > start_y:
            for i in range(0, end_y-start_y):
                var = start_y+i
                pathArr.append({'x_loc': end_x, 'y_loc':var})
        else:
            for i in range(0, start_y-end_y):
                var = end_y+i
                pathArr.append({'x_loc': end_x, 'y_loc':var})


    return pathArr
