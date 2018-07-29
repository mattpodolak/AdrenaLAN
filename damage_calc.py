import random

def attackSurround(player, monster_arr):
    enemy_around = []
    char_x = player['x_loc']
    char_y = player['y_loc']
    # add all enemies in range
    for enemy in monster_arr:
        if((enemy['x_loc'] <= char_x + 2) and (enemy['x_loc'] >= char_x - 2)) and ((enemy['y_loc'] <= char_y + 2) and (enemy['y_loc'] >= char_y - 2)):
            enemy_around.append(enemy)
    # damage all enemies
    for enemy_near in enemy_around:
        damageTaken(enemy_near, player, monster_arr)


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
    print('You took', damage, 'damage from', enemy['name'], '!')
    print('HP:', player['hp'])

# calculates dmg done to an enemy
def damageTaken(monster, player, monster_arr):
    if monster['hp'] > 0:
        base_att = player['att']
        def_rating = int(monster['def']) / 10
        chance = random.randint(0, 100)
        if chance <= player['crit_chc']:
            # crit occurs
            crit_multiplier = player['crit_dmg']
        else:
            crit_multiplier = 1
        damage = round((base_att * crit_multiplier) * def_rating, 2)
        print(damage, 'damage dealt.')
        monster['hp'] = monster['hp'] - damage

        if monster['hp'] <= 0:
            # monster dead
            monster['hp'] = 0
            player['xp'] = player['xp'] + monster['xp']
            print('You gained', monster['xp'], 'experience.')
            temp_monster_arr = [enemy for enemy in monster_arr if enemy != monster]
            monster_arr = temp_monster_arr

        print(monster['name'], 'has', monster['hp'], 'hp remaining')
        print(monster_arr)
    else:
        temp_monster_arr = [enemy for enemy in monster_arr if enemy != monster]
        monster_arr = temp_monster_arr
        print(monster_arr)
        print(monster['name'], 'is already dead. No attacks made.')