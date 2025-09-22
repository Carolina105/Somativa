import unittest
import main

def soma(a, b):
    return a + b

class TestMinhasFuncoes(unittest.TestCase):


    def test_soma_numeros_positivos(self):
       
        resultado = soma(5, 5)
        self.assertEqual(resultado, 10)

    
    def test_soma_numeros_negativos(self):
        resultado = soma(-1, -1)
        self.assertEqual(resultado, -2)

   
    def test_soma_zero(self):
        resultado = soma(0, 0)
        self.assertEqual(resultado, 0)


if __name__ == '__main__':
    unittest.main()
