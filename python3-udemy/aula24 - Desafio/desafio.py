"""
DESAFIO: um contador progressivo e regressivo
0 10
1 9
2 8
3 7
4 6
5 5
6 4
7 3
8 2
"""

# ==== MINHA SOLUÇAO ====

contd = 10

while True:
    contc = 10
    contc -= contd
    print(contc,contd)
    if contd == 2 and contc == 8:
        break
    contd -= 1    

# ==== PROFESSOR ====

for p, r in enumerate(range(10,1,-1)):
    print(p, r)