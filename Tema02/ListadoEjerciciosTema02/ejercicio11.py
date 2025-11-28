numPalab=int(input("Diga el número de palabras que quiere para las listas: "))
listadoPalabras1=[]
listadoPalabras2=[]
listado1=[]
listado2=[]
listado3=[]
listado4=[]

palabraLeida=""
palabraActual=""

for i in range(numPalab):
    palabraLeida=input("Diga una palabra: ")
    listadoPalabras1.append(palabraLeida)

for i in range(numPalab):
    palabraLeida=input("Diga una palabra: ")
    listadoPalabras2.append(palabraLeida)

print(listadoPalabras1)
print(listadoPalabras2)

for i in range(len(listadoPalabras1)):
    palabraActual=listadoPalabras1[i]
    for j in range(len(listadoPalabras1)):
        if palabraActual==listadoPalabras2[j]:
            listado1.append(palabraActual)

for i in range(len(listadoPalabras1)):
    palabraActual=listadoPalabras1[i]
    if palabraActual not in listadoPalabras2:
        listado2.append

for i in range(len(listadoPalabras2)):
    palabraActual=listadoPalabras2[i]
    if palabraActual not in listadoPalabras1:
        listado3.append

