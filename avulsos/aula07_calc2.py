# NO PYTHON
# Método/Função/definição (def) é tudo aquilo uqe retorna um valor

class Calculadora:
    def __init__(self):  # Opcional
        pass             # Uma definição não pode estar vazio,por isso usa-se o 'pass'

    def soma(self, valor_a, valor_b):
        return valor_a + valor_b

    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b

    def multiplicacao(self, valor_a, valor_b):
        return valor_a * valor_b

    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b

# def soma(a, b):
#     return a + b
# print(soma(3, 7))
# print(soma(4, 4))
# print(subtracao(10, 2))

# COMO INSTANCIAR UMA CLASSE
calculadora = Calculadora()
# print(calculadora.valor_a)
# print(calculadora.valor_b)
print(calculadora.soma(20, 80))
print(calculadora.subtracao(80, 20))
print(calculadora.multiplicacao(4, 7))
print(calculadora.divisao(100, 2))
