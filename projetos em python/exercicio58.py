import random
vrau = random.randint(0, 10)
print("sou seu computador... acabei de pensar em um numero entre 0 e 10")
print("será que você consegue adivinhar qual foi? ")
acertou = False
palpites = 0
while not acertou:
    n = int(input("qual é o seu palpite?: "))
    palpites = palpites + 1
    if n == vrau:
        acertou = True
    else:
        if n < vrau:
            print("mais...")
        elif n > vrau:
            print("menos...")
print("acertou com {} tentativas".format(palpites))