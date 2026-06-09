num = int(input("Diga el numero de palabras que quiere agregar: "))
palabras = []
palabra = ""
i = 0

while i < num:
    i += 1
    palabra = input("Diga una palabra: ")

    palabras.append(palabra)

for j, palabra in enumerate(palabras):
    print(j + 1, palabra)
