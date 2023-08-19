from mesa.visualization.modules import CanvasGrid 
from mesa.visualization.ModularVisualization import ModularServer

from model.model import VacuumWorld
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.UserParam import Slider
from mesa import Agent

def agent_portrayal(agent: Agent):
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

def run():
    x = 5
    y = 5

    number_of_agents = Slider("Number of agents", 1, 1, x)
    number_of_dirt = Slider("Number of dirt", 2, 1, x*y)
    number_of_obstacles = Slider("Number of obstacles", 3, 1, 30)

    model_params = {
        "N": number_of_agents,
        "D": number_of_dirt,
        "O": number_of_obstacles,
        "width": x,
        "height": y
    }

    grid = CanvasGrid(agent_portrayal, x, y, 500, 500)

    server = ModularServer(VacuumWorld, [grid], "Vaccuum World", model_params)
    serverPort = 8521
    server.launch(port=serverPort)