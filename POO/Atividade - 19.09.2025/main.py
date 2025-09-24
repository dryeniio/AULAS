# 2NB - 01851994 - Enio Enrique
from aviao import Aviao

Aviao1 = Aviao()
Aviao1.criar_aviao('Embraer', 'E295', 'AVALON', 'PS-KSB')

print('------------------------------------------------')
Aviao1.alterar_operador('Azul Linhas Aereas')
print(f'Operador alterado para {Aviao1.operador}')
print('------------------------------------------------')
Aviao1.alterar_rota('REC - GRU')
print(f'Rota alterada para: {Aviao1.rota}')
print('------------------------------------------------')
print('------------------------------------------------')
Aviao1.exibir_dados()
print('------------------------------------------------')
