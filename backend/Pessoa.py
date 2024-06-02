import requests

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        self.dados_obtidos = False  # Inicializando internamente

    def obter_todos_dados(self):
        resposta=requests.get('https://www.w3schools.com/')
        if resposta.ok:
            return "CONECTADO"
        else:
            return "ERRO 404"
