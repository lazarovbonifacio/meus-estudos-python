hora = input("Que horas são? (Ex.: 0-23)\nHora: ")

try:
    hora = int(hora)
    if hora >= 6 and hora <= 11:
        print("Bom dia pra quem?")
    elif hora >= 12 and hora <= 17:
        print("Boa tarde!")
    elif hora >= 18 and hora <= 23:
        print("Boa noiteeeeeeee!")
    elif (hora >= 0 and hora <=5) or hora == 24:
        print("A noite é uma criança, bebé!")
    else:
        print("WTF, man? Tá doidão? kkkkkkkkkkkkkkkk")
except:
    print("Digite um valor válido.")
