'''
En esta segunda actividad tome como ejemplo lo visto en clase
para graficar tiempos de ordenamiento, aquí decidí utilizar InsertSort
y MergeSort ya que en clase utilice QuickSort. Para la GUI me apegue 
a lo visto en la primera clase y hay dos botones donde el usuario 
selecciona el metodo de ordenamiento que desea utilizar.
'''

#Librerias
import time
import random
import matplotlib.pyplot as plt
from math import log
import tkinter as tk

#InsertSort
def insert_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

#MergeSort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

#Medir tiempo de ejecución
def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    end_time = time.time()
    return end_time - start_time

#Generar lista aleatoria de 1000 elementos
def generador(size):
    return [random.randint(1, 10000) for _ in range(size)]

#Graficar
def plot(sizes, times, title):
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times, marker='o', linestyle='--', color='deepskyblue')
    plt.xlabel('Tamaño de la lista')
    plt.ylabel('Tiempo de ejecución en segundos')
    plt.title(title)
    plt.grid(True)
    plt.show()

#Función para ejecutar el algoritmo seleccionado por el usuario y mostrar los resultados
def run_algorithm(algorithm):
    sizes = list(range(50, 1050, 50))  #Listas
    times = []
    repetitions = 5  #Reps para promediar los tiempos

    for size in sizes:
        total_time = 0
        for _ in range(repetitions):
            random_list = generador(size)
            if algorithm == "InsertSort":
                total_time += measure_time(insert_sort, random_list[:])
                title = 'Tiempo de ejecución InsertSort'
            elif algorithm == "MergeSort":
                total_time += measure_time(merge_sort, random_list[:])
                title = 'Tiempo de ejecución de MergeSort'
        average_time = total_time / repetitions
        times.append(average_time)
        print(f"Tamaño de la lista: {size} - Tiempo de ejecución: {average_time:.4f} seg.")

    #Graficar resultados
    plot(sizes, times, title)

#GUI
root = tk.Tk()
root.title("Actividad 2. Análisis de Algoritmos")
root.geometry("300x150")

#Labels de selección de algoritmo
label = tk.Label(root, text="Selecciona un algoritmo de ordenamiento:")
label.pack(pady=10)

#Buttons para seleccionar el algoritmo
insertion_button = tk.Button(root, text="InsertSort", command=lambda: run_algorithm("InsertSort"))
insertion_button.pack(pady=5)

merge_button = tk.Button(root, text="MergeSort", command=lambda: run_algorithm("MergeSort"))
merge_button.pack(pady=5)

root.mainloop()
