from itertools import groupby,tee

# Se você quer agrupar os alunos por nota, o modulo groupby precisa que as notras estajam todas ordenadas
alunos = [
    {'nome':'Lazaro','nota':'A'},
    {'nome':'Ana','nota':'B'},
    {'nome':'Apolo','nota':'B'},
    {'nome':'Gabriel','nota':'A'},
    {'nome':'Beatriz','nota':'B'},
    {'nome':'Vinícius','nota':'A'},
    {'nome':'Selena','nota':'C'},
    {'nome':'Lídia','nota':'D'},
    {'nome':'Micael','nota':'F'},
    {'nome':'João','nota':'C'},
]

alunos.sort(key=lambda item: item['nota'])
alunos_agrupados = groupby(alunos, lambda item: item['nota'])

for grupo, grupo_alunos in alunos_agrupados:
    va1, va2 = tee(grupo_alunos)  # grupo_alunos é iterador, por isso precisamos copiá-lo para as duas variáveis
    print(grupo, len(list(va1)))

    for i in va2:
        print(i)
