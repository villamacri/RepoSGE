def validar_tamano(func):
    def wrapper(self, tamanoMl, *args, **kwargs):
        if tamanoMl < 50:
            raise ValueError(f"Tamaño insuficiente ({tamanoMl}ml). El mínimo es 50ml.")
        return func(self, tamanoMl, *args, **kwargs)

    return wrapper


def comprobarYogur(func):
    def wrapper(self, *args, **kwargs):
        if not getattr(self, "es_fermentado", False):
            print("Aviso: Esto es un postre lácteo, no un yogur real.")
        return func(self, *args, **kwargs)

    return wrapper


class YogurNormal:
    caloriasBasePor100Ml = 120.5

    def __init__(self, sabor: str, marca: str, conTrocitos: bool):
        self.sabor = sabor
        self.marca = marca
        self.conTrocitos = conTrocitos
        self.es_fermentado = True

    @validar_tamano
    @comprobarYogur
    def calcularCalorias(self, tamanoMl: float) -> float:
        return (tamanoMl * self.caloriasBasePor100Ml) / 100

    def __eq__(self, otro):
        if not isinstance(otro, YogurNormal):
            return False

        return self.calcularCalorias(125) == otro.calcularCalorias(125)


class YogurDesnatado(YogurNormal):
    def __init__(self, sabor, marca, conTrocitos, reduccionPorcentaje: float):
        super().__init__(sabor, marca, conTrocitos)
        self.reduccionPorcentaje = reduccionPorcentaje

    def calcularCalorias(self, tamanoMl: float) -> float:
        caloriasNormal = super().calcularCalorias(tamanoMl)
        return caloriasNormal - (caloriasNormal * self.reduccionPorcentaje / 100)


class PostreProteinas(YogurNormal):
    def __init__(self, sabor, marca, conTrocitos, extraProteinaKcal: float):
        super().__init__(sabor, marca, conTrocitos)
        self.extraProteina = extraProteinaKcal

    def calcularCalorias(self, tamanoMl: float) -> float:
        return super().calcularCalorias(tamanoMl) + self.extraProteina


class ContadorCalorias:
    @staticmethod
    def contarUno(yogur, tamanoMl):
        return yogur.calcularCalorias(tamanoMl)

    @staticmethod
    def contarConjunto(yogures):
        total = 0
        for y, t in yogures:
            total += y.calcularCalorias(t)
        return total

    @staticmethod
    def contarPorTipo(yogures, tipo):
        total = 0
        for y, t in yogures:
            if isinstance(y, tipo):
                total += y.calcularCalorias(t)
        return total
