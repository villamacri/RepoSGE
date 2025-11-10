diccionario={}
palabraAgre=""
signAgreg=""
opcion=0
palabrBuscada=""

while opcion==0:
    encontrada=False
    print(f"""Bienvenido, elija una opción:
          0. Para salir.
          1. Para agregar palabra.
          2. Para imprimir diccionario
          3. Buscar una palabra y mostrar su significado.
          """)

    match(opcion):
        case 0:
            print("Saliendo...")
        case 1:
            diccionario[input("Diga la palabra: ")]=input("Diga significado")

        case 2:
            for palabra, significado in diccionario.items():
                print(f"{palabra}: {significado}")
        case 3:
            palabrBuscada=input("Diga la palabra a buscar: ")
            if palabrBuscada in diccionario:
                print(diccionario.get(palabrBuscada))
            else:
                print("Error, la palabra no está en el diccionario")
        case 4:
            palabrBuscada=input("Diga la palabra que quiere modificar: ")

            if palabrBuscada in diccionario:
                diccionario[palabrBuscada]=input("Diga el nuevo significado: ")
            else:
                print("Error, la palabra no está en el diccionario")
                

        