lista = [
    ('chave0', 'valor0'),
    ('chave1', 'valor1'),
    ('chave2', 'valor2'),
]

d1 = {x: y for x, y in lista}  # ...É igual a 'd1 = dict()'

d2 = {x: y*2 for x, y in lista}
d3 = {x.upper(): y.title() for x, y in lista}  # Diferente da função dict(), a compreensão de dicionário é capaz de manipular os elementos antes de definí-los

d4 = {f'chave_{x}': x**3 for x in range(5)}
# print(d4)

l1 = list(range(10))
s1 = {x for x in l1}  # Isso vai formar um set/conjunto
