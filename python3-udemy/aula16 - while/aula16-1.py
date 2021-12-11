"""
LAÇO DE REPETIÇÃO WHILE
"""
# =========== EXEMPLO 1 ==========================

# while True:  # Loop infinito
#     print('Olá mundo!')

# =========== EXEMPLO 2 ==========================

# x = 0
# while x < 10:
#     if x == 3:
#         x += 1
#         continue  # Retorne para o proximo laço
#         # break  # Terminei o laço 'while'
#     print(x)
#     x += 1
# print('Acabou!')

# ============ EXEMPLO 3 =========================

# z = 0
# while z < 7:
#     y = 0
#     while y < 12:
#         print(f'X: {z}, Y:{y}')
#         y += 1
#     z += 1

# =========== EXEMPLO 4 ==========================

while True:
    print('Inicie seus calculos!\n')
    num1 = ''
    while not num1.isnumeric():
        num1 = input('1° Número: ')
        if num1 == 's':
            break
    
    ope = ''
    while ope not in {'+','-','*','/'}:
        ope = input(f'Um operador(+,-,*,/):\n{num1} ')
        if ope == 's':
            break
        elif ope not in {'+','-','*','/'}:
            print("\nEntre com um operadopr válido, engraçadinho\n")

    num2 = ''
    while not num2.isnumeric():
        num2 = input(f'2° Número: {num1} {ope} ')
        if num2 == 's':
            break

    num1 = float(num1)
    num2 = float(num2)

    if ope == '+':
        print(f"\nResultado:", num1 + num2,"\n")
    elif ope == '-':
        print(f"\nResultado:", num1 - num2,"\n")
    elif ope == '*':
        print(f"\nResultado:", num1 * num2,"\n")
    elif ope == '/':
        print(f"\nResultado:", num1 / num2,"\n")
    else:
        pass
