import unittest
from calculadora import soma

class TesteCalculadora(unittest.TestCase):
    def test_soma_de_numeros_positivos(self):
        self.assertEqual(soma(5, 5), 10)

    def test_soma_de_um_numero_negativo_e_um_positivo(self):
        self.assertEqual(soma(-5, 5), 0)

    def test_soma_de_varias_entradas(self):
        entradas = [
            (10, 10, 20),
            (5, 5, 10),
            (1.5, 1.5, 3),
            (-5, 5, 0),
            (100, 100, 200)
        ]
        for entradas in entradas:
            with  self.subTest(entradas=entradas):
                x,y,saida=entradas
                self.assertEqual(soma(x,y),saida)

    
    def test_soma_x_nao_e_int_ou_float_deve_voltar_assertionerror(self):
        with self.assertRaises(AssertionError):
            soma("11",0)


if __name__ == '__main__':
    unittest.main()
