def verificar_secuencia(cuantos):
    numeros = []
    for i in range(cuantos):
        num = int(input(f"Diga el número {i+1}: "))
        numeros.append(num)
        
        if i > 0 and num <= numeros[i-1]:
            print(f"¡Cuidado! El número {num} no es mayor que el anterior ({numeros[i-1]}).")

cuantos = int(input("¿Cuántos números va a introducir? "))
verificar_secuencia(cuantos)