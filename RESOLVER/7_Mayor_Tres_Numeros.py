import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("¿Cuál es el mayor de tres números?")
ventana.geometry("300x250")

etiqueta_0 = tk.Label(ventana, text="Ingrese el primer número:")
etiqueta_0.pack(pady=5)
entrada_0 = tk.Entry(ventana)
entrada_0.pack(pady=5)

etiqueta_1 = tk.Label(ventana, text="Ingrese el segundo número:")
etiqueta_1.pack(pady=5)
entrada_1 = tk.Entry(ventana)
entrada_1.pack(pady=5)

etiqueta_2 = tk.Label(ventana, text="Ingrese el tercer número:")
etiqueta_2.pack(pady=5)
entrada_2 = tk.Entry(ventana)
entrada_2.pack(pady=5)

def calcular_mayor():
    try:
        numero1 = float(entrada_0.get())
        numero2 = float(entrada_1.get())
        numero3 = float(entrada_2.get())
        
        mayor = max(numero1, numero2, numero3)
        mensaje = f"El número mayor es {mayor}"
        messagebox.showinfo("Resultado", mensaje)
    except ValueError:
        messagebox.showerror("Error", "Ingrese números correctos")

boton = tk.Button(ventana, text="Calcular", command=calcular_mayor)
boton.pack(pady=10)

ventana.mainloop()
