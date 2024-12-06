import math

def area_circulo(radio):
    return math.pi * radio ** 2

radio = float(input("Ingrese el radio del círculo: "))
print(f"El área del círculo es: {area_circulo(radio):.2f}")
