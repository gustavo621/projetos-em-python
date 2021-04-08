num = soma = cont = 0
while True:
    num = int(input("digite um valor (999 para parar): "))
    if num == 999:
        break
    soma += num
    cont += 1
print(f"foram usados {cont} numeros, e sua soma é igual á {soma}")

