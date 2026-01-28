class yogurNormal:
    def __init__(self, sabor, marca, troci):
        self.sabor=sabor
        self.marca=marca
        self.troci=troci
        
    def calcularCalorias(self, cantMl, cantAdic=0):
        calorias=120.5
        return (cantMl*calorias)/100
    
class yogurDesnatado(yogurNormal):
    def calcularCalorias(self, cantMl, cantAdic=0):
        porc=30.0
        return super().calcularCalorias(cantMl)-((super().calcularCalorias(cantMl)*porc)/100)

class postreProt(yogurNormal):
    def calcularCalorias(self, cantMl, cantAdic=0):
        return super().calcularCalorias(cantMl)+cantAdic

class contarCalorias:
    def contarCalorias(self, yogurPas, cantMl):
        return yogurPas.calcularCalorias(cantMl)
    
    def contarVarios(self, listadoYogur, cantMl, cantAdic):
        totalCal=0.0
        for yogur in listadoYogur:
            totalCal+=yogur.calcularCalorias(cantMl, cantAdic)
        return totalCal
    
    def calcularPorTipo(self, listadoYogur, tipo, cantMl, cantAdic):
        totalCal=0.0
        for yogur in listadoYogur:
            if isinstance(yogur, tipo):
                totalCal+=yogur.calcularCalorias(cantMl, cantAdic)
        return totalCal


yogur1=yogurDesnatado("Fresa", "Danone", True)
yogur2=yogurNormal("Limón", "Puleva", True)
yogur3=postreProt("Coco", "Danone", True)
yogur4=postreProt("Coco", "Danone", True)
opVarias=contarCalorias()
yogures=[
    yogur1,
    yogur2,
    yogur3,
    yogur4,
]

print(f"El yogur de fresa tiene {opVarias.contarCalorias(yogur1, 200.0)}")
print(f"Las calorías totales son de {opVarias.contarVarios(yogures, 400.0, 200.0)}")
print(f"Las calorías de los yogures proteícos son {opVarias.calcularPorTipo(yogures, postreProt, 300.0, 30.0)}")