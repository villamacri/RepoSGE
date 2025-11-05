numPalab=int(input("Diga el número de palabras que quiere: "))
listadoPalabras=[]
copiaListado=[]
palabraLeida=""
palabraActual=""

for i in range(numPalab):
    palabraLeida=input("Diga una palabra: ")
    listadoPalabras.append(palabraLeida)
print(listadoPalabras)

i = 0
while i < len(listadoPalabras):
    palabraActual=listadoPalabras[i]
    for j in range(len(listadoPalabras)-1, i, -1):
        if listadoPalabras[j] == palabraActual:
            listadoPalabras.pop(j)
    i += 1

print(listadoPalabras)