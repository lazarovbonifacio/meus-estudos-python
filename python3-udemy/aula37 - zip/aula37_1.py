"""
Zip - unindo iteraveis
Zip_longest - Itertools
"""
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Natal']
estados = ['SP','MG','BA','RN']

cidades_estados = zip(cidades,estados)  # Retorna um iterador, composto por tuplas com os 2 valorea associados
print(next(cidades_estados))
for valor in cidades_estados:
    print(valor)

# É possivel converter esse gerador em lista ou dicionário
print(list(cidades_estados))
print(dict(cidades_estados))

# Essa ferramenta só uni até o tamanho da menor lista
cores = ['Rosa','Vermelho','Verde','Azul','Amarelo']
pecas = ['Gravata','Sapato','Cinto']
pecas_cores = zip(pecas,cores)
for roupa in pecas_cores:
    print(roupa)  # ultimo laço: ('Cinto', 'Verde')

# Para casos de tamanhos diferentes de iteraveis, use o método 'zip_longest'
from itertools import zip_longest
import itertools
pecas_cores = zip_longest(pecas,cores,fillvalue='default')  # O parametro 'fillvalue' define o valor padrão para elementos não zipados. O padrão é None.
for roupa in pecas_cores:
    print(roupa)

from itertools import count
indice = count()  # Essa função cria um gerador com numeros infinitos
cidades_estados = zip(indice, estados, cidades)  # A zip_longest pode te causar problemas caso você não saiba o tamanho dos iteráveis que você está trabalhando
for valor in cidades_estados:
    print(valor)