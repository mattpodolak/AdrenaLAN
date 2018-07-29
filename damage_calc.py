import random

def attackSurround(player, monster_arr, console):
    fail_move = ['You hit nothing...', 'Wow the air felt that one...', 'You should get your eyes checked mate.', 'What are you looking for?']
    enemy_around = []
    char_x = player['x_loc']
    char_y = player['y_loc']
    # add all enemies in range
    for enemy in monster_arr:
        if((enemy['x_loc'] <= char_x + 1) and (enemy['x_loc'] >= char_x - 1)) and ((enemy['y_loc'] <= char_y + 1) and (enemy['y_loc'] >= char_y - 1)):
            enemy_around.append(enemy)
    # damage all enemies
    for enemy_near in enemy_around:
        damageTaken(enemy_near, player, console)
    if not enemy_around:
        console.append(random.choice(fail_move))


# calculates dmg done to a player
def attack(enemy, player, monster_arr):
    base_att = enemy['att']
    def_rating = (int(player['def']) / 10)
    chance = random.randint(0, 100)
    if chance <= enemy['crit_chc']:
        # crit occurs
        crit_multiplier = enemy['crit_dmg']
    else:
        crit_multiplier = 1
    if def_rating <= 0:
        damage = round((base_att * crit_multiplier) * (def_rating + 1), 2)
    else:
        damage = round((base_att * crit_multiplier) * (def_rating), 2)
    player['hp'] = player['hp'] - damage
    # print('You took', damage, 'damage from', enemy['name'], '!')
    # print('HP:', player['hp'])

# calculates dmg done to an enemy
def damageTaken(monster, player, console):
    if monster['hp'] > 0:
        base_att = player['att']
        def_rating = int(abs(monster['def'])) / 10
        chance = random.randint(0, 100)
        if chance <= player['crit_chc']:
            # crit occurs
            crit_multiplier = player['crit_dmg']
        else:
            crit_multiplier = 1
        if def_rating == 0:
            def_rating = 0.5
        damage = (base_att * crit_multiplier) * def_rating
        console.append(str(damage) + ' damage dealt to ' +  str(monster['name']))
        
        monster['hp'] = monster['hp'] - damage

        if monster['hp'] <= 0:
            # monster dead
            monster['hp'] = 0
            player['xp'] = player['xp'] + monster['xp']
            console.append('You gained ' +  str(monster['xp']) + ' experience. Total XP: ' + str(player['xp']))
            # temp_monster_arr = [enemy for enemy in monster_arr if enemy != monster]
            # monster_arr = temp_monster_arr

        # print(monster['name'], 'has', monster['hp'], 'hp remaining')
        # print(monster_arr)
    # else:
    #     temp_monster_arr = [enemy for enemy in monster_arr if enemy != monster]
    #     monster_arr = temp_monster_arr
        # print(monster_arr)
        # print(monster['name'], 'is already dead. No attacks made.')