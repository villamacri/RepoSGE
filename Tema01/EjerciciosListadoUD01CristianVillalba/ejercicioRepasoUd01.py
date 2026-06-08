#Ejercicio01
print('hola mundo')

#Ejercicio02
num1 = 5
num2 = 8.4
print(num1+num2)

#Ejecicio03
val = 100
iva = 21
cien = 100

precioFinal = val*(iva/cien)
print(precioFinal)

#Ejercicio04
num1 = 7
num2 = 9

if (num1 > num2):
    print(f'El mayor es {num1}')
    
else:
    print(f'el mayor es {num2}')
    
#Ejercicio05
num=9

if (num > 0 and num < 10):
    print(f'{num} está entre 0 y 10')
else:
    print('Él número no se encuentra entre 0 y 10')

#Ejercicio06
num=15

if (num >= 0 and num <= 10):
    print(f'{num} está entre 0 y 10')
elif (num >= 10 and num <= 20):
    print(f'{num} está entre 11 y 21')
elif (num >= 20 and num <= 30):
    print(f'{num} está entre 21 y 30')
else:
    print('Él número no se encuentra entre 0 y 10, 11 y 20 o 21 y 30')
    
#Ejercicio07
num = 0
while num != 100:
    num+=1
    print(f'{num}')

#Ejercicio08
for num in range(0, 100):
    print(f'{num+1}')
    
#Ejercicio09
listadoPalabras=[]
opcion = 'S'

while opcion is 'S':
    palabra= input('Diga una palabra: ')
    listadoPalabras.append(palabra)
    opcion= input('¿Desea introducir otra palabra? S/N:')
    if opcion not in 'SN':
        print('Respuesta desconocida, se volverá a pedir una palabra')
        opcion = 'S'
        continue
print('Inserción finalizada, se imprimirá el listado:')
for palabra in listadoPalabras:
    print(palabra)

#Ejercicio10
listadoNumeros=[]
opcion = 'S'

while opcion is 'S':
    numero= int(input('Diga un número: '))
    listadoNumeros.append(numero)
    opcion= input('¿Desea introducir otro número? S/N:')
    if opcion not in 'SN':
        print('Respuesta desconocida, se volverá a pedir una palabra')
        opcion = 'S'
        continue
print('Inserción finalizada, se imprimirá el listado:')
for numero in listadoNumeros:
    print(numero)