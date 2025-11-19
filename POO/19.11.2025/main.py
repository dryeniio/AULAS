import random
#Enio Enrique - 01851994
#Atividade 05 - Listas

#Questão 1
lista = list(range(1, 6)) 
print(lista[0], lista[-1]) 

#Questão 2
print(lista[0],lista[len(lista)//2],lista[-1])

#Questão 3
lista[random.randint(0,len(lista)-1)] = 27
print(lista)

#Questão 4
# Se eu adicionar dois elemento: lista.extend([6,7])
lista.append(6)
lista.append(7)
print(lista)