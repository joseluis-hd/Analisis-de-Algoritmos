import time
from itertools import permutations

def traveling_salesman(data):
    n = len(data)
    min_path = float('inf')
    max_path = float('-inf')
    best_route = []
    worst_route = []
    
    for perm in permutations(range(1, n)):
        current_path = data[0][perm[0]] + sum(data[perm[i]][perm[i+1]] for i in range(len(perm) - 1)) + data[perm[-1]][0]
        
        # Verificar si es la ruta mínima
        if current_path < min_path:
            min_path = current_path
            best_route = [0] + list(perm) + [0]
        
        # Verificar si es la ruta máxima
        if current_path > max_path:
            max_path = current_path
            worst_route = [0] + list(perm) + [0]
    
    return min_path, best_route, max_path, worst_route

# Matriz de datos
data = [
    [9, 2, 7, 8],
    [4, 0, 35, 25],
    [15, 35, 3, 17],
    [1, 4, 30, 0]
]

# Medición de tiempo de ejecución
inicio = time.time()
min_dist, best_route, max_dist, worst_route = traveling_salesman(data)
fin = time.time()

# Resultados
print(f"Mejor ruta: {best_route}, Distancia mínima: {min_dist}")
print(f"Peor ruta: {worst_route}, Distancia máxima: {max_dist}")
print(f"Tiempo de ejecución: {fin - inicio}")
