from random import randint
v = 0
while True:
    jogador = int(input("digite um valor: "))
    computador = randint(1, 10)
    total = jogador + computador
    tipo = " "
    while tipo not in "PI":
        tipo = str(input("par ou impar? [P/I]: ")).strip().upper()[0]
    print(f"você jogou {jogador} e o computador {computador}. total de {total}", end=" ")
    print("deu par" if total % 2 == 0 else "deu impar")
    if tipo == "P":
        if total % 2 == 0:
            print("você venceu!")
            v += 1
        else:
            print("você perdeu!")
            break
    elif tipo == "I":
        if total % 2 != 0:
            print("você venceu")
            v += 1
        else:
            print("você perdeu!")
            break
    print("vamos jogar novamente...")
print(f"game over. Você venceu {v} vezes!")

