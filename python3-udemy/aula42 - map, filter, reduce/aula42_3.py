
from aula42_1 import produtos, pessoas, lista

n_lista = filter(lambda x: x>5,lista)  # retorna True ou False
# a_lista = [x for x in lista if x > 5]
print(list(n_lista))
# print(a_lista)

# ================

print(produtos)

n_produtos = filter(lambda p: p['preco'] > 30, produtos)  #  A vantagem de criar funções é a possibilidade de reutilização
for prod in n_produtos:
    print(prod)

# =======

print(pessoas)

def filtra(p):
    if p['idade'] < 18:
        return True

n_pessoas = filter(filtra, pessoas)
for pessoa in n_pessoas:
    print(pessoa)