from mesa import Agent
from mesa.model import Model

class Obstacle(Agent):
    """
    A class representing an obstacle in a grid world.
    """
    def __init__(self, unique_id: int, model: Model) -> None:
        """
        Constructor method that initializes the Obstacle object with a unique ID and a 
        reference to the model it belongs to.

        Args:
            unique_id (int): A unique identifier for the obstacle.
            model (Model): A reference to the model the obstacle belongs to.
        """
        super().__init__(unique_id, model)
        
    def step(self) -> None:
        """
        Method that represents a step in the simulation for the obstacle. Since obstacles do not move, 
        this method does nothing.
        """
        pass