import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Clasificación de Edades")
ventana.geometry("300x150")

etiqueta_1 = tk.Label(ventana, text="¿Eres un niño, adolescente o adulto?")
etiqueta_1.pack()

etiqueta_0 = tk.Label(ventana, text="Ingrese su edad:")
etiqueta_0.pack(pady=10)
entrada_0 = tk.Entry(ventana)
entrada_0.pack(pady=5)

def clasificar_edad():
    try:
        edad = int(entrada_0.get())
        if edad <= 12:
            mensaje = "Eres un niño"
        elif edad <= 17:
            mensaje = "Eres un adolescente"
        else:
            mensaje = "Eres un adulto"
        messagebox.showinfo("Resultado", mensaje)
    except ValueError:
        messagebox.showerror("Error", "Ingrese una edad válida.")

boton_0 = tk.Button(ventana, text="Clasificar", command=clasificar_edad)
boton_0.pack(pady=10)

ventana.mainloop()