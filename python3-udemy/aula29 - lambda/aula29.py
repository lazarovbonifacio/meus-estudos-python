#!/usr/bin/python
#*-* coding: utf-8 *-*

# Função anônima - Expressões lambda

a = lambda x, y: x*y
print(a(3,6))

lista = [['P3',35],['P1',13],['P2',24],['P5',57],['P4',46]]

print(sorted(lista, key=lambda i: i[1]))  # Não altera a lista

lista.sort(key=lambda item: item[1], reverse=True)
print(lista)

