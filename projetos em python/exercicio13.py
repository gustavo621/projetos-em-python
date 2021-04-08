pipoca = str(input("escreva qualquer numero real: ")).strip()
if "/" in pipoca:
    vdc = int(pipoca[0:1]) / int(pipoca[2:])
    if vdc > 0.5:
        print('o numero inteiro mais proximo é {:.1f}'.format(vdc))
    else:
        print("o resultado da fração foi {}".format(vdc))


