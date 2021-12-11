"""
Manipulando strings
 - String indices
 - Fatiamento de strings [inicio:fim:passo]
"""
# Índices:

# positivos   [0123456789]
texto       = "Pythonic T"
# negativos -[10987654321]

print( texto[:] )  # Imprime a string inteira
# OUTPUT: Pythonic T

print( texto[:5] )  # Imprime do inicio até o 4° caracter
# OUTPUT: Pytho

print( texto[5:] )  # Imprime do 5° caracter até o final da string
# OUTPUT: nic T

print( texto[3:8] )  # Imprime do 3° caracter até o 7° caracter
# OUTPUT: honic

print( texto[:-1] )  # Imprime até a penúltima letra da string
# OUTPUT: Pythonic 

print( texto[-3] )  # Imprime o 3° indice de trás pra frente
# OUTPUT: c

print( texto[::2] )  # Imprime de 2 em 2 caracteres
# OUTPUT: Ptoi_ 

print( texto[1:6:3] )  # Imprime do a partir do 2° índice até o 6° índice de 3 em 3 caracteres
# OUTPUT: yo_


