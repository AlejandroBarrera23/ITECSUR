import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Control Acceso")
ventana.geometry("300x250")

intentos = 3
usuario_correcto = "admin"
contraseña_correcta = "12345"

etiqueta_2 = tk.Label(ventana, text="Usuario:admin Contraseña:12345")
etiqueta_2.pack()

etiqueta_0 = tk.Label(ventana, text="Usuario:")
etiqueta_0.pack(pady=10)
entrada_0 = tk.Entry(ventana)
entrada_0.pack(pady=5)

etiqueta_1 = tk.Label(ventana, text="Contraseña:")
etiqueta_1.pack(pady=10)
entrada_1 = tk.Entry(ventana, show="*")
entrada_1.pack(pady=5)

def verificar_acceso():
    global intentos
    usuario = entrada_0.get()
    contraseña = entrada_1.get()

    if usuario == usuario_correcto and contraseña == contraseña_correcta:
        messagebox.showinfo("Acceso", f"Bienvenido, {usuario}.")
        ventana.quit()
    else:
        intentos -= 1
        if intentos > 0:
            messagebox.showwarning("Error", f"Credenciales incorrectas. Te quedan {intentos} intentos.")
        else:
            messagebox.showerror("Bloqueo", "Número máximo de intentos alcanzado. Acceso bloqueado.")
            ventana.quit()

boton_0 = tk.Button(ventana, text="Ingresar", command=verificar_acceso)
boton_0.pack(pady=20)

ventana.mainloop()