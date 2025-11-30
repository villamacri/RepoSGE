def ordenar_numeros(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort()
    return numeros

num1 = int(input("Escriba el primer número: "))
num2 = int(input("Escriba el segundo número: "))
num3 = int(input("Escriba el tercer número: "))

resultado = ordenar_numeros(num1, num2, num3)
print(f"Los números ordenados son: {resultado}")