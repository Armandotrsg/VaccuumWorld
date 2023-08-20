import argparse

def get_inputs():
    """
    Parses command line arguments and returns a dictionary of input parameters.
    Valid arguments are:
    - -x: Number of tiles in x.
    - -y: Number of tiles in y.
    - --max-time: Maximum number of minutes to run the simulation.
    - --max-steps: Maximum number of steps the agent can take.
    - --show-chart: Show the chart. Or alternatively, --no-show-chart to hide the chart.
    
    Returns:
        dict: A dictionary containing the input parameters for the simulation. The dictionary
        contains the following keys:
        - x (int): The number of tiles in the x direction.
        - y (int): The number of tiles in the y direction.
        - max_time (float): The maximum number of minutes to run the simulation.
        - max_steps (int): The maximum number of steps the agent can take.
    """

    parser = argparse.ArgumentParser(description="Run the vacuum world simulation.")
    parser.add_argument("--x", "-x", type=int, help="Number of tiles in x")
    parser.set_defaults(x=10)
    
    parser.add_argument("--y", "-y", type=int, help="Number of tiles in y")
    parser.set_defaults(y=10)
    
    parser.add_argument("--max-time", '-t', type=float, help="Maximum number of minutes to run the simulation")
    parser.set_defaults(max_time=None)
    
    parser.add_argument("--max-steps", type=int, help="Maximum number of steps the agent can take")
    parser.set_defaults(max_steps=None)
    
    parser.add_argument("--show-chart", action=argparse.BooleanOptionalAction, help="Show the chart")
    parser.set_defaults(show_chart=True)
    
    args = parser.parse_args()
    
    return {
        "x": args.x,
        "y": args.y,
        "max_time": args.max_time,
        "max_steps": args.max_steps,
        "show_chart": args.show_chart
    }