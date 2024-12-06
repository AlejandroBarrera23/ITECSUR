import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Validar Contraseña")
ventana.geometry("300x150")

etiqueta_1 = tk.Label(ventana, text="Contraseña correcta: 232916")
etiqueta_1.pack()

etiqueta_0 = tk.Label(ventana, text="Ingrese la contraseña:")
etiqueta_0.pack(pady=10)
entrada_0 = tk.Entry(ventana, show="*")
entrada_0.pack(pady=5)

def validar_contraseña():
    contraseña = entrada_0.get()

    if contraseña == "232916":
        mensaje = "Contraseña correcta"
    else:
        mensaje = "Contraseña incorrecta. Intentelo de nuevo"
    
    messagebox.showinfo("Resultado", mensaje)

boton_0 = tk.Button(ventana, text="Validar", command=validar_contraseña)
boton_0.pack(pady=10)

ventana.mainloop()