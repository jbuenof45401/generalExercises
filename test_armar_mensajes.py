from unittest import TestCase
import condicionales as f

class TestArmar_mensajes(TestCase):
    def test_armar_mensajes(self):
        self.assertEqual(f.armar_mensajes(-30),'El numero es negativo')
        self.assertEqual(f.armar_mensajes(30), 'El numero es positivo')
