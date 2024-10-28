from cliente import Cliente
from orden import Orden
from item import Item

items = [Item(100, 2), Item(200, 1)]
orden = Orden(items)
cliente = Cliente("Ana", orden)

print(cliente.obtener_total())  # Debería imprimir 400
