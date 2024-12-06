numero = int(input("Ingrese un número: "))
invertido = 0
while numero > 0:
    invertido = invertido * 10 + numero % 10
    numero //= 10
print(invertido)
