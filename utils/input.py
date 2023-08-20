import argparse

def get_inputs():
    """
    Parses command line arguments and returns a dictionary of input parameters.
    Valid arguments are:
    - -x: Number of tiles in x.
    - -y: Number of tiles in y.
    - --max-time: Maximum number of minutes to run the simulation.
    - --max-steps: Maximum number of steps the agent can take. Defaults to x * y + 10.
    - --show-chart: Show the chart. Or alternatively, --no-show-chart to hide the chart.
    - --no-max-steps: Don't set a maximum number of steps the agent can take.
    
    Returns:
        dict: A dictionary containing the input parameters for the simulation.
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
    
    parser.add_argument("--no-max-steps", action="store_true", help="Don't set a maximum number of steps the agent can take")
    parser.set_defaults(no_max_steps=False)
    
    parser.add_argument("--show-chart", action=argparse.BooleanOptionalAction, help="Show the chart")
    parser.set_defaults(show_chart=True)
    
    args = parser.parse_args()
    
    if args.no_max_steps:
        args.max_steps = None
    else:
        args.max_steps = args.x*args.y + 10 if args.max_steps is None else args.max_steps
    
    return {
        "x": args.x,
        "y": args.y,
        "max_time": args.max_time,
        "max_steps": args.max_steps,
        "show_chart": args.show_chart
    }