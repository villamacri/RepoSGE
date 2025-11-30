def filtrar_calorias(lista_comidas, max_calorias):
    if not lista_comidas:
        return []
    
    return [comida for comida in lista_comidas if comida[1] <= max_calorias]


if __name__ == "__main__":
    comidas = [
        ("Ensalada", 150),
        ("Pizza", 800),
        ("Manzana", 95),
        ("Hamburguesa", 600),
        ("Yogur", 120)
    ]
    
    resultado = filtrar_calorias(comidas, 200)
    print("Comidas con máximo 200 calorías:")
    for comida in resultado:
        print(f"  - {comida[0]}: {comida[1]} calorías")
    
    print("\nPrueba con lista vacía:", filtrar_calorias([], 100))