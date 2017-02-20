import readline 
import Locations
from User import User


class Game():

    def run(self):
        name = raw_input('Please enter your name? ')
        #name ="Simon"
        self.user = User(name)
        Locations.buildMap() # Create the Map Data
        start = Locations.getStartLocation()
        self.user.Move(start)
        print "Running Game"
        #print "Location; " 
        #print self.user.getLocation().name
        #print "User: "
        #rint self.user.name
        #print "Items: "
        #print self.user.getItems()
        while self.user.isAlive():
            displayStatus(self.user)
            actions = self.user.getLocation().getActions()
            action = self.getAction(actions)
            self.processAction(self.user,action,actions)
            
            
        
    def getAction(self,actions):
        #print actions
        idx = 0
        print("ACTIONS")
        print("________")
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
    ch = raw_input("Please enter your choice: ")
    choice = int(ch)
    if choice < 0 or choice > max-1:
        print("Invalid choice")
        choice = getChoice(max)
    return choice

def displayStatus(user):
    print("STATUS")
    print("________")
    print("User:"+str(user.name))
    print("items:"+str(user.getItems()))
    print("Location:"+user.getLocation().name)
    print("Health: "+str(user.health))
    print
    
    

if __name__ == "__main__":
    game=Game()
    game.run()