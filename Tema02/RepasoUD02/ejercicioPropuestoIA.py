clases = ("Yoga", "Crossfit", "Pilates")
clientes = {"Juan Pérez": set(), "Cristian Villalba": set(), "Ángel Naranjo": set()}
opcion = 0
print("Bienvenido, elija una opción:")

while opcion != 3:
    opcion = int(
        input(
            "1. Apuntar cliente a una clase\n2. Ver las clases de un cliente\n3. Salir\n"
        )
    )
    match opcion:
        case 1:
            cliente = input("Diga el nombre del cliente: ")
            clase = input("Diga la clase a apuntar: ")
            if clase not in clases:
                print("error, la clase no existe")
            elif cliente not in clientes:
                clientes[cliente] = {clase}
                print("Cliente nuevo registrado, clase agregada")
            else:
                clientes[cliente].add(clase)
                print("Clase agregada al cliente")

        case 2:
            cliente = input("Diga el nombre del cliente: ")
            if cliente not in clientes:
                print("No existe el cliente")
            else:
                print(clientes[cliente])

        case 3:
            print("Saliendo del programa")

        case _:
            print("Error, opción no válida")

print("Adiós")
