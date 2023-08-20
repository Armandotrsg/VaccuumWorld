import threading
from model.model import VacuumWorld

def run_single_simulation(N, D, O, results):
    model = VacuumWorld(N, D, O, width=10, height=10, max_steps= 250)
    while model.running:
        model.step()
    steps = model.schedule.steps
    total_movements = steps * N
    results.append((N, D, O, steps, total_movements))

def main():
    # Define the range of values
    agent_values = range(1, 11)
    dirt_values = range(1, 21)
    obstacle_values = range(1, 21)

    TIMEOUT = 0.1  # tiempo límite en segundos para cada simulación

    results = []

    for N in agent_values:
        for D in dirt_values:
            for O in obstacle_values:
                # Inicia la simulación en un hilo separado
                simulation_thread = threading.Thread(target=run_single_simulation, args=(N, D, O, results))
                simulation_thread.start()
                simulation_thread.join(timeout=TIMEOUT)  # Espera hasta que termine la simulación o hasta que se alcance el tiempo límite

                # Si el hilo todavía está activo después del tiempo límite, se considera que la simulación se ha quedado atascada
                if simulation_thread.is_alive():
                    print(f"Simulation with Agents: {N}, Dirt: {D}, Obstacles: {O} exceeded the time limit. Moving to the next simulation.")
                    simulation_thread.join()  # Esto es solo por precaución para asegurarse de que el hilo termine antes de continuar

    # Guarda los resultados en un archivo
    with open("results.txt", "w") as file:
        for N, D, O, steps, total_movements in results:
            file.write(f"Agents: {N}, Dirt: {D}, Obstacles: {O}, Steps: {steps}, Total Movements: {total_movements}\n")

if __name__ == "__main__":
    main()
