
# ==========================================
# DEFINICIÓN DE DECORADORES PERSONALIZADOS
# ==========================================
# Decorador para validar el tamaño mínimo de un yogur
def validar_tamano(func):
    """Verifica que el yogur tenga al menos 50g."""
    def wrapper(self, yogur, *args, **kwargs):
        if yogur.tam < 50:
            print(f"AVISO: El yogur {yogur.sabor} de {yogur.marca} es demasiado pequeño ({yogur.tam}g). No se contará.")
            return 0
        return func(self, yogur)
    return wrapper

# Decorador para validar que la marca sea un yogur real
def validar_es_yogur(func):
    """Evita que se procesen 'postres lácteos' como Activia."""
    def wrapper(self, yogur, *args, **kwargs):
        if yogur.marca == "Activia":
            print(f"AVISO: La marca {yogur.marca} no vende yogures, son postres lácteos. No se contará.")
            return 0
        return func(self, yogur)
    return wrapper

# ==========================================
# CLASES Y HERENCIA
# ==========================================
class YogurNormal:
    def __init__(self, sabor, marca, tam, cal=120.5, troz=True):
        self.sabor=sabor
        self.marca=marca
        self.tam=tam     # Atributo nuevo para el tamaño en gramos
        self.cal=cal
        self.troz=troz

    # Método mágico __eq__: Permite usar el operador == entre dos yogures
    # Compara si tienen las mismas calorías base (mismo grupo calórico)
    def __eq__(self, other):
        if isinstance(other, YogurNormal):
            return self.cal == other.cal
        return False
    
class YogurDes(YogurNormal):
    def __init__(self, sabor, marca, tam, cal=120.5, troz=True):
        # Llama al constructor padre reduciendo un 30% las calorías
        super().__init__(sabor, marca, tam, cal-(cal*(30/100)), troz)

class YogurProt(YogurNormal):
    def __init__(self, sabor, marca, tam, calAdic, cal=120.5, troz=True):
        # Llama al constructor padre sumando las calorías adicionales de la proteína
        super().__init__(sabor, marca, tam, cal+calAdic, troz)

# ==========================================
# CLASE OPERACIONES (Con Decoradores)
# ==========================================
class Operaciones:
    # Se aplican las validaciones antes de ejecutar contarCalorias
    # El orden de ejecución de decoradores es de abajo hacia arriba (primero validar_tamano, luego validar_es_yogur)
    @validar_es_yogur
    @validar_tamano
    def contarCalorias(self, yogur):
        # Cálculo: calorias_base * (gramos / 100)
        return yogur.cal*(yogur.tam/100)
    
    # *yogures permite pasar un número variable de argumentos (tupla)
    def contarConjunto(self, *yogures):
        totalCal=0.0
        for yogur in yogures:
            totalCal+=self.contarCalorias(yogur)
        return totalCal
    
    # Filtra por tipo exacto de clase
    def contarPorTipo(self, tipo, *yogures):
        totalCal=0.0
        for yogur in yogures:
            # Usamos 'is' o comparamos tipos para evitar que las subclases cuenten como la clase padre
            if type(yogur) is tipo:
                totalCal+=self.contarCalorias(yogur)
        return totalCal
    
# ==========================================
# CREACIÓN DE INSTANCIAS (OBJETOS)
# ==========================================
# Se crean varios yogures con diferentes valores para probar el sistema
yogur1=YogurNormal("Fresa", "Puleva", 300.0)
yogur2=YogurNormal("Limón", "Puleva", 250.0)
yogur3=YogurDes("Coco", "Asturiana", 200.0)
yogur4=YogurProt("Natural", "Danone", 300.0, 50.0)
yogur5=YogurProt("Vainilla", "Hacendado", 250.0, 30.0)

opcion=1
op = Operaciones()

print("Bienvenido")

# ==========================================
# BUCLE PRINCIPAL DEL MENÚ
# ==========================================
while opcion!=0:
    # input con triple comilla para mostrar el menú formateado
    opLeida=int(input("""Elija una opcion:
0. Para salir
1. Contar calorias de un yogur
2. Contar calorias de todos los yogures
3. Contar calorias de solo un tipo: """))

    match (opLeida):
        case 0:
            print("Saliendo...")
            opcion=0

        case 1:
            opLeida=int(input("""Que yogur quiere calcular:
1. Fresa Normal
2. Limón normal
3. Coco desnatado
4. Natural proteico
5. Vainilla proteico: """))
            # Submenú para elegir un yogur específico
            match (opLeida):
                case 1:
                    print(f"El yogur tiene {op.contarCalorias(yogur1)} calorías")

                case 2:
                    print(f"El yogur tiene {op.contarCalorias(yogur2)} calorías")

                case 3:
                    print(f"El yogur tiene {op.contarCalorias(yogur3)} calorías")

                case 4:
                    print(f"El yogur tiene {op.contarCalorias(yogur4)} calorías")

                case 5:
                    print(f"El yogur tiene {op.contarCalorias(yogur5)} calorías")

        case 2:
            # Llama a contarConjunto pasando todos los yogures desempaquetados como argumentos
            print(f"Las calorías de todos los yogures son {op.contarConjunto(yogur1, yogur2, yogur3, yogur4, yogur5)}")

        case 3:
            opLeida=int(input("""Diga de que tipo quiere calcular:
1. Normales
2. Desnatados
3. Proteicos: """))

            match (opLeida):
                case 1:
                    # Cuenta solo los que son EXACTAMENTE YogurNormal
                    print(f"Los normales tienen {op.contarPorTipo(YogurNormal, yogur1, yogur2, yogur3, yogur4, yogur5)} calorias")

                case 2:
                    # Cuenta solo los YogurDes
                    print(f"Los desnatados tienen {op.contarPorTipo(YogurDes, yogur1, yogur2, yogur3, yogur4, yogur5)} calorias")

                case 3:
                    # Cuenta solo los YogurProt
                    print(f"Los proteicos tienen {op.contarPorTipo(YogurProt, yogur1, yogur2, yogur3, yogur4, yogur5)} calorias")

print("Adiós")