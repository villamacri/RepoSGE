f=open("ejercicio03/origen.txt", "w")

for linea in range(0,10):
    f.write(f"linea {linea}\n")
f.close

f1=open("ejercicio03/origen.txt", "r")
f2=open("ejercicio03/copia.txt", "a")

lista=f1.readlines()

for linea in lista:
    f2.write(linea+"\n")

f1.close
f2.close