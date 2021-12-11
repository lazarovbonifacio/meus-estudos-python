import datetime

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
ano_atual = datetime.date.today().year
ano_nascimento = int(ano_atual) - int(idade)

print(f'\n{nome} tem {idade} anos. Nascido em {ano_nascimento}')