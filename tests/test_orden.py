import unittest
from cliente import Cliente
from orden import Orden

class TestOrden(unittest.TestCase):
    def test_calcular_total(self):
        items = [{'precio': 100, 'cantidad': 2}, {'precio': 200, 'cantidad': 1}]
        orden = Orden(items)
        self.assertEqual(orden.calcular_total(), 400)

class TestCliente(unittest.TestCase):
    def test_obtener_total(self):
        items = [{'precio': 100, 'cantidad': 2}, {'precio': 200, 'cantidad': 1}]
        orden = Orden(items)
        cliente = Cliente("Ana", orden)
        self.assertEqual(cliente.obtener_total(), 400)

if __name__ == '__main__':
    unittest.main()
