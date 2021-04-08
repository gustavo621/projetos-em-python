casa = float(input("qual é o valor da casa?: "))
salar = float(input("quanto você ganha por mês?: "))
anos = int(input("em quantos anos você quer pagaar a casa?: "))
parcela = casa/(anos*12)
porc = salar*30/100
if parcela <= porc:
    print("você poderá pagagar o valor da parcela!")
    print("o valor da parcela será %.2f" % parcela)
else:
    print("não será possivel pagar o valor da parcela, pois o valor da parcela é maior do que 30% do seu salário!")
    print("%.2f" % parcela)
