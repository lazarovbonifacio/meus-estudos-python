
# EXEMPLO

a = int(input('Entre com valor1: '))
while a > 10:
    a = int(input('Você digitou o número errado. Primeiro bimestre: '))
b = int(input('Entre com valor2: '))
while b > 10:
    b = int(input('Você digitou o número errado. Segundo bimestre: '))
c = int(input('Entre com valor3: '))
while c > 10:
    c = int(input('Você digitou o número errado. Terceiro bimestre: '))
d = int(input('Entre com valor4: '))
while d > 10:
    d = int(input('Você digitou o número errado. Primeiro bimestre: '))
media = (a + b + c + d) / 4
print('Sua média foi: {}'.format(media))

# Validação dos dados entrados:
# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print('Média é igual a: {}'.format(media))
# else:
#     print('Não foi digitado a nota correta.')

## WHILE

a = 0
while a <= 10:
    # print(a)
    a += 1

# É O MESMO QUE:

range(11)

## FOR dentro de FOR

# a = int(input('Entre um numero: '))
# for num in range(a+1):
#     div = 0
#     for x in range (1, num+1):
#         resto = num % x
#         if resto == 0:
#             div += 1
#     if div == 2:
#         print(num)

## FOR simples

# a = int(input('Entre um numero: '))
#
# div = 0
# # O "range() veio para subsituir o while para incrementar variável"
# for x in range (1, a+1):
#     resto = a % x
#     if resto == 0:
#        div += 1
# if div == 2:
#     print('Número {} é primo!'.format(a))
# else:
#     print('Número {} não é primo.'.format(a))

# for x in range(9, 101):
#     print(x)