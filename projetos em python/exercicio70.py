total = totmil = menor = cont = 0
barato = " "
while True:
    produlto = str(input("nome do produlto?: "))
    preço = float(input("preço: R$"))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produlto
    resp = " "
    while resp not in "SN":
        resp = str(input("quer cotinuar?: [S/N]")).strip().upper()[0]
    if resp == "N":
        break
print("{:-^40}".format("fim do programa!"))
print(f"o total da compra foi R${total:.2f}")
print(f"temos {totmil} produltos custando mais de R$1000,00")
print(f"o produlto mais barato foi {barato} que custa R${menor:.2f}")
