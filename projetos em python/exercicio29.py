n1 = int(input("digite o valor de quantos km/h o carro estava: "))
if n1 <= 80:
     print("parabéns, você estava na velocidade certa")
else:
     print("você estava mais rápido que a velocidade permitida, você receberá uma multa de R$5 por cada km rodado")
     n2 = n1*7
     print("multa: R$", n2)
