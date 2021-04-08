num = cont = 0
while True:
    num = int(input("digite um numero e veja sua tabuada: "))
    print("=" * 30)
    if num < 0:
        break
    for c in range (1, 11):
        print(f"{num} x {c} = {c*num}")
    print("="*30)
print("programa encerrado, volte sempre!")