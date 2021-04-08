num1 = int(input("digite o primeiro numero: "))
num2 = int(input("digite o segundo numero: "))
if num1 > num2:
    print("o valor {} é maior que o valor {}!".format(num1, num2))
elif num2 > num1 :
    print("o valor {} é maior que o valor {}!".format(num2, num1))
else:
    print("não existe valor maior ou menor, os dois valores são iguais!")