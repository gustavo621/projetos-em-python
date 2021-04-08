lista = []
mai = 0
men = 0
for c in range(0, 5):
    lista.append(int(input(f'digite um valor para a posição {c}: ')))
    if c == 0:
        mai = men = lista[c]
    else:
        if lista[c] > mai:
            mai = lista[c]
        if lista[c] < men:
            men = lista[c]
print("=-"*30)
print(f"você digitou os valores {lista}")
print(f"o maior digitado foi {mai} nas posições ", end='')
for i, v in enumerate(lista):
    if v  == mai:
        print(f"{i}... ", end='')
print()
print(f"o menor valor digitado foi {men} nas posições ", end='')
for i, v in enumerate(lista):
    if v == men:
        print(f"{i}... ", end='')
print()
