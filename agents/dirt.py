from mesa import Agent
from mesa.model import Model

class Dirt(Agent):
    """
    A class representing dirt in a grid world.
    """
    def __init__(self, unique_id: int, model: Model) -> None:
        """
        Constructor method that initializes the Dirt object with a unique ID and a 
        reference to the model it belongs to.

        Args:
            unique_id (int): A unique identifier for the dirt.
            model (Model): A reference to the model the dirt belongs to.
        """
        super().__init__(unique_id, model)
        
    def step(self) -> None:
        """
        Method that represents a step in the simulation for the dirt. Since dirt does not move, 
        this method does nothing.
        """
        pass
    