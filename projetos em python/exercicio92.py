from datetime import datetime
dados = dict()
dados["nome"] = str(input("nome: "))
nasc = int(input("ano de nascimento: "))
dados["idades"] = datetime.now().year - nasc
dados["ctps"] = int(input("carteira de trabalho (0 não tem): "))
if dados["ctps"] != 0:
    dados["contratação"] = int(input("ano de contratação: "))
    dados["salário"] = float(input("salario: R$"))
    dados["aposentadoria"] = ((dados["contratação"] + 35) - datetime.now().year)    
print("-=" * 30)
for k, v in dados.items():
    print(f"{k} tem o valor {v}")
