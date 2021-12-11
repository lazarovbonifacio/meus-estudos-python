from random import randint

numero = str(randint(10000000,999999999))

soma = 0
for i,number in enumerate(numero):
    soma += int(number) * (10 - i)

first_digit = '0' if (11 - (soma % 11)) > 9 else str(11 - (soma % 11))
numero += first_digit

soma = 0
for i,number in enumerate(numero):
    soma += int(number) * (11 - i)

second_digit = '0' if (11 - (soma % 11)) > 9 else str(11 - (soma % 11))
numero += second_digit

print(numero)