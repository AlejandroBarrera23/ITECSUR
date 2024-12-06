import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x320")

etiqueta_0 = tk.Label(ventana, text="Ingrese el 1er número:")
etiqueta_0.pack(pady=5)
entrada_0 = tk.Entry(ventana)
entrada_0.pack(pady=5)

etiqueta_1 = tk.Label(ventana, text="Ingrese el 2do número:")
etiqueta_1.pack(pady=5)
entrada_1 = tk.Entry(ventana)
entrada_1.pack(pady=5)

def realizar_calculo(operacion):
    try:
        num1 = float(entrada_0.get())
        num2 = float(entrada_1.get())

        if operacion == "+":
            resultado = num1 + num2
        elif operacion == "-":
            resultado = num1 - num2
        elif operacion == "*":
            resultado = num1 * num2
        elif operacion == "/":
            if num2 != 0:
                resultado = num1 / num2
            else:
                mensaje = "Error: División por cero."
                messagebox.showerror("Error", mensaje)
                return

        mensaje = f"Resultado: {resultado}"
        messagebox.showinfo("Resultado", mensaje)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

etiqueta_2 = tk.Label(ventana, text="Elija una operación")
etiqueta_2.pack(pady=5)

boton_suma = tk.Button(ventana, text="+", command=lambda: realizar_calculo("+"))
boton_suma.pack(pady=5)

boton_resta = tk.Button(ventana, text="-", command=lambda: realizar_calculo("-"))
boton_resta.pack(pady=5)

boton_multiplicacion = tk.Button(ventana, text="*", command=lambda: realizar_calculo("*"))
boton_multiplicacion.pack(pady=5)

boton_division = tk.Button(ventana, text="/", command=lambda: realizar_calculo("/"))
boton_division.pack(pady=5)

ventana.mainloop()
