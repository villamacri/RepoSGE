import math
class Figura:
    def calcularArea(self):
        pass

    def calcularPerimetro(self):
        pass
    
    def aumentarTamanio(self, tamanio):
        pass

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base=base
        self.altura=altura
    
    def calcularArea(self):
        return self.base*self.altura
    
    def calcularPerimetro(self):
        return 2*(self.base + self.altura)

class Triangulo(Figura):
    def __init__(self, base, altura, lado2, lado3):
        self.base=base
        self.altura=altura
        self.lado2=lado2
        self.lado3=lado3

    def calcularArea(self):
        return (self.base * self.altura) / 2
    
    def calcularPerimetro(self):
        return self.base + self.lado2 + self.lado3
    
    def aumentarTamanio(self, tamanio):
        self.base *= tamanio
        self.altura *= tamanio
        self.lado2 *= tamanio
        self.lado3 *= tamanio
    

class Circulo(Figura):
    
    def __init__(self, radio):
        self.radio = radio
    
    def calcularArea(self):
        return math.pi*(self.radio ** 2)
    
    def calcularPerimetro(self):
        return 2 * math.pi*self.radio
    
    def aumentarTamanio(self, tamanio):
        self.radio *= tamanio

figuras = [
    Circulo(5),
    Rectangulo(4, 6),
    Triangulo(3, 4, 4, 5),
    Triangulo(5, 6, 6, 7),
    Rectangulo(10, 2)
]

areaTotal = 0
perimetraTotal = 0
mayorTriangulo = None

for f in figuras:
    areaTotal += f.calcularArea()
    perimetraTotal += f.calcularPerimetro()

    if isinstance(f, Triangulo):
        if mayorTriangulo is None or f.calcularArea() > mayorTriangulo.calcularArea():
            mayorTriangulo = f

print(f"Suma de áreas: {areaTotal}")
print(f"Perimetro total: {perimetraTotal}")

if mayorTriangulo:
    print(f"El área del mayor triangulo es: {mayorTriangulo.calcularArea()}")