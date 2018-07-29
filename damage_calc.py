import random

# calculates dmg done to a player
def attack(enemy, player):
    base_att = enemy['att']
    def_rating = int(player['def']) / 14
    chance = random.randint(0, 100)
    if chance <= enemy['crit_chc']:
        # crit occurs
        crit_multiplier = enemy['crit_dmg']
    else:
        crit_multiplier = 1
    damage = (base_att * crit_multiplier) * def_rating

# calculates dmg done to an enemy
def damageTaken():
