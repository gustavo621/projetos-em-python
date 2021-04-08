frase = str(input("digite uma frase: ")).strip().upper()
palavra = frase.split()
junto = "".join(palavra)
inverso = ""
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print("o inverso de {} é {}".format(junto, inverso))
if inverso == junto:
    print("temos um palidromo!")
else:
    print("a frase digitada não é um palidromo!")
#ou vc pode colocar
#inverso = junto[::-1] no lugar do inverso normal e tira todo o comando for!



