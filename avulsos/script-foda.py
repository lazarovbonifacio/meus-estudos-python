def menu_real():
    acao = input(" O que você deseja fazer?\n Escolha entre 'add', 'rm', 'mv', 'rename', 'help' ou 'exit': ")
    if acao in ['add', 'rm', 'mv', 'rename']:
        menu_gp_ou_conv(acao)
    elif acao == 'exit' :
        exit()
    else:
        chama_help()

def menu_gp_ou_conv(acao):
    opcao = input(f" O que você deseja {acao}: um convidado(c) ou um grupo(g): ")
    if opcao == 'g' :
        adiciona_grupo()
    elif opcao == 'c' :
        adiciona_convidado()
    elif opcao == 'exit' :
        pass
    else:
        chama_help()

def adiciona_grupo():
    entrada = ""
    while entrada != 'exit':
        entrada = input(" Entre o nome de um grupo de convidados: ")
        if entrada == 'exit':
            pass
        elif len(entrada) <= 3 :
            entrada = input('Seja mais criativo: ')
        else:
            grupos.append(entrada)

def adiciona_convidado():
    pass

def chama_help():
    print("\n Sabe ler não, poha?\n")

boas_vindas = '''
  Esse script me ajudou a contar e gerenciar a lista de convidados para o meu casamento, \n
  mas eu creio que posso ajudar outras pessoas que precisem fazer isso e queira usar-lo. \n
  Se quiser usar, use. Se não, foda-se.

'''
grupos = []
print(boas_vindas)

while True :
    menu_real()
