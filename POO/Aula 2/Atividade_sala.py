#Enio Enrique - 2NB (01851994)

class Saudacao:
    def exibir_mensagem(self):
        nome = input('Qual seu primeiro nome? ')
        sobrenome = input('Qual seu sobrenome? ')
        self.nome_completo = nome + ' ' + sobrenome
        print(f'Olá Mundo!')
        print('Olá, {}' .format(self.nome_completo))
            
class Calculadora:
    def buscar_numero(self):
        self.numero_1 = float(input('Digite o primeiro número: '))
        self.numero_2 = float(input('Digite o segundo número: '))
    
    def somar(self, num1, num2):
        resultado = num1 + num2
        return resultado

    def subtrair(self, num1, num2):
        resultado = num1 - num2
        return resultado


hello = Saudacao()
hello.exibir_mensagem()


print(f'------------------------------------')
print(f'Calculador - v1')   
print(f'------------------------------------')


operacao = input('Qual a operação? + ou -?: ')
Calc = Calculadora()

if operacao == '+':
    Calc.buscar_numero()
    resultado = Calc.somar(Calc.numero_1, Calc.numero_2)
    print('O Resulado é: {}'.format(resultado))
    
if operacao == '-':
    Calc.buscar_numero()
    resultado = Calc.subtrair(Calc.numero_1, Calc.numero_2)
    print('O Resulado é: {}'.format(resultado))
    
else:
    print(f'OPERAÇÃO INVÁLIDA...')
    print(f'')
    
print(f'ENCERRANDO.....')
        



