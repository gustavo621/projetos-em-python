temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input("nome: ")))
    temp.append(float(input("peso")))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    prnc.append(temp[:])
    resp = str(input("quer continuar? [S/N] "))
    if resp in "Nn":
        break
print("-="*30)
print(f"ao todo, você cadastrou {len(princ)} pessoas.")
print(f"o maior peso foi de {mai}kg. peso de" , end="")
for p in princ:
    if p[1] == mai:
        print(f"{p[0]}", end="")
print()
print(f"o menor peso foi de {men}kg. peso de", end="")
for p in princ:
    if p[1] == men:
        print(f"[{p[0]}]", end="")
print()
