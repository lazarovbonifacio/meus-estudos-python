"""
Forma de iterar sobre os elementos de uma lista
- Só funciona com listas
"""
l1 = [1,2,3,4,5,6,7,8,9]
l2 = [variavel for variavel in l1]  # l2 é exatamente igual a l1
# Coleto cada valor presente em 'l1' e jogo para dentro de 'l2' pela variável 'variavel'

l3 = [v*2 for v in l1]  # Cada elemento de 'l1' será multiplicado por 2

l4 = [(v,v2) for v in l1 for v2 in range(3)]  # Para cada elemento de l1 será criado um for que criar 3 tuplas para cada número

l5 = ['Luiz', 'Lazaro', 'Thiago']
l6 = [v.replace('a','@') for v in l5]
# print(l6)

t1 = (
    ('valor','chave'),
    ('valor1','chave1'),
    ('valor2','chave2'),
)

l7 = [(y, x) for x, y in t1]  # inverto os valores
print(l7)

l8 = list(range(101))
l9 = [elemento for elemento in l8 if elemento%3 == 0 if elemento%5 == 0]  # 'l9' vai iterar sobre os elementos de 'l8' e
                                                                          # receberá os elementos que forem divisiveis por
                                                                          # 3 e por 5.

l10 = [v if v % 3 == 0 and v % 8 == 0 else 0 for v in l8]
print(l10)

# ======================================================

# Utilizada aotimização e escrever menos linhas de código

l1 = list(range(1,10))
l2 = [num for num in l1]  # itera sobre cada elementeo de l1, o joga na vairavel 'num' e criando um nova lista
# print(l2)

l3 = [num*2 for num in l1]  # Itera sobre cada elemento de l1, o joga na vairavel 'num', o multiplica por 2 e cria um nova lista
# print(l3)

l4 = [(v,v2) for v in l1 for v2 in range(3)]  # Gera algo como [(1,0),(1,1),(1,2),(2,0),...]

l5 = ['lazaro','bia','apolo']
l6 = [name.replace('a','?') for name in l5]  # Manipula as string de l5
# print(l6)

l7 = list(range(100))
l8 = [num for num in l7 if num % 3 == 0]  # itera sobre l7 e filtra apenas o valores que são divíseis por 3
# print(l8)

l9 = [num for num in l7 if num % 2 == 0 if num % 5 == 0]  # a quantidade de if's é infinita
# print(l9)

l10 = [v if v % 2 == 0 else 'Impar' for v in l7]
# print(l10)