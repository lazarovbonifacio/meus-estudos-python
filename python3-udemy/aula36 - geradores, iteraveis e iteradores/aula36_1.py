# O que é um interável?
## São elementos que possuem o atributo '__iter__'
lista0 = [1,2,3,4,5]
print(hasattr(lista0, '__iter__'))  # retorno esperado: True

# Numeros não são iteráveis, mas strings são.
# elementos iteraveis podem se tornar iteradores. É basicamente o que o laço 'for' faz.
# Elementos iteradores possuem o método '__next__'. Ou seja, basicamente, o 'for' faz o seguinte: 
lista1 = iter(lista0)
print(hasattr(lista1, '__next__'))

# Um elemento iteravel nem sempre é um iterador. Porque o iterador entrega um elemento por vez, enquanto o iteravel pode ser consultado por completo de uma vez. Observe:
print(next(lista1))  # retorno esperado: 1
print(next(lista1))  # retorno esperado: 2
print(next(lista1))  # retorno esperado: 3
print(next(lista1))  # retorno esperado: 4
print(next(lista1))  # retorno esperado: 5

# Iterador: te entrega um valor de cada vez; Iterável: pode entregar um valor de cada vez


# Geradores são utilizados geralmente para valores qeu utilizam muita memória ou tempo de processamento. Exemplo:
import sys
lista2 = list(range(10))

print(sys.getsizeof(lista2))  # retorno esperado: 136
# retorna o espaço de memória utilizado em bytes da variável

lista3 = list(range(2000))  # retorno esperado: 16056
print(sys.getsizeof(lista3))

# Esses valores podem são irelevantes considerando o tamanho da lista, mas se tivermos uma lista com 100000000 valores o python vai querer armazenar tudo isso na memória
# o que vai reduzir a performance e aumentar o consumo de memória sem necessidade. Imagine o seguinte cenário:

import time
def gera0():
    r = list()
    for n in range(100):
        r.append(n)
        time.sleep(0.1)  # simula um operação pesada
        return r

g = gera0()
for v in g:
    print(v)

# Por isso existem os geradores. Para tornar a função acima em um gerador basta fazer as seguintes alterações:

def gera1():
    for n in range(100):
        yield n
        time.sleep(0.1)  # simula um operação pesada

g = gera1()
# for v in g:
#     print(v)
print(next(g))
print(next(g))
print(next(g))
print(next(g))

# O elementros geradores possuem o atributo '__next__' e o atributo '__iter__'. Isso significa que ele é tanto um iteravel como um iterador. Ou seja, eu posso usar tanto o 'for' quanto o 'next()'
# Uma forma mais manual de se representar um gerador é o seguinte:

def gera2():
    v = 'a'
    yield v
    v = 'b'
    yield v
    v = 'c'
    yield v
    v = 'd'
    yield v

g = gera2()
# for v in g:
#     print(v)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
# print(next(g))  # Se você iterar mais do que o tamamnho do gerador o python vai lhe mostrar uma exceção.

# Nos podemos facilmente transformar um lista em um gerador da seguinte forma:
lista4 = (x for x in range(100000))
print(type(lista4))

# Vamos fazer uma comparação
lista5 = [x for x in range(100000)]

# Observando assim elas parecem identicas, mas a diferença está a seguir:
print(sys.getsizeof(lista4))  # Muito menor
print(sys.getsizeof(lista5))