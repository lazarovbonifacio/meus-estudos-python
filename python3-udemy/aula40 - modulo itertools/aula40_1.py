"""
combinations, permutations e product
combinations: ordem não importa. Retorna combinações únicas em elementos.
permutations: ordem importa. Retorna combinações únicas em combinações.
Ambos não repetem valores unicos
product: ordem importa e repete valores únicos. Retorna todas as combinações possíveis
"""
from itertools import combinations, permutations, product

pessoas = ['Lazaro','Ana','Apolo','Selena','Gabriel','Beatriz']

for grupo in combinations(pessoas,2):  # retorna grupos de 2
    print(grupo)

for grupo in permutations(pessoas,3):  # retorna grupos de 3
    print(grupo)

for grupo in product(pessoas, repeat=2):  # retorna grupos de 2
    print(grupo)