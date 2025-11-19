import random

#Questão 1
lista = list(range(1, 6)) 
print(lista[0], lista[-1]) 

#Questão 2
print(lista[0],lista[len(lista)//2],lista[-1])

#Questão 3
lista[random.randint(0,len(lista)-1)] = 27
print(lista)