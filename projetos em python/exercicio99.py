from time import sleep


def maior(* num):
    cont = maior = 0
    print("-=" * 30)
    print("Analisando os valores pasados..")
    for valor in num:
        print(f"{valor}", end="", flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                cont += 1
    print(f"foram informados {cont} valores ao todo.")
    print(f"o maior valor informado foi {maior}.")

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()