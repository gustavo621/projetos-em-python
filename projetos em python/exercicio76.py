listagem = ("lapis", 1.75,
            "borracha", 2.00,
            "caderno", 15.90,
            "estojo", 20.00,
            "merda enlatada", 1.50,
            "cabo daciolo", 13.00,
            "bucho de bode", 25.00,
            "trapesio", 6.00,
            "descendente", 8.00)
print("-"*40)
print(f"{'LISTAGEM DE PREÇOS':^40}")
print("-"*40)

for item in range(0, len(listagem)):
    if item % 2 == 0:
        print(f"{listagem[item]:.<30}", end="")
    else:
        print(f"R${listagem[item]:>6.2f}")
print("-"*40)