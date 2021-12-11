"""
Uso do operador condicional OR
"""
# ==== BRUTO ====

# var1 = input("Digite um valor: ")

# if var1:
#     var2 = var1
# else:
#     var2 = 'None'

# print(var2)

# ==== REFINADO ====

var1 = input("Digite um valor: ")
print(var1 or False or 'None')  # O OR vai setar o primeiro valor verdadeiro

# ==== OUTRO USOS ====

a = False
b = []
c = {}
d = None
e = 0
f = ''
g = 'Oi!'
h = 'Gayzao'

teste_de_or = a or b or c or d or e or f or g or h  # O OR vai setar o primeiro valor verdadeiro
print(teste_de_or)
