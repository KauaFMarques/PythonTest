import unittest
from unittest.mock import patch
from Pessoa import Pessoa

class TestPessoa(unittest.TestCase):
    def setUp(self):
        self.p1 = Pessoa("Luiz", "Otavio")
    
    def test_pessoa_nome_tem_o_valor_correto(self):
        self.assertEqual(self.p1.nome, "Luiz")

    def test_pessoa_sobrenome_tem_o_valor_correto(self):
        self.assertEqual(self.p1.sobrenome, "Otavio")
    
    def test_pessoa_nome_tem_o_valor_str(self):
        self.assertIsInstance(self.p1.nome, str)

    def test_pessoa_sobrenome_tem_o_valor_str(self):
        self.assertIsInstance(self.p1.sobrenome, str)
        
    def test_pessoa_dados_obtidos_tem_iniciar_false(self):
        self.assertFalse(self.p1.dados_obtidos)

    def obter_todos_dados_ok(self):
        with patch('request.get') as fake_request:
            fake_request.return_value.ok=True

            self.assertEqual("Conectado com sucesso!")

if __name__ == '__main__':
    unittest.main(verbosity=2)
