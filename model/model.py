"""
Nombre del archivo: model.py
Autor: Armando Terrazas -- A01640924
       Juan Daniel Muñoz -- A01641792
       Jorge Wolburg -- A01640826
       Diego Curiel -- A01640372
Fecha de creación: 20/08/2023
Descripción: Este archivo contiene la clase VacuumWorld, la cual representa el modelo del mundo de la aspiradora.
"""

from mesa import Model 
from agents.vacuum import VacuumAgent
from agents.dirt import Dirt
from agents.obstacle import Obstacle
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
from time import time

class VacuumWorld(Model):
    """
    A class representing a vacuum world model that contains agents, dirt, and obstacles.
    """
    def __init__ (self, N: int, D: int, O: int, width: int, height: int, max_time: int = None, max_steps: int = None):
        """
        Constructor method that initializes the VacuumWorld object with the number of agents, dirt, 
        obstacles, and the width and height of the grid and places them randomly in the grid.

        Args:
            N (int): The number of vacuum agents in the model.
            D (int): The number of dirt cells in the model.
            O (int): The number of obstacle cells in the model.
            width (int): The width of the grid.
            height (int): The height of the grid.
            max_time (int): The maximum number of minutes to run the simulation. Defaults to None.
            max_steps (int, optional): The maximum number of steps to run the simulation. Defaults to None.
        """
        self.running = True
        self.num_agents = N
        self.num_dirt = D
        self.num_obstacles = O
        self.max_time = max_time
        self.start_time = time()
        self.max_steps = max_steps
        
        self.grid = MultiGrid(width, height, False)
        self.schedule = RandomActivation(self)
        self.dirt_cleaned = 0
        
        self.datacollector = DataCollector(
            {
                "cleaned": lambda m: m.dirt_cleaned
            }
        )
                
        for i in range(self.num_dirt):
            unique_id = f"dirt_{i}"
            d = Dirt(unique_id, self)
            self.schedule.add(d)
            
            # Add the dirt to a random grid cell
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(d, (x, y))
        
        for i in range(self.num_agents):
            unique_id = f"vaccuum_{i}"
            a = VacuumAgent(unique_id, self)
            self.schedule.add(a)
            
            # Add the agent to a random grid cell where there is no other agent
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))
        
        for i in range(self.num_obstacles):
            unique_id = f"obstacle_{i}"
            o = Obstacle(unique_id, self)
            self.schedule.add(o)
            
            # Add the obstacle to a random grid cell
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(o, (x, y))
            if not self.grid.is_cell_empty((x, y)):
                self.grid.move_to_empty(o)
                
    def step(self):
        """
        Method that represents a step in the simulation for the vacuum world. It calls the step() method 
        for each agent in the model and stops the simulation if all dirt has been cleaned or if the 
        maximum time has been reached.
        """
        self.schedule.step()
        self.datacollector.collect(self)
        if self.dirt_cleaned == self.num_dirt:
            # Stop the simulation if all dirt has been cleaned
            self.running = False
            print(f"All dirt cleaned in {self.schedule.steps} steps.")
        elif self.max_time is not None and time() - self.start_time > self.max_time * 60:
            # Stop the simulation if the maximum time has been reached
            self.running = False
            print(f"Maximum time of {self.max_time} minutes reached.")
        elif self.max_steps is not None and self.schedule.steps >= self.max_steps:
            # Stop the simulation if the maximum number of steps has been reached
            self.running = False
            print(f"Maximum number of steps reached: {self.max_steps}.")
        
            