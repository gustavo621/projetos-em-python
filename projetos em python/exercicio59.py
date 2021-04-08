n1 = float(input("digite um numero: "))
n2 = float(input("digite outro numero: "))
print("[ 1 ] somar")
print("[ 2 ] multiplicar")
print("[ 3 ] maior")
print("[ 4 ] novos numeros")
print("[ 5 ] sair do programa")
opcao = int(input("qual é a sua opção: "))
while opcao != 5:
    if opcao == 1:
        soma = n1+n2
        print("a soma entre {} e {} é igual a {}".format(n1, n2, soma))
    elif opcao == 2:
        mult = n1*n2
        print("a multiplicação entre {} e {} é igual a {}".format(n1, n2, mult))
    elif opcao == 3:
        if n1>n2:
            print("{} é maior que {}".format(n1, n2))
        else:
            print("{} é maior que {}".format(n2, n1))
    elif opcao == 4:
        n1 = float(input("digite um numero: "))
        n2 = float(input("digite outro numero: "))
        print("[ 1 ] somar")
        print("[ 2 ] multiplicar")
        print("[ 3 ] maior")
        print("[ 4 ] novos numeros")
        print("[ 5 ] sair do programa")
        opcao = int(input("qual é a sua opção: "))
        while opcao != 5:
            if opcao == 1:
                soma = n1 + n2
                print("a soma entre {} e {} é igual a {}".format(n1, n2, soma))
            elif opcao == 2:
                mult = n1 * n2
                print("a multiplicação entre {} e {} é igual a {}".format(n1, n2, mult))
            elif opcao == 3:
                if n1 > n2:
                    print("{} é maior que {}".format(n1, n2))
                else:
                    print("{} é maior que {}".format(n2, n1))
        print("fim do programa!")
print("fim do programa!")