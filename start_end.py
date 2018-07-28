import random
import numpy as np

def gen_start(rooms):
    print('Picking starting point')
    num_rooms = len(rooms)

    # pick a start room
    room_pick = random.randint(0, num_rooms-1)
    print('Start Room ', room_pick)
    room = rooms[room_pick]

    x = room['x_loc']
    x2 = x+room['width']
    y = room['y_loc']
    y2 = y+room['height']

    start_x = random.randint(x, x2)
    start_y = random.randint(y, y2)
    print('Start x, y ', start_x, start_y)

    return start_x, start_y, room_pick

def gen_end(rooms, start_room):
    print('Picking end point')
    num_rooms = len(rooms)

    while True:
        # pick a start room
        room_pick = random.randint(0, num_rooms-1)
        if room_pick != start_room:
            break

    print('End Room ', room_pick)
    room = rooms[room_pick]

    x = room['x_loc']
    x2 = x+room['width']
    y = room['y_loc']
    y2 = y+room['height']

    end_x = random.randint(x, x2)
    end_y = random.randint(y, y2)
    print('End x, y ', end_x, end_y)

    return end_x, end_y

