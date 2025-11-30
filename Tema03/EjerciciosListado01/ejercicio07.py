def modo_avion(texto, activar=True):
    if activar:
        return f"[MODO AVIÓN] {texto}"
    else:
        return texto


if __name__ == "__main__":
    mensaje = "Tienes un mensaje nuevo"
    
    print("Con modo avión activado:")
    print(modo_avion(mensaje))
    
    print("\nCon modo avión desactivado:")
    print(modo_avion(mensaje, False))
    
    print("\nPor defecto (sin especificar):")
    print(modo_avion("Llamada entrante"))