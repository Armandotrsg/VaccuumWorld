# Vacuum World

### Introducción

El programa VacuumWorld es una simulación orientada a agentes utilizando el marco MESA en Python. La simulación representa una habitación con una cuadrícula de espacios MxN, donde los agentes aspiradores se mueven para limpiar espacios sucios. Las posiciones de todos los elementos (agentes, suciedad y obstáculos) se determinan aleatoriamente.

### Prerrequisitos

1. Python 3.x instalado.
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

1. La simulación inicializa una habitación de tamaño MxN con un número especificado de agentes aspiradores y espacios sucios.
2. Cada agente aspirador solo puede moverse hacia adelante y puede girar en cuatro direcciones (N, S, E, W).
3. El agente solo puede "ver" un conjunto determinado de espacios a su alrededor.
4. Si un agente está en un espacio sucio, lo limpiará.
5. La simulación termina cuando:
   - Todos los espacios están limpios.
   - Se alcanza el número máximo de pasos.

### Ejecutando la Simulación

1. Navega al directorio del proyecto.
2. Ejecuta el script `main.py`:
   ```bash
   python3 main.py
   ```

3. Esto iniciará el servidor MESA y abrirá la simulación en tu navegador web predeterminado.
4. Usa los deslizadores proporcionados para ajustar el número de agentes y la suciedad.
5. Haz clic en "Start" para comenzar la simulación y en "Step" para avanzarla un paso a la vez.

### Entendiendo el Código

- **VaccuumAgent**: Representa al agente aspirador. Tiene métodos para limpiar la suciedad y moverse a celdas vecinas.
- **Dirt**: Representa el espacio con suciedad. En el momento que `VacuumAgent` ingresa a esta celda, se vuelve en una celda limpia.
- **Obstacle**: Representa al los obstáculos dentro de la cuadrícula. `VacuumAgent` no puede ingresar a esta celda. Se limitó su cantidad a 30.

- **VaccuumWorld**: Representa el modelo del mundo. Inicializa la cuadrícula, los agentes y la suciedad.
- **Server**: Contiene la configuración de visualización para el servidor MESA. Define cómo se representan los agentes y la suciedad en la cuadrícula.
- **Main.py**: El punto de entrada del programa. Inicia el servidor MESA.


## Explicación del Algoritmo del Agente Aspiradora

La clase `VaccuumAgent` representa el comportamiento de un agente aspiradora en la simulación VacuumWorld. Aquí hay un desglose del algoritmo principal seguido por el `VaccuumAgent`:

1. **Inicialización (método `__init__`)**:
   - El agente se inicializa con un ID único y una referencia al modelo al que pertenece.
   - El agente lleva un registro del número de pasos realizados, el número de celdas limpiadas, los posibles pasos para la Búsqueda en Profundidad (DFS) y las celdas que ha visitado.
   - El agente tiene un estado `is_returning` para determinar si está retrocediendo.
   - El color del agente se determina en función del ID único.

2. **Limpieza (método `clean`)**:
   - El agente verifica su posición actual en busca de suciedad.
   - Si hay suciedad en la misma celda que el agente, este la limpia, incrementa su contador de celdas limpiadas y decrementa el contador de suciedad del modelo.

3. **Movimiento (método `step`)**:
   - El agente primero intenta limpiar la celda actual.
   - Luego intenta moverse a una celda vecina usando el método `move`.

4. **Determinar Pasos Posibles (método `get_possible_steps`)**:
   - Dada la posición actual del agente, este método determina las celdas vecinas a las que el agente puede moverse.
   - Filtra las celdas que contienen obstáculos u otros agentes.
   - Actualiza la lista `adjacent_steps` con cualquier nueva celda vecina que no haya sido visitada anteriormente.

5. **Lógica de Movimiento (método `move`)**:
   - Si el agente no está en el estado `is_returning`:
     - Añade su posición actual a la lista `visited`.
     - Determina los posibles pasos desde su posición actual.
     - Si no hay pasos posibles, establece `is_returning` en `True` para comenzar a retroceder.
     - De lo contrario, se mueve a la última celda en la lista `adjacent_steps`.
   - Si el agente está en el estado `is_returning` (retrocediendo):
     - Intenta volver a la última celda visitada.
     - Si la posición objetivo (última celda en `adjacent_steps`) es alcanzable, se mueve allí y sale del estado `is_returning`.
     - Si la última celda visitada es alcanzable, se mueve allí y continúa retrocediendo.

El agente utiliza un enfoque de búsqueda por DFS para explorar la cuadrícula. Intenta moverse lo más profundo posible en la cuadrícula hasta que no pueda moverse más, momento en el que comienza a retroceder (volviendo a las celdas visitadas anteriormente) hasta que encuentra un nuevo camino para explorar. Este proceso continúa hasta que el agente ha explorado toda la cuadrícula o hasta que finaliza la simulación (toda la suciedad está limpia o se alcanza el número máximo de pasos).
