# Vacuum World

### Introducción

El programa VacuumWorld es una simulación orientada a agentes utilizando el marco MESA en Python. La simulación representa una habitación con una cuadrícula de espacios MxN, donde los agentes aspiradores se mueven para limpiar espacios sucios. Las posiciones de todos los elementos (agentes, suciedad y obstáculos) se determinan aleatoriamente.

### Prerrequisitos

1. Python >3.9 instalado.
2. Librería MESA instalada.

### Configuración del Entorno Virtual

Antes de ejecutar el programa, se recomienda configurar un entorno virtual. Esto garantiza que las dependencias del proyecto no interfieran con otros proyectos de Python.

1. Instala `virtualenv` si aún no lo has hecho:
   ```bash
   pip install virtualenv
   ```

2. Navega al directorio del proyecto y crea un entorno virtual:
   ```bash
   virtualenv venv
   ```

3. Activa el entorno virtual:
   - En Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - En macOS y Linux:
     ```bash
     source venv/bin/activate
     ```

4. Instala los paquetes requeridos:
   ```bash
   pip install -r requirements.txt
   ```

### Resumen del Algoritmo

1. La simulación inicializa una habitación de tamaño MxN con un número especificado de agentes aspiradores, obstáculos y espacios sucios.
2. Cada agente aspirador solo puede moverse hacia adelante y puede girar en cuatro direcciones (N, S, E, W).
3. El agente solo puede "ver" un conjunto determinado de espacios a su alrededor (solo en las 4 direcciones que se puede mover).
4. Si un agente está en un espacio sucio, lo limpiará.
5. Un agente no se puede mover a un espacio que contenga un obstáculo u otro agente.
6. La simulación termina cuando:
   - Todos los espacios están limpios.
   - Se alcanza el número máximo de pasos.
   - Se alcanza el tiempo máximo de ejecución.

### Ejecutando la Simulación

1. Navega al directorio del proyecto.
2. Ejecuta el script `main.py`:
   ```bash
   python3 main.py
   ```
   Puedes agregar las banderas `-x` y `-y` para especificar el tamaño de la cuadrícula:
   ```bash
   python3 main.py -x 10 -y 10
   ```
   También puedes agregar las banderas `-t` y `--max-steps` para especificar el tiempo máximo de ejecución y el máximo de pasos (de no ponerse, el valor predeterminado es x * y + 10), respectivamente:
   ```bash
   python3 main.py -t 100 --max-steps 1000
   ```
3. Esto iniciará el servidor MESA y abrirá la simulación en tu navegador web predeterminado.
4. Usa los deslizadores proporcionados para ajustar el número de agentes y la suciedad.
5. Haz clic en "Start" para comenzar la simulación y en "Step" para avanzarla un paso a la vez.

Para obtener más información sobre las banderas disponibles, ejecuta el siguiente comando:
```bash
python3 main.py --help
```

### Entendiendo el Código

- **VacuumAgent**: Representa al agente aspirador. Tiene métodos para limpiar la suciedad y moverse a celdas vecinas.
- **Dirt**: Representa el espacio con suciedad. En el momento que `VacuumAgent` ingresa a esta celda, se vuelve en una celda limpia.
- **Obstacle**: Representa a los obstáculos dentro de la cuadrícula. `VacuumAgent` no puede ingresar a esta celda. Se limitó su cantidad a 30.

- **VacuumWorld**: Representa el modelo del mundo. Inicializa la cuadrícula, los agentes y la suciedad.
- **Server**: Contiene la configuración de visualización para el servidor MESA. Define como se representan los agentes y la suciedad en la cuadrícula.
- **Main.py**: El punto de entrada del programa. Inicia el servidor MESA.

## Explicación del Algoritmo del Agente Aspiradora

La clase `VacuumAgent` representa el comportamiento de un agente aspiradora en la simulación VacuumWorld. Aquí hay un desglose del algoritmo principal seguido por el `VacuumAgent`:

1. **Inicialización (método `__init__`)**:
   - El agente se inicializa con un ID único y una referencia al modelo al que pertenece.
   - Se establecen contadores para los pasos realizados y las celdas limpiadas.
   - Se inicializan listas y conjuntos para rastrear los pasos adyacentes, las celdas visitadas y las celdas a las que debe regresar.
   - Se determina el color del agente basado en su ID único.

2. **Limpieza (método `clean`)**:
   - El agente verifica su posición actual en busca de suciedad.
   - Si encuentra suciedad en su posición, la limpia y actualiza los contadores correspondientes.

3. **Movimiento (método `step`)**:
   - El agente intenta limpiar la celda actual.
   - Posteriormente, intenta moverse a una celda vecina usando el método `move`.

4. **Agregar a Pasos Adyacentes (método `append_to_adjacent`)**:
   - Este método agrega nuevas posiciones a la lista de pasos adyacentes y ajusta el contador de pasos necesarios para regresar a esa posición.

5. **Determinar Pasos Posibles (método `get_possible_steps`)**:
   - El agente identifica las celdas vecinas a las que puede moverse.
   - Se excluyen las celdas que contienen obstáculos u otros agentes aspiradores.
   - Las celdas no visitadas se agregan a la lista de pasos adyacentes.

6. **Lógica de Retroceso (método `return_to_previous_cell`)**:
   - Si el agente está retrocediendo, este método intenta mover al agente de regreso a una celda anterior en la lista de pasos adyacentes.
   - Si no puede regresar directamente a la celda objetivo, retrocede a la última celda visitada.

7. **Mover a la Siguiente Celda (método `move_to_next_cell`)**:
   - Si hay pasos posibles, el agente se mueve a la siguiente celda en la lista de pasos adyacentes, dando prioridad a las celdas sucias.
   - Si no hay pasos posibles, cambia su estado a `is_returning` para comenzar a retroceder.

8. **Lógica de Movimiento (método `move`)**:
   - Si el agente no está retrocediendo (`is_returning` es `False`), utiliza el método `move_to_next_cell` para avanzar.
   - Si el agente está retrocediendo (`is_returning` es `True`), utiliza el método `returnToPreviousCell` para retroceder.

El algoritmo del agente aspiradora utiliza un enfoque de búsqueda en profundidad (DFS) para explorar la cuadrícula. Cuando se encuentra en un callejón sin salida o no puede avanzar más, comienza a retroceder a las celdas anteriores hasta que encuentra un nuevo camino para explorar. Este proceso se repite hasta que el agente ha explorado toda la cuadrícula o hasta que se cumplan las condiciones de finalización de la simulación.

## Authors 🖋
- Armando Terrazas Gomez - A01640924
- Jorge German Wolburg Trujillo - A01640826
- Juan Daniel Muñoz Dueñas - A01641792
- Diego Curiel Castellanos - A01640372
