#!/usr/bin/python
#*-* coding: utf-8 *-*

t1 = (1,2,3,'a','Lázaro',-6)  # Tupla explicita
t2 = 3,-7,54,'r'  # Pode ser criada sem virgula
t3 = 1,   # Tupla de um elemento

for item in t1:
    print(item)

t4 = t1 + t2
t5 = list(t4)  # Transforme uma tupla em lista
t6 = tuple(t5)  # Transforme uma lista em tupla