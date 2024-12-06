suma = 0
contador = 0
while True:
    calificacion = float(input("Ingrese una calificación (-1 para terminar): "))
    if calificacion == -1:
        break
    suma += calificacion
    contador += 1
if contador > 0:
    promedio = suma / contador
    print(f"Promedio: {promedio:.2f}")
else:
    print("No se ingresaron calificaciones")
