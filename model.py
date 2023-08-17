from mesa import Model 
from vaccuum import VaccuumAgent
from dirt import Dirt
from mesa.time import RandomActivation
from mesa.space import MultiGrid

class VaccuumWorld(Model):
    def __init__ (self, N, D, width, height):
        #self.running = True
        self.num_agents = N
        self.num_dirt = D
        self.grid = MultiGrid(width, height, False)
        self.schedule = RandomActivation(self)
        self.dirt_count = 0
        
        for i in range(self.num_agents):
            unique_id = f"vaccuum_{i}"
            a = VaccuumAgent(unique_id, self)
            self.schedule.add(a)
            
            # Add the agent to a random grid cell where there is no other agent
            try:
                start_cell = self.grid.find_empty()
                self.grid.place_agent(a, start_cell)
            except:
                x = self.random.randrange(self.grid.width)
                y = self.random.randrange(self.grid.height)
                self.grid.place_agent(a, (x, y))
                
        for i in range(self.num_dirt):
            unique_id = f"dirt_{i}"
            d = Dirt(unique_id, self)
            self.schedule.add(d)
            self.dirt_count += 1
            
            # Add the dirt to a random grid cell
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(d, (x, y))
                
            
            
        
    def step(self):
        self.schedule.step()