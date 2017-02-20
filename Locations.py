import Actions
import Items


class Location():
    def __init__(self, name):
        self.name = name
        self.actions = Actions.getDefaultActions()
        self.items = []
        self.monsters = []
        self.neighbours = []
        self.explored = False
        
        
    def display(self):
        return self.name
    
    def displayDesc(self):
        return
        
    def displayItems(self):
        if self.items:
            print("A number of items are here")
            for item in self.items:
                print(item.display())
            return
        print("No items are visible here")
        
    def displayMonsters(self):
        if self.monsters:
            print("A number of monsters are here")
            for enemy in self.monsters:
                print(enemy.display())
            return
        print("No monsters are visible here")
        return
        
    def displayInfo(self):
        print("You are now at the " + self.name)
        self.displayDesc()
        #self.displayItems()
        self.displayMonsters()
        
    def explore(self):
        self.explored = True    
        
    def getActions(self):
        return self.actions
        
    def setNeighbour(self,location):
        self.neighbours.append(location) #CHECK for duplicates
        
    def getNeighbours(self):
        return self.neighbours
    
    def getItems(self):
        return self.items
    
    def removeItem(self,item):
        self.items.remove(item)
        
    
    
START = Location("Start")
BEACH = Location("Beach")
JUNGLE = Location("Jungle")

def buildMap():
    START.setNeighbour(BEACH)
    BEACH.setNeighbour(JUNGLE)
    BEACH.setNeighbour(START)
    JUNGLE.setNeighbour(BEACH)
    setItems()

def getStartLocation():
    return START
    
def setItems():
    for item in Items.ITEMS:
        JUNGLE.items.append(item)
    