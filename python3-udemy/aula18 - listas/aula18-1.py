"""
Listas em Python

* Principio de Fatiamento
* Listas suportam multiplos valores de multiplos tipos

Comandos:
append(), insert(), pop(), del(), clear(), extend()
"""

l1 =[1,2,3]
l2 = [4,5,6]
l3 = l1 + l2  # concatena as listas
l1.extend(l2)  # concatena o que está entre parenteses a lista 'l1'
l2.append('b')  # Insere um valor no final da lista
l2.insert(2,'banana')  # Insere o valor 'banana' no indice 2 dad lista
l2.pop()  # Remove o ultimo item da lista
del(l3[3:5])  # remove um fatia da lista
max = max(l2)
min = min(l3)
l4 = list(range(1,10))