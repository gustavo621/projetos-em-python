num = cont = soma = 0
num = int(input("digite um numero [999 para parar!]: "))
while num != 999:
    soma = soma + num
    cont = cont + 1
    num = int(input("digite um numero [999 para parar!]: "))
print("você digitou {} numeros e a soma entre eles foi {}".format(cont, soma))