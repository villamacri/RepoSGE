class Animal:
    def __init__(self, costeDiario):
        self.costeDiario=costeDiario
    
    def calcularCosteAnual(self, dias=365):
        return self.costeDiario*dias

class Osos(Animal):
    def calcularCosteAnual(self, costeAdicional, dias=365):
        diasAdicionales=((4*2)*12)
        return super().calcularCosteAnual(dias)+(costeAdicional*diasAdicionales)
    
class Serpiente(Animal):
    def calcularCosteAnual(self, costeAdicional, dias=365):
        diasAdicionales=((4*2)*12)
        return super().calcularCosteAnual(dias)+(costeAdicional*diasAdicionales)