import aula46_3.calc_precos

preco = 49.90

preco_aumentado = aula46_3.calc_precos.aumento(preco, 15, True)
print(preco_aumentado)

preco_descontado = aula46_3.calc_precos.desconto(preco, 15)
print(preco_descontado)