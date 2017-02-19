

class User():
    name = "User"
    
    def __init__(self,name):
        self.name = name
        self.health = 10
        self.location = None
        
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
            item.destroy()
              
    def Move(self,location):
        self.location = location
        
    def getLocation(self):
        return self.location
        