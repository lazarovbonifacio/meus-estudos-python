"""
# Tipos primitivos
 - string (str): Texto. Exemplo: 'Assim', "Assim" ...;
 - inteiro (int): Numero inteiro. Exemplo: 1, 2, -3, 45, 0, -1000 ...;
 - Fracionário (float): Número com virgula/casas decimais. Exemplo: 10.0, 0.0, 12.7, 6.8, 65.77894 ...;
 - Booleano/Lógico (bool): Exemplo: True/1, False/0.
""" 

print('Texto',type('Texto'))
print(123, type(123))
print(7.86,type(7.86))
print(True, type(True))

"""
Typing casting
"""
print(int('10'),type(int('10')))
print(bool(''), type(bool('')))
print(bool(1), type(bool(1)))
print(float('10'),type(float('10')))
print(10,type(str(10)))