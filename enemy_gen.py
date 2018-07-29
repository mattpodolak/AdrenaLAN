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
            default_xp = 10
            stat_mut = setMutation()
            enemy_arr.append({'x_loc' : x_pos, 'y_loc' : y_pos, 'hp' : stat_hp, 'att' : stat_att, 'def' : stat_def, 'elem' : stat_elem, 'crit_dmg' : crit_dmg, 'crit_chc' : crit_chc, 'mutations' : stat_mut, 'size' : default_size, 'xp' : default_xp})
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

# mutations affect stats
def updateMut(sel_enemy):
    mut_list = sel_enemy['mutations']
    # check each mutation
    if 'Hellspawn' in mut_list:
        sel_enemy['att'] = float("{0:.2f}".format(sel_enemy['att'] + int(createStats(2, 1))))
        sel_enemy['xp'] = sel_enemy['xp'] + 2
    elif 'Friendly' in mut_list:
        sel_enemy['xp'] = sel_enemy['xp'] - 4
        sel_enemy['crit_dmg'] = 0
        sel_enemy['crit_chc'] = 0
    elif 'Spiteful' in mut_list:
        sel_enemy['att'] = float("{0:.2f}".format(sel_enemy['att'] + int(createStats(4, 1))))
        sel_enemy['xp'] = sel_enemy['xp'] + 3
    elif 'Thicc' in mut_list:  
        sel_enemy['hp'] = float("{0:.2f}".format(int(sel_enemy['hp'] * 1.5)))
        sel_enemy['xp'] = sel_enemy['xp'] + 4
    elif 'Goofy' in mut_list:
        sel_enemy['def'] = sel_enemy['def'] - 5
        sel_enemy['xp'] = sel_enemy['xp'] - 5
    elif 'Facist' in mut_list:
        sel_enemy['xp'] = sel_enemy['xp'] + 5
    elif 'Undead' in mut_list:
        sel_enemy['att'] = float("{0:.2f}".format(sel_enemy['att'] + int(createStats(3, 1))))
        sel_enemy['def'] = sel_enemy['def'] - 2
        sel_enemy['xp'] = sel_enemy['xp'] + 3
        sel_enemy['elem'] = 'dark'
    elif 'Nefarious' in mut_list:
        sel_enemy['att'] = float("{0:.2f}".format(sel_enemy['att'] + int(createStats(8, 1))))
        sel_enemy['hp'] = sel_enemy['hp'] + 5
        sel_enemy['xp'] = sel_enemy['xp'] + 20
        sel_enemy['elem'] = 'fire'
    elif 'Useless' in mut_list:
        sel_enemy['hp'] = 5
        sel_enemy['def'] = 10
    elif 'Raid' in mut_list:
        sel_enemy['att'] = float("{0:.2f}".format(sel_enemy['att'] + int(createStats(2, 1))))
        sel_enemy['hp'] = sel_enemy['hp'] + 2
        sel_enemy['xp'] = sel_enemy['xp'] + 8
        sel_enemy['elem'] = 'fire'
    elif 'Dank' in mut_list:
        sel_enemy['att'] = float("{0:.2f}".format(sel_enemy['att'] * 2))
        sel_enemy['hp'] = float("{0:.2f}".format(sel_enemy['hp'] / 4))
        sel_enemy['def'] = 0
        sel_enemy['xp'] = sel_enemy['xp'] + 10
        sel_enemy['elem'] = 'Earth'
    
    # balance defence
    if (sel_enemy['def'] >= 10):
        sel_enemy['def'] = 10
