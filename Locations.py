import Actions


class Location():
    def __init__(self, name):
        self.name = name
        self.actions = Actions.getDefaultActions()
        self.items = []
        self.monsters = []
        self.neighbours = []
        
        
    def display(self):
        return self.name

    def getActions(self):
        return self.actions
        
    def setNeighbour(self,location):
        self.neighbours.append(location) #CHECK for duplicates
        
    def getNeighbours(self):
        return self.neighbours
    
    
START = Location("Start")
BEACH = Location("Beach")
JUNGLE = Location("Jungle")

def buildMap():
    START.setNeighbour(BEACH)
    BEACH.setNeighbour(JUNGLE)
    BEACH.setNeighbour(START)
    JUNGLE.setNeighbour(BEACH)

def getStartLocation():
    return START
    
    