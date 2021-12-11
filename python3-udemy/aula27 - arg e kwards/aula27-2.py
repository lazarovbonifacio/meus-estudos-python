"""
Escopo de variavéis
"""
variavel = 'valor'  # variável de escopo global

def func():
    # Usa o valor de escopo global
    print(variavel)
    
    # variavel = 123  # Não é possivel alterar o valor de um variável global, a fim de um valor local, após referenciá-la
    # print(variavel)

def func2():
    variavel = 'Outro valor'  # Variável de escopo local (com o mesmo nome da global)
    print(variavel)

def func3():
    global variavel  # É possivel alterar o valor de uma variável global desta forma (Não recomendado)
    variavel = 'Valor diferente'
    print(variavel)

def func4(var):  # Forma recomendada de utilizar uma variável
    var = var.replace('e','3')
    return var


func()

func2()
print(variavel)  # O valor de uma variável global não pode ser alterado de dentro de uma função

func3()
print(variavel)  # O valor da variável foi alterado

outra_var = func4(variavel)  # Deste jeito é bem melhor
print(outra_var)
