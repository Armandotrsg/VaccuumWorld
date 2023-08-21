import matplotlib.pyplot as plt

# Leer los datos desde el archivo
with open("results.txt", "r") as file:
    lines = file.readlines()

# Procesar los datos
processed_data = []
for line in lines:
    # Divide la línea en palabras y extrae los números
    parts = line.split()
    agent = int(parts[1].replace(",", ""))
    dirt = int(parts[3].replace(",", ""))
    obstacle = int(parts[5].replace(",", ""))
    step = int(parts[7].replace(",", ""))
    movement = int(parts[10])
    processed_data.append([agent, dirt, obstacle, step, movement])

# Separar los datos en listas individuales
agents, dirt, obstacles, steps, movements = zip(*processed_data)
# Graficar la relación entre el número de agentes y la cantidad de movimientos
plt.figure(figsize=(10, 6))
plt.scatter(agents, movements, color='blue')
plt.title('Relación entre el número de agentes y la cantidad de movimientos')
plt.xlabel('Número de agentes')
plt.ylabel('Cantidad de movimientos')
plt.grid(True)
plt.show()

# Graficar la relación entre el número de agentes y los pasos totales
plt.figure(figsize=(10, 6))
plt.scatter(agents, steps, color='red')
plt.title('Relación entre el número de agentes y los pasos totales')
plt.xlabel('Número de agentes')
plt.ylabel('Pasos totales')
plt.grid(True)
plt.show()

# Graficar la relación entre la cantidad de basura y la cantidad de movimientos
plt.figure(figsize=(10, 6))
plt.scatter(dirt, movements, color='green')
plt.title('Relación entre la cantidad de basura y la cantidad de movimientos')
plt.xlabel('Cantidad de basura')
plt.ylabel('Cantidad de movimientos')
plt.grid(True)
plt.show()

# Graficar la relación entre la cantidad de basura y los pasos totales
plt.figure(figsize=(10, 6))
plt.scatter(dirt, steps, color='orange')
plt.title('Relación entre la cantidad de basura y los pasos totales')
plt.xlabel('Cantidad de basura')
plt.ylabel('Pasos totales')
plt.grid(True)
plt.show()

# Graficar la relación entre la cantidad de obstáculos y la cantidad de movimientos
plt.figure(figsize=(10, 6))
plt.scatter(obstacles, movements, color='purple')
plt.title('Relación entre la cantidad de obstáculos y la cantidad de movimientos')
plt.xlabel('Cantidad de obstáculos')
plt.ylabel('Cantidad de movimientos')
plt.grid(True)
plt.show()

# Graficar la relación entre la cantidad de obstáculos y los pasos totales
plt.figure(figsize=(10, 6))
plt.scatter(obstacles, steps, color='brown')
plt.title('Relación entre la cantidad de obstáculos y los pasos totales')
plt.xlabel('Cantidad de obstáculos')
plt.ylabel('Pasos totales')
plt.grid(True)
plt.show()
