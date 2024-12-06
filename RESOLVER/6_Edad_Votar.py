import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("¿Ya puedes votar?")
ventana.geometry("300x150")

etiqueta_0 = tk.Label(ventana, text="¿Ya tienes edad para votar?")
etiqueta_0.pack()

etiqueta_1 = tk.Label(ventana, text="Ingrese su edad:")
etiqueta_1.pack(pady=10)

entrada = tk.Entry(ventana)
entrada.pack(pady=5)

def verificar_edad():
    try:
        edad = int(entrada.get())
        if edad < 0:
            mensaje = "No existen edades negativas"
        elif edad >= 18:
            mensaje = "Puedes votar"
        else:
            mensaje = "No puedes votar"
        messagebox.showinfo("Resultado", mensaje)
    except ValueError:
        messagebox.showerror("Error", "Ingrese una edad correcta")

boton = tk.Button(ventana, text="Validar", command=verificar_edad)
boton.pack(pady=10)

ventana.mainloop()