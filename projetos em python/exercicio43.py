peso = float(input("digite aqui o seu peso(kg): "))
altura = float(input("digite sua altura: "))
imc = peso/altura**2
print("seu imc é {:3.2f}".format(imc))
if imc < 18.5:
    print("você está abaixo do peso")
elif 18.5 <= imc < 25:
    print("parabéns, você está no peso ideal!")
elif 25 <= imc < 30:
    print("sobrepeso")
elif 30 <= imc < 40:
    print("você está obeso")
elif imc >= 40:
    print("obesidade morbida!")