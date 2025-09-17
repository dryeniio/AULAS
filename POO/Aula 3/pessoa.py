class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome_completo = nome + ' ' + sobrenome
    def exibirdados(self):
        print(f'{self.nome_completo}')