# ================== INÍCIO ===================

class Calculadora:  # Diz ao programa para criar um objeto nomeador Calculadora
    def __init__(self):  # Informa as caracteriscitas basicas do objeto (também chamado de Construtor)
        pass

    def run(self):  # Define um método (nosso algoritmo)
        while True:
            self.saudacao()

            verificado = False
            while verificado == False:
                termo = 1
                valor_para_avaliar = self.entrada(termo)
                verificado = self.verificador_numerico(valor_para_avaliar)

            num1 = verificado

            verificado = False
            while verificado == False:
                termo = 2
                valor_para_avaliar = self.entrada(termo)
                verificado = self.verificador_operacao(valor_para_avaliar)

            ope = verificado

            verificado = False
            while verificado == False:
                termo = 3
                valor_para_avaliar = self.entrada(termo)
                verificado = self.verificador_numerico(valor_para_avaliar)

            num2 = verificado

            if ope == '+':  # Verifica se é uma soma
                self.soma(num1,num2)
            elif ope == '-':  # Verifica se é uma subtração
                self.subtracao(num1,num2)
            elif ope == '*':  # Verifica se é uma multiplicação
                self.multiplicacao(num1,num2)
            elif ope == '/':  # Verifica se é uma divisão
                self.divisao(num1,num2)
            else:
                print("ERROR")
    
    def saudacao(self):  # Sauda ao usuário
        print('\
Inicie seus cálculos!\n\
=====================\n')

    def entrada(self,termo):  # Recebe a entrada do usuário
        if termo == 1:
            valor_digitado = input("Digite um número ou [s]air: ")
        if termo == 2:
            valor_digitado = input("Escolha um operador (+,-,/,*) ou [s]air: ")
        if termo == 3:
            valor_digitado = input("Digite outro número ou [s]air: ")
        return valor_digitado

    def verificador_numerico(self, valor_entrado):  # Verifica se o valor digitado é numerico (Natural)
        if valor_entrado == 's':
            exit()
        elif valor_entrado.isnumeric():
            return float(valor_entrado)
        else:
            return False
    
    def verificador_operacao(self, valor_entrado):  # Verifica se o valor digitado é uma operação válida
        if valor_entrado == 's':
            exit()
        elif valor_entrado not in {'+','-','*','/'}:
            return False
        else:
            return valor_entrado

    def soma(self, valor_a, valor_b):  # Realiza a soma dos valores entrados
        return print(valor_a + valor_b)

    def subtracao(self, valor_a, valor_b):  # Realiza a subtração dos valores entrados
        return print(valor_a - valor_b)

    def multiplicacao(self, valor_a, valor_b):  # Realiza a multiplicação dos valores entrados
        return print(valor_a * valor_b)

    def divisao(self, valor_a, valor_b):  # Realiza a divisão dos valores entrados
        return print(valor_a / valor_b)

bolinha = Calculadora()  # Instância a classe
bolinha.run()  # Chama o método 'run()', que será o nosso algoritmo.

# ================== FIM ===================
