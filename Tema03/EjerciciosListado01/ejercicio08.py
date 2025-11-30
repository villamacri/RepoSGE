def maraton_series(horas):
    dias = horas // 24
    horas_restantes = horas % 24
    return (dias, horas_restantes)


if __name__ == "__main__":
    resultado1 = maraton_series(27)
    print(f"27 horas → {resultado1}")
    
    resultado2 = maraton_series(50)
    print(f"50 horas → {resultado2}")
    
    resultado3 = maraton_series(24)
    print(f"24 horas → {resultado3}")
    
    resultado4 = maraton_series(15)
    print(f"15 horas → {resultado4}")