import sys, pygame, map_gen, path_gen2, start_end, enemy_gen, damage_calc, enemy_turn
import numpy as np
import pygame.surfarray as surfarray
import pygame
import random

#pylint shows as an errror
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 12)
consolefont = pygame.font.SysFont('Comic Sans MS', 16)
hudfont = pygame.font.SysFont('Arial', 30)

'''

GENERATION VARIABLES

'''
map_min_width = 50
map_max_width = 65
map_min_height = 50
map_max_height = 65
min_rooms = 4
max_rooms = 6
min_size = 4
max_size = 8
min_dist_bw_rooms = 2

'''

DISPLAY VARIABLES

'''
# pixels in a unit
unit_size = 64

white = 1, 1, 1
black = 0, 0, 0

# window location
window_x_units = 0
window_y_units = 0

# window size with pixels and units
window_width_units = 20
window_height_units = 10
window_width = window_width_units * unit_size
window_height = window_height_units * unit_size

# window size
size = window_width, window_height
fog_size = 3

mapArr = map_gen.generateMap(map_min_width, map_max_width, map_min_height, map_max_height)
mapWidth, mapHeight = mapArr.shape

print('Width, Height', mapWidth, mapHeight)
rooms = map_gen.generateRooms(min_rooms, max_rooms, min_size, max_size, min_dist_bw_rooms, mapWidth, mapHeight)

console_log = []

# main hero
hero_stats = {
    'x_loc': 0,
    'y_loc' : 0,
    'hp' : 100,
    'att' : 10,
    'def' : 10,
    'crit_dmg' : 1.5,
    'crit_chc' : 30,
    'xp' : 0,
    'mutations': [],
    'elem' : None,
    'weapon' : 'Fist'
}


# add rooms
print('Loading rooms onto map')
for room in rooms:
    x = room['x_loc']
    x2 = x+room['width']
    y = room['y_loc']
    y2 = y+room['height']
    print('Passed room vars (x, x2, y, y2): ', x, x2, y, y2)
    # 2 is wall surrounding a floor
    mapArr[x-1:x2+1, y-1:y2+1] = 2
    # 0 is floor
    mapArr[x:x2, y:y2] = 0

# pick start and end points
char_x, char_y, start_room = start_end.gen_start(rooms)
end_x, end_y = start_end.gen_end(rooms, start_room)

# char position relative to screen
char_x_rel = window_width_units//2
char_y_rel = window_height_units//2

# adjust screen to focus on character
# ensure screen isnt pushed out of area
if(char_x < char_x_rel):
    char_x_rel = char_x
    window_x_units = 0
elif(char_x+char_x_rel>= mapWidth):
    char_x_rel = char_x-mapWidth+window_width_units
    window_x_units = mapWidth-window_width_units
else:
    window_x_units = char_x - char_x_rel

if(char_y < char_y_rel):
    char_y_rel = char_y
    window_y_units = 0
elif(char_y+char_y_rel>= mapHeight):
    char_y_rel = char_y-mapHeight+window_height_units
    window_y_units = mapHeight-window_height_units
else:
    window_y_units = char_y - char_y_rel

# add paths
print('______________________________________________')
print('Generating paths')
paths = path_gen2.path(rooms)
print('Loading paths onto map')
for path in paths:
    x = path['x_loc']
    y = path['y_loc']
    mapArr[x, y] = 0


# add walls for paths
for x in range(1, mapWidth-2):
    for y in range(1, mapHeight-2):
        if(mapArr[x, y] == 0):
            if(mapArr[x, y+1] == 1):
                mapArr[x, y+1] = 2
            if(mapArr[x+1, y] == 1):
                mapArr[x+1, y] = 2
            if(mapArr[x, y-1] == 1):
                mapArr[x, y-1] = 2
            if(mapArr[x-1, y] == 1):
                mapArr[x-1, y] = 2

