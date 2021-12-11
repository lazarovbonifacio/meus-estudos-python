def func(a1,a2, a3, a4='Oi', a5='Olá'):  # Argumentos após o primeiro arg. c/ valor default preecisam ter valor default definido
    print(a1, a2, a3, a4, a5,end='\n\n')

func(1,2,a5=3, a4=4, a3=5)  # Após nomear um argumento para a função os seguintes também devem ser nomeados

"""
Funções (def) em Python - *args (arguments) e **kwargs (keyword arguments)
"""

def func2(*args, **kwargs):  # Os nomes 'args' e 'kwargs' são convenções da comunidade 

    print(args)  # '*args' é usado quando não se tem ideia de quantos argumentos NÂO-NOMEADOS serão passados para a função
    print(kwargs)  # '**kwargs' é utilizado quando não se tem ideia de quantos argumentos NOMEADOS serão passados para a função
   
    # print(args[0])  #  È possivel acessar os elementos da tupla como nas listas e...
    # print(kwargs['var1'])  # É possivel acesar os elementos dos dicionários pelo nome, porém esse não é o metodo mais recomendado
    
    var = kwargs.get('var1')  # Fazendo desta forma você evita erros
    print(var,end='\n\n')

lista = [1,2,3,4,5]
lista2 = [6,7,8,9,10]

func2(lista, var1=lista2)
func2(*lista,*lista2,*'Valha')  # Quando um objeto iteravel é enviado com '*' na frente ele é desempacotado,
                                # cada item dentro dele se torna uma elemento da tupla do '*args'



