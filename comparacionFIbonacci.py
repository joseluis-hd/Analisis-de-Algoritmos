'''
Este código hace una comparación del tiempo de ejecución de dos algoritmos para calcular la serie de Fibonacci () 
uno iterativo y otro recursivo. Se mide el tiempo de ejecución de ambos algoritmos para valores de N
desde 0 hasta 100. Los tiempos se grafican en una misma gráfica para visualizar las diferencias de rendimiento entre ambos enfoques.
'''

import time
import matplotlib.pyplot as plt

#Método iterativo (fuerza bruta)
def fibonacciIterativo(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

#Método recursivo
def fibonacciRecursivo(n):
    if n <= 1:
        return n
    return fibonacciRecursivo(n-1) + fibonacciRecursivo(n-2)

#Función para medir tiempos de ejecución
def medirTiempo(nMax):
    tiemposIterativo = []
    tiemposRecursivo = []
    valN = list(range(nMax+1))

    for n in valN:
        #Medir tiempo iterativo
        inicio = time.time()
        fibonacciIterativo(n)
        fin = time.time()
        tiemposIterativo.append(fin - inicio)

        #Medir tiempo  recursivo
        if n <= 35: #Se limita a 35 para evitar overflow

            inicio = time.time()
            fibonacciRecursivo(n)
            fin = time.time()
            tiemposRecursivo.append(fin - inicio)
        else:
            tiemposRecursivo.append(0)

    return tiemposIterativo, tiemposRecursivo, valN

#Graficar tiempos de ejecución
def graficaTiempos():
    nMax = 100  #N max
    tiemposIterativo, tiemposRecursivo, valN = medirTiempo(nMax)

    #Grafica
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(valN, tiemposIterativo, linestyle='-', color='coral', label='Iterativo')
    ax.plot(valN[:36], tiemposRecursivo[:36], linestyle='--', color='deepskyblue', label='Recursivo')
    ax.set_xlabel('N Elementos')
    ax.set_ylabel('Tiempo de ejecución en segundos')
    ax.set_title('Fibonacci Iterativo vs Recursivo')
    ax.legend()
    ax.grid(True)

    plt.show()

graficaTiempos()