# LOAD ENEMIES
enemyArr = []
enemyArr.extend(enemy_gen.loadEnemies(rooms, max_rooms, 'Starboi'))
enemyArr.extend(enemy_gen.loadEnemies(rooms, round(max_rooms * 1.5), 'Demondog'))
enemyArr.extend(enemy_gen.loadEnemies(rooms, 3, 'Hells Janitor'))
for enemy in enemyArr:
    # enemy_arr.append({'x_loc' : x_pos, 'y_loc' : y_pos, 'hp' : stat_hp, 'att' : stat_att, 'elem' : stat_elem, 'crit_dmg' : crit_dmg, 'crit_chc' : crit_chc, 'mutations' : stat_mut, 'size' : default_size})
    enemy_gen.updateMut(enemy)
    round(enemy['hp'], 2)
    round(enemy['att'], 2)
    round(enemy['def'], 2)
    print('MONSTER:', enemy['name'], '| HP:', enemy['hp'],'| ATT:', enemy['att'], '| DEF:', enemy['def'], '| Element', enemy['elem'], '| CDMG:', str(enemy['crit_dmg']) + 'X', '| CHC:', str(enemy['crit_chc']) + '%', '| MUTATIONS:', enemy['mutations'], '| XP:', str(enemy['xp']) + ' pts')

# hero stats
print('HERO BASE STATS ', '     HP:', hero_stats['hp'],'| ATT:', hero_stats['att'], '| DEF:', hero_stats['def'], '| Element:', hero_stats['elem'], '| CDMG:', str(hero_stats['crit_dmg']) + 'X', '| CHC:', str(hero_stats['crit_chc']) + '%', '| MUTATIONS: ', hero_stats['mutations'], 'XP:', hero_stats['xp'])


# Create graphical window
screen = pygame.display.set_mode(size)
screen.fill(white)

wall = pygame.image.load("assets/wall/default-wall-64.bmp")
floor = pygame.image.load("assets/floor/default-floor-64.bmp")
char = pygame.image.load("assets/character/knight-64.png")
goal = pygame.image.load("assets/floor/goal-64.png")
fog = pygame.image.load("assets/misc/fog-64.png")
antifog = pygame.image.load("assets/misc/antifog-64.png")
starfish = pygame.image.load("assets/enemy/starfish-64.png")
dog = pygame.image.load("assets/enemy/demondog-64.png")
ogre = pygame.image.load("assets/enemy/hellsjanitor.png")

def checkForEnemy(x, y):
    # return false if enemy occupying space
    # return true if u can move there
    for enemy in enemyArr:
        en_x = enemy['x_loc']
        en_y = enemy['y_loc']
        if(en_x == x and en_y == y):
            console_log.append({'log' : 'Enemy in the way', 'id' : 0})
            damage_calc.attackSurround(hero_stats, enemyArr, console_log)
            renderMap()
            return False
    return True
    
def validMove(move):
    arrayLoc_x = window_x_units + char_x_rel
    arrayLoc_y = window_y_units + char_y_rel

    if(move == 'w' and arrayLoc_y != 0):
        # print('next move ', mapArr[arrayLoc_x, arrayLoc_y-1])
        if(mapArr[arrayLoc_x, arrayLoc_y-1] == 0):
            return checkForEnemy(arrayLoc_x, arrayLoc_y-1)
        else:
            return False
    elif(move == 's' and arrayLoc_y != mapHeight):
        # print('next move ', mapArr[arrayLoc_x, arrayLoc_y+1])
        if(mapArr[arrayLoc_x, arrayLoc_y+1] == 0):
            return checkForEnemy(arrayLoc_x, arrayLoc_y+1)
        else:
            return False
    elif(move == 'a' and arrayLoc_x != 0):
        # print('next move ', mapArr[arrayLoc_x-1, arrayLoc_y])
        if(mapArr[arrayLoc_x-1, arrayLoc_y] == 0):
            return checkForEnemy(arrayLoc_x-1, arrayLoc_y)
        else:
            return False
    elif(move == 'd' and arrayLoc_x != mapWidth):
        # print('next move ', mapArr[arrayLoc_x+1, arrayLoc_y])
        if(mapArr[arrayLoc_x+1, arrayLoc_y] == 0):
            return checkForEnemy(arrayLoc_x+1, arrayLoc_y)
        else:
            return False
    else:
        return False
        

