"""
Iterando elementos com 'while'
(Passar por todos os elementos de um conjunto)

Elementos interaveis precisam possuir índece, por exemplo.
"""
# ================ AULA ==================
frase = "o original numa se desoriginaliza"
tamanho_frase = len(frase)
contador = 0
nova_string = ""

input_usuario = input("Qual a letra deseja colocar maiúscula: ")

while contador < tamanho_frase:
    letra = frase[contador]
    if letra == input_usuario:
        nova_string += input_usuario.upper()
    else:
        nova_string += letra
    contador += 1

print(nova_string)

