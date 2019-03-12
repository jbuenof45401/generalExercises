import unittest
import condicionales as f

class TestCondicionales(unittest.TestCase):
    def condicionales(self):
        self.assertEqual(f.armar_mensajes(-30),'El numero es negativo')
        self.assertEqual(f.armar_mensajes(30), 'El numero es positivo')
        self.assertRaises(TypeError,f.armar_mensajes('asd'))

        self.assertEqual(f.quien_es_mayor(18,20),'El mayor es el segundo')
        self.assertEqual(f.quien_es_mayor(20, 19), 'El mayor es el primero')
        self.assertEqual(f.quien_es_mayor(20, 20), 'Ambos tienen la misma edad')

        self.assertEqual(f.saludo_segun_hora(1),'sidjasid')
        self.assertRaises(TypeError,f.saludo_segun_hora('bca'))
        self.assertEqual(f.saludo_segun_hora(12),'buenas tardes')
        self.assertEqual(f.saludo_segun_hora(19),'buenas noches')


        self.assertEqual(f.parentesis('c'), None)
        self.assertEqual(f.parentesis('('), 'El caracter es un parentesis')
        self.assertEqual(f.parentesis(')'), 'El caracter es un parentesis')
        self.assertRaises(TypeError, f.parentesis('asASDd'))
        with self.assertRaises(TypeError):
            f.parentesis('231233')




if __name__ == 'main':
    unittest.main()

