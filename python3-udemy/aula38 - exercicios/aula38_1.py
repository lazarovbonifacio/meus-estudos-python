# Entrada: listas com inteiros ou fracionários
# Saída: soma de cada elemento que possui o mesmo indice, considerando apenas lista menor

# Entradas:
l1 = list(range(2,20,2))
l2 = list(range(5,11))

# Script:
l3 = [i + j for i,j in zip(l1,l2)]

# Saída:
print(l1,l2,l3)
