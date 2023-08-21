"""
Nombre del archivo: dirt.py
Autor: Armando Terrazas -- A01640924
       Juan Daniel Muñoz -- A01641792
       Jorge Wolburg -- A01640826
       Diego Curiel -- A01640372
Fecha de creación: 20/08/2023
Descripción: Función que regresa un color aleatorio.
"""
def get_color(random_int: int):
    """
    Method that takes a random integer as input and returns a color string based on the integer.

    Args:
        random_int (int): A random integer.

    Returns:
        str: A color string.
    """
    if random_int == 0:
        return "red"
    elif random_int == 1:
        return "blue"
    elif random_int == 2:
        return "green"
    elif random_int == 3:
        return "yellow"
    elif random_int == 4:
        return "orange"
    elif random_int == 5:
        return "purple"
    elif random_int == 6:
        return "pink"
    elif random_int == 7:
        return "gray"
    else:
        return "lightblue"