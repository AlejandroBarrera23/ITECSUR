def es_par(numero):
    validar = numero % 2 == 0
    if validar == False:
        return "Impar"
    else:
        return "Par"

numero = int(input("Ingrese un número: "))
print(es_par(numero))
