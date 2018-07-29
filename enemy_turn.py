import math
import numpy as np

def enemy_move(char_x_rel, char_y_rel, fog_size, window_x_units, window_y_units, enemyArr, mapArr):
    # only make a move if in fog
    fog_x = char_x_rel-fog_size
    fog_x2 = char_x_rel+fog_size
    fog_y = char_y_rel-fog_size
    fog_y2 = char_y_rel+fog_size
    tempArr = []
    for enemy in enemyArr:
        tempEnemy = enemy

        x_rel = enemy['x_loc'] - window_x_units
        y_rel = enemy['y_loc'] - window_y_units
        tempEnemy['willAtk']=False

        # make a move if in non fog
        if((x_rel >= fog_x and x_rel <= fog_x2) and (y_rel >= fog_y and y_rel <= fog_y2)):
            x = enemy['x_loc']
            y = enemy['y_loc']

            # check if can attack
            if((char_x_rel == x_rel and (char_y_rel == y_rel+1 or char_y_rel == y_rel-1)) or (char_y_rel == y_rel and (char_x_rel == x_rel+1 or char_x_rel == x_rel-1))):
                tempEnemy['willAtk']=True
            
            else:
                #check for move
                char_x = char_x_rel + window_x_units
                char_y = char_y_rel + window_y_units
                new_x, new_y = validMoves(x, y, enemyArr, mapArr, char_x, char_y)
                tempEnemy.update({'x_loc': new_x, 'y_loc': new_y})
        tempArr.append(tempEnemy)
    return tempArr
            
# calculates distance between 2 points
def dist(x1, x2, y1, y2):
    distX = math.pow(x1 - x2, 2)
    distY = math.pow(y1 - y2, 2)
    
    return math.sqrt(distX + distY)            



def validMoves(x, y, enemyArr, mapArr, char_x, char_y):
    check = []
    if(mapArr[x, y+1] == 0):
        check.append({'x':x, 'y':y+1})
    if(mapArr[x, y-1] == 0):
        check.append({'x':x, 'y':y-1})
    if(mapArr[x+1, y] == 0):
        check.append({'x':x+1, 'y':y})
    if(mapArr[x-1, y] == 0):
        check.append({'x':x-1, 'y':y})
    
    minDist = 1000
    minpair_x = x
    minpair_y = y
    for pair in check:
        # dont walk onto other enemies
        if checkForEnemy(pair['x'], pair['y'], enemyArr):
            distance = dist(pair['x'], char_x, pair['y'], char_y)

            if distance < minDist:
                minpair_x = pair['x']
                minpair_y = pair['y']
                minDist = distance
    
    return minpair_x, minpair_y



def checkForEnemy(x, y, enemyArr):
    # return false if enemy occupying space
    # return true if u can move there
    for enemy in enemyArr:
        en_x = enemy['x_loc']
        en_y = enemy['y_loc']
        if(en_x == x and en_y == y):
            print('Enemy in the way')
            return False
    
    return True
