import math

PI = math.pi

def pares(lista):
    pares = list()
    for i in lista:
        if i % 2 == 0:
            pares.append(True)
        else:
            pares.append(False)
    return pares

def multiplica(lista):
    r = 1
    for i in lista:
        r = r * i
    return r

if __name__ == "__main__":  # Artificio utilizado para não executar determinada parte do modulo se ele for importado
    lista = [1,2,3,4,5,6]
    print(PI)
    print(pares(lista))
    print(multiplica(lista))