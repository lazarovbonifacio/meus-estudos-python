from aula42_1 import produtos, pessoas, lista
from functools import reduce

# ===== acumulador =====
acumula = 0
for item in lista:
    acumula += item
print(acumula)

# ===== reduce() com listas =====
soma_lista = reduce(lambda ac, i: i + ac, lista, 0)
print(soma_lista)

# ===== reduce() com dicionário =====
soma_lista = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)
print(soma_lista)

soma_lista = reduce(lambda ac, p: p['idade'] + ac, pessoas, 0)
print(soma_lista/len(pessoas))