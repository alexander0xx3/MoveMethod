import unittest
from cliente import Cliente
from orden import Orden
from item import Item

class TestItem(unittest.TestCase):
    def test_calcular_subtotal(self):
        item = Item(precio=100, cantidad=2)
        self.assertEqual(item.calcular_subtotal(), 200)

class TestOrden(unittest.TestCase):
    def test_calcular_total(self):
        items = [Item(100, 2), Item(200, 1)]
        orden = Orden(items)
        self.assertEqual(orden.calcular_total(), 400)

class TestCliente(unittest.TestCase):
    def test_obtener_total(self):
        items = [Item(100, 2), Item(200, 1)]
        orden = Orden(items)
        cliente = Cliente("Ana", orden)
        self.assertEqual(cliente.obtener_total(), 400)

if __name__ == '__main__':
    unittest.main()
