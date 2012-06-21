'''
Created on Jun 18, 2012

@author: ApigeeCorporation
'''

import json
import gen
import random

def manual_roll_ship(ship):
    results = {}
    list = []
    for roll in ship["dice_data"]:
        myroll = roll[random.randint(0,roll.__len__()-1)]
        list.append(myroll)
    print list
    while True:
        icmd = raw_input("--reroll: ")
        if (icmd == "done"):
            break
        cmd = int(icmd) - 1
        if cmd > list.__len__() - 1 or cmd < 0:
            print "index out of bounds error, retry..."
        else:
            list[cmd] = ship["dice_data"][cmd][random.randint(0,roll.__len__()-1)]
            print list
    for roll in list:
        if not results.has_key(roll[0]):
            results[roll[0]] = roll[1]
        else:
            results[roll[0]] += roll[1]
    print results

def auto_roll_ship(ship):
    results = {}
    list = []
    for i in range(0,100):
        for roll in ship["dice_data"]:
            myroll = roll[random.randint(0,roll.__len__()-1)]
            list.append(myroll)
    for roll in list:
        if not results.has_key(roll[0]):
            results[roll[0]] = roll[1]
        else:
            results[roll[0]] += roll[1]
    print results
    
load = open('src/alien_storm/data/ships.json', 'r')
data4 = json.load(load)
load.close()
auto_roll_ship(data4[0])
auto_roll_ship(data4[1])

if __name__ == '__main__':
    pass