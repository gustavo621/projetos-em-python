import random
nome1 = input("primeiro nome: ")
nome2 = input("segundo nome: ")
nome3 = input("terceiro nome: ")
nome4 = input("quarto nome: ")
lista = [nome1,nome2,nome3,nome4]
escolhido = random.choice(lista)
print("o aluno escolhido foi {}".format((escolhido)))
