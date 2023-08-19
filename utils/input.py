def get_inputs(argv: list):
    """Get the inputs from the command line in this order: x, y, max_time, max_steps.
    
    Args:
        argv (list): A list of strings representing the command line arguments.
    
    Returns:
        dict: A dictionary containing the parsed arguments.
    """
    x = 10
    y = 10
    max_time = None
    max_steps = None
    
    if len(argv) > 1:
        x = int(argv[1])
    if len(argv) > 2:
        y = int(argv[2])
    if len(argv) > 3:
        max_time = float(argv[3])
    if len(argv) > 4:
        max_steps = int(argv[4])
    return {
        "x": x,
        "y": y,
        "max_time": max_time,
        "max_steps": max_steps
    }