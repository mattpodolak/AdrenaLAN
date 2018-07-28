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
            
            # monster stats
            stat_hp = float("{0:.2f}".format(createStats(10, 2)))
            stat_att = float("{0:.2f}".format(createStats(2, 1)))
            stat_def = float("{0:.2f}".format(createStats(2, 1)))
            stat_elem = None
            crit_dmg = 1.5
            crit_chc = 25
            default_size = 1

            stat_mut = setMutation()
            enemy_arr.append({'x_loc' : x_pos, 'y_loc' : y_pos, 'hp' : stat_hp, 'att' : stat_att, 'elem' : stat_elem, 'crit_dmg' : crit_dmg, 'crit_chc' : crit_chc, 'mutations' : stat_mut, 'size' : default_size})
            # health, lvl, attack, xp 
    print('Enemies Loaded:', start_counter)
    return enemy_arr

def createStats(base, deviation):
    mu, sigma = base, deviation
    return random.choice(np.random.normal(mu, sigma, 100))

def setMutation():
    mut_list = ['Hellspawn', 'Friendly', 'Spiteful', 'Thicc', 'Goofy', 'Facist', 'Undead', 'Nefarious', 'Useless', 'Raid', 'Dank']
    full_list = []
    num_mut = abs(int(createStats(2, 2)))
    for i in range(num_mut - 1):
        full_list.append(random.choice(mut_list))
    return full_list
