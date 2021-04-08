acu = 0
cont = 0
num = int(input("digite um numero e veja sua tabuada: "))
for c in range(1, 110):
    acu = acu + 1
    cont = cont + num
    print("{} x {} = {}".format(acu, num, cont))
