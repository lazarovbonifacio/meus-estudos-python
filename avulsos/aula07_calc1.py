# NO PYTHON
# Método/Função/definição (def) é tudo aquilo uqe retorna um valor

class Calculadora:
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2

    def soma(self):
        return self.valor_a + self.valor_b

    def subtracao(self):
        return self.valor_a - self.valor_b

    def multiplicacao(self):
        return self.valor_a * self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b

# def soma(a, b):
#     return a + b
# print(soma(3, 7))
# print(soma(4, 4))
# print(subtracao(10, 2))
if __name__ == '__main__':
    # COMO INSTANCIAR UMA CLASSE
    calculadora = Calculadora(10, 2)
    # print(calculadora.valor_a)
    # print(calculadora.valor_b)
    print(calculadora.soma())
    print(calculadora.subtracao())
    print(calculadora.multiplicacao())
    print(calculadora.divisao())
