import sys
import unittest

# Adicionando o diretório pai ao sys.path
sys.path.append('../') 

from app import create_app

class TestRoutes(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app()
        cls.client = cls.app.test_client()

    def test_hello_route(self):
        response = self.client.get('/api/hello')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Hello, World!"})

if __name__ == '__main__':
    unittest.main(verbosity=2)
