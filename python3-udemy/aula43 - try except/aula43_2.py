
def divide(x,y):
    try:
        return x/y
    except ZeroDivisionError as erro:
        print(erro)
        raise  # lançar exceção

try:
    print(divide(3,0))
except:
    print('erro')

def divide(x,y):
    if y == 0:
        raise ValueError("Y não pode ser 0.")
    return x/y
    
print(divide(3,0))

# COnsulte a documentação dos erros builtins do python: https://docs.python.org/3/library/exceptions.html