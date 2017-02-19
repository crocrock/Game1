# Items for use in the Game

class Item():
    def __init__(self):
        self.name="Item"
        self.combat = 0
        self.weight = 1
        self.uses = 1 #single use by default
        self.broken = False
        
    def getName(self):
        return self.name()
    def getWeight(self):
        return self.weight
    def getCombat(self):
        return self.combat
    def getUses(self):
        return self.uses
    
    def useItem(self):
        if self.broken:
            return False
        self.uses = self.uses - 1
        if self.uses == 0:
            self.breaks()
        return True
    
    def breaks(self):
        self.broken = True
        
class Sword(Item):
    def __init__(self):
        Item.__init__(self)
        self.name = "Sword"
        self.combat = 2
        self.weight = 5
        
class Axe(Item):
    def __init__(self):
        Item.__init__(self)
        self.name = "Axe"
        self.combat = 1
        self.weight = 4  
        
global ITEMS

ITEMS = {
    "Axe" :  Axe(),
    "Sword" :  Sword(),
    }      