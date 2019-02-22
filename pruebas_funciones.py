import unittest
import ejerciciosIn as f

class pruebas(unittest.TestCase):

    def test_es_vocal(self):
        self.assertTrue(f.siesvocal('x'),print('probando con a'))
        self.assertTrue(f.siesvocal('e'), 'probando con e')
        self.assertTrue(f.siesvocal('i'))
        self.assertTrue(f.siesvocal('o'))
        self.assertTrue(f.siesvocal('u'))
        self.assertTrue(f.siesvocal('aeiou'), 'esto debe votar error')
        self.assertTrue(f.siesvocal('g'))

if __name__ == 'main':
    unittest.main()