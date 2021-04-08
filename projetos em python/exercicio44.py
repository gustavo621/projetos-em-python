preco = float(input("preço das compras(R$): "))
print('''formas de pagamento...
[ 1 ]a vista dinheiro/cheque
[ 2 ] á vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x no cartão''')
opcao = int(input("qual sua opção?: "))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)

elif opcao == 3:
    total = preco
    parcela = total / 2
    print("sua compra será parcelada em 2x de R${:.2f} sem juros!".format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input("quantas parcelas?: "))
    parcela = total / totparc
    print("sua compra será parcelada em {}x de R${:.2f} com juros".format(totparc, parcela))
else:
    total = preco
    print("opção invalida de pagamento!")
print("sua compra de R${:.2f} vai custar R${:.2f} no final".format(preco, total))