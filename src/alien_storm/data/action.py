'''
Created on Jun 25, 2012

@author: ApigeeCorporation
'''
import json

class action(object):
    def __init__(self, json_in):
        data = json.load(json_in)
        '''
        actions have
        --timing (when you can use it)
        --cost (when you use it)
        --limit (how much can you use it)
        --result (of the action)
        '''
        self.timing = [
            "pre_repair",
            "repair",
            "pre_event",
            "event",
            "end",
            ]
        # Pay all costs of any single list item. Each dict is the full cost.
        self.cost = [
            {"attack_dice":1, "civilian_dice":1},
            {"frigate":1}
            ]
        # Limits. Number per phase, and number per turn. Also, maybe per game abilities? Etc.
        self.limit = {
            "phase":1,
            "turn":2
            }
        self.result = ""