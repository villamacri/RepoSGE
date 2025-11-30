def dibujar_cuadrados(num):
    for i in range(num):
        linea = ""
        for j in range(num):
            linea += "* "
        for j in range(num):
            linea += "  "
        print(linea)

    for i in range(num):
        linea = ""
        for j in range(num):
            linea += "  "
        for j in range(num):
            linea += "* "
        print(linea)

num = int(input("Escriba un número entero positivo: "))
dibujar_cuadrados(num)