import unittest
from backend.Unitest2.baconcomovos import bacon_com_ovos

class TestBaconComOvos(unittest.TestCase):
    def test_bacon_com_ovos_dev_levantar_assertionerror_se_int_vazio(self):
        with self.assertRaises(AssertionError):
            bacon_com_ovos("não é um inteiro")

    def test_bacon_com_ovos_deve_retorna_se_a_entrada_for_mult3e5(self):
        entradas = (15, 30, 45, 60)
        saida = 'Bacon com ovos'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida, msg=f'{entrada} nao retornou {saida}')

    def test_bacon_com_ovos_deve_retorna_se_a_entrada_nao_for_mult3e5(self):
        entradas = (3,2,7,8)
        saida = 'passar fome'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida, msg=f'{entrada} nao retornou {saida}')

if __name__ == '__main__':
    unittest.main(verbosity=2)
