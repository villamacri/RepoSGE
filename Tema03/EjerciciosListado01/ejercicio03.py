def verificar_secuencia(tope):
    numeros = []
    for i in range(tope):
        num = int(input(f"Diga el número {i+1}: "))
        numeros.append(num)
    
        if i > 0 and num <= numeros[i-1]:
            print(f"El número {num} es menor que el anterior {numeros[i-1]}.")

tope = int(input("¿Cuántos números va a introducir? "))
verificar_secuencia(tope)