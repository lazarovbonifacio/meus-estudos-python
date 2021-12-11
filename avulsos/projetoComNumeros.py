# DECLARAÇÃO DE VARIÁVEIS
restoDoNumeroPrincipal = 3
divisaoExata = 0
divisaoInexata = 0
# INTERAÇÃO COM O USUÁRIO
print('Esse código fornece algumas informações sobre números naturais.')
numeroPrincipal = int(input('Forneça um número inteiro: '))

# VERIFICA SE É PRIMO
for divisor in range(1, numeroPrincipal + 1):
    if numeroPrincipal % divisor == 0:
        divisaoExata += 1
    else:
        divisaoInexata += 1
if divisaoExata == 2:
    print('Esse número é primo.')
    fatoravel = False
else:
    print('Esse número NÂO é primo')
    fatoravel = True

# VERIFICA SE É PAR
while (restoDoNumeroPrincipal >= 2):
    restoDoNumeroPrincipal = numeroPrincipal % 2
if restoDoNumeroPrincipal == 1:
    print('Esse número é impar.')
elif restoDoNumeroPrincipal == 0:
    print('Esse número é par.')

# SIMPLIFICAÇÃO EM FATORES PRIMOS
# if fatoravel == True:
