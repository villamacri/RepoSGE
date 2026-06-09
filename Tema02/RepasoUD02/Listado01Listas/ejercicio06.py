palabras = []
i = 0
num = int(input("Diga cuantas palabras quiere agregar: "))

while i < num:
    i += 1
    palabra = input("Diga la palabra: ")
    palabras.append(palabra)

print(palabras)

palabraBuscada = input("Diga la palabra que quiere cambiar: ")

palabraNueva = input("Diga la palabra por la que quiere sustituir: ")

for i in range(len(palabras)):
    if palabras[i] == palabraBuscada:
        palabras[i] = palabraNueva

print(palabras)