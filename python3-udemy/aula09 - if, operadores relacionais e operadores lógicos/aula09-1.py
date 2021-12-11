"""
Condicional - IF, ELIF, ELSE
Operadores relacionais - ==, >, >=, <, <=, !=
Operadores lógicos - and, or, not, in, not in
"""
usuario = input('Nome: ')
senha = input('Senha: ')

usuario_db = 'luiz'
senha_db = '123456'

if usuario == usuario_db and senha == senha_db:
    print("Logado")
else:
    print("É burro é?")