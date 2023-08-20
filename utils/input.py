import argparse

def get_inputs():
    """
    Parses command line arguments and returns a dictionary of input parameters.
    Valid arguments are:
    - -x: Number of tiles in x.
    - -y: Number of tiles in y.
    - -t: Maximum number of minutes to run the simulation.
    - -s: Maximum number of steps the agent can take.
    
    Returns:
        dict: A dictionary containing the input parameters for the simulation. The dictionary
        contains the following keys:
        - x (int): The number of tiles in the x direction.
        - y (int): The number of tiles in the y direction.
        - max_time (float): The maximum number of minutes to run the simulation.
        - max_steps (int): The maximum number of steps the agent can take.
    """
    x = 10
    y = 10
    max_time = None
    max_steps = None
    
    parser = argparse.ArgumentParser(description="Run the vacuum world simulation.")
    parser.add_argument("--x", "-x", type=int, help="Number of tiles in x")
    parser.add_argument("--y", "-y", type=int, help="Number of tiles in y")
    parser.add_argument("--max_time", "-t", type=float, help="Maximum number of minutes to run the simulation")
    parser.add_argument("--max_steps", "-s", type=int, help="Maximum number of steps the agent can take")
    
    args = parser.parse_args()
    
    if args.x:
        x = args.x
    if args.y:
        y = args.y
    if args.max_time:
        max_time = args.max_time
    if args.max_steps:
        max_steps = args.max_steps
    
    return {
        "x": x,
        "y": y,
        "max_time": max_time,
        "max_steps": max_steps
    }