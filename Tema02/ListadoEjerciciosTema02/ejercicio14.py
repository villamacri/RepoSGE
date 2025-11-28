palabLeida=input("Diga una palabra: ")
conversion=[]
esPalindromo=True

conversion=list(palabLeida)

i = 0
while i < len(conversion)//2 and esPalindromo:
    if conversion[i] != conversion[len(conversion)-1-i]:
        esPalindromo=False
    i += 1
if esPalindromo is True:
    print(f"La palabra {palabLeida} es un palíndromo")
else:
        print(f"La palabra {palabLeida} no es un palíndromo")