numero = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezeseis", "dezesete", "dezoito", "dezenove", "vinte")
while True:
    num = int(input("digite um numero entre 0 e 20: "))
    if 20 >= num >= 0:
        break
    print("numero invalido. Tente novamente!.", end="")
print(f"o numero digitado foi {numero[num]}")


