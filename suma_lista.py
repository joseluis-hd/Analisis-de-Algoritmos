import time
import random

def suma_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

#Generar una lista de números aleatorios
tamaño_lista = 10  #Se puede cambiar el tamaño de la lista
lista = [random.randint(1, 100) for _ in range(tamaño_lista)]  #Números aleatorios entre 1 y 100

#Print lista generada
print(f"Lista generada: {lista}")

#Medición del tiempo de ejecución
inicio = time.time()
resultado = suma_lista(lista)
fin = time.time()

print(f"Suma de la lista: {resultado}")
print(f"Tiempo de ejecución: {fin - inicio} segundos")
