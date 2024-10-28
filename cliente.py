from orden import Orden

class Cliente:
    def __init__(self, nombre, orden):
        self.nombre = nombre
        self.orden = orden

    def obtener_total(self):
        return self.orden.calcular_total()
