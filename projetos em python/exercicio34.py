salar = int(input("digite seu salário aqui: "))
if salar > 1250:
   salar2 = salar+(salar*10/100)
   print("salários superiores a R$1250 irão receber um acrecimo de 10%")
   print("portanto seu salário de {} com o acrecimo de 10% será igual á {}".format(salar, salar2))
else:
    salar3 = salar+(salar*15/100)
    print("salários inferiores a R$1250 irão receber um acrecimo de 15%")
    print("portanto seu salario de {} com o acrecimo de 15% será igual á {}".format(salar, salar3))
