# def contar_mayores(numeros, numLeido):
#     contador = 0
#     for i in range(1, len(numeros)):
#         if numeros[i] > numLeido:
#             contador += 1
#     return contador
# 
# numLeido=int(input("Diga un número: "))
# cuantos = int(input("¿Cuántos números va a introducir? "))
# 
# numeros = []
# for i in range(cuantos):
#     num = int(input(f"Diga el número {i+1}: "))
#     numeros.append(num)
# 
# resultado = contar_mayores(numeros)
# print(f"{resultado} números son mayores que el anterior.")


#VERSIÓN DEL TOÑETE(MEJOR)
numero1 = int(input("Diga un número que sera con el que se compararán: "))

cantNumeros = int(input("Diga la cantidad de números que vas a meter: "))

numerosMayores = []

def contar(num, cantNumero):
    for i in range (0, cantNumero):
        numero = int(input("Diga un numero"))
        if numero > num:
            numerosMayores.append(numero) 
    return print(numerosMayores)


contar(numero1, cantNumeros)