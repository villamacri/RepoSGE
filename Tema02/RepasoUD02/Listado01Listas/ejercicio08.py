lista1 = []
lista2 = []
i = 0
j = 0
num = int(input("Diga cuantas palabras va a agregar a la primera lista: "))

while i < num:
    i += 1
    palabra = input("Diga la palabra: ")
    lista1.append(palabra)

num = int(input("Diga cuantas palabras va a agregar a la segunda lista: "))
while j < num:
    j += 1
    palabra = input("Diga la palabra: ")
    lista2.append(palabra)
lista1 = [palabra for palabra in lista1 if palabra not in lista2]

print(lista1)
