import json, random

class die(object):
    myid = 0
    def __init__(self, json_in):
        self.data = json.loads(json_in)
        self.did = die.myid
        die.myid += 1
        self.name = self.data["name"]
        self.color = self.data["color"]
        self.sides = self.data["sides"]
    def __str__(self):
        return self.name + "-" + str(self.did)
    def roll(self):
        self.faceup = self.sides[random.randint(0,self.sides.__len__()-1)]
    def pickup(self):
        self.faceup = None
    def json(self):
        return json.dumps(self.data)

all_dice = {}
def add_to_all_dice(idie):
    if all_dice.has_key(idie.name):
        print "--die already exists...updating with newest values...!"
    all_dice[idie.name] = idie

def load_die_by_name(dname):
    return all_dice[dname]