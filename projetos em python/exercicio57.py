sexo = str(input("informe seu sexo [M/F]: ")).strip().upper()[0]
while sexo not in "MmFf":
    sexo = str(input("sexo invalido, informe seu sexo novamente: ")).strip().upper()[0]
print("sexo {} resistrado com sucesso".format(sexo))
