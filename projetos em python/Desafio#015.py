print("====================ALUGUEL DE CARROS====================")
print(" ")
alug = int(input("Quantos dias alugados? "))
KMs = int(input("Quntos km rodados? "))
pago = alug * 60
print("O total a pagar é de R${:.2f}".format(pago))
