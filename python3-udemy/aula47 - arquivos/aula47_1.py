# Trabalhando com arquivos

## Maneira 1:

file = open('abc.txt','w+')  # abrir (criando) arquivo para leitura, leitura e escrita

file.write('Linha1\n')
file.write('Linha2\n')
file.write('Linha3\n')

print(file.read())  # Se tentarmos ler o arquivo o cursor vai estar no final do arquivo
file.seek(0, 0)  # Reseta o cursor. seek(offset, posição relativa). # seek(0, 0) volta ao inicio do arquivo
print(file.read())
print('###')

file.seek(0, 0)
print(file.readline())
print(file.readline())
print(file.readline())
print('###')

file.seek(0, 0)
print(file.readlines())  # lista cada linha do arquivo

file.seek(0, 0)
for linha in file.readlines():#file:
    print(linha,end='')

file.close()

## Maneira 2:
try:
    file = open('abc.txt','w+')
    file.write('Lorem Ipsum Dolor')
    file.seek(0)
    print(file.read())
finally:
    file.close()

## Maneira 3 (forma mais pythonica): 
### Gerenciador de contexto
with open('abc.txt','w+') as file:
    file.write('Lorem Ipsum Dolor\n')
    file.write('Lorem Dolor\n')
    file.write('Lorem Ipsum\n')

    file.seek(0)
    print(file.read())

"""
Opção 'r+' apenas lé o arquivo
Opção 'a+' ativa o append mode (adiciona coisas sem apagar, ou seja, posiciona o cursos no final do arquivo)
Opção 'w+' apaga o arquivo todo e escreve
"""

import os 
os.remove('abc.txt')  # para remover arquivos

import json
d0 = {
    'p0': {
        'n':'oi',
        'i': 10,
    },
    'p1': {
        'n':'ola',
        'i': 20,
    },
}

d0_json = json.dumps(d0,indent=True)
print(d0_json)

with open('abc.json','w+') as file:
    file.write(d0_json)