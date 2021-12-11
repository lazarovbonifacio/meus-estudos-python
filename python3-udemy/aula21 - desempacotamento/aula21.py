"""
Desempacotamento de listas em python
"""
lista = ['Olá','Mundo','Eu','uso','python']

e1, e2, e3, *valores_sobrando = lista
print(e1, e2, e3, valores_sobrando)

e4, *valores_do_meio, e5, e6 = lista
print(e4, e5, e6, valores_do_meio)

*_, e7, e8 = lista  # A notaçaõ '*_' é utilizada para indicar à outros programadores que lerem o código de que os termos dentro
                    # desta lista (não nomeados) não serão usado.
print(e7, e8)