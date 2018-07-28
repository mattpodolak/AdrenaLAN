import random

def loadEnemies(room_arr, num_enemies):

    enemy_arr = []
    start_counter = 0
    while (start_counter != num_enemies):
        # 30%
        random_room = random.choice(room_arr)
        chance = random.randint(0, 100)
        if chance <= 30:
            print(random_room)
            start_counter = start_counter + 1
            x_pos = random.randint(random_room['x_loc'], random_room['x_loc'] + random_room['width'])
            y_pos = random.randint(random_room['y_loc'], random_room['y_loc'] + random_room['height'])
            enemy_arr.append({'x_loc' : x_pos, 'y_loc' : y_pos})
    print('Enemies Loaded:', start_counter)
    return enemy_arr
