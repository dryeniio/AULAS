class Aviao:
    fabricante = 'EMBRAER'
    modelo = 'E195-E2'
    operador = 'AZUL LINHAS AÉREAS'
    matricula = 'PS-KSB'
    rota = 'FEN - REC'
    
    def alterar_rota(self, rota):
        old_rota = self.rota
        self.rota = rota
        print(f'Trecho alterado de {old_rota} para {rota} com SUCESSO!')
        
    def alterar_matricula(self, matricula):
        old_mat = self.matricula
        self.matricula = matricula
        print(f'Mátricula alterada de {old_mat} para {matricula} com SUCESSO!')
        