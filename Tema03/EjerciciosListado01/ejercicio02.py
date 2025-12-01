def ordenar_numeros(tope):
    numLeido=0
    numeros=[]
    numeros_ordenados=[]
    for i in range(tope):
        numLeido=int(input("Diga un número: "))
        numeros.append(numLeido)

    numeros_ordenados.append(min(numeros))
    for i in range(len(numeros)):
        if numeros[i] != min(numeros) and numeros[i] != max(numeros):
            numeros_ordenados.append(numeros[i])
    numeros_ordenados.append(max(numeros))
    return numeros_ordenados

tope=int(input("Diga cuantos números quiere introducir: "))
resultado = ordenar_numeros(tope)
print(f"Los números ordenados son: {resultado}")