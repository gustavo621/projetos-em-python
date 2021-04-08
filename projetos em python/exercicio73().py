tabela = "flamengo", "gremio", "internacional", "palmeiras", "atletico-go", "america-mg", "bahia", "paraná", "vasco", "são paulo", "cruseiro", "avai", "santos", "fluminence", "bota-fogo", "corintians", "atletico-pr", "america-mg", "chapecoence", "ceará sc", "sporte recife"
print("-=-=-=-=-=-=-=-=OS_5_PRIMEIROS_COLOCADOS-=-=-=-=-=-=-=-=")
print("1° {}".format(tabela[0]))
print("2° {}".format(tabela[1]))
print("3° {}".format(tabela[2]))
print("4° {}".format(tabela[3]))
print("5° {}".format(tabela[4]))
print("-=-=-=-=-=-=-=-=OS_4_ULRIMOS_COLOCADOS-=-=-=-=-=-=-=-=")
print("17° {}".format(tabela[-4]))
print("18° {}".format(tabela[-3]))
print("19° {}".format(tabela[-2]))
print("20° {}".format(tabela[-1]))
print("-=-=-=-=-=-=-=-=A_TABELA_EM_ORDEM-=-=-=-=-=-=-=-=")
print(sorted(tabela))
print("-=-=-=-=-=-=-=-=COLOCAÇÃO_DA_CHAPECOENSE-=-=-=-=-=-=-=-=")
for c in tabela:
    if c == "chapecoense":
        break
print(f"o time chapecoense está na posição {c}")
