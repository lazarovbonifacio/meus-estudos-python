import datetime

nome = 'Lázaro'
idade = 20
altura = 1.81
peso = 90
imc = peso/altura**2
ano_atual = datetime.date.today().year
ano_nascimento = int(ano_atual) - idade
print(f"{nome} tem {idade} anos, {altura}m de altura e pesa {peso}Kg.\nSeu IMC é {imc:.2f}.\nEle nasceu em {ano_nascimento}.")