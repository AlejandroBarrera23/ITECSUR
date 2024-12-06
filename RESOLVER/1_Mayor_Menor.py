import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Mayor, igual o menor")
ventana.geometry("300x150")

etiqueta_0 = tk.Label(ventana, text="¿El número es mayor, igual o menor que 10?")
etiqueta_0.pack()

etiqueta_1 = tk.Label(ventana, text="Ingrese un número:")
etiqueta_1.pack(pady=10)

entry = tk.Entry(ventana)
entry.pack(pady=5)

button = tk.Button(
    ventana, 
    text="Validar", 
    command=lambda: messagebox.showinfo(
        "Resultado", 
        "El número es mayor que 10" if float(entry.get()) > 10 
        else "El número es menor que 10" if float(entry.get()) < 10 
        else "Es número es igual a 10"
    )
)
button.pack(pady=10)

ventana.mainloop()