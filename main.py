from server.server import run_simulation
from sys import argv
from utils.input import get_inputs

def main():
    # Get the inputs from the command line in this order: x, y, max_time, max_steps.
    inputs = get_inputs(argv)
    
    run_simulation(
        x = inputs["x"],
        y = inputs["y"],
        max_time = inputs["max_time"],
        max_steps = inputs["max_steps"]
    )
    
if __name__ == "__main__":
    main()
    