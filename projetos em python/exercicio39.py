from datetime import date
atual = date.today().year
sex = str(input("você é de que sexo?: ")).lower().strip()
if sex == "feminino":
    print("você não precisa se alistar!")
if  sex == "masculino":
    nasc = int(input("em que ano você nasceu?: "))
    idade = atual - nasc
    print("quem nasceu em {} tem {} anos em {}".format(nasc, idade, atual))
    if idade == 18:
            print("você tem que se alistar imediatamente")
    elif idade < 18:
        saldo = 18 - idade
        print("você ainda não tem 18 anos, ainda faltam {} para o alistamento".format(saldo))
        ano = atual + saldo
        print("seu alistamento será em {} ".format(ano))
    elif idade > 18:
        saldo = idade - 18
        print("você ja deveria ter se alistado há {} anos".format(saldo))
        ano = atual - saldo
        print("seu alistamento foi em {} ".format(ano))

