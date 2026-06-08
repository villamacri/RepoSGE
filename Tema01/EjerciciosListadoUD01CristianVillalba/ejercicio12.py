import random


numAleatorio = random.randint(0, 10)
numIntentos = 1
acertado = False

numLeido=int(input("Diga un número: "))

while numIntentos < 3 and not acertado:
    numLeido=int(input("Cagaste, prueba de nuevo: "))
    numIntentos += 1
    
    if numAleatorio==numLeido:
        print('wenaa')
        acertado=True
if not acertado:
    print(f"Se acabó. El número era {numAleatorio}")