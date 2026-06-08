def comprobarMedida(func):
    def wrapper(self, other):
        if other.medida is "GRANDE":
            self.precioBase+=(self.precioBase*(5/100))
            return func
    return wrapper

class Pedido:
    def __init__(self, precioBase:float, cant:int, medida:str, distancia:float):
        self.precioBase=precioBase
        self.cant=cant
        self.medida=medida
        self.distancia=distancia
        
    @comprobarMedida
    def calcularPrecio(self, precioBulto):
        return self.cant*(self.precioBase+precioBulto)
    
class PedidoPersonalizado(Pedido):
    def __init__(self, precioBase, cant, medida, distancia):
        super().__init__(precioBase, cant, medida, distancia)
        
    def calcularPrecio(self, precioBulto, exPers):
        return super().calcularPrecio(precioBulto)+exPers
    
class PedidoUrgente(Pedido):
    def __init__(self, precioBase, cant, medida, distancia):
        super().__init__(precioBase, cant, medida, distancia)
        
    def calcularPrecio(self, precioBulto, porcUrg):
        return super().calcularPrecio(precioBulto)+(super().calcularPrecio(precioBulto)*(porcUrg/100))
    
class GestionPedidos:
    
    def contarPorMedida(self, medBuscada:str, pedidos):
        cont=0
        for p in pedidos:
            if p.medida is medBuscada:
                cont+=1
        return cont 