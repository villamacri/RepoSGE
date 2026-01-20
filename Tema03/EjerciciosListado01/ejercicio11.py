porcLeido=float(input("Diga el porcentaje de la batería: "))
while porcLeido > 100:
    porcLeido=float(input("Incorrecto, diga el porcentaje de la batería: "))    
def estado_bateria(porcentaje):
    if porcentaje >= 80:
        return "Perfecto"
    elif porcentaje >= 30:
        return "Aceptable"
    elif porcentaje >= 10:
        return "Modo ahorro YA"
    else:
        return "Busca un enchufe"
print(estado_bateria(porcLeido))