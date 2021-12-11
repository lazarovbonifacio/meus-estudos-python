lista = ['Tiago', 'Lazaro', 'Luis','Pedro']

for nome in lista:
    if nome.lower().startswith('p'):
        pass
        # continue
        # break
    print(nome)
else:  # Se o laco nao for interrompido, execute:
    print("Nao existe palavra que comeca com 'p'")