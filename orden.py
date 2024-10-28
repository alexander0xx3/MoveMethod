from item import Item

class Orden:
    def __init__(self, items):
        self.items = items

    def calcular_total(self):
        return sum(item.calcular_subtotal() for item in self.items)
