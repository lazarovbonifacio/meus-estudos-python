lista = [12, 3, 15, 7]
lista_animais = ['cachorro', 'gato', 'elefante', 'arara', 'ramerti']
lista_mesclada = [1, 'gato', 3]

# Mostra a lista completa
# print(lista)

# Mostra um item especifico da lista
# print(lista_animais[1])

# Mostrar o valor de cada variável individualmente
# for x in lista_animais:
#     print(x)

# Soma todos os elementos de uma lista
# soma = 0
# for i in lista:
#     soma += i
# print(soma)

# Mostrar a soma de todos os elementos da lista
# print(sum(lista))

# Mostra o maior valor de uma lista independente da posição
# print(max(lista))

# Mostra o menor valor de uma lista independente da posição
# print(min(lista))

# Mostra o primeiro elementos em ordem alfabética
# print(max(lista_animais))

# Mostra o último elemento em ordem alfabética
# print(min(lista_animais))

# Procurar por um elemento na lista

# animal = 'lobo'
# if animal in lista_animais:
#     print('Existe um {} na lista.'.format(animal))
# else:
#     print('Não existe um {} na lista.'.format(animal))
#     # Adicione um elemento à lista
#     lista_animais.append(animal)
#     print(lista_animais)

# lista_animais.pop() # Default: retire o ultimo elemento dessa lista
# # Retire um elemento específico colocando a posição dele entre "()!
# # a começar do "0"
# print(lista_animais)

# lista_animais.remove('elefante') # Retire um elementos conhecido
# print(lista_animais)

# Organize os elementos da lista de maneira crescente
lista.sort()
print(lista)
lista_animais.sort()
print(lista_animais)

# Organize de maneira decrescente os elementos da lista
lista_animais.reverse()
print(lista_animais)

# TUPLA: é um recurso usado quando se quer uma lista imutável
exemplo = (1,10,5,7)

# Descubra quantos elementos tem em uma lista ou tupla
print(len(exemplo))
print(len(lista_animais))

# Converta uma lista em uma tupla
tupla_animal = tuple(lista_animais)

# Converta uma tupla em lista
lista_numerica = list(exemplo)