numero = int(input("Ingrese un número: "))
suma = 0
while numero > 0:
    suma += numero % 10
    numero //= 10
print(suma)
