sessao = list(range(11))  # Cria uma lista que inicia no 0 e termina em 10
print(sessao)

lista = [
    ['Ed','Laura','David'],
    ['Thiago','Cirius','Manoel'],
    ['Paloma','Pedro','Matheus']
]

for numero,listinha in enumerate(lista, 67):  # enumerate(Elemento iteravel, começe por NUM)
    print(numero,listinha)
    nome1, nome2, nome3 = listinha
    print(nome2, nome3, nome1)