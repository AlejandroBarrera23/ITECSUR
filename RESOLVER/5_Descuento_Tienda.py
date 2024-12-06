import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Calculadora de descuentos")
ventana.geometry("300x150")

etiqueta_0 = tk.Label(ventana, text="¿Tienes un descuento del 20%?")
etiqueta_0.pack()

etiqueta = tk.Label(ventana, text="Ingrese la cantidad:")
etiqueta.pack(pady=10)

entrada = tk.Entry(ventana)
entrada.pack(pady=5)

def calcular_descuento():
    try:
        monto = float(entrada.get())
        if monto < 0:
            mensaje = "La cantidad no puede ser negativo"
        elif monto > 100:
            monto_final = monto * 0.8
            monto_descuento = monto * 0.2
            mensaje = f"Cantidad a pagar: ${monto_final:.2f} (Con descuento de ${monto_descuento:.2f})"
        else:
            mensaje = f"Cantidad a pagar: ${monto:.2f} (Sin descuento)"
        messagebox.showinfo("Resultado", mensaje)
    except ValueError:
        messagebox.showerror("Error", "Ingrese una cantidad válido.")

boton = tk.Button(ventana, text="Calcular Descuento", command=calcular_descuento)
boton.pack(pady=10)

ventana.mainloop()
