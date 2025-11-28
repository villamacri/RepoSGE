
f = open("ejercicio01/ejemplo.txt", "w")


for linea in range (0,10):
    f.write(f"linea {linea+1}\n\n")
    f.close

f = open("ejercicio01/ejemplo.txt", "r")
cont=0
for linea in f:
    if f.readline() is not None :
        cont+=1
print(f"El fichero tiene {cont} lineas escritas.")