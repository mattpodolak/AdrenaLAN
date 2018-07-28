import random
import numpy as np

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
            x_pos = random.randint(random_room['x_loc'], random_room['x_loc'] + random_room['width'] -1)
            y_pos = random.randint(random_room['y_loc'], random_room['y_loc'] + random_room['height'] -1)
            stat_hp = float("{0:.2f}".format(createStats(10, 2)))
            stat_att = float("{0:.2f}".format(createStats(5, 1)))
            enemy_arr.append({'x_loc' : x_pos, 'y_loc' : y_pos, 'hp' : stat_hp, 'att' : stat_att})
            # health, lvl, attack, xp 
    print('Enemies Loaded:', start_counter)
    return enemy_arr

def createStats(base, deviation):
    mu, sigma = base, deviation
    return random.choice(np.random.normal(mu, sigma, 100))
