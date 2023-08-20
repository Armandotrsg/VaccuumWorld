from mesa import Agent
from mesa.model import Model
from utils.color import get_color

class VacuumAgent(Agent):
    """
    A class representing a vacuum agent that cleans dirt from a grid world.
    """
    def __init__(self, unique_id: int, model: Model) -> None:
        """
        Constructor method that initializes the VacuumAgent object with a unique ID and a 
        reference to the model it belongs to.

        Args:
            unique_id (int): A unique identifier for the agent.
            model (Model): A reference to the model the agent belongs to.
        """
        super().__init__(unique_id, model)
        self.steps = 0  # Number of steps taken
        self.cleaned = 0  # Number of tiles cleaned
        
        self.adjacent_steps = []  # Possible steps for DFS in this form: [(position, num_steps_to_return), ...)]
        self.visited = set()  # Visited tiles
        self.back_track = [] # Backtrack tiles 
        
        self.is_returning = False  # Is returning to previous cell in adjacent_steps       
        
        self.color = get_color(int(unique_id[8:]))
        
    def clean(self) -> None:
        """
        Method that checks if the current cell contains dirt and removes it if it does. It also 
        updates the number of tiles cleaned and the total dirt count in the model.
        """
        # Get the contents of the cell
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        # If there is dirt, clean it
        for i in cellmates:
            if type(i).__name__ == "Dirt":
                self.model.grid.remove_agent(i)
                self.cleaned += 1
                self.model.dirt_cleaned += 1

    def step(self) -> None:
        """
        Method that calls the clean() method and then attempts to move the agent to a neighboring 
        cell using the move() method.
        """
        self.clean()
        # try:
        self.move()
        self.steps += 1
        # except:
        #     pass
        
    def append_to_adjacent(self, position: list) -> None:
        """
        Method that appends a new position to the adjacent_steps list.

        Args:
            position (list of tuples): A list of tuples representing the positions to append to the adjacent_steps list.
        """

        # If the last adjacent step has the same position as the new position, increment the counter
        if len(self.adjacent_steps) > 0:
            self.adjacent_steps[-1] = (self.adjacent_steps[-1][0], self.adjacent_steps[-1][1] + 1)
        
        for pos in position:
            self.adjacent_steps.append((pos, 1))
        
        
    def get_possible_steps(self, position: tuple) -> list:
        """
        Method that returns a list of possible steps from the current position.

        Args:
            position (tuple): A tuple representing the current position.

        Returns:
            list: A list of possible steps from the current position.
        """
        possible_steps = self.model.grid.get_neighborhood(position, moore=False, include_center=False)
        not_obstacle_steps = []
        will_append_to_adjacent = []
        for step in possible_steps:
            cellmates = self.model.grid.get_cell_list_contents([step])
            not_obstacle = True
            for cellmate in cellmates:
                # Check if the cellmate is an obstacle or another agent then set not_obstacle to False
                if type(cellmate).__name__ == "Obstacle" or type(cellmate).__name__ == "VacuumAgent":
                    not_obstacle = False
                    
            # Add the step to adjacent_steps if it has not been visited before and is not an obstacle
            if step not in self.visited and not_obstacle and not self.is_returning:
                will_append_to_adjacent.append(step)
                not_obstacle_steps.append(step)
            elif not_obstacle and self.is_returning:
                not_obstacle_steps.append(step)
                
        if len(will_append_to_adjacent) > 0:
            self.append_to_adjacent(will_append_to_adjacent)
            
        return not_obstacle_steps
    
    def return_to_previous_cell(self) -> None:
        """
        Method that moves the agent to the previous cell in the adjacent_steps list if the agent is returning.
        """
        try:
            target_position = self.adjacent_steps[-1][0] # Target position is the last adjacent step
            target_position_counter = self.adjacent_steps[-1][1] # Target position counter is the number of steps to return to the target position
        except:
            print("Error: No adjacent steps")
            self.is_returning = False
            return
        possible_steps = self.get_possible_steps(self.pos)
        
        if target_position_counter >= 1:
            # If the target position counter is greater than 1, move to the last back_track position
            new_position = self.back_track[-1]
            if new_position in possible_steps:
                self.model.grid.move_agent(self, new_position)
                self.back_track.pop()
                self.adjacent_steps[-1] = (self.adjacent_steps[-1][0], self.adjacent_steps[-1][1] - 1)
        else:
            # If the target position counter is 1, move to the target position
            if target_position in possible_steps:
                self.back_track.append(self.pos)
                self.model.grid.move_agent(self, target_position)
                self.adjacent_steps.pop()
                self.is_returning = False
                self.visited.add(target_position)
    
    def move_to_next_cell(self) -> None:
        """
        Method that moves the agent to the next cell in the adjacent_steps list if there are possible steps, 
        giving priority to cells with dirt.
        """
        possible_steps = self.get_possible_steps(self.pos)
        if len(possible_steps) == 0:
            # If there are no possible steps, set is_returning to True
            self.is_returning = True
            self.return_to_previous_cell()
        else:
            self.visited.add(self.pos) # Add the current position to visited
            self.back_track.append(self.pos) # Add the current position to back_track
            
            # Check if there are any adjacent steps with dirt with a 1 distance and are in the possible steps
            i = -1
            while abs(i) <= len(self.adjacent_steps) and self.adjacent_steps[i][1] == 1:
                # Get cellmates of the adjacent step
                cellmates = self.model.grid.get_cell_list_contents([self.adjacent_steps[i][0]])
                if self.adjacent_steps[i][0] in possible_steps and len(cellmates) > 0 and type(cellmates[0]).__name__ == "Dirt":
                    self.model.grid.move_agent(self, self.adjacent_steps[i][0])
                    self.adjacent_steps.remove(self.adjacent_steps[i])
                    return
                i -= 1
            
            new_position = self.adjacent_steps.pop()
            self.model.grid.move_agent(self, new_position[0])

    def move(self) -> None:
        """
        Method that calls the move_to_next_cell() or return_to_previous_cell() method depending on whether the agent is returning.
        """
        if not self.is_returning: # If the agent is not returning, add the current position to visited and get possible steps
            self.move_to_next_cell()
        else:
            self.return_to_previous_cell()