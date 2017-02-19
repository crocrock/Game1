from Items import ITEMS
import Locations
from Locations import LOCATIONS

class Game():
    items=ITEMS
    locations=LOCATIONS
    
    def run(self):
        self.location = Locations.getStartLocation()
        


if __name__ == "__main__":
    game=Game()
    game.run()