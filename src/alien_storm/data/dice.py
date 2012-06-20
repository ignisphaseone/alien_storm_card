import json
import random
import os.path

class die(object):
    def __init__(self, json_in):
        self.sides = []
        data = json.loads(json_in)
        print "--new die from: " + data.__str__()
        self.name = data["name"]
        self.color = data["color"]
        for side in data["sides"]:
            self.sides.append(side)
    def roll(self):
        self.faceup = self.sides[random.randint(0,self.sides.__len__()-1)]
        return self.faceup
    def reset(self):
        self.faceup = None
        
'''
clump of code to load all_dice with all the dice
'''
all_dice = {}
filename = os.path.relpath("dice.json")
print filename
data = open(filename, "r")
input = json.load(data)
for ele in input:
    all_dice[ele["name"]] = ele


def get_die(name):
    return die(json.dumps(all_dice[name]))

dice_list = []
dice_list.append(get_die("basic_attack"))
dice_list.append(get_die("basic_attack"))
dice_list.append(get_die("civilian"))

print get_die("basic_attack").sides
print get_die("civilian").sides

def roll_all(dice):
    for die in dice:
        die.roll()
    while True:
        for die in dice:
            print die.faceup
        icmd = raw_input("--reroll? ")
        if icmd == "done":
            break
        else:
            try:
                cmd = int(icmd)
                if cmd <= dice.__len__() and cmd > 0:
                    dice[cmd-1].roll()
                else:
                    print "--invalid value (out of bounds)..."
            except ValueError:
                print "--invalid value (not an int)..."
    results = {}
    faces = []
    for die in dice:
        if (die.faceup is not None):
            faces.append(die.faceup)
    for face in faces:
        if not results.has_key(face[0]):
            results[face[0]] = face[1]
        else:
            results[face[0]] += face[1]
    print results
    return results
        
roll_all(dice_list)