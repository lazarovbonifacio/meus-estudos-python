def exercicio1(saudacao, nome):
    print(f'{saudacao.capitalize()}, {nome.capitalize()}!')

# exercicio1('oi','thiago')

def exercicio2(a,b,c):
    print(a+b+c)

# exercicio2(3,5,7)

def exercicio3(num,porcentage):
    return num*(porcentage+100)/100

# print(exercicio3(100,100))

def exercicio4(num):
    j = "Fizz" if num % 3 == 0 else ""
    i = "Buzz" if num % 5 == 0 else ""
    return num if i+j == "" else j+i
    
# print(exercicio4(25))