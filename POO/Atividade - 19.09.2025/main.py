# 2NB - 01851994 - Enio Enrique
from aviao_class import Aviao

Voo1 = Aviao()

print('------------------------------------------------')
Voo1.alterar_matricula('PS-AEK')
print('------------------------------------------------')
Voo1.alterar_rota('REC - GRU')
print('------------------------------------------------')
print('------------------------------------------------')

print(f'Avião: {Voo1.modelo} | Matrícula: {Voo1.matricula} | Rota: {Voo1.rota} | Operador: {Voo1.operador}')
print('------------------------------------------------')
