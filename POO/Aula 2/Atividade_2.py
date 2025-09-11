#Atividade POO - Enio Enrique #01851994

class Carro:
    def __init__(self,modelo,ano):
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0.0
        self.farol = 0
        self.limpador = 0
    
    def acelerar(self, aceleracao):
        if aceleracao < 0:
            self.velocidade = self.velocidade - aceleracao
        else:
            self.velocidade = self.velocidade + aceleracao
        
    def freiar(self,aceleracao):
        if aceleracao > 0:
            self.velocidade = self.velocidade - aceleracao
        else:
            self.velocidade = self.velocidade + aceleracao
            
        if self.velocidade < -10.0:
            self.velocidade = -10.0
        
    def alternarFarol(self):
        if self.farol == 0:
            self.farol = 1
        else:
            self.farol = 0
            
    def alternarLimpador(self):
        if self.limpador == 0:
            self.limpador = 1
        else:
            self.limpador = 0



print(f'------------------------------------')
print(f'Bem vindo ao programa do carrinho ;)')
print(f'------------------------------------')
print(f'POO - ENIO ENRIQUE #01851994')
print(f'------------------------------------')

menu = 0

print(f'Para começar, informe o carro: ')
car1 = Carro(input('Insira o modelo: '), input('Insira o ano de fabricação: '))





while menu == 0:
    print(f'------------------------------------')
    print(f'           >>>> MENU <<<<           ')
    print(f'------------------------------------')
    print(f'1 - ACELERAR')
    print(f'2 - FREIAR')
    print(f'3 - ALTERNAR FAROIS')
    print(f'4 - ALTERNAR LIMPADOR PARABRIZA')
    print(f'0 - Sair')
    print(f'------------------------------------')
    print(f'          >>>> VEICULO <<<<         ')
    print(f'------------------------------------')
    
    print(f'Estado do veículo: ')
    print('Modelo: {}, Ano: {}'.format(car1.modelo,car1.ano))
    print('Velocidade: {} Km/h'.format(car1.velocidade))
    print('Estado do farol: {} || (1) Ligado | (0) Desligado'.format(car1.farol))
    print('Estado do limpador: {} || (1) Ligado | (0) Desligado'.format(car1.limpador))
    
    print(f'------------------------------------')
    option = input('Digite a opção: ')
    print(f'------------------------------------')
    
    if option == '0':
        menu = 1
        print(f'---------- >>> SAINDO <<< ----------')
    elif option == '1':
        car1.acelerar(float(input('Quanto o carro deve acelerar? (KM/h) ')))
    elif option == '2':
        car1.freiar(float(input('Quanto o carro deve freiar? (KM/h) ')))
    elif option == '3':
        car1.alternarFarol()
    elif option == '4':
        car1.alternarLimpador()
    else:
        print(f'Código incorreto, tente novamente..')
    
    print(f'------------------------------------')