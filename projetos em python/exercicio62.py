primeiro = int(input("primeiro termo: "))
razão = int(input("razão: "))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print("{}→".format(termo), end="")
        termo += razão
        cont += 1
    print("pausa")
    mais = int(input("quantos termos você quer mostrar a mais? "))
print("a progreção realiada com {} trmos mostrados".format(total))