n1 = float(input("primeira nota: "))
n2 = float(input("segunda nota: "))
med = (n1+n2)/2
if med >= 7:
    print("tirando {} e {} a média é {:2.1f}".format(n1, n2, med))
    print("você foi aprovado!")
elif med == 7:
    print("tirando {} e {} a média é {:2.1f}".format(n1, n2, med))
    print("você está aprovado!")
else:
    print("tirando {} e {} a média é {:2.1f}".format(n1, n2, med))
    print("você está REPROVADO!")