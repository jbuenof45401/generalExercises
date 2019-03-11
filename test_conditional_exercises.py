import unittest
import conditional_exercises as f


class test_conditional_exercises(unittest.TestCase):
    def edad_minima(self):
        self.assertTrue(f.edad_minima(1),"")

if __name__ == '__main__':
    unittest.main()
