import random

# calculates dmg done to a player
def attack(enemy, player):
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
    print('You took', damage, 'damage!')
    print('HP:', player['hp'])

# calculates dmg done to an enemy
def damageTaken(monster, player):
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
        print('Monster has', monster['hp'], 'hp remaining')
    else:
        print('Monster is already dead. No attacks made.')


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
    'hp' : 10,
    'att' : 6,
    'def' : 3,
    'crit_dmg' : 1.5,
    'crit_chc' : 25,
    'xp' : 18,
    'mutations': ['Raid'],
    'elem' : None
}
print('///// 1 /////')
damageTaken(monster_1, default_p1)
print('///// 2 /////')
damageTaken(monster_1, default_p1)
print('///// 3 /////')
damageTaken(monster_1, default_p1)
print('///// 4 /////')
damageTaken(monster_1, default_p1)
print('Total XP:', default_p1['xp'])