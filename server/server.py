from mesa.visualization.modules import CanvasGrid 
from mesa.visualization.ModularVisualization import ModularServer

from model.model import VacuumWorld
from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization.UserParam import Slider
from mesa import Agent

def agent_portrayal(agent: Agent):
    """
    Function that returns a dictionary of attributes that define how an agent is displayed in the visualization.

    Args:
        agent (Agent): The agent to be displayed.

    Returns:
        dict: A dictionary of attributes that define how the agent is displayed in the visualization.
    """
    #Check if the agent is an instance of class VaccuumAgent
    if type(agent).__name__ == "VacuumAgent":
        #Get random color for each agent
        portrayal = {"Shape": "circle",
                     "Filled": "true",
                     "Layer": 1,
                     "Color": agent.color,
                     "r": 0.5}
    elif type(agent).__name__ == "Dirt":
        portrayal = {"Shape": "rect",
                     "Filled": "true",
                     "Layer": 0,
                     "Color": "brown",
                     "w": 1,
                     "h": 1}
    
    else: #Type obstacle
        portrayal = {"Shape": "rect",
                        "Filled": "true",
                        "Layer": 0,
                        "Color": "black",
                        "w": 1,
                        "h": 1}
        
    return portrayal

def run_simulation(x: int = 10, y:int = 10, max_time: float = 1.5, max_steps: int = None) -> None:
    """
    Function that runs the simulation with the given parameters.

    Args:
        x (int, optional): Number of tiles in x. Defaults to 10.
        y (int, optional): Number of tiles in y. Defaults to 10.
        max_time (float, optional): Maximum number of minutes to run the simulation. Defaults to 1.5.
        max_steps (int, optional): Maximum number of steps the agent can take. Defaults to None.
    """
    number_of_agents = Slider("Number of agents", 1, 1, x)
    number_of_dirt = Slider("Number of dirt", 2, 1, x*y)
    number_of_obstacles = Slider("Number of obstacles", 3, 1, 30)

    model_params = {
        "N": number_of_agents,
        "D": number_of_dirt,
        "O": number_of_obstacles,
        "width": x,
        "height": y,
        "max_time": max_time,
        "max_steps": max_steps
    }

    grid = CanvasGrid(agent_portrayal, x, y, 500, 500)
    chart = ChartModule(
        [
            {"Label": "cleaned", "Color": "blue"}
        ]        
    )

    server = ModularServer(VacuumWorld, [grid, chart], "Vaccuum World", model_params)
    serverPort = 8521
    server.launch(port=serverPort)