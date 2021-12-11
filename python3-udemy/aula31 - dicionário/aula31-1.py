#!/usr/bin/python
#*-* coding: utf-8 *-*

# É uma estrutura de dados que suporta um par de chave/valor, o indice/chave é definido por você.

# _- METODO 1 - Mais comum
dic1 = {
    'chave1':'valor'
}

dic1['nova_chave'] = 'Valor da chave'  # Cria e atualiza valores de chaves

print(dic1)

# _- METODO 2 

dic2 = dict(chave1='valor1', chave2='valor2')  # Construtor

print(dic2['chave1'])

# Se um dicionário tiver elementos do tipo 'chave' repetidos, o valor que será utilizado será o ultimo definido.
dic3 = {54:'valor1',54:'valor2',54:'valor3'}

# Você só pode utilizar elementos imutáveis como chave em uma tupla (strings, inteiros, e tuplas)
dic4 = {
    'str': 'string',
    123: 'inteiro',
    (34,56): 'tupla'
}
dic4.update({(34,56):'tupla12'})  # Cria e atualiza valores de chaves em um dicionário

print(dic4)

print(dic4.get(123))  # Como utilizar o valor de uma chave uqe você não tem certeza que existe sem quebrar o código

del dic4[123]  # remover uma chave do dicionário

print(dic4)

# _- Como checar elementos em um dicionário
print('str' in dic4)
print('str' in dic4.keys())
print('inteiro' in dic4.values())

# _- Iteração com dicionários
dic5 = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': 'value3'
}

for k in dic5:  # itera sob as chaves
    print(k)

for v in dic5.values:  # itera sob os valores
    print(v)

for k, v in dic5.items():  # itera sob as chaves e os valores individualmente (desempacotados)
    print(k, v)

for i in dic5.items():  #  itera sob os pares
    print(i)  # Cada para é uma tupla com 2 valores