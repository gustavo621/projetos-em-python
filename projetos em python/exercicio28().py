from random import randint
from time import sleep
computador = randint(0,5)# faz o computador "pensar"
print("-=-" * 20)
print("vou pensar em um numero entre 0 e 5. Tente adivinhar...")
print("-=-" * 20)
jogador = int(input("em que numero eu pensei?: ")) # o jogador tenta adivinhar
print("processando...")
sleep(2)
if jogador == computador:
    print("parabéns! você conseguiu me vencer!")
else:
    print("ganhei! eu pensei no numero {} e não no {}!".format(computador, jogador))
