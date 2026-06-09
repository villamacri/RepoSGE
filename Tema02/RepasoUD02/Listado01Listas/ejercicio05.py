palabras = []
i = 0
num = int(input("Diga cuantas palabras quiere agregar: "))

while i < num:
    i += 1
    palabra = input("Diga la palabra: ")
    palabras.append(palabra)

print(palabras)

palabraBuscada = input("Diga la palabra que quiere contar: ")

print(f'La palabra aparece {palabras.count(palabraBuscada)} veces')