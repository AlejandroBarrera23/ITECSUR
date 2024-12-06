import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Año Bisiesto")
ventana.geometry("300x150")

etiqueta_0 = tk.Label(ventana, text="Ingrese el año:")
etiqueta_0.pack(pady=10)
entrada_0 = tk.Entry(ventana)
entrada_0.pack(pady=5)

def verificar_bisiesto():
    try:
        año = int(entrada_0.get())

        if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
            mensaje = "Es un año bisiesto"
        else:
            mensaje = "No es un año bisiesto"
        
        messagebox.showinfo("Resultado", mensaje)
    except ValueError:
        messagebox.showerror("Error", "Ingrese un año válido.")

boton_0 = tk.Button(ventana, text="Verificar", command=verificar_bisiesto)
boton_0.pack(pady=10)

ventana.mainloop()
