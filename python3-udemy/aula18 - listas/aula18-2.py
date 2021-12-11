# ======== PROFESSOR ========

# palavra_secreta = 'boletos'
# digitadas = list()
# chances = 4

# while True:
#     if chances <= 0:
#         print('Você perdeu!')
#         break
    
#     digitado = input("Digite uma letra: ")
    
#     if len(digitado) > 1:
#         print('Digite apenas uma letra.')
#         continue

#     digitadas.append(digitado)

#     if digitado in palavra_secreta:
#         print(f'A letra {digitado} existe na palavra secreta.')
#     else:
#         print(f'A letra {digitado} NÂO EXISTE na palavra secreta.')
#         digitadas.pop()
    
#     acertos = ''
#     for letra in palavra_secreta:
#         if letra in digitadas:
#             acertos += letra
#         else:
#             acertos += '*'
    
#     if acertos == palavra_secreta:
#         print("Parabens! Você GANHOU!")
#         break
#     else:
#         print(f'A palavra secreta está assim: {acertos}')

#     if digitado not in palavra_secreta:
#         chances -= 1
    
#     print(f'Você tem {chances} chances')
#     print()

# ====== EU =========

palavra_secreta = 'boletos'
digitadas = list()
chances = 4

while True:
    if chances <= 0:
        print(f'Você perdeu! A palavra era {palavra_secreta}.')
        break

    digitado = input("Digite uma letra: ")
    
    if len(digitado) > 1:
        chances -= 1
        print('Digite apenas uma letra.')
        print(f'Chances: {chances}')
        continue

    if digitado in palavra_secreta:
        digitadas.append(digitado)
        print(f"A letra '{digitado}' existe na palavra secreta.")
    else:
        print(f"A letra '{digitado}' NÂO EXISTE na palavra secreta.")

    acertos = ''
    for letra in palavra_secreta:
        if letra in digitadas:
            acertos += letra
        else:
            acertos += '*'
            
    if digitado not in palavra_secreta:
        chances -= 1

    print(f'Chances: {chances}/4.')

    if acertos == palavra_secreta:
        print(f"Parabens! Você GANHOU! A palavra era {palavra_secreta}.")
        break
    else:
        print(f'Acertos: {acertos}\n')
