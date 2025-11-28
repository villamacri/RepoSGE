numPedido=int(input("Diga un número: "))
numLeido=""
topeLeido=int(input("Diga cuantos numeros va a introducir: "))
listadoNumeros=[]

for i in range(topeLeido):
    numLeido=int(input("Diga un número: "))
    listadoNumeros[i]=numLeido

def comprobarMayores(numPedido, listadoNumeros):
    cont=0
    for i in listadoNumeros:
        if(listadoNumeros[i]>numPedido):
            cont+=1
    return cont

print(f"Hay {comprobarMayores()} mas grandes que {numPedido}")
