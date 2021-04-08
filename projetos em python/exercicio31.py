viagem = int(input("digite quantos km você irá percorrer nesta viagem: "))
if viagem <= 200:
    viagem2 = viagem*0.50
    print("uma viagem de até 200 km, se paga 50 centavos por km rodado")
    print("portanto o preço a pagar será igual á: R${}".format(viagem2))
else:
    viagem3 = viagem*0.45
    print("uma viagem com mais de 200 km, se paga 45 centavos por km rodado")
    print("portanto o preço a se pagar será igual á: R${}".format(viagem3))
