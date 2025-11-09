numPalab=int(input("Diga el número de palabras que quiere: "))
listadoPalabras=[]
copiaListado=[]
palabraLeida=""

for i in range(numPalab):
    palabraLeida=input("Diga una palabra: ")
    listadoPalabras.append(palabraLeida)

copiaListado=list(reversed(listadoPalabras))

print(listadoPalabras)
print(copiaListado)