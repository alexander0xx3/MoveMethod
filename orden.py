class Orden:
    def __init__(self, items):
        self.items = items

    def calcular_total(self):
        return sum(item['precio'] * item['cantidad'] for item in self.items)
