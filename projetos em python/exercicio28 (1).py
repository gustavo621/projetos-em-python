import random
import time
print("-=-"*20)
print("{}vou pensar em um numero entre 0 e 5. tente adivinhar...{}".format("\033[35m","\033[m"))
print("-=-"*20)
numero = int(input("em que numero eu pensei? "))
print("{}processando...{}".format("\033[36m", "\033[m"))
time.sleep(3)
numero1 = random.randint(0, 6)
if numero < 0 and numero > 5:
    print("{}este numero não está entre o intervalo de 0 e 5. tente novamente!{}".format("\033[34m", "\033[m"))
if numero == numero1:
    print("{}parabéns você acertou!{}".format("\033[34m", "\033[m"))
elif numero != numero1:
    print("{}numero errado{}".format("\033[34m", "\033[m"))

    
