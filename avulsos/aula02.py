#AULA 02

##Atribução de variável

a = int(input('Entre com o primeiro valor, seu animal: '))
b = int(input('Entre com o segundo valor, por favor: '))

##Operadores matemáticos

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

###Descubra o tipo de uma variável

# print(type(soma))

##Conversão de variável

# soma = str(soma)
# print(type(soma))
# print('soma: ' + str(soma))
###OBS.: Quando os elementos entre "()" são do memso tipo, o compilador concatena-os

##Uma maneira melhor de fazer isso é usando o comando abaixo:

# print('soma: {}'.format(soma))
#Independente do tipo da variavel a informação será mostrada.

print('Soma: {sum}; \nSubstração: {sub}; \nMultiplicação: {mult};'
      '\nResto: {resto}; \nDivisão: {div}'.format(sum=soma,
                                                  sub=subtracao,
                                                  mult=multiplicacao,
                                                  div=divisao,
                                                  resto=resto))
# Com o mesmo comando eu consigo realizar uma série de print utilizando os recursos como
# "\n" -> para quebra de linha;
# "{texto}" -> para definir alias para o campo

# print(subtracao)
# print(multiplicacao)
#
# print(type(divisao))
# print(int(divisao))
# print(type(divisao))
#
# print(resto)
