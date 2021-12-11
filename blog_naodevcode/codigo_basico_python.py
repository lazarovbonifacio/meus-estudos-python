#!/usr/bin/python
#*-* coding: utf-8 *-*

# .:! INÍCIO !:.
caracter = input("Digite um caracter: ")

if caracter.isnumeric():
    print(caracter + " é um número.")

    ate_numero = int(caracter) + 1 
    contador_resto_0 = 0

    for num in range(ate_numero):
        resto = num % int(caracter)
        if resto == 0:
            contador_resto_0 += 1
    
    if contador_resto_0 == 2:
        print(caracter + " é primo.")

elif caracter.isalpha():
    print(caracter + " é uma letra.")
    if caracter in {'a','e','i','o','u'}:
        print(caracter + " é uma vogal.")
    else:
        print(caracter + " é uma consoante.")
else:
    print(caracter + " é uma caracter especial")

# .:* FIM *:.
