from unittest import TestCase
from while_for.taller_listas_dic_bucles import ejercicios as e

class Unit_test_taller_corte_3(TestCase):
    def test_suma(self):
        self.assertEqual(e.suma([1,3,6,7],[2,2,5,-3]),[3,5,11,4])
        self.assertEqual(e.suma([1,3,6,7],[1000000,2,5,-3]),[1000001,5,11,4])
        self.assertEqual(e.suma('xxxx','xxxx'),'ingrese un vector con numeros')
    def test_producto_punto(self):
        self.assertEqual(e.producto_punto([1,1,1],[1,1,1]),3)
        self.assertEqual(e.producto_punto([1,1,1],[1,7,-4]),4)
        self.assertRaises(TypeError,e.producto_punto,'x','y')
    def test_mayor_que(self):
        self.assertEqual(e.mayor_elemento([2938,9483,1]),9483)
        self.assertEqual(e.mayor_elemento([-50000,1]),1)
        self.assertRaises(TypeError,e.mayor_elemento(''))
    def test_menor_que(self):
        self.assertEqual(e.menor_elemento([2390293,12932,384]),384)
        self.assertEqual(e.menor_elemento([-2390293,12932,384]),-2390293)
        self.assertRaises(TypeError,e.menor_elemento,'x','x')
    def test_promedio(self):
        self.assertEqual(e.promedio([2,2,2]),2)
        self.assertEqual(e.promedio([-23903,29230,-1]),1775.3333333333333)
        self.assertEqual(e.promedio('y'),'ingrese un vector con numeros')
    def test_desviacion_estandar(self):
        self.assertEqual(e.desviacion_estandar([1,56.3434,343434]),161882.82580105052)
        self.assertEqual(e.desviacion_estandar([2293923.323,-23231.1,0]),1086882.8269586703)
        self.assertRaises(TypeError,e.desviacion_estandar('1'))
    def test_norma(self):
        self.assertEqual(e.norma([431,-4,-1]),426.0)
        self.assertEqual(e.norma([4/2,-4,-1]),3.0)
        self.assertEqual(e.norma(['x','y','z']),'ingrese un vector con numeros')
        self.assertEqual(e.norma('y'),'ingrese un vector con numeros')
    def test_comparar(self):
        self.assertEqual(e.comparar([1,2,3],[4,5,6]),'menor')
        self.assertEqual(e.comparar([1,2,100],[4,5,6]),'mayor')
        self.assertEqual(e.comparar([1,2,100],[14,-5,94]),'igual')
        self.assertEqual(e.comparar([1,2,100],[4,5,94]),'igual')
        self.assertEqual(e.comparar([1,2,100],[4,5,'']),'ingrese un vector con numeros')