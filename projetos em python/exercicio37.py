n1 = int(input("digite aqui o valor que você quer converter: "))
print("escolha uma das bases para a converção:")
print("[ 1 ] para base binário")
print("[ 2 ] para base octal")
print("[ 3 ] para base hexadecimal")
opcao = int(input("qual a sua opção?: "))
if opcao == 1:
    print("{} convertido para binário é {} ".format(n1, bin(n1)[2:]))
elif opcao == 2:
    print("{} convertido para octal é {}".format(n1, oct(n1)[2:]))
elif opcao == 3:
    print("{} convertido para hexadecimal é {}".format(n1, hex(n1)[2:]))
else:
    print("opção inválida. tente novamente!")

