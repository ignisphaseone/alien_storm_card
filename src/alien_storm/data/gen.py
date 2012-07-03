import json, dice
from dice import die, add_to_all_dice

json_die = {
    "name":"basic-attack",
    "color":"red",
    "sides":[
        {"attack":1},
        {"attack":1},
        {"attack":1},
        {"attack":2},
        {"attack":2},
        {"miss":1},
        ],
    }
new_die = die(json.dumps(json_die))
add_to_all_dice(new_die)