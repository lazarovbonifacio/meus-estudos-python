def funcao1():  # Funções servem para representar treixos de código que se repetem
    print('Hello World!')

funcao1()

def funcao2(param1, param2):  # Funções podem receber parâmetros
    print(param1, param2)

funcao2('mensagem', 8)

def funcao3(msg='Olá', nome='Fulano'):  # podemos definir parametros padrão
    print(msg, nome)

funcao3()
funcao3('Errado', 'Mensagem')
funcao3(nome='Certa', msg='mensagem')

def funcao4(param1='Vitor', param2='Leo'):
    return f'{param1} e {param2}'

variavel = funcao4
print(variavel('frfs','sadas'))