"""
Nombre del archivo: obstacle.py
Autor: Armando Terrazas -- A01640924
       Juan Daniel Muñoz -- A01641792
       Jorge Wolburg -- A01640826
       Diego Curiel -- A01640372
Fecha de creación: 20/08/2023
Descripción: Este archivo contiene la clase Obstacle, la cual representa los obstáculos en el modelo.
"""
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