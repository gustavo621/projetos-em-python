import math
co = float(input("Qual o comprimento do cateto oposto? "))
ca = float(input("Qual o comprimento do cateto adjacente? "))
hi = math.hypot(co,ca)
print("A hipotenusa é: {:.2f}".format(hi))
