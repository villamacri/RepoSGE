import datetime

f = open("ejercicio02/ejemplo.txt", "w")
for linea in range(0,10):
    f.write(f"linea {linea+1}\n")
f.close

f = open("ejercicio02/ejemplo.txt", "a")

for linea in f:
    f.write(f"{datetime.datetime.now}")
f.close