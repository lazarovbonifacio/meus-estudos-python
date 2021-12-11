primeiro_nome = input("Qual seu primeiro nome? ")

if primeiro_nome.isalpha():
    tamanho_primeiro_nome = len(primeiro_nome)
    if tamanho_primeiro_nome <= 4:
        print("Nome de preguiçoso.")
    elif tamanho_primeiro_nome >= 5 and tamanho_primeiro_nome <= 6:
        print("Nome normal.")
    elif tamanho_primeiro_nome > 6 and tamanho_primeiro_nome < 11:
        print("Nome grande do carai.")
    else:
        print("Carai de nome é esse, macho? kkkkkkkkkkkkk") 
else:
    print("Tá tão engraçadinho hoje, hein? \nO que aconteceu?\nTá como patati e o patata enfiado no cu?")
