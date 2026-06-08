class Droid:
    def __init__(self, modelo):
        self.modelo = modelo
    
    def calcularDistanciaRecorr(self):
        return 0
    
    def calcularBajasConfirmadas(self):
        return 0
    
class ProtocolDroid(Droid):
    def __init__(self, modelo, vueltas, kmPorVuelta):
        super().__init__(modelo)
        self.vueltas = vueltas
        self.kmPorVuelta = kmPorVuelta
        
    def calcularDistanciaRecorr(self):
        return self.kmPorVuelta * self.vueltas

class AstromechDroid(Droid):
    def __init__(self, modelo, totalBajas, derribos):
        super().__init__(modelo)
        self.totalBajas = totalBajas
        self.derribos = derribos
        
    def calcularBajasConfirmadas(self):
        return self.totalBajas - self.derribos
    
    
class SuperDroid(AstromechDroid, ProtocolDroid):
    def __init__(self, modelo, vueltas, kmPorVuelta, totalBajas, derribos):
        Droid.__init__(self, modelo)
        self.vueltas = vueltas
        self.kmPorVuelta = kmPorVuelta
        self.totalBajas = totalBajas
        self.derribos = derribos
    
class HyperDroid(ProtocolDroid, AstromechDroid):
    def __init__(self, modelo, vueltas, kmPorVuelta, totalBajas, derribos):
        Droid.__init__(self, modelo)
        self.vueltas = vueltas
        self.kmPorVuelta = kmPorVuelta
        self.totalBajas = totalBajas
        self.derribos = derribos
    

droides = [
    ProtocolDroid("C-3PO", 5, 10),
    AstromechDroid("R2-D2", 10, 2),
    SuperDroid("IG-88", 10, 5, 20, 5),
    HyperDroid("BB-8", 20, 2, 5, 1)
]

print(f"{'Modelo':<10} | {'Distancia':<10} | {'Bajas':<10}")
print("-" * 36)

for droid in droides:
    dist = droid.calcularDistanciaRecorr()
    bajas = droid.calcularBajasConfirmadas()
    print(f"{droid.modelo:<10} | {dist:<10} | {bajas:<10}")