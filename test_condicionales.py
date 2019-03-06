from unittest import TestCase
import condicionales as f

class TestCondicionales(TestCase):
    def test_armar_mensajes(self):
        self.assertEqual(f.armar_mensajes(-30),'El numero es negativo')
        self.assertEqual(f.armar_mensajes(30), 'El numero es positivo')

    def test_compara_edades(self):
        self.assertEqual(f.quien_es_mayor(18,20),'El mayor es el segundo')
        self.assertEqual(f.quien_es_mayor(20, 19), 'El mayor es el primero')
        self.assertEqual(f.quien_es_mayor(20, 20), 'Ambos tienen la misma edad')

    def test_parentesis(self):
        self.assertEqual(f.parentesis('c'), None)
        self.assertEqual(f.parentesis('('), 'El caracter es un parentesis')
        self.assertEqual(f.parentesis(')'), 'El caracter es un parentesis')
        self.assertRaises(ZeroDivisionError, f.division(3, 0))
        self.assertRaises(TypeError,f.parentesis('xa'))
