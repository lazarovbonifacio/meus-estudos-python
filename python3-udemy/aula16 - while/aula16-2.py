"""
Contadores e acumuladores
"""
contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)
    
    if contador > 8:
        break

    acumulador += contador
    contador += 1
else:
    print("O 'else' em uma função while só é executado quando a condição se tornar falsa")

print("Quando o 'while' termina em 'break' o 'else' não é executado")