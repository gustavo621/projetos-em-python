nome = str(input("escreva seu nome completo: ")).strip()
n = nome.split()
print("ANALIZANDO SEU NOME...")
print("seu primeiro nome é: {}".format(n[0]))
print("seu ultimo  nome é: {}".format(n[len(n)-1]))

