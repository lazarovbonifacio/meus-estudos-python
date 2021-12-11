"""
Métodos: add (adiciona), update (atualiza), clear, dsicard
         union (|): une
         intersection (&): Retorna todos os elementos presentes nos dois sets
         difference (-): Retorna elementos presentes apenas no set da esquerda
         symmetric_difference (^): Retorna elementos que estão nos sets, mas não em ambos (como um XOR)
"""
# Como criar um Set (Conjunto)
set1 = set()  # Set vazio
set2 = {1,2,3,4,5}

dicionario_vazio = {}

# Como adicionar elementos - parte 1
set1.add('a')
set1.add('b')

# Como remover um elemento
set1.discard('a')

# Como adicionar elementos - parte 2
set1.update('c')
set1.update('Python',[1,2,3,4],(2,3,4,5,6))  # O método update pode ser receber um elemento iteravel, e ele o iterará

# >>..>>..>>.
set2 = {1,2,4,7,8,5,'b','o'}

# Como unir dois conjuntos
set3 = set1 | set2
print(set3)

# Pegar os elementos presentes em ambos os conjuntos
set3 = set1 & set2
print(set3)

# Pegar os elementos presentes apenas no set da esquerda
set3 = set1 - set2
print(set3)

# Pegar os elementos que estão nos sets, mas não em ambos
set3 = set1 ^ set2
print(set3)