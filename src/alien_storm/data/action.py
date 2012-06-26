import json

class action(object):
    myid = 0
    def __init__(self, json_in):
        self.data = json.loads(json_in)
        '''
        actions have
        --timing (when you can use it)
        --cost (when you use it)
        --limit (how much can you use it)
        --scope (what you can use it on)
        --result (of the action)
        
        Because actions may support multiple timings, costs, and scopes, each of these returns a list.
        Because results 
        '''
        self.aid = action.myid
        action.myid += 1
        self.timing = self.data["timing"]
        self.cost = self.data["cost"]
        self.limit = self.data["limit"]
        self.scope = self.data["scope"]
        self.result = self.data["result"]
    def json(self):
        return json.dumps(self.data)

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