def renderMap():
    global enemyArr
    for enemies in enemyArr:
        if enemies['hp'] <= 0:
            enemyArr.remove(enemies)
        float("{0:.2f}".format(enemies['hp']))
        float("{0:.2f}".format(enemies['att']))
        float("{0:.2f}".format(enemies['def']))
    #Clear screen
    screen.fill(black) 
    # if called either init / player made a move
    tempArr = enemy_turn.enemy_move(char_x_rel, char_y_rel, fog_size, window_x_units, window_y_units, enemyArr, mapArr)
    enemyArr = tempArr
    # enemies attack
    for enemy in enemyArr:
        if enemy['willAtk'] == True:
            damage_calc.attack(enemy, hero_stats, console_log)

    # create rectangles
    for x in range(window_x_units, window_width_units+window_x_units):
        for y in range(window_y_units, window_height_units+window_y_units):
            # shift graphics depending on window location
            new_x = x-window_x_units
            new_y = y-window_y_units
            if(mapArr[x, y] == 2):
                #print('Drawing wall')
                screen.blit(wall, (new_x*unit_size, new_y*unit_size, unit_size, unit_size))
            elif(mapArr[x, y] == 0):
                #print('Drawing floor')
                screen.blit(floor, (new_x*unit_size, new_y*unit_size, unit_size, unit_size))               

    #load fog data
    fog_x = char_x_rel-fog_size
    fog_x2 = char_x_rel+fog_size
    fog_y = char_y_rel-fog_size
    fog_y2 = char_y_rel+fog_size
    for x in range(0, window_width_units):
        for y in range(0, window_height_units):
            # draw antifog of war
            if not ((x >= fog_x and x <= fog_x2) and (y >= fog_y and y <= fog_y2)):
                screen.blit(fog, (x*unit_size, y*unit_size, unit_size, unit_size))

    # draw goal point
    new_x = end_x-window_x_units
    new_y = end_y-window_y_units
    # if not in the fog display
    if((new_x >= fog_x and new_x <= fog_x2)and (new_y >= fog_y and new_y <= fog_y2)):
        screen.blit(goal, (new_x*unit_size, new_y*unit_size, unit_size, unit_size))

    # draw hero
    hero_stats['x_loc'] = char_x_rel + window_x_units
    hero_stats['y_loc'] = char_y_rel + window_y_units
    screen.blit(char, (char_x_rel*unit_size, char_y_rel*unit_size, unit_size, unit_size))


    # console log
    # id 0 = passive, 1 = combat, 2 = xp
    count = 0
    for log in reversed(console_log):
        consoleX = hero_stats['x_loc'] - 5
        consoleY = hero_stats['y_loc'] + 500
        if log['id'] == 0:
            color = (255, 255, 0)
        elif log['id'] == 1:
            color = (255, 0, 0)
        elif log['id'] == 2:
            color = (0, 191, 255)
        elif log['id'] == 3:
            color = (255, 69, 0)
        elif log['id'] == 4:
            color = (0, 255, 0)

        console_text = consolefont.render(log['log'], 1, color)
        screen.blit(console_text, (consoleX, consoleY - (count * 20)))
        count = count + 1
    
    # HUD
    # HEALTH
    for i in range(int(hero_stats['hp'])):
        hud_hp = hudfont.render('I', 1, (0, 255, 0))
        screen.blit(hud_hp, (hero_stats['x_loc'] + 1200 - (i * 10), hero_stats['y_loc'] - 5))
    # ATT
    hud_att = hudfont.render(str(hero_stats['att']), 1, (255, 0, 0))
    screen.blit(hud_att, (hero_stats['x_loc'] + 1180, (hero_stats['y_loc'] + 30)))
    # DEF
    hud_def = hudfont.render(str(hero_stats['def']), 1, (128, 128, 128))
    screen.blit(hud_def, (hero_stats['x_loc'] + 1180, (hero_stats['y_loc'] + 60)))
    # XP
    hud_xp = hudfont.render('XP: ' + str(hero_stats['xp']), 1, (0, 191, 255))
    screen.blit(hud_xp, (hero_stats['x_loc'] + 1130, (hero_stats['y_loc'] + 90)))
    # Current weapon
    hud_wep = hudfont.render('Equipped: ' + str(hero_stats['weapon']), 1, (100, 100, 100))
    screen.blit(hud_wep, (hero_stats['x_loc'] + 1048, (hero_stats['y_loc'] + 120)))    

    # draw enemies
    ct = 0
    for enemy in enemyArr:
        showStats_HP = myfont.render('HP: '+str(enemy['hp']), 1, (255, 0, 0))
        new_x = enemy['x_loc']-window_x_units
        new_y = enemy['y_loc']-window_y_units
        print(ct, enemy['x_loc'], enemy['y_loc'])
        ct+=1
    
        # if not in the fog display
        if((new_x >= fog_x and new_x <= fog_x2)and (new_y >= fog_y and new_y <= fog_y2)):
            if (enemy['name'] == 'Starboi'):
                screen.blit(starfish, (new_x*unit_size, new_y*unit_size, unit_size, unit_size))
            elif (enemy['name'] == 'Demondog'):
                screen.blit(dog, (new_x*unit_size, new_y*unit_size, unit_size, unit_size))
            elif (enemy['name'] == 'Hells Janitor'):
                screen.blit(ogre, (new_x*unit_size, new_y*unit_size, unit_size, unit_size))
            screen.blit(showStats_HP, (new_x*unit_size + (0.1*unit_size), new_y*unit_size - (0.4*unit_size)))

    # nextArr = enemy_turn.enemy_move(char_x_rel, char_y_rel, fog_size, window_x_units, window_y_units, enemyArr, mapArr)
    # for i in range(len(nextArr)):
    #     enemyArr[i]['x_loc'] = nextArr[i]['x_loc']
    #     enemyArr[i]['y_loc'] = nextArr[i]['y_loc']

renderMap()

def moveScreen(keyWASD):
    global window_x_units
    global window_y_units
    global char_x_rel
    global char_y_rel
    list_moves = ['Slash!', 'Stab!', 'Cleave!', 'Charge!']

    if(keyWASD == 'w'):
        # check if move is possible
        if(window_y_units > 0 and char_y_rel == window_height_units//2):
            if(True == validMove('w')):
                window_y_units-=1
                renderMap()
        elif(True == validMove('w')):
            char_y_rel-=1
            renderMap()
        else:
            print('Cant move that direction')

    elif(keyWASD == 'a'):
        # check if move is possible
        if(window_x_units > 0 and char_x_rel == window_width_units//2):
            if(True == validMove('a')):
                window_x_units-=1
                renderMap()
        elif(True == validMove('a')):
            char_x_rel-=1
            renderMap()
        else:
            print('Cant move that direction')

    elif(keyWASD == 's'):
        # check if move is possible
        if(window_y_units + window_height_units < mapHeight and char_y_rel == window_height_units//2):
            if(True == validMove('s')):
                window_y_units+=1
                renderMap()
        elif(True == validMove('s')):
            char_y_rel+=1
            renderMap()
        else:
            print('Cant move that direction')

    elif(keyWASD == 'd'):
        # check if move is possible
        if(window_x_units + window_width_units < mapWidth and char_x_rel == window_width_units//2):
            if(True == validMove('d')):
                window_x_units+=1
                renderMap()
        elif(True == validMove('d')):
            char_x_rel+=1
            renderMap()
        else:
            print('Cant move that direction')

    # attack move
    elif(keyWASD == 'p'):
        console_log.append({'log' : random.choice(list_moves), 'id' : 1})
        damage_calc.attackSurround(hero_stats, enemyArr, console_log)
        renderMap()


# runs the game
while 1:
    for event in pygame.event.get():
        #pylint shows as an error
        if event.type == pygame.QUIT: 
            print('Exiting..')
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # button is being pressed
            if event.key == pygame.K_w:
                # print('Pressed w')
                moveScreen('w')
            elif event.key == pygame.K_s:
                # print('Pressed s')
                moveScreen('s') 
            elif event.key == pygame.K_a:
                # print('Pressed a')
                moveScreen('a') 
            elif event.key == pygame.K_d:
                # print('Pressed d')
                moveScreen('d')
            elif event.key == pygame.K_p:
                # attack
                moveScreen('p') 
    
    #Make drawn items appear
    pygame.display.flip()