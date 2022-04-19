from aula42_1 import produtos, pessoas, lista

print(lista)
# nova_lista = map(lambda x: x * 2, lista)  # similar a list compresention
nova_lista = [x * 2 for x in lista]
print(list(nova_lista))

# ===============

print(produtos)

def aumenta_preco(p):
    p['preco'] = round(p['preco'] * 1.05,2)
    return p

precos = map(aumenta_preco, produtos)
for preco in precos:
    print(preco)

# ===============

print(pessoas)

nomes = map(lambda p: p['nome'], pessoas)
for nome in nomes:
    print(nome)