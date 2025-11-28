import random

#Teniendo en cuenta el número de transacciones que hay semanalmente (leido por teclado) en nuestra aplicación de compra y venta de libros, necesatimos:
# 1. Calcular el número y la media total de transacciones.(Se rellena lista mediante aleatorio)
# 2. La media del número de transacciones que se realizan en cada género en un día.
# 3. El género más vendido (es decir al que menos transacciones se le realizan)
# 4. El género menos vendido (es decir al que más transacciones se le realizan)
# 5. Mostrar todos los géneros con mas rentabilidad (mayor número de transacciones) que la media.

#1

topeMin=0
topeMax=60
diasSemana=7
mediaTransacc: 0.0

listadoGeneros = ["Fantasía", "Histórico", "Romance", "Ciencia Ficción", "Terror", "Romantasy"]
listadoTransacciones=[]

for i in range(len(listadoGeneros)):
    listadoTransacciones.append(random.randint(topeMin, topeMax))

mediaTransacc=sum(listadoTransacciones)/len(listadoGeneros)

print(f"Las transacciones totales son {sum(listadoTransacciones)} y la media es de {mediaTransacc:.2f}.")

#2
for genero, transaccion in zip(listadoGeneros, listadoTransacciones):
    print(f"Media {genero}:\n{(transaccion/diasSemana):.2f}")

#3
print("El género más vendido es/son:")
for genero, transaccion in zip(listadoGeneros, listadoTransacciones):
    if transaccion == max(listadoTransacciones):
        print(f"{genero}: {transaccion}")
#4
print("El género menos vendido es/son:")
for genero, transaccion in zip(listadoGeneros, listadoTransacciones):
    if transaccion == min(listadoTransacciones):
        print(f"{genero}: {transaccion}")

#5
print("Los generos con más rentabilidad son:")
for genero, transaccion in zip(listadoGeneros, listadoTransacciones):
    if mediaTransacc<transaccion :
        print(f"{genero}")