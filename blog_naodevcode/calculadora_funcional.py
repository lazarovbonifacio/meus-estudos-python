# ================== INÍCIO ===================
while True:

    # Mensagem de boas-vindas
    print('\
Inicie seus cálculos!\n\
=====================\n')

    # Define o primeiro numero da operação
    num1 = ''

    # Solicita que o usuário digite o número natural
    while not num1.isnumeric():
        num1 = input('1° Número: ')

        # Sai do código se o usuário digitar 's'
        if num1 == 's':
            exit()
    
    # Define a operação
    ope = ''

    # Solicita que o usuário digite uma operação válida
    while ope not in {'+','-','*','/'}:
        ope = input(f'Um operador(+,-,*,/):\n{num1} ')

        # Sai do código se o usuário digitar 's'
        if ope == 's':
            exit()
        
        # Mensagem de erro
        elif ope not in {'+','-','*','/'}:
            print("\nEntre com um operador válido, engraçadinho\n")

    # Define o segundo numero da operação
    num2 = ''

    # Solicita que o usuário digite o número natural
    while not num2.isnumeric():
        num2 = input(f'2° Número: {num1} {ope} ')

        # Sai do código se o usuário digitar 's'
        if num2 == 's':
            exit()

    # Converte as entradas numéricas para números de ponto flutuante
    num1 = float(num1)
    num2 = float(num2)

    # Realiza as operações e as mostra no console
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
# ================== FIM ===================