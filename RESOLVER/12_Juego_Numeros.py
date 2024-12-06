import tkinter as tk
from tkinter import messagebox
import random

ventana = tk.Tk()
ventana.title("Juego de Números")
ventana.geometry("300x125")

numero_aleatorio = random.randint(1, 10)

etiqueta_0 = tk.Label(ventana, text="Adivina el número entre 1 y 10:")
etiqueta_0.pack(pady=10)
entrada_0 = tk.Entry(ventana)
entrada_0.pack(pady=5)

def adivinar_numero():
    try:
        numero_usuario = int(entrada_0.get())
        
        if numero_usuario == numero_aleatorio:
            mensaje = "¡Felicidades, acertaste!"
        else:
            mensaje = "Intenta de nuevo."
        
        messagebox.showinfo("Resultado", mensaje)
    except ValueError:
        messagebox.showerror("Error", "Ingresa un número válido.")

boton_0 = tk.Button(ventana, text="Adivinar", command=adivinar_numero)
boton_0.pack(pady=10)

ventana.mainloop()