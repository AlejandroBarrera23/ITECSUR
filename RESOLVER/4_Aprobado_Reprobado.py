import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("¿Está aprobado o reprobado?")
ventana.geometry("400x150")

etiqueta_0 = tk.Label(ventana, text="¿El estudiante está aprobado o reprobado?")
etiqueta_0.pack()

etiqueta_1 = tk.Label(ventana, text="Ingrese la calificación:")
etiqueta_1.pack(pady=10)

entrada = tk.Entry(ventana)
entrada.pack(pady=5)

boton = tk.Button(
    ventana,
    text="Validar",
    command=lambda: messagebox.showinfo(
        "Resultado",
        (
            "Ingrese una calificación válida (entre 0 y 10)."
            if not entrada.get().replace('.', '', 1).isdigit() or not (0 <= float(entrada.get()) <= 10)
            else "El estudiante está aprobado" if float(entrada.get()) >= 7
            else "El estudiante está reprobado"
        )
    )
)
boton.pack(pady=10)

ventana.mainloop()
