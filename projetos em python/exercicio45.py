import random
pc = ["pedra", "papel", "tesoura"]
pc2 = random.choice(pc)
print('''suas opções:
[ 1 ] pedra
[ 2 ] papel
[ 3 ] tesoura''')
seu = int(input("escolha uma opção: "))
if pc2 == "pedra" and seu == 3:
    print("você perdeu! o pc escolheu pedra")
elif pc2 == "papel" and seu == 1:
    print("você perdeu! o pc escolheu papel")
elif pc2 == "tesoura" and seu == 2:
    print("você perdeu! o pc scolheu tesoura")
elif pc2 == "pedra" and seu == 2:
    print("você ganhou! o pc escolheu pedra")
elif pc2 == "papel" and seu == 3:
    print("você ganhou! o pc escolheu papel")
elif pc2 == "tesoura" and seu == 1:
    print("você ganhou! o pc escolheu tesoura")
elif pc2 == "pedra" and seu == 1:
    print("o jogo deu empate!")
elif pc2 == "papel" and seu == 2:
    print("o jogo deu empate!")
elif pc2 == "tesoura" and seu == 3:
    print("o jogo deu empate!")