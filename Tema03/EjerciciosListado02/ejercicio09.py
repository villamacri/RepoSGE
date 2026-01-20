class Droid:
    def __init__(self, modelo, vueltas, kmPorVuelta, totalBajas, derribos):
        self.modelo=modelo
        pass
    
    def calcularDistanciaRecorr():
        pass
    
    def calcularBajasConfirmadas():
        pass
    
class ProtocolDroid(Droid):
    def __init__(self, modelo, vueltas, kmPorVuelta):
        super().__init__(modelo)
        self.vueltas=vueltas
        self.kmPorVuelta=kmPorVuelta
        
    def calcularDistanciaRecorr(vueltas, kmPorVuelta):
        return kmPorVuelta*vueltas

class AstromechDroid(Droid):
    def __init__(self, modelo, totalBajas, derribos):
        super().__init__(modelo)
        self.totalBajas=totalBajas
        self.derribos=derribos
        
    def calcularBajasConfirmadas(totalBajas, derribos):
        return totalBajas-derribos
    
    
class SuperDroid(AstromechDroid, ProtocolDroid):
    def __init__(self, modelo, vueltas, kmPorVuelta, totalBajas, derribos):
        super().__init__(modelo)
        self.vueltas=vueltas
        self.kmPorVuelta=kmPorVuelta
        self.totalBajas=totalBajas
        self.derribos=derribos
    
    def calcularBajasConfirmadas(totalBajas, derribos):
        return super().calcularBajasConfirmadas(derribos)
    
    def calcularDistanciaRecorr(vueltas, kmPorVuelta):
        return super().calcularDistanciaRecorr(kmPorVuelta)
    
class HyperDroid(ProtocolDroid, AstromechDroid):
    def __init__(self, modelo, vueltas, kmPorVuelta, totalBajas, derribos):
        super().__init__(modelo)
        self.vueltas=vueltas
        self.kmPorVuelta=kmPorVuelta
        self.totalBajas=totalBajas
        self.derribos=derribos
        
    def calcularDistanciaRecorr(vueltas, kmPorVuelta):
        return super().calcularDistanciaRecorr(kmPorVuelta)
    
    def calcularBajasConfirmadas(totalBajas, derribos):
        return super().calcularBajasConfirmadas(derribos)
    

    
droides=[
    Droid()
]        