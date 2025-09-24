class Aviao:
    
    fabricante = ''
    modelo = ''
    operador = ''
    matricula = ''
    rota = ''
    
    def criar_aviao(self, fabricante, modelo, operador, matricula):
        self.fabricante = fabricante
        self.modelo = modelo
        self.operador = operador
        self.matricula = matricula
    
    def alterar_rota(self, rota):
        self.rota = rota
    
    def alterar_operador(self, operador):
        self.operador = operador

    def exibir_dados(self):
        print(f'Avião: {self.modelo} | Matrícula: {self.matricula} | Rota: {self.rota} | Operador: {self.operador}')