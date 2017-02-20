from Game import getChoice


class Action():
    name = "Action"

    def __init__(self,name):
        self.name = name
        
    def run(self,user):
        user.acts()
        print("You have finished  your action, your health is now:" + str(user.getHealth()))
        return True
    
    def display(self):
        return str(self.name)
    
    def showOptions(self,options):
        #print options
        idx = 0
        for opt in options:
            print(str(idx) + " : " + str(opt.display()))
            idx += 1
        
        
class Move(Action):
    
    def __init__(self):
        Action.__init__(self,"Move")
        
    def run(self, user):
        location = user.getLocation()
        neighbours = location.getNeighbours()
        self.showOptions(neighbours)
        loc = getChoice(len(neighbours))
        user.Move(neighbours[loc])
        return Action.run(self, user)
    
        
        
class Explore(Action):
    
    def __init__(self):
        Action.__init__(self,"Explore")
        
    def run(self, user):
        location = user.getLocation()
        location.displayItems()
        location.explore()
        return Action.run(self, user)
        
class Eat(Action):
    
    def __init__(self):
        Action.__init__(self,"Eat")

    def run(self, user):
        items = user.getItems()
        self.showOptions(items)
        item = items[getChoice(len(items))]
        user.eat(item)
        if item.destroyed:
            items.remove(item)
        return Action.run(self, user)
    
class PickUp(Action):
    
    def __init__(self):
        Action.__init__(self,"Pick Up")
        
    def run(self, user):
        location = user.getLocation()
        if location.explored:
            items = location.getItems()
            self.showOptions(items)
            item = getChoice(len(items))
            user.pickUp(items[item])
            location.removeItem(items[item])
        else:
            print("Explore first to locate any items")
        return Action.run(self, user)
        
def getDefaultActions():
    actions = []
    actions.append(Move())
    actions.append(Explore())
    actions.append(PickUp())
    actions.append(Eat())
    
    return actions