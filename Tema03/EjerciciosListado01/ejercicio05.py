def dibujar_segmentos(m, n):
    linea = ""
    for i in range(n):
        for j in range(m):
            linea += "* "
        if i < n - 1:
            for j in range(m):
                linea += "  "
    return linea

m = int(input("Escriba el tamaño del segmento: "))
n = int(input("Escriba el número de segmentos: "))

resultado = dibujar_segmentos(m, n)
print(resultado)