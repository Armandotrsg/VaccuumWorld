"""
Nombre del archivo: main.py
Autor: Armando Terrazas -- A01640924
       Juan Daniel Muñoz -- A01641792
       Jorge Wolburg -- A01640826
       Diego Curiel -- A01640372
Fecha de creación: 20/08/2023
Descripción: Este archivo contiene la función main, la cual se encarga de correr la simulación.
"""
from server.server import run_simulation
from utils.input import get_inputs

def main():
    # Get the inputs from the command line in this order: x, y, max_time, max_steps.
    inputs = get_inputs()
    
    run_simulation(
        x = inputs["x"],
        y = inputs["y"],
        max_time = inputs["max_time"],
        max_steps = inputs["max_steps"],
        show_chart=inputs["show_chart"]
    )
    
if __name__ == "__main__":
    main()
    