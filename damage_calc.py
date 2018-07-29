import random

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


default_p1 ={
    'hp' : 30,
    'att' : 10,
    'def' : 8,
    'crit_dmg' : 1.5,
    'crit_chc' : 30,
    'xp' : 0,
    'mutations': [],
    'elem' : None
}

monster_1 ={
    'name': 'badboi',
    'hp' : 10,
    'att' : 6,
    'def' : 3,
    'crit_dmg' : 1.5,
    'crit_chc' : 25,
    'xp' : 18,
    'mutations': ['Raid'],
    'elem' : None
}


monster_2 ={
    'name' : 'spookyboi',
    'hp' : 8,
    'att' : 4,
    'def' : 8,
    'crit_dmg' : 2.5,
    'crit_chc' : 25,
    'xp' : 10,
    'mutations': ['Raid'],
    'elem' : None
}

monster_arr = []
monster_arr.append(monster_1)
monster_arr.append(monster_2)
print(monster_arr)


print('\n')
damageTaken(monster_1, default_p1, monster_arr)
print('\n')
damageTaken(monster_1, default_p1, monster_arr)
print('\n')
if monster_1['hp'] == 0:
    damageTaken(monster_2, default_p1, monster_arr)
else:
    damageTaken(monster_1, default_p1, monster_arr)
print('\n')
damageTaken(monster_2, default_p1, monster_arr)
print('\n')
damageTaken(monster_2, default_p1, monster_arr)
print('\n')
damageTaken(monster_2, default_p1, monster_arr)
print('Total XP:', default_p1['xp'])
print('________________________________________________________________________________________________________________')