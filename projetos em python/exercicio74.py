from random import randint
n = (randint(1,10), randint(1,10), randint(1,10), randint(1,10) ,randint(1,10))
print(f"os valores sorteados foram: ", end="")
for numeros in n:
    print(f"{numeros} ", end="")
print(f"\no maior valor sorteado foi {max(n)}")
print(f"o menor valor sorteado foi {min(n)}")