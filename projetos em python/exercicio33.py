a = int(input("digite um numero: "))
b = int(input("digite outro numero: "))
c = int(input("digite outro numero: "))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print("o menor valor digitado foi {}".format(menor))
print("o meior valor digitado foi {}".format(maior))
