from mesa import Agent

class VaccuumAgent(Agent):
    """
    A class representing a vaccuum agent that cleans dirt from a grid world.
    """
    def __init__(self, unique_id, model):
        """
        Constructor method that initializes the VaccuumAgent object with a unique ID and a reference to the model it belongs to.

        Args:
            unique_id (int): A unique identifier for the agent.
            model (object): A reference to the model the agent belongs to.
        """
        super().__init__(unique_id, model)
        self.steps = 0  # Number of steps taken
        self.cleaned = 0  # Number of tiles cleaned
        self.adjacent_steps = []  # Possible steps for DFS
        self.visited = []  # Visited tiles
        self.is_returning = False  # Is returning to previous cell in adjacent_steps

    def clean(self) -> None:
        """
        Method that checks if the current cell contains dirt and removes it if it does. It also updates the number of tiles cleaned and the total dirt count in the model.
        """
        # Get the contents of the cell
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        # If there is dirt, clean it
        for i in cellmates:
            if type(i).__name__ == "Dirt":
                self.model.grid.remove_agent(i)
                self.cleaned += 1
                self.model.dirt_count -= 1

    def step(self) -> None:
        """
        Method that calls the clean() method and then attempts to move the agent to a neighboring cell using the move() method.
        """
        self.clean()
        try:
            self.move()
        except:
            pass
        
    def get_possible_steps(self, position) -> list:
        """
        Method that takes a position as input and returns a list of neighboring cells that are not obstacles or other agents. It also updates the adjacent_steps list with any new adjacent steps that have not been visited before.

        Args:
            position (tuple): A tuple representing the current position of the agent.

        Returns:
            list: A list of neighboring cells that are not obstacles or other agents.
        """
        possible_steps = self.model.grid.get_neighborhood(position, moore=False, include_center=False)
        not_obstacle_steps = []
        for step in possible_steps:
            cellmates = self.model.grid.get_cell_list_contents([step])
            not_obstacle = True
            for cellmate in cellmates:
                # Check if the cellmate is an obstacle or another agent then set not_obstacle to False
                if type(cellmate).__name__ == "Obstacle" or type(cellmate).__name__ == "VaccuumAgent":
                    not_obstacle = False
                    
            # Add the step to adjacent_steps if it has not been visited before and is not an obstacle
            if step not in self.visited and not_obstacle:
                self.adjacent_steps.append(step)
            
            if not_obstacle:
                # If the step is not an obstacle or another agent, add it to not_obstacle_steps
                not_obstacle_steps.append(step)
        return not_obstacle_steps

    def move(self) -> None:
        """
        Method that attempts to move the agent to a neighboring cell. If the agent is not currently returning to a previous cell, 
        it first updates the adjacent_steps list with any new adjacent steps that have not been visited before. 
        It then attempts to move the agent to the last adjacent step in the list. If the agent is returning to a previous cell, 
        it attempts to move the agent to the last visited cell or the last adjacent step if the visited cell is not reachable.
        """
        if not self.is_returning:
            # If the agent is not returning, add the current position to visited and get possible steps
            self.visited.append(self.pos)
            possible_steps = self.get_possible_steps(self.pos)
            
            if len(possible_steps) == 0:
                # If there are no possible steps, set is_returning to True
                self.is_returning = True
            else:
                # If there are possible steps, move to the last adjacent step in adjacent_steps
                new_position = self.adjacent_steps.pop()
                self.model.grid.move_agent(self, new_position)
                
        else:
            # If the agent is returning, get the last visited cell and the last adjacent step which is the target position
            new_position = self.visited[-1] # New position is the last visited cell
            target_position = self.adjacent_steps[-1] # Target position is the last adjacent step

            possible_steps = self.get_possible_steps(self.pos)

            if target_position in possible_steps:
                # If the target position is reachable, move to it and remove it from adjacent_steps
                self.model.grid.move_agent(self, target_position)
                self.adjacent_steps.pop()
                self.is_returning = False
            elif new_position in possible_steps:
                # If the last visited cell is reachable, move to it and remove it from visited
                self.visited.pop()
                self.model.grid.move_agent(self, new_position)