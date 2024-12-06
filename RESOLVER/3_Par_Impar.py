import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("¿Es par o impar?")
ventana.geometry("300x150")

etiqueta_0 = tk.Label(ventana, text="¿El número es par o impar?")
etiqueta_0.pack()

etiqueta = tk.Label(ventana, text="Ingrese un número entero positivo:")
etiqueta.pack(pady=10)

entrada = tk.Entry(ventana)
entrada.pack(pady=5)

boton = tk.Button(
    ventana,
    text="Validar",
    command=lambda: messagebox.showinfo(
        "Resultado",
        (
            "Por favor, ingrese un número entero válido."
            if not entrada.get().lstrip('-').isdigit()
            else "El número es par" if int(entrada.get()) % 2 == 0
            else "El número es impar"
        )
    )
)
boton.pack(pady=10)

ventana.mainloop()