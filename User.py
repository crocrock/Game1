

class User():
    name = "User"
    
    def __init__(self,name):
        self.name = name
        self.health = 10
        self.location = None
        self.items = []
        
    def isAlive(self):
        if self.health > 0:
            return True
        return False
    
    def getHealth(self):
        return self.health
    
    def acts(self):
        self.health -= 1
        
    def eat(self,item):
        health = self.health
        if item.isFood():
            health = health+10
            if  health > 100:
                health = 100
            self.health = health
            item.destroy()
              
    def Move(self,location):
        print("You move to the new location")
        location.displayInfo()
        self.location = location
        
    def pickUp(self,item):
        self.items.append(item)
        
    def getItems(self):
        return self.items
        
    def getLocation(self):
        return self.location
        