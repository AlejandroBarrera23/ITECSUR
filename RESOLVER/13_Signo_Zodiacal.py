import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Calcula tu Signo Zodiacal")
ventana.geometry("300x200")

etiqueta_0 = tk.Label(ventana, text="Ingrese el día de nacimiento (en números):")
etiqueta_0.pack(pady=10)
entrada_0 = tk.Entry(ventana)
entrada_0.pack(pady=5)

etiqueta_1 = tk.Label(ventana, text="Ingrese el mes de nacimiento (en letras):")
etiqueta_1.pack(pady=10)
entrada_1 = tk.Entry(ventana)
entrada_1.pack(pady=5)

def calcular_signo():
    try:
        dia = int(entrada_0.get())
        mes = entrada_1.get().lower()

        signos = [
            ("capricornio", "enero", 1, 19), ("acuario", "enero", 20, 31), ("acuario", "febrero", 1, 18),
            ("piscis", "febrero", 19, 29), ("piscis", "marzo", 1, 20), ("aries", "marzo", 21, 31),
            ("aries", "abril", 1, 19), ("tauro", "abril", 20, 30), ("tauro", "mayo", 1, 20),
            ("geminis", "mayo", 21, 31), ("geminis", "junio", 1, 20), ("cancer", "junio", 21, 30),
            ("cancer", "julio", 1, 22), ("leo", "julio", 23, 31), ("leo", "agosto", 1, 22),
            ("virgo", "agosto", 23, 31), ("virgo", "septiembre", 1, 22), ("libra", "septiembre", 23, 30),
            ("libra", "octubre", 1, 22), ("escorpio", "octubre", 23, 31), ("escorpio", "noviembre", 1, 21),
            ("sagitario", "noviembre", 22, 30), ("sagitario", "diciembre", 1, 21), ("capricornio", "diciembre", 22, 31)
        ]
        
        for signo, mes_zodiaco, inicio, fin in signos:
            if mes == mes_zodiaco and inicio <= dia <= fin:
                mensaje = f"Tu signo es {signo.capitalize()}"
                messagebox.showinfo("Resultado", mensaje)
                return
        
        messagebox.showerror("Error", "Fecha inválida. Ingresa una fecha válida.")

    except ValueError:
        messagebox.showerror("Error", "Ingresa un día y mes válidos.")

boton_0 = tk.Button(ventana, text="Calcular", command=calcular_signo)
boton_0.pack(pady=20)

ventana.mainloop()