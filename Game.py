from Items import ITEMS
import Locations
from User import User


class Game():
    items=ITEMS

    
    def run(self):
        print "Please enter your name?"
        name ="Simon"
        self.user = User(name)
        Locations.buildMap() # Create the Map Data
        start = Locations.getStartLocation()
        self.user.Move(start)
        print "Running Game"
        print "Location; " 
        print self.user.getLocation().name
        print "User: "
        print self.user.name
        while self.user.isAlive():
            displayStatus(self.user)
            actions = self.user.getLocation().getActions()
            action = self.getAction(actions)
            self.processAction(self.user,action,actions)
            
            
        
    def getAction(self,actions):
        #print actions
        idx = 0
        for action in actions:
            
            print (str(idx) + ":" + action.display())
            idx += 1
        choice = getChoice(idx)
        act = actions[choice]
        return act
    
    def processAction(self,user,action,actions):
        print("doing action: "+action.display())
        action.run(user)
        
        
def getChoice(max):
    return 0

def displayStatus(user):
    print("User:"+user.name)
    print("Location:"+user.getLocation().name)
    print("Health: "+str(user.health))
    

if __name__ == "__main__":
    game=Game()
    game.run()