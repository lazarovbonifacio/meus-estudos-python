#!/usr/bin/python
#*-* coding: utf-8 *-*

print("Show do Milhão!")

perguntas = {
    'Pergunta 1': {
        'enunciado':'Quanto é 2 + 2?',
        'alternativas': {'a':'1', 'b': '3', 'c':'4', 'd': '5'},
        'resposta': 'c',
    },
    'Pergunta 2': {
        'enunciado':'Quanto é 2 * 4?',
        'alternativas': {'a':'8', 'b': '3', 'c':'5', 'd': '4'},
        'resposta': 'a',
    },
}

respostas_certas = 0
for pk, pv in perguntas.items():
    print(f"\n{pk}: {pv['enunciado']}")

    print("Alternativas")
    for ak, av in pv['alternativas'].items():
        print(f"{ak}) {av}")
    
    resposta_usuario = input("\nSua resposta: ")

    if resposta_usuario == pv['resposta']:
        respostas_certas += 1
        print('Correto!')
    else:
        print('Errado!')
    