n1 = int(input("digite a base do triangulo: "))
n2 = int(input("digite um dos lados do triangulo: "))
n3 = int(input("digite outro lado do trinagulo: "))
if n2 < n1 + n3 and n2 > n1 - n2 - n3:
    print("esses lados podem formar um triangulo!")
    if n1 == n2 and n1 == n3:
        print("esse triangulo é equilatero!")
    elif n2 == n3 and n2 != n1:
        print("esse triangulo é isósceles!")
    else:
        print("esse triangulo é escaleno!")
else:
    print("esses lados não da condição para formar um triangulo!")