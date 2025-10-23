print("======== Questão 1 ========")
repetir = 1
while repetir == 1:
    while True:
    
        nome = input("Digite seu nome: ")
        if len(nome)<=3:
            print("Nome menor que 3!")
            break
        idade = int(input("Digite sua idade: "))
        if not 0 < idade < 150:
            print("Idade não está entre 0 e 150")
            break
        salario = float(input("Digite o seu salário: "))
        if salario <= 0:
            print("Salário menor que 0!")
            break
        genero = input("Digite o seu gênero: ")
        if not genero in ('f', 'm'):
            print('Genero não é f ou m.')
            break
        estado_civil = input("Digite o estado civil: (s, c, v, d) ")
        if not estado_civil in ('s','c','v','d'):
            print('Estado civil não é (s, c, v ou d)')
            break
        repetir = 0
        break

print("======== Questão 2 ========")
num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))

valor_maior = max(num1, num2)

print(f'O maior número digitado é: {valor_maior}')


print("======== Questão 3 ========")

num_real = float(input('Digite um valor Positivo ou Negativo: '))

if num_real > 0:
    print('Número POSITIVO')
elif num_real < 0:
    print('Número NEGATIVO')
else:
    print('Número ZERO')