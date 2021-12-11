#EXEMPLO 4:

a = int(input('Entre com valor1: '))
if a > 10:
    a = int(input('Você digitou o número errado. Primeiro bimestre: '))
b = int(input('Entre com valor2: '))
c = int(input('Entre com valor3: '))
d = int(input('Entre com valor4: '))
media = (a+b+c+d)/4
# Validação dos dados entrados:
if a <= 10 and b <= 10 and c <= 10 and d <= 10:
    print('Média é igual a: {}'.format(media))
else:
    print('Não foi digitado a nota correta.')

#EXEMPLO 3:

# a = int(input('Entre com valor1: '))
# b = int(input('Entre com valor2: '))
# resto_a = a%2
# resto_b = b%2
#
# if resto_a == 0 or resto_b == 0:
# # if resto_a == 0 or not resto_b > 0:
#     print('Foi digitado um número par.')
# else:
#     print('Não foi digitado um número par.')

#EXEMPLO 2:

# a = int(input('Entre um número: '))
# resto = a%2
# if resto == 0:
#     print('Número é par')
# else:
#     print('Número é inpar')

# EXEMPLO 1:

# a = int(input('valor1: '))
# b = int(input('valor2: '))
# c = int(input('valor3: '))
# if a > b and a > c:
#     print('O maior número é {}'.format(a))
# elif b > a and b > c:
#     print('O maior númeeo é: {}'.format(b))
# else:
#     print('O maior número é {}'.format(c))
#     # Em python o condional é definido pela identação do código, prova é que a
#     # linha de código abaixo será printada.
# print('final do programa')