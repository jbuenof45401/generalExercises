from unittest import TestCase
import condicionales as f

class TestArmar_mensajes(TestCase):
    def test_armar_mensajes(self):
        self.assertEqual(f.armar_mensajes(-30),'El numero es negativo')
        self.assertEqual(f.armar_mensajes(30), 'El numero es positivo')
        self.assertEqual(f.quien_es_mayor(18,20),'El mayor es el segundo')
        self.assertEqual(f.quien_es_mayor(20, 19), 'El mayor es el primero')
        self.assertEqual(f.quien_es_mayor(20, 20), 'Ambos tienen la misma edad')