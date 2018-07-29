import math
import numpy as np

def enemy_move(char_x_rel, char_y_rel, fog_size, window_x_units, window_y_units, enemyArr, mapArr):
    # only make a move if in fog
    fog_x = char_x_rel-fog_size
    fog_x2 = char_x_rel+fog_size
    fog_y = char_y_rel-fog_size
    fog_y2 = char_y_rel+fog_size

    tempArr = enemyArr
    ct = 0
    for enemy in enemyArr:
        x_rel = enemy['x_loc'] - window_x_units
        y_rel = enemy['y_loc'] - window_y_units
        tempArr[ct]['willAtk']=False

        # make a move if in non fog
        if((x_rel >= fog_x and x_rel <= fog_x2) and (y_rel >= fog_y and y_rel <= fog_y2)):
            x = enemy['x_loc']
            x1 = x -1
            x2 = x +1
            y = enemy['y_loc']
            y1 = y -1
            y2 = y +1

            # check if can attack
            if((char_x_rel == x_rel and (char_y_rel == y_rel+1 or char_y_rel == y_rel-1)) 
            or (char_y_rel == y_rel and (char_x_rel == x_rel+1 or char_x_rel == x_rel-1))):
                tempArr[ct]['willAtk']=True
            
            else:
                #check for move
                new_x, new_y = validMoves(x_rel, y_rel, enemyArr, mapArr, char_x_rel, char_y_rel)
        
            ct+=1
            
# calculates distance between 2 points
def dist(x1, x2, y1, y2):
    distX = math.pow(x1 - x2, 2)
    distY = math.pow(y1 - y2, 2)
    
    return math.sqrt(distX + distY)            



def validMoves(x, y, enemyArr, mapArr, char_x_rel, char_y_rel):
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
    minpair = {'x':x, 'y':y}
    for pair in check:
        distance = dist(pair['x'], char_x_rel, pair['y'], char_y_rel)

        if distance < minDist:
            minpair = pair
            minDist = distance
    
    return minpair['x'], minpair['y']



def checkForEnemy(x, y):
    # return false if enemy occupying space
    # return true if u can move there
    for enemy in enemyArr:
        en_x = enemy['x_loc']
        en_y = enemy['y_loc']
        if(en_x == x and en_y == y):
            print('Enemy in the way')
            return False
    
    return True
