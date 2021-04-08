from math import radians, sin, cos, tan
ângulo = float(input("Digite o ângulo que você deseja: "))
seno = sin(radians(ângulo))
coseno = cos(radians(ângulo))
tangente = tan(radians(ângulo))
print("O ângulo de {:.0f}º tem o SENO de {:.2f} seu COSENO é {:.2f} e a TANGENTE é {:.2f} ".format(ângulo,seno,coseno,tangente))
