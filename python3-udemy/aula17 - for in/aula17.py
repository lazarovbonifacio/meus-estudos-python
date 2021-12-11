"""
Enquanto o 'while' é mais usado para coisas infinitas,
o 'for' é utilizado para coisa finitas
"""
# Iteração

frase = "Python"

for letra in frase:
    print(letra)

# Função range()
#
# default: range(start=0, stop, step=1)
# 
# OBS.: o parâmetro 'stop' não é incluido nem para incrementar como para decrementar

for numero in range(10):  # Conte de um 0 a 9
    print(numero)
    # OUTPUT: 
    #         1
    #         2
    #         3
    #         4
    #         5
    #         6
    #         7
    #         8
    #         9

for numero in range(5,15,2):  # Conte de 5 até 14 pulando de 2 em 2.
    print(numero)

for numero in range (20,10,-1):  # Conta de 1 em 1 de forma decrescente de 20 até 11.
    print(numero)
