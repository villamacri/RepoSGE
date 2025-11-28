palabLeida=input("Diga una palabra: ")
conversion=[]
i=0
esIsograma=True
elementoActual=""

conversion=list(palabLeida)

while i < len(conversion) and esIsograma:
    if conversion[i] in conversion[i+1:]:
        esIsograma=False
    i += 1

if esIsograma:
    print(f"{palabLeida} es un isograma.")
else:
    print(f"{palabLeida} no es isograma.")