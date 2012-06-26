import json
import alien_storm.data.dice
from alien_storm.data.dice import load_die_by_name, die
from alien_storm.data.action import action

class ship(object):
    myid = 0
    def __init__(self, json_in):
        self.data = json.loads(json_in)
        self.sid = ship.myid
        ship.myid += 1
        
        self.name = self.data["name"]
        self.desc = self.data["desc"]
        self.dice = []
        for d in self.data["dice"]:
            self.dice.append(die(d))
        self.actions = []
        for a in self.data["actions"]:
            self.actions.append(action(a))

dsample1 = {
    "name":"basic_attack",
    "color":"red",
    "sides":[
        {"attack":1},
        {"attack":1},
        {"attack":1},
        {"attack":2},
        {"attack":2},
        {"miss":1},
        ]
    }
dsample2 = {
    "name":"basic_attack",
    "color":"red",
    "sides":[
        {"attack":1},
        {"attack":1},
        {"attack":1},
        {"attack":2},
        {"attack":2},
        {"miss":1},
        ]
    }
asample = {
    "timing":[
        "explore",
        ],
    "cost":[
        {"attack_dice":1,"civilian_dice":1,},
        {"frigate":1},
        ],
    "limit":{
        "phase":1,
        "turn":2,
        },
    "scope":[
        "any",
        ],
    "result":[
        {"attack":1,"shield":1,},
        {"attack":6},
        ],
    }
dsample_one = die(json.dumps(dsample1))
dsample_two = die(json.dumps(dsample2))
asample_one = action(json.dumps(asample))

ssample = {
    "name":"frigate",
    "desc":"A basic attack frigate.",
    "dice":[
        dsample_one.json(),
        dsample_two.json(),
        ],
    "actions":[
        asample_one.json(),
        ]
    }

myship = ship(json.dumps(ssample))
print myship.name
print myship.sid
print myship.desc
print myship.dice
print myship.actions