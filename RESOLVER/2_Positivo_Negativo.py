import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("¿Es positivo o negativo?")
ventana.geometry("300x150")

etiqueta_0 = tk.Label(ventana, text="¿El número es positivo o negativo?")
etiqueta_0.pack()

etiqueta_1 = tk.Label(ventana, text="Ingrese un número:")
etiqueta_1.pack(pady=10)

entrada = tk.Entry(ventana)
entrada.pack(pady=5)

boton = tk.Button(
    ventana,
    text="Validar",
    command=lambda: messagebox.showinfo(
        "Resultado",
        (
            "El número es positivo" if float(entrada.get()) > 0
            else "El número es negativo" if float(entrada.get()) < 0
            else "El número es cero"
        )
    )
)
boton.pack(pady=10)

ventana.mainloop()
