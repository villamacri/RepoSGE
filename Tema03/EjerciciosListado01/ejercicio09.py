def mas_procrastina(diccionario_horas):
    if not diccionario_horas:
        return None
    
    max_persona = max(diccionario_horas, key=diccionario_horas.get)
    return max_persona


if __name__ == "__main__":
    procrastinadores = {
        "Ana": 15,
        "Carlos": 23,
        "Elena": 18,
        "David": 30,
        "Beatriz": 12
    }
    
    ganador = mas_procrastina(procrastinadores)
    print(f"Quien más procrastina: {ganador} con {procrastinadores[ganador]} horas")
    
    print("\nPrueba con diccionario vacío:", mas_procrastina({}))