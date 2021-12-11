guess = 0
chance = 0
chances = 8
number = 87

while guess != number and chance < chances:
    if chance == 0:
        guess = int(input("Adivinha o numero que eu estu pensando, de 0-100: "))
    else:
        guess = int(input(f"Tu tem mais {chances - chance} chances, de 0-100: "))

    if guess > (number + 10):
        print("Passou muito, burro!")
    if guess < (number - 10):
        print("Desceu demais, burro!")
    if guess > number and guess < (number + 10):
        print("Desce um pouco")
    if guess < number and guess > (number - 10):
        print ("Sobe um pouco")
    chance+=1

if guess == number: 
    print("Acertou, miseravi! Cê é o bichão mesmo, hein.")
else:
    print("Mano, cê tem demencia? Tu é ruim, errou tudo!")