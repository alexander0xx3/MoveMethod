class Item:
    def __init__(self, precio, cantidad):
        self.precio = precio
        self.cantidad = cantidad

    def calcular_subtotal(self):
        return self.precio * self.cantidad
