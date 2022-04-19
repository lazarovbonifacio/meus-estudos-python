"""
Exceções são erros
"""

try:
    a = []
    print(a[1])  # aciona exceção 2
    print(a)  # Aciona exceção 1
except NameError as erro:  # Colocamos a classe de erro que queremos tratar
    print('Erro do desenvolvedor')
except (IndexError, KeyError):
    print('Erro de indice')
except Exception as erro:
    print('Ocorreu um erro inesperado')
else:
    print('Esse bloco é executado sempre que o "try" der certo.')
finally:
    print('Esse bloco é executado sempre no final, independente do resultado.')
    # Você pode utilizar esse bloco para definir variáveis para que serão utilizadas no restante do seu código

print('bora lá...')