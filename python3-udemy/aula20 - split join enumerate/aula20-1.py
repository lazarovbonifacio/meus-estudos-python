"""
Split, Join e Enumerate
* Split - Divide um string
* Join - Junta uma lista
* Enumerate - Enumera elementos da lista (iteraveis)
"""

text = "Um ninho de mafagarfos para sete mafagarfinho, quantos mafargifagos será?"
lista_1 = text.split(' ')
lista_2 = text.split(',')

for palavra in lista_1:
    print(palavra)

for frase in lista_2:
    print(frase.strip().capitalize())  # strip(): remove os espaços no inicio e no final de uma string
                                       # capitalize(): Torne a primeira letra de uma string maiuscula

lista_3 = lista_2[1].strip().capitalize()
lista_4 = lista_3.split(' ')
string = '_'.join(lista_4)
print(string)

# =======

nomes = ['Thiago', 'Lázaro', 'Luiz','Pedro']

for indice,nome in enumerate(nomes):
    print(indice, nome, nomes[indice])

# É o mesmo que...

nomes_spy = [
    [0,'Thiago'],
    [1, 'Lázaro'],
    [2, 'Luiz'],
    [3, 'Pedro']
]
for indice,nome in nomes_spy:
    print(indice, nome)

# Porém, o Enumerate() utiliza tuplas

# O que essa função faz é o desempacotamento. Um exemplo bruto:

n1, n2, n3, n4 = nomes
print(n1)