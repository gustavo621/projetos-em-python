import random
n11 = 1
n12 = 2
n13 = 3
n14 = 4
n15 = 5
lista = [n11, n12, n13, n14, n15]
escolhido = random.choice(lista)
n1 = int(input("digite o numero que você acha que é: "))
if n1 == escolhido:
    print("parabéns faustão você acertou!")
else:
    print("você não acertou, o pc ganhou de você!  :(")