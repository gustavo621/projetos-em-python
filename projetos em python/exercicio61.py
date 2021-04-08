primeiro = int(input("primeiro termo: "))
razão = int(input("razão: "))
termo = primeiro
cont = 1
while cont <= 10:
    print("{}→".format(termo), end="")
    termo += razão
    cont += 1
print("ACABOU!")