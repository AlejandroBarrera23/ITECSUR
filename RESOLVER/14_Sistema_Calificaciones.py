import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Sistema de Calificaciones")
ventana.geometry("300x150")

etiqueta_0 = tk.Label(ventana, text="Ingrese la calificación (entre 0 y 100):")
etiqueta_0.pack(pady=10)
entrada_0 = tk.Entry(ventana)
entrada_0.pack(pady=5)

def calcular_calificacion():
    try:
        calificacion = float(entrada_0.get())
        
        if 90 <= calificacion <= 100:
            mensaje = "Tu calificación es A"
        elif 80 <= calificacion < 90:
            mensaje = "Tu calificación es B"
        elif 70 <= calificacion < 80:
            mensaje = "Tu calificación es C"
        elif 60 <= calificacion < 70:
            mensaje = "Tu calificación es D"
        elif calificacion < 60 and calificacion >= 0:
            mensaje = "Tu calificación es F"
        else:
            mensaje = "Calificación incorrecta. Debe estar entre 0 y 100"
        
        messagebox.showinfo("Resultado", mensaje)
    except ValueError:
        messagebox.showerror("Error", "Ingresa una calificación válida.")

boton_0 = tk.Button(ventana, text="Calcular", command=calcular_calificacion)
boton_0.pack(pady=20)

ventana.mainloop()