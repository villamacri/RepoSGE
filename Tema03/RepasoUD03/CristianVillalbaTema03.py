def comprobarCombustible(func):
    def wrapper(turismo, cantFij=50.0):
        if turismo.tipoCombustible == "gasolina" or turismo.tipoCombustible == "diesel":
            turismo.precioBase+=cantFij
            return func
    return wrapper
        

class Vehiculo:
    def __init__(self, matricula, marca, tipoCombustible, velMax, diasRev, precioBase):
        self.matricula=matricula
        self.marca=marca
        self.tipoCombustible=tipoCombustible
        self.velMax=velMax
        self.diasRev=diasRev
        self.precioBase=precioBase
    
    def calcularPrecio(self):
        pass

class Turismo(Vehiculo):
    def __init__(self, matricula, marca, tipoCombustible, velMax, diasRev, precioBase):
        super().__init__(matricula, marca, tipoCombustible, velMax, diasRev, precioBase)
    
    @comprobarCombustible
    def calcularPrecio(self):
        return self.precioBase

class Camion(Vehiculo):
    def __init__(self, capac, matricula, marca, tipoCombustible, velMax, diasRev, precioBase):
        self.capac=capac
        super().__init__(matricula, marca, tipoCombustible, velMax, diasRev, precioBase)
        
    def calcularPrecio(self, cantFija=5.0):
        return self.precioBase+(self.capac*cantFija)

class Furgoneta(Camion, Turismo):
    def __init__(self, esAlquiler, capac, matricula, marca, tipoCombustible, velMax, diasRev, precioBase, cantFija=20):
        self.esAlquiler=esAlquiler
        super().__init__(capac, matricula, marca, tipoCombustible, velMax, diasRev, precioBase, cantFija)
    
    def calcularPrecio(self, cantFija=20):
        return super().calcularPrecio(cantFija)+super().calcularPrecio(cantFija=0)
    
class EstacionITV:
    def calcularTotalVehiculos(self, listaVehiculos=[]):
        totalRec=0.0
        for v in listaVehiculos:
            totalRec+=v.calcularPrecio()
        return totalRec
    
    def cambiarVelMax(self, nuevaVel, listaVehiculos=[]):
        for v in listaVehiculos:
            v.velMax=nuevaVel

    def contarVehiculos(self, listaVehiculos=[]):
        num=len(listaVehiculos)
        return num
    
    def __enter__(self, listaVehiculos=[], dias=0):
        for v in listaVehiculos:
            v.diasRev=dias


v1=Turismo("1111A", "Toyota", "gasolina", 160, 15, 200.0)
v2=Turismo("1111B", "Citroen", "diesel", 130, 25, 250.0)
v3=Camion(300, "2222A", "Renault", "gasolina", 160, 10, 150.0)
v4=Camion(400, "2222B", "SEAT", "gasolina", 180, 20, 250.0)
#v5=Furgoneta( True, 150, "3333A", "Renault", "gasolina", 180, 5, 200.0)
#v6=Furgoneta(False, 200, "3333B", "Citroen", "diesel", 180, 5, 200.0)

op=EstacionITV()
listaVehiculos=[v1, v2, v3, v4]
    
velNueva=0
opcion=1

while opcion!=0:
    print("""
          Elija una opción:
          
          0. Para salir
          1. Calcular un vehiculo
          2. Calcular el total
          3. Cambiar la velocidad máxima
          4. Contar vehículos.
          5. Reiniciar dias
          """)
    opLeida=int(input(""))
    
    match(opLeida):
        case 0:
            print("Saliendo...")
            opcion=0
        case 1:
            print("Diga un vehículo: 1. Para Turismo gasolina\n2. Para Turismo diesel\n3. Para Camión Renault\n4 Para Camión Seat")
            opLeida=int(input(""))
            
            match(opLeida):
                case 1:
                    print(f"El precio del vehículo es {v1.calcularPrecio}€")
                
                case 2:
                    print(f"El precio del vehículo es {v2.calcularPrecio}€")
                case 3:
                    print(f"El precio del vehículo es {v3.calcularPrecio}€")
                case 4:
                    print(f"El precio del vehículo es {v4.calcularPrecio}€")
        case 2:
            print(f"El precio total es de {op.calcularTotalVehiculos(listaVehiculos)}")
            
        case 3:
            print("Diga nueva velocidad")
            velNueva=int(input(""))
            
            op.cambiarVelMax(velNueva, listaVehiculos)
            
        case 4:
            print(f"Hay {op.contarVehiculos(listaVehiculos)} vehículos")
            
        case 5:
            op.__enter__(listaVehiculos)