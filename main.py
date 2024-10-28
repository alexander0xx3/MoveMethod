from cliente import Cliente
from orden import Orden

# Ejemplo de items en la orden
items = [{'precio': 100, 'cantidad': 2}, {'precio': 200, 'cantidad': 1}]
orden = Orden(items)
cliente = Cliente("Ana", orden)

# Imprimir el total de la orden
print(cliente.obtener_total())  # Debería imprimir 400
