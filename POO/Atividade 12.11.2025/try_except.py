while True:
    try:
        nome = input('Digite seu nome: ')
        if not nome.strip():
            print('Nome não pode ser vazio. Tente novamente.')
            continue
        elif nome.isdigit():
            print('Nome não pode ser um número. Tente novamente.')
            continue
    except Exception as error:
        print(f'Ocorreu um erro: {error}. Tente novamente.')
        continue
    break

while True:
    try:
        idade = int(input('Digite sua idade: '))
        if idade < 0:
            print('Idade não pode ser negativa. Tente novamente.')
            continue
    except ValueError:
        print('Entrada inválida. Por favor, digite um número inteiro para a idade.')
        continue
    break

print(f'Nome: {nome}, Idade: {idade}')