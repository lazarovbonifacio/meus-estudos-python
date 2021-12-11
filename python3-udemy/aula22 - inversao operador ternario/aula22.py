"""
Como inverter o valor de 2 variáveis
"""
x = 10
y = 'Lázaro'
x, y = y, x

print(f'x={x}, y={y}')

"""
Operador ternário
"""
# ==== BRUTO ====

# logado = True

# if logado:
#     msg = "Oi!"
# else:
#     msg = "Logar agora."

# print(msg)

# ==== REFINADO ====

logado = True

msg = "Oi!" if logado else "Logar agora."

print(msg)