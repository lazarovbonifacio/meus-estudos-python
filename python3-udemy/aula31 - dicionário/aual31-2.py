#!/usr/bin/python
#*-* coding: utf-8 *-*

# _- Como copiar um dicionário

dic1 = {1:'a', 2:'b', 3:'c', 'd':'e', 'f':[1,2,3,4]}

atribuicao = dic1  # Isso é uam atribuição, não uma cópia
copia_rasa = dic1.copy()  # Copia rasa. Ou seja, elementos mutáveis (listas e dicionários) continua atrelados, como uma atriubuição

import copy

copia_profunda = copy.deepcopy(dic1)  # Cópia real, sem nenhuma atribuição

# Casting: Utilize o construtor 'dict()'. Vocé precisa de uma estrutura 'chave:valor'

lista1 = [
    [1,2],
    [3,4],
    [5,6],
    [7,8],
]
dic2 = dict(lista1)

lista2 = [
    (1,2),
    (3,4),
    (5,6),
    (7,8),
]
dic2 = dict(lista2)

tupla1 = (
    [1,2],
    [3,4],
    [5,6],
    [7,8],
)
dic2 = dict(tupla1)

tupla2 = (
    (1,2),
    (3,4),
    (5,6),
    (7,8),
)
dic2 = dict(tupla2)

# _- Removendo elementos
dic2.pop(7)  # Pelo nome da chave
dic2.popitem()  # O ultimo elemento declarado

# _- Extendendo dicionários
dic1.update(dic2)