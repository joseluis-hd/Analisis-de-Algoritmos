import time

def knapsack(values, weights, capacidad):
    n = len(values)
    dp = [[0 for _ in range(capacidad + 1)] for _ in range(n + 1)]
    
    #Calcular el valor óptimo (máximo valor posible)
    for i in range(1, n + 1):
        for w in range(1, capacidad + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    
    #Valor óptimo
    valor_optimo = dp[n][capacidad]

    #Valor mínimo (peor caso): el primer valor que no excede la capacidad
    # Se busca en la primera columna de la última fila
    valor_minimo = min(dp[i][capacidad] for i in range(1, n + 1) if dp[i][capacidad] > 0)

    return valor_optimo, valor_minimo

#Datos de entrada
values = [7, 3, 4, 5]
weights = [42, 12, 40, 25]
capacidad = 120

#Medición de tiempo de ejecución
inicio = time.time()
valor_optimo, valor_minimo = knapsack(values, weights, capacidad)
fin = time.time()

#Resultados
print(f"Mejor caso (Valor óptimo): {valor_optimo}")
print(f"Peor caso (Valor mínimo no nulo): {valor_minimo}")
print(f"Tiempo de ejecución: {fin - inicio}")
