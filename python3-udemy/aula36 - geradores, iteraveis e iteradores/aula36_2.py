# Listas, tuplas e strings -> Sequencias -> iteraveis
nome = "Lázaro Vinícius"

for letra in nome:
    print(letra)
print("#"*72)
for letra in nome:
    print(letra)

# o 'for' converter o iteravle em iterador, e vai usar a função next até a exceção 'stopIteration'.
# Você pode fazer o 'for' manualmente
iterador = iter(nome)
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))

print("Acima: iterador manual | Abaxio: laço 'for'")

for i in iterador:
    print(i)  # Como você ainda nõa consumiu todo o iterador ele ainda tem alguns valores

gerador = (letra for letra in nome)

# Geradores e iteradores foram feitos para você consumir os valores que eles recebem e até o fim.

## Comentário resumido do professor

# Iteráveis - Qualquer elemento que possa ser iterado. Por "ser iterado" quero dizer, que possa retornar um elemento por vez... Exemplos de iteráveis: listas e strings.
# Resumindo:  um iterável é capaz de lhe entregar um elemento por vez a cada iteração.
# Iterador - Um objeto capaz de ler um item por vez de um iterável. Um iterador é capaz de "puxar" um elemento de um iterável e entregar este valor para seu código. O fato sobre os iteradores é mais complexo porque você ainda não aprendeu a criar "iteradores", você usa o "for" que usa um "iterador" padrão para obter um valor por vez de um iterável. Mas vamos aprender a fazer isso na aula sobre "protocolos" dos iteradores.
# Mas para resumir, quando você usa o for, o for "pede" para o seu iterável o objeto iterador dele. Esse objeto é capaz de capturar um elemento por vez do seu iterável para que o for possa fazer algo com ele.
# Gerador - Um gerador é um tipo especial de iterador que trabalha um pouquinho diferente... Um gerador é uma função capaz de ser "pausada" a cada chamada do "yield". Quando essa função é executada, na primeira vez que o yield for chamado, ele entrega o valor e pausa a função ali. Na segunda vez que a função for chamada, o próximo yield será encarregado de entregar o valor (e assim vai até quando você quiser). Você pode criar uma função que retorna valores infinitos.
# É basicamente isso, não tem muito mais o que falar sobre iteráveis, iteradores e geradores.
