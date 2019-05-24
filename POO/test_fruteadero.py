from unittest import TestCase
from POO.Fruteadero import Frutas,Fruteadero,Jugo


class TestFruteadero(TestCase):
    def testFrutas(self):
        #Prueba Frutas
        mi_fruta = Frutas("banano",False,100)

        #Prueba pelar la fruta
        self.assertRaises(ValueError,mi_fruta.cortar,1)
        espero = True;
        obtengo = mi_fruta.pelar();
        self.assertEqual(obtengo,espero);
        self.assertRaises(ValueError,mi_fruta.pelar)

        #Cortar
        espero = 3
        obtengo = mi_fruta.cortar(1)
        self.assertEqual(espero,obtengo)
        #Licuar
        espero = 100
        obtengo = mi_fruta.licuar(1)
        self.assertEqual(espero,obtengo)


