class yogurNormal:
    def __init__(self, sabor, marca, troci):
        self.sabor=sabor
        self.marca=marca
        self.troci=troci
        
    def calcularCalorias(cantMl):
        calorias=120.5
        return (cantMl*calorias)/100
    
class yogurDesnatado(yogurNormal):
    def calcularCalorias(cantMl):
        porc=30.0
        return super().calcularCalorias()-((super().calcularCalorias*porc)/100)

class postreProt(yogurNormal):
    def calcularCalorias(cantMl, cantAdic):
        return super().calcularCalorias()+cantAdic

class contarCalorias:
    def contarCalorias(yogurPas):
        return yogurPas.calcularCalorias()
    
    def contarVarios(listadoYogur, cantMl, cantAdic):
        totalCal=0.0
        for yogur in listadoYogur:
            totalCal+=yogur.calcularCalorias(cantMl, cantAdic)
        return totalCal
    
    def calcularPorTipo(listadoYogur, tipo, cantMl, cantAdic):
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

print(f"El yogur de fresa tiene {yogur1.calcularCalorias()}")
print(f"Las calorías totales son de {opVarias.contarVarios(yogures, 400.0, 200.0)}")