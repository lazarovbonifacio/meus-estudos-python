
familia_do_noivo = ['Pai', 'Mae', 'Irmao', 'Magna', 'Mariana']
parentes_do_noivo = ['Amanda', 'Natalia', 'Walkiria?', 'Emerson?', 'Agata?', 'Heitor?', 'Vô Joao', 'Vo Lidia', 'Iara', 'Samuel', 'Felipe', 'Debora', 'Primo do tio Luiz', 'Prima do tio Luiz', 'Vô Rodrigo', 'Vovo Neves', 'Alisson', 'Namora de alisson', 'Vo carminha', 'Vo Bras']
amigos_do_noivo = ['Daniel', 'Larissa', 'Lais?', 'Juninho', 'Jamylle', 'Amanda', 'Mirtis', 'Alexandre?', 'Everton', 'Namorada de Everton?', 'David?', 'Namorada de David?', 'Roseli']
amigos_do_trabalho = ['Bruno', 'Alessandra', 'Maria', 'Namorado de maria?', 'Rodrigo?', 'Wlademir?', 'Namorada de Wlademir?', 'Rosiery?', 'Esposo de Rosiery?', 'Filha de rosy Bruna?', 'Filha de rosy Lara?', 'Isaac?', 'Joao Vitor?']

familia_da_noiva = ['Aille', 'Joao', 'Gabriel', 'Camille', 'Vo Gorett', 'Jose', 'Reinaldo', 'Caninde', 'Jaciara', 'Vitoria']
parentes_da_noiva = ['Vo Chiquita?', 'Enilson?', 'Gordinho?']
amigos_da_noiva = ['Lara', 'Natan', 'Gorett', 'tais', 'boy de tais', 'clara', 'boy de clara', 'uesilei', 'Mizael', 'Vanessa?', 'boy de Vanessa?', 'Amanda', 'boy de Amanda', ' ticinha', 'Gabriel', 'Jessica', 'Jaqueline Mizael', 'clara Fidelis?', 'Joao olimpio', 'Gabi', 'Jussara', 'Namorado de Jussara', 'Tabata', 'Vitor', 'Leticia', 'Naka']

convidados = []
convidados.extend(familia_do_noivo + parentes_do_noivo + amigos_do_noivo + amigos_do_trabalho + familia_da_noiva + parentes_da_noiva + amigos_da_noiva)
#convidados_bia.extend(familia_da_noiva, parentes_da_noiva, amigos_da_noiva)

convidados_por_educacao = []

for convidado in convidados :
    if "?" in convidado :
        convidados_por_educacao.append(convidado)

print(f'Quantidade de convidados: {len(convidados)}')
print(f'Convidados por educação: {len(convidados_por_educacao)}')
print(f'Convidados prováveis: {len(convidados) - len(convidados_por_educacao)}')
print(f"lista de convidados: {', '.join(convidados)}.")
print(f'Amigos da noiva: {len(amigos_da_noiva)}')
print(f'Amigos  do noivo: {len(amigos_do_noivo)+len(amigos_do_trabalho)}')
