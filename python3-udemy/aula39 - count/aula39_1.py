from types import GeneratorType

variavel = zip('Alo','Alo')
print(isinstance(variavel, GeneratorType))  # Iterador

variavel = ((x,y) for x,y in zip('Alo','Alo'))
print(isinstance(variavel, GeneratorType))  # Gerador

# ======================================================

"""
count - Itertools
"""
from itertools import count

contador = count()  # iterador infinito
contador = count(start=5, step=0.3)  # o 'step' pode ser um float()

for i in contador:
    print(round(i,2))  # round() serve poara arredondar
    if i > 20:
        break

contador = count()
lista = ['lazaro','ana','apolo','leo']
lista_indexada = zip(contador,lista)
print(dict(lista_indexada))