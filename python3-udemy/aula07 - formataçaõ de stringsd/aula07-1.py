nome = "Lázaro"
idade = 20
altura = 1.81
peso = 91
imc = peso/altura**2

print(nome,'tem',idade,'anos de idade e seu IMC é', imc)
print(f'{nome} tem {idade} anos de idade e seu IMC é {imc:.2f}')
print('{} tem {} anos de idade e sei IMC é {:.2f}'.format(nome,idade,imc))
print('{n} tem {i} anos de idade e sei IMC é {r:.2f}'.format(n=nome,i=idade,r=imc))