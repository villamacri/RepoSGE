def contar_mayores(numeros):
    contador = 0
    for i in range(1, len(numeros)):
        if numeros[i] > numeros[i-1]:
            contador += 1
    return contador

cuantos = int(input("¿Cuántos números va a introducir? "))

numeros = []
for i in range(cuantos):
    num = int(input(f"Diga el número {i+1}: "))
    numeros.append(num)

resultado = contar_mayores(numeros)
print(f"{resultado} números son mayores que el anterior.")
