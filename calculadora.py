#219416828 - Jose Luis Haro Diaz
import tkinter as tk
from tkinter import ttk

def calcular(operation):
    try:
        op1 = float(valor1_entry.get())
        num2 = float(valor2_entry.get())

        if operation == "+":
            result = op1 + num2
        elif operation == "-":
            result = op1 - num2
        elif operation == "*":
            result = op1 * num2
        elif operation == "/":
            if num2 != 0:
                result = op1 / num2
            else:
                result = "Error"

        result_entry.delete(0, tk.END)
        result_entry.insert(0, str(result))
    except ValueError:
        result_entry.delete(0, tk.END)
        result_entry.insert(0, "Error")

#Ventana
window = tk.Tk()
window.title("Calculadora Jose Luis Haro Diaz")

#Entradas
ttk.Label(window, text="Numero 1:").grid(column=0, row=0, padx=10, pady=10)
valor1_entry = ttk.Entry(window)
valor1_entry.grid(column=1, row=0, padx=10, pady=10)

ttk.Label(window, text="Numero 2:").grid(column=0, row=1, padx=10, pady=10)
valor2_entry = ttk.Entry(window)
valor2_entry.grid(column=1, row=1, padx=10, pady=10)

#Botones
ttk.Button(window, text="+", command=lambda: calcular("+")).grid(column=2, row=0, padx=10, pady=10)
ttk.Button(window, text="-", command=lambda: calcular("-")).grid(column=2, row=1, padx=10, pady=10)
ttk.Button(window, text="*", command=lambda: calcular("*")).grid(column=3, row=0, padx=10, pady=10)
ttk.Button(window, text="/", command=lambda: calcular("/")).grid(column=3, row=1, padx=10, pady=10)

#Resultado
ttk.Label(window, text="Resultado:").grid(column=0, row=2, padx=10, pady=10)
result_entry = ttk.Entry(window)
result_entry.grid(column=1, row=2, padx=10, pady=10)

window.mainloop()