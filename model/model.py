from mesa import Model 
from agents.vaccuum import VaccuumAgent
from agents.dirt import Dirt
from agents.obstacle import Obstacle
from mesa.time import RandomActivation
from mesa.space import MultiGrid

class VaccuumWorld(Model):
    def __init__ (self, N: int, D: int, O: int, width: int, height: int):
        #self.running = True
        self.num_agents = N
        self.num_dirt = D
        self.num_obstacles = O
        
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
        
        for i in range(self.num_obstacles):
            unique_id = f"obstacle_{i}"
            o = Obstacle(unique_id, self)
            self.schedule.add(o)
            
            # Add the obstacle to a random grid cell
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(o, (x, y))

    def step(self):
        self.schedule.step()