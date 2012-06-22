'''
Created on Jun 18, 2012

@author: ApigeeCorporation
'''
import json

dice = []
die = {
    "name": "basic_attack",
    "color": "red",
    "sides": [
        ("attack",1),
        ("attack",1),
        ("attack",1),
        ("attack",1),
        ("attack",2),
        ("miss", 1)
        ]
}
dice.append(die);

die = {
    "name": "advanced_attack",
    "color": "dark_red",
    "sides": [
        ("attack",1),
        ("attack",1),
        ("attack",2),
        ("attack",2),
        ("attack",2),
        ("attack",3),
        ]
}
dice.append(die);

die = {
    "name": "drone_attack",
    "color": "yellow",
    "sides": [
        ("attack",1),
        ("attack",1),
        ("shield",1),
        ("attack",2),
        ("drone", 1),
        ("drone", 2)
        ]
}
dice.append(die);

die = {
    "name": "missile_attack",
    "color": "grey",
    "sides": [
        ("attack",1),
        ("attack",2),
        ("attack",3),
        ("missile",1),
        ("missile",2),
        ("lockon", 1)
        ]
}
dice.append(die);

die = {
    "name": "artillery_attack",
    "color": "white",
    "sides": [
        ("miss",1),
        ("miss",1),
        ("attack",2),
        ("attack",2),
        ("attack",3),
        ("siege", 1)
        ]
}
dice.append(die);

die = {
    "name": "civilian_special",
    "color": "silver",
    "sides": [
        ("civilian",1),
        ("civilian",1),
        ("civilian",2),
        ("civilian",2),
        ("civilian",3),
        ("civilian",4)
        ]
}
dice.append(die);
die = {
    "name": "fleet_special",
    "color": "gold",
    "sides": [
        ("fleet",1),
        ("fleet",1),
        ("fleet",2),
        ("fleet",2),
        ("fleet",3),
        ("fleet",4)
        ]
}
dice.append(die);
die = {
    "name": "civilian",
    "color": "black",
    "sides": [
        ("shield",1),
        ("shield",1),
        ("shield",1),
        ("repair",1),
        ("scan",1),
        ("break", 1)
        ]
}
dice.append(die)

die = {
    "name": "scanner",
    "color": "green",
    "sides": [
        ("shield",1),
        ("shield",1),
        ("scan",1),
        ("scan",1),
        ("scan",1),
        ("lockon", 1)
        ]
}
dice.append(die);
die = {
    "name": "support",
    "color": "blue",
    "sides": [
        ("repair",1),
        ("repair",1),
        ("shield",2),
        ("scan",1),
        ("repair",2),
        ("shield", 1)
        ]
}
dice.append(die);

die = {
    "name": "alien",
    "color": "purple",
    "sides": [
        ("miss",1),
        ("damage",1),
        ("damage",1),
        ("damage",2),
        ("damage",1),
        ("infect", 1)
        ]
}
dice.append(die);

die = {
    "name": "alien_leader",
    "color": "pink",
    "sides": [
        ("damage",1),
        ("damage",2),
        ("damage",2),
        ("damage",2),
        ("infect",1),
        ("infect",2)
        ]
}
dice.append(die);
print dice;

data = open('dice.json', 'w+')
json.dump(dice, data)
data.close()

load = open('dice.json', 'r')
data2 = json.load(load)
load.close()
print data2
for d in data2:
    print d['name']

ships = []
ship = {
    "name": "frigate",
    "dice": [
        "basic_attack",
        "basic_attack"],
    "dice_data":[]
    }

for d1 in ship["dice"]:
    for d2 in data2:
        if d1 == d2["name"]:
            ship["dice_data"].append(d2["sides"])
ships.append(ship)

ship = {
    "name": "civilian",
    "dice": [
        "civilian"
        ],
    "dice_data":[]
    }

for d1 in ship["dice"]:
    for d2 in data2:
        if d1 == d2["name"]:
            ship["dice_data"].append(d2["sides"])
ships.append(ship)

print ships
data3 = open('ships.json', 'w+')
json.dump(ships, data3)
data3.close()