from unittest import TestCase
from POO.introPOO import Casa

class TestCasa(TestCase):
    def test__repr__(self):
        self.assertEqual(Casa('Avenida siempre viva, springfield'), 'Casa ubicada en Avenida siempre viva, springfield')
    def test__init__(self):
        self.fail()
    def test__eq__(self):
        self.fail()
