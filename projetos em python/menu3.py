import webbrowser
print("{}=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~{}".format("\033[32m", "\033[m"))
print("{}~~~SEJA BEM VINDO(A) AO MUNDO DO OURO~~~{}".format("\033[32m", "\033[m"))
print("{}=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~{}".format("\033[32m", "\033[m"))
while True:
    opcao = int(input("""{}
    ESCOLHA UMA OPÇÂO PARA JOGAR: {}
             {}SAIR{} {}[ 0 ]{}
            {}JOGAR{} {}[ 1 ]{}
    {}CONSIDERAÇÔES{} {}[ 2 ]{}
    
    {}digite sua opção aqui: {}""".format("\033[32m", "\033[m", "\033[31m", "\033[m", "\033[32m", "\033[m", "\033[32m", "\033[m" , "\033[32m", "\033[m", "\033[35m", "\033[m", "\033[32m", "\033[m", "\033[32m", "\033[m")))
    if opcao == 0:
        print("""{}
+---------------------------------------------------+
|JOGO FINALIZADO COM SUCESSO! OBRIGADO PELA ATENÇÂO!|
+---------------------------------------------------+{}""".format("\033[31m", "\033[m"))
        break
    elif opcao == 1:
        print("{}=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~{}".format("\033[36m", "\033[m"))
        print("{}~~~~~~~~~~~~~~MUNDO DO FOGO~~~~~~~~~~~~~{}".format("\033[36m", "\033[m"))
        print("{}=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~{}".format("\033[36m", "\033[m"))
        print("""
{}[o MUNDO DO FOGO tem 36 fases (do 36 ao 71).]
[Para jogar, escolha uma fase!]{}
                                    """.format("\033[31m", "\033[m"))
        opcao1 = int(input("ECOLHA UMA FASE: "))
        while True:
            if opcao1 == 72:
                import exercicio72
                webbrowser.open("https://www.youtube.com/watch?v=IV13X0QOMU8&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=4")
                opcao = int(input("""{}
                            +---------------------------------+
                            |ESCOLHA UMA OPÇÂO PARA JOGAR:    |{}
                            {}|{}    {}SAIR MENU{} {}[ 0 ]{}              {}|{}
                            {}|{}    {}CONTINUAR{} {}[ 1 ]{}              {}|{}
                            {}|{}{}CONSIDERAÇÔES{} {}[ 2 ]{}              {}|{}
                            {}|{}   {}VER CODIGO{} {}[ 3 ]{}              {}|{}
                            {}|{}                                 {}|{}
                            {}|{}{}digite sua opção aqui: {}          {}|{}
                            {}+---------------------------------+: {}""".format("\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[37m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[36m", "\033[m",
                                                                                "\033[35m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m", "\033[32m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m")))
                if opcao == 0:
                    break
                elif opcao == 1:
                    opcao1 = int(input("ECOLHA UMA FASE: "))
                elif opcao == 2:
                    import consideracoes
                elif opcao == 3:
                    fou = open("exercicio36.py", "r")
                    for c in fou.readlines():
                        print(c)
                    fou.close()
                else:
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
                    print("{}o MENU não tem essa opção. Tente novamente!{}".format("\033[31m", "\033[m"))
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
            elif opcao1 == 73:
                import exercicio73
                webbrowser.open("https://www.youtube.com/watch?v=B3F0IjH5WAM&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=5")

                opcao = int(input("""{}
                            +---------------------------------+
                            |ESCOLHA UMA OPÇÂO PARA JOGAR:    |{}
                            {}|{}    {}SAIR MENU{} {}[ 0 ]{}              {}|{}
                            {}|{}    {}CONTINUAR{} {}[ 1 ]{}              {}|{}
                            {}|{}{}CONSIDERAÇÔES{} {}[ 2 ]{}              {}|{}
                            {}|{}   {}VER CODIGO{} {}[ 3 ]{}              {}|{}
                            {}|{}                                 {}|{}
                            {}|{}{}digite sua opção aqui: {}          {}|{}
                            {}+---------------------------------+: {}""".format("\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[37m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[36m", "\033[m",
                                                                                "\033[35m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m", "\033[32m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m")))
                if opcao == 0:
                    break
                elif opcao == 1:
                    opcao1 = int(input("ECOLHA UMA FASE: "))
                elif opcao == 2:
                    import consideracoes
                elif opcao == 3:
                    fou = open("exercicio37.py", "r")
                    for c in fou.readlines():
                        print(c)
                    fou.close()
                else:
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
                    print("{}o MENU não tem essa opção. Tente novamente!{}".format("\033[31m", "\033[m"))
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))

            elif opcao1 == 74:
                import exercicio74
                webbrowser.open("https://www.youtube.com/watch?v=iuPbB9uHczM&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=6")
                opcao = int(input("""{}
                            +---------------------------------+
                            |ESCOLHA UMA OPÇÂO PARA JOGAR:    |{}
                            {}|{}    {}SAIR MENU{} {}[ 0 ]{}              {}|{}
                            {}|{}    {}CONTINUAR{} {}[ 1 ]{}              {}|{}
                            {}|{}{}CONSIDERAÇÔES{} {}[ 2 ]{}              {}|{}
                            {}|{}   {}VER CODIGO{} {}[ 3 ]{}              {}|{}
                            {}|{}                                 {}|{}
                            {}|{}{}digite sua opção aqui: {}          {}|{}
                            {}+---------------------------------+: {}""".format("\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[37m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[36m", "\033[m",
                                                                                "\033[35m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m", "\033[32m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m")))
                if opcao == 0:
                    break
                elif opcao == 1:
                    opcao1 = int(input("ECOLHA UMA FASE: "))
                elif opcao == 2:
                    import consideracoes
                elif opcao == 3:
                    fou = open("exercicio38.py", "r")
                    for c in fou.readlines():
                        print(c)
                    fou.close()
                else:
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
                    print("{}o MENU não tem essa opção. Tente novamente!{}".format("\033[31m", "\033[m"))
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
            elif opcao1 == 75:
                import exercicio75
                webbrowser.open("https://www.youtube.com/watch?v=ePwP4gU_waY&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=7")

                opcao = int(input("""{}
                            +---------------------------------+
                            |ESCOLHA UMA OPÇÂO PARA JOGAR:    |{}
                            {}|{}    {}SAIR MENU{} {}[ 0 ]{}              {}|{}
                            {}|{}    {}CONTINUAR{} {}[ 1 ]{}              {}|{}
                            {}|{}{}CONSIDERAÇÔES{} {}[ 2 ]{}              {}|{}
                            {}|{}   {}VER CODIGO{} {}[ 3 ]{}              {}|{}
                            {}|{}                                 {}|{}
                            {}|{}{}digite sua opção aqui: {}          {}|{}
                            {}+---------------------------------+: {}""".format("\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[37m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[36m", "\033[m",
                                                                                "\033[35m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m", "\033[32m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m")))
                if opcao == 0:
                    break
                elif opcao == 1:
                    opcao1 = int(input("ECOLHA UMA FASE: "))
                elif opcao == 2:
                    import consideracoes
                elif opcao == 3:
                    fou = open("exercicio39.py", "r")
                    for c in fou.readlines():
                        print(c)
                    fou.close()
                else:
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
                    print("{}o MENU não tem essa opção. Tente novamente!{}".format("\033[31m", "\033[m"))
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
            elif opcao1 == 76:
                import exercicio76
                webbrowser.open("https://www.youtube.com/watch?v=QuWDyUeoaJs&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=8")

                opcao = int(input("""{}
                            +---------------------------------+
                            |ESCOLHA UMA OPÇÂO PARA JOGAR:    |{}
                            {}|{}    {}SAIR MENU{} {}[ 0 ]{}              {}|{}
                            {}|{}    {}CONTINUAR{} {}[ 1 ]{}              {}|{}
                            {}|{}{}CONSIDERAÇÔES{} {}[ 2 ]{}              {}|{}
                            {}|{}   {}VER CODIGO{} {}[ 3 ]{}              {}|{}
                            {}|{}                                 {}|{}
                            {}|{}{}digite sua opção aqui: {}          {}|{}
                            {}+---------------------------------+: {}""".format("\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[37m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[36m", "\033[m",
                                                                                "\033[35m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m", "\033[32m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m")))
                if opcao == 0:
                    break
                elif opcao == 1:
                    opcao1 = int(input("ECOLHA UMA FASE: "))
                elif opcao == 2:
                    import consideracoes
                elif opcao == 3:
                    fou = open("exercicio40.py", "r")
                    for c in fou.readlines():
                        print(c)
                    fou.close()
                else:
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
                    print("{}o MENU não tem essa opção. Tente novamente!{}".format("\033[31m", "\033[m"))
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
            elif opcao1 == 77:
                import exercicio77
                webbrowser.open("https://www.youtube.com/watch?v=ZiC5NgSGJXU&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=9")

                opcao = int(input("""{}
                            +---------------------------------+
                            |ESCOLHA UMA OPÇÂO PARA JOGAR:    |{}
                            {}|{}    {}SAIR MENU{} {}[ 0 ]{}              {}|{}
                            {}|{}    {}CONTINUAR{} {}[ 1 ]{}              {}|{}
                            {}|{}{}CONSIDERAÇÔES{} {}[ 2 ]{}              {}|{}
                            {}|{}   {}VER CODIGO{} {}[ 3 ]{}              {}|{}
                            {}|{}                                 {}|{}
                            {}|{}{}digite sua opção aqui: {}          {}|{}
                            {}+---------------------------------+: {}""".format("\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[37m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[36m", "\033[m",
                                                                                "\033[35m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m", "\033[32m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m")))
                if opcao == 0:
                    break
                elif opcao == 1:
                    opcao1 = int(input("ECOLHA UMA FASE: "))
                elif opcao == 2:
                    import consideracoes
                elif opcao == 3:
                    fou = open("exercicio41.py", "r")
                    for c in fou.readlines():
                        print(c)
                    fou.close()
                else:
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
                    print("{}o MENU não tem essa opção. Tente novamente!{}".format("\033[31m", "\033[m"))
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
            elif opcao1 == 78:
                import exercicio78
                webbrowser.open("https://www.youtube.com/watch?v=ZX7sCPjcHA0&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=10")

                opcao = int(input("""{}
                            +---------------------------------+
                            |ESCOLHA UMA OPÇÂO PARA JOGAR:    |{}
                            {}|{}    {}SAIR MENU{} {}[ 0 ]{}              {}|{}
                            {}|{}    {}CONTINUAR{} {}[ 1 ]{}              {}|{}
                            {}|{}{}CONSIDERAÇÔES{} {}[ 2 ]{}              {}|{}
                            {}|{}   {}VER CODIGO{} {}[ 3 ]{}              {}|{}
                            {}|{}                                 {}|{}
                            {}|{}{}digite sua opção aqui: {}          {}|{}
                            {}+---------------------------------+: {}""".format("\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[37m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[36m", "\033[m",
                                                                                "\033[35m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m", "\033[32m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m")))
                if opcao == 0:
                    break
                elif opcao == 1:
                    opcao1 = int(input("ECOLHA UMA FASE: "))
                elif opcao == 2:
                    import consideracoes
                elif opcao == 3:
                    fou = open("exercicio42.py", "r")
                    for c in fou.readlines():
                        print(c)
                    fou.close()
                else:
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
                    print("{}o MENU não tem essa opção. Tente novamente!{}".format("\033[31m", "\033[m"))
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
            elif opcao1 == 79:
                import exercicio79
                webbrowser.open("https://www.youtube.com/watch?v=b7r34za963I&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=11")

                opcao = int(input("""{}
                            +---------------------------------+
                            |ESCOLHA UMA OPÇÂO PARA JOGAR:    |{}
                            {}|{}    {}SAIR MENU{} {}[ 0 ]{}              {}|{}
                            {}|{}    {}CONTINUAR{} {}[ 1 ]{}              {}|{}
                            {}|{}{}CONSIDERAÇÔES{} {}[ 2 ]{}              {}|{}
                            {}|{}   {}VER CODIGO{} {}[ 3 ]{}              {}|{}
                            {}|{}                                 {}|{}
                            {}|{}{}digite sua opção aqui: {}          {}|{}
                            {}+---------------------------------+: {}""".format("\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[37m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[36m", "\033[m",
                                                                                "\033[35m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m", "\033[32m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m")))
                if opcao == 0:
                    break
                elif opcao == 1:
                    opcao1 = int(input("ECOLHA UMA FASE: "))
                elif opcao == 2:
                    import consideracoes
                elif opcao == 3:
                    fou = open("exercicio43.py", "r")
                    for c in fou.readlines():
                        print(c)
                    fou.close()
                else:
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
                    print("{}o MENU não tem essa opção. Tente novamente!{}".format("\033[31m", "\033[m"))
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
            elif opcao1 == 80:
                import exercicio80
                webbrowser.open("https://www.youtube.com/watch?v=tapTa6KVG-A&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=13")

                opcao = int(input("""{}
                            +---------------------------------+
                            |ESCOLHA UMA OPÇÂO PARA JOGAR:    |{}
                            {}|{}    {}SAIR MENU{} {}[ 0 ]{}              {}|{}
                            {}|{}    {}CONTINUAR{} {}[ 1 ]{}              {}|{}
                            {}|{}{}CONSIDERAÇÔES{} {}[ 2 ]{}              {}|{}
                            {}|{}   {}VER CODIGO{} {}[ 3 ]{}              {}|{}
                            {}|{}                                 {}|{}
                            {}|{}{}digite sua opção aqui: {}          {}|{}
                            {}+---------------------------------+: {}""".format("\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[37m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[36m", "\033[m",
                                                                                "\033[35m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m", "\033[32m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m")))
                if opcao == 0:
                    break
                elif opcao == 1:
                    opcao1 = int(input("ECOLHA UMA FASE: "))
                elif opcao == 2:
                    import consideracoes
                elif opcao == 3:
                    fou = open("exercicio44.py", "r")
                    for c in fou.readlines():
                        print(c)
                    fou.close()
                else:
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
                    print("{}o MENU não tem essa opção. Tente novamente!{}".format("\033[31m", "\033[m"))
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
            elif opcao1 == 81:
                import exercicio81
                webbrowser.open("https://www.youtube.com/watch?v=tapTa6KVG-A&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=13")

                opcao = int(input("""{}
                            +---------------------------------+
                            |ESCOLHA UMA OPÇÂO PARA JOGAR:    |{}
                            {}|{}    {}SAIR MENU{} {}[ 0 ]{}              {}|{}
                            {}|{}    {}CONTINUAR{} {}[ 1 ]{}              {}|{}
                            {}|{}{}CONSIDERAÇÔES{} {}[ 2 ]{}              {}|{}
                            {}|{}   {}VER CODIGO{} {}[ 3 ]{}              {}|{}
                            {}|{}                                 {}|{}
                            {}|{}{}digite sua opção aqui: {}          {}|{}
                            {}+---------------------------------+: {}""".format("\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[37m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[36m", "\033[m",
                                                                                "\033[35m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m", "\033[32m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m")))
                if opcao == 0:
                    break
                elif opcao == 1:
                    opcao1 = int(input("ECOLHA UMA FASE: "))
                elif opcao == 2:
                    import consideracoes
                elif opcao == 3:
                    fou = open("exercicio45.py", "r")
                    for c in fou.readlines():
                        print(c)
                    fou.close()
                else:
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
                    print("{}o MENU não tem essa opção. Tente novamente!{}".format("\033[31m", "\033[m"))
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
            elif opcao1 == 82:
                import exercicio82
                webbrowser.open("https://www.youtube.com/watch?v=NR1RKt6NT8s&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=15")

                opcao = int(input("""{}
                            +---------------------------------+
                            |ESCOLHA UMA OPÇÂO PARA JOGAR:    |{}
                            {}|{}    {}SAIR MENU{} {}[ 0 ]{}              {}|{}
                            {}|{}    {}CONTINUAR{} {}[ 1 ]{}              {}|{}
                            {}|{}{}CONSIDERAÇÔES{} {}[ 2 ]{}              {}|{}
                            {}|{}   {}VER CODIGO{} {}[ 3 ]{}              {}|{}
                            {}|{}                                 {}|{}
                            {}|{}{}digite sua opção aqui: {}          {}|{}
                            {}+---------------------------------+: {}""".format("\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[37m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[36m", "\033[m",
                                                                                "\033[35m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m", "\033[32m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m")))
                if opcao == 0:
                    break
                elif opcao == 1:
                    opcao1 = int(input("ECOLHA UMA FASE: "))
                elif opcao == 2:
                    import consideracoes
                elif opcao == 3:
                    fou = open("exercicio46.py", "r")
                    for c in fou.readlines():
                        print(c)
                    fou.close()
                else:
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
                    print("{}o MENU não tem essa opção. Tente novamente!{}".format("\033[31m", "\033[m"))
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
            elif opcao1 == 83:
                import exercicio83
                webbrowser.open("https://www.youtube.com/watch?v=Qws8-E-YrlY&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=16")

                opcao = int(input("""{}
                            +---------------------------------+
                            |ESCOLHA UMA OPÇÂO PARA JOGAR:    |{}
                            {}|{}    {}SAIR MENU{} {}[ 0 ]{}              {}|{}
                            {}|{}    {}CONTINUAR{} {}[ 1 ]{}              {}|{}
                            {}|{}{}CONSIDERAÇÔES{} {}[ 2 ]{}              {}|{}
                            {}|{}   {}VER CODIGO{} {}[ 3 ]{}              {}|{}
                            {}|{}                                 {}|{}
                            {}|{}{}digite sua opção aqui: {}          {}|{}
                            {}+---------------------------------+: {}""".format("\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[37m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[36m", "\033[m",
                                                                                "\033[35m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m", "\033[32m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m")))
                if opcao == 0:
                    break
                elif opcao == 1:
                    opcao1 = int(input("ECOLHA UMA FASE: "))
                elif opcao == 2:
                    import consideracoes
                elif opcao == 3:
                    fou = open("exercicio47.py", "r")
                    for c in fou.readlines():
                        print(c)
                    fou.close()
                else:
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
                    print("{}o MENU não tem essa opção. Tente novamente!{}".format("\033[31m", "\033[m"))
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
            elif opcao1 == 84:
                import exercicio84
                webbrowser.open("https://www.youtube.com/watch?v=iHjsUxNA-wo&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=17")

                opcao = int(input("""{}
                            +---------------------------------+
                            |ESCOLHA UMA OPÇÂO PARA JOGAR:    |{}
                            {}|{}    {}SAIR MENU{} {}[ 0 ]{}              {}|{}
                            {}|{}    {}CONTINUAR{} {}[ 1 ]{}              {}|{}
                            {}|{}{}CONSIDERAÇÔES{} {}[ 2 ]{}              {}|{}
                            {}|{}   {}VER CODIGO{} {}[ 3 ]{}              {}|{}
                            {}|{}                                 {}|{}
                            {}|{}{}digite sua opção aqui: {}          {}|{}
                            {}+---------------------------------+: {}""".format("\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[37m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[36m", "\033[m",
                                                                                "\033[35m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m", "\033[32m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m")))
                if opcao == 0:
                    break
                elif opcao == 1:
                    opcao1 = int(input("ECOLHA UMA FASE: "))
                elif opcao == 2:
                    import consideracoes
                elif opcao == 3:
                    fou = open("exercicio48.py", "r")
                    for c in fou.readlines():
                        print(c)
                    fou.close()
                else:
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
                    print("{}o MENU não tem essa opção. Tente novamente!{}".format("\033[31m", "\033[m"))
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
            elif opcao1 == 85:
                import exercicio85
                webbrowser.open("https://www.youtube.com/watch?v=QtElJDa9ICM&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=18")

                opcao = int(input("""{}
                            +---------------------------------+
                            |ESCOLHA UMA OPÇÂO PARA JOGAR:    |{}
                            {}|{}    {}SAIR MENU{} {}[ 0 ]{}              {}|{}
                            {}|{}    {}CONTINUAR{} {}[ 1 ]{}              {}|{}
                            {}|{}{}CONSIDERAÇÔES{} {}[ 2 ]{}              {}|{}
                            {}|{}   {}VER CODIGO{} {}[ 3 ]{}              {}|{}
                            {}|{}                                 {}|{}
                            {}|{}{}digite sua opção aqui: {}          {}|{}
                            {}+---------------------------------+: {}""".format("\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[37m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[36m", "\033[m",
                                                                                "\033[35m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m", "\033[32m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m")))
                if opcao == 0:
                    break
                elif opcao == 1:
                    opcao1 = int(input("ECOLHA UMA FASE: "))
                elif opcao == 2:
                    import consideracoes
                elif opcao == 3:
                    fou = open("exercicio49.py", "r")
                    for c in fou.readlines():
                        print(c)
                    fou.close()
                else:
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
                    print("{}o MENU não tem essa opção. Tente novamente!{}".format("\033[31m", "\033[m"))
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
            elif opcao1 == 86:
                import exercicio86
                webbrowser.open("https://www.youtube.com/watch?v=rJaBLOW57Jg&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=19")

                opcao = int(input("""{}
                            +---------------------------------+
                            |ESCOLHA UMA OPÇÂO PARA JOGAR:    |{}
                            {}|{}    {}SAIR MENU{} {}[ 0 ]{}              {}|{}
                            {}|{}    {}CONTINUAR{} {}[ 1 ]{}              {}|{}
                            {}|{}{}CONSIDERAÇÔES{} {}[ 2 ]{}              {}|{}
                            {}|{}   {}VER CODIGO{} {}[ 3 ]{}              {}|{}
                            {}|{}                                 {}|{}
                            {}|{}{}digite sua opção aqui: {}          {}|{}
                            {}+---------------------------------+: {}""".format("\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[37m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[36m", "\033[m",
                                                                                "\033[35m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m", "\033[32m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m")))
                if opcao == 0:
                    break
                elif opcao == 1:
                    opcao1 = int(input("ECOLHA UMA FASE: "))
                elif opcao == 2:
                    import consideracoes
                elif opcao == 3:
                    fou = open("exercicio50.py", "r")
                    for c in fou.readlines():
                        print(c)
                    fou.close()
                else:
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
                    print("{}o MENU não tem essa opção. Tente novamente!{}".format("\033[31m", "\033[m"))
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
            elif opcao1 == 87:
                import exercicio87
                webbrowser.open("https://www.youtube.com/watch?v=-OnqSGh0u4g&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=20")

                opcao = int(input("""{}
                            +---------------------------------+
                            |ESCOLHA UMA OPÇÂO PARA JOGAR:    |{}
                            {}|{}    {}SAIR MENU{} {}[ 0 ]{}              {}|{}
                            {}|{}    {}CONTINUAR{} {}[ 1 ]{}              {}|{}
                            {}|{}{}CONSIDERAÇÔES{} {}[ 2 ]{}              {}|{}
                            {}|{}   {}VER CODIGO{} {}[ 3 ]{}              {}|{}
                            {}|{}                                 {}|{}
                            {}|{}{}digite sua opção aqui: {}          {}|{}
                            {}+---------------------------------+: {}""".format("\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[37m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[36m", "\033[m",
                                                                                "\033[35m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m", "\033[32m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m")))
                if opcao == 0:
                    break
                elif opcao == 1:
                    opcao1 = int(input("ECOLHA UMA FASE: "))
                elif opcao == 2:
                    import consideracoes
                elif opcao == 3:
                    fou = open("exercicio51.py", "r")
                    for c in fou.readlines():
                        print(c)
                    fou.close()
                else:
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
                    print("{}o MENU não tem essa opção. Tente novamente!{}".format("\033[31m", "\033[m"))
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
            elif opcao1 == 88:
                import exercicio88
                webbrowser.open("https://www.youtube.com/watch?v=Er5Hyd4LyVw&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=21")

                opcao = int(input("""{}
                            +---------------------------------+
                            |ESCOLHA UMA OPÇÂO PARA JOGAR:    |{}
                            {}|{}    {}SAIR MENU{} {}[ 0 ]{}              {}|{}
                            {}|{}    {}CONTINUAR{} {}[ 1 ]{}              {}|{}
                            {}|{}{}CONSIDERAÇÔES{} {}[ 2 ]{}              {}|{}
                            {}|{}   {}VER CODIGO{} {}[ 3 ]{}              {}|{}
                            {}|{}                                 {}|{}
                            {}|{}{}digite sua opção aqui: {}          {}|{}
                            {}+---------------------------------+: {}""".format("\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[37m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[36m", "\033[m",
                                                                                "\033[35m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m", "\033[32m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m")))
                if opcao == 0:
                    break
                elif opcao == 1:
                    opcao1 = int(input("ECOLHA UMA FASE: "))
                elif opcao == 2:
                    import consideracoes
                elif opcao == 3:
                    fou = open("exercicio52.py", "r")
                    for c in fou.readlines():
                        print(c)
                    fou.close()
                else:
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
                    print("{}o MENU não tem essa opção. Tente novamente!{}".format("\033[31m", "\033[m"))
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
            elif opcao1 == 89:
                import exercicio89
                webbrowser.open("https://www.youtube.com/watch?v=5VBWe6BXzRo&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=22")

                opcao = int(input("""{}
                            +---------------------------------+
                            |ESCOLHA UMA OPÇÂO PARA JOGAR:    |{}
                            {}|{}    {}SAIR MENU{} {}[ 0 ]{}              {}|{}
                            {}|{}    {}CONTINUAR{} {}[ 1 ]{}              {}|{}
                            {}|{}{}CONSIDERAÇÔES{} {}[ 2 ]{}              {}|{}
                            {}|{}   {}VER CODIGO{} {}[ 3 ]{}              {}|{}
                            {}|{}                                 {}|{}
                            {}|{}{}digite sua opção aqui: {}          {}|{}
                            {}+---------------------------------+: {}""".format("\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[37m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[36m", "\033[m",
                                                                                "\033[35m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m", "\033[32m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m")))
                if opcao == 0:
                    break
                elif opcao == 1:
                    opcao1 = int(input("ECOLHA UMA FASE: "))
                elif opcao == 2:
                    import consideracoes
                elif opcao == 3:
                    fou = open("exercicio53.py", "r")
                    for c in fou.readlines():
                        print(c)
                    fou.close()
                else:
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
                    print("{}o MENU não tem essa opção. Tente novamente!{}".format("\033[31m", "\033[m"))
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
            elif opcao1 == 90:
                import exercicio90
                webbrowser.open("https://www.youtube.com/watch?v=IL5iBWoKRIs&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=23")

                opcao = int(input("""{}
                            +---------------------------------+
                            |ESCOLHA UMA OPÇÂO PARA JOGAR:    |{}
                            {}|{}    {}SAIR MENU{} {}[ 0 ]{}              {}|{}
                            {}|{}    {}CONTINUAR{} {}[ 1 ]{}              {}|{}
                            {}|{}{}CONSIDERAÇÔES{} {}[ 2 ]{}              {}|{}
                            {}|{}   {}VER CODIGO{} {}[ 3 ]{}              {}|{}
                            {}|{}                                 {}|{}
                            {}|{}{}digite sua opção aqui: {}          {}|{}
                            {}+---------------------------------+: {}""".format("\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[37m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[36m", "\033[m",
                                                                                "\033[35m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m", "\033[32m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m")))
                if opcao == 0:
                    break
                elif opcao == 1:
                    opcao1 = int(input("ECOLHA UMA FASE: "))
                elif opcao == 2:
                    import consideracoes
                elif opcao == 3:
                    fou = open("exercicio54.py", "r")
                    for c in fou.readlines():
                        print(c)
                    fou.close()
                else:
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
                    print("{}o MENU não tem essa opção. Tente novamente!{}".format("\033[31m", "\033[m"))
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
            elif opcao1 == 91:
                import exercicio91
                webbrowser.open("https://www.youtube.com/watch?v=Kjpb_IAOKRQ&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=24")

                opcao = int(input("""{}
                            +---------------------------------+
                            |ESCOLHA UMA OPÇÂO PARA JOGAR:    |{}
                            {}|{}    {}SAIR MENU{} {}[ 0 ]{}              {}|{}
                            {}|{}    {}CONTINUAR{} {}[ 1 ]{}              {}|{}
                            {}|{}{}CONSIDERAÇÔES{} {}[ 2 ]{}              {}|{}
                            {}|{}   {}VER CODIGO{} {}[ 3 ]{}              {}|{}
                            {}|{}                                 {}|{}
                            {}|{}{}digite sua opção aqui: {}          {}|{}
                            {}+---------------------------------+: {}""".format("\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[37m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[36m", "\033[m",
                                                                                "\033[35m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m", "\033[32m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m")))
                if opcao == 0:
                    break
                elif opcao == 1:
                    opcao1 = int(input("ECOLHA UMA FASE: "))
                elif opcao == 2:
                    import consideracoes
                elif opcao == 3:
                    fou = open("exercicio55.py", "r")
                    for c in fou.readlines():
                        print(c)
                    fou.close()
                else:
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
                    print("{}o MENU não tem essa opção. Tente novamente!{}".format("\033[31m", "\033[m"))
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
            elif opcao1 == 92:
                import exercicio92
                webbrowser.open("https://www.youtube.com/watch?v=fokDF4th0IY&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=25")

                opcao = int(input("""{}
                            +---------------------------------+
                            |ESCOLHA UMA OPÇÂO PARA JOGAR:    |{}
                            {}|{}    {}SAIR MENU{} {}[ 0 ]{}              {}|{}
                            {}|{}    {}CONTINUAR{} {}[ 1 ]{}              {}|{}
                            {}|{}{}CONSIDERAÇÔES{} {}[ 2 ]{}              {}|{}
                            {}|{}   {}VER CODIGO{} {}[ 3 ]{}              {}|{}
                            {}|{}                                 {}|{}
                            {}|{}{}digite sua opção aqui: {}          {}|{}
                            {}+---------------------------------+: {}""".format("\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[37m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[36m", "\033[m",
                                                                                "\033[35m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m", "\033[32m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m")))
                if opcao == 0:
                    break
                elif opcao == 1:
                    opcao1 = int(input("ECOLHA UMA FASE: "))
                elif opcao == 2:
                    import consideracoes
                elif opcao == 3:
                    fou = open("exercicio56.py", "r")
                    for c in fou.readlines():
                        print(c)
                    fou.close()
                else:
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
                    print("{}o MENU não tem essa opção. Tente novamente!{}".format("\033[31m", "\033[m"))
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
            elif opcao1 == 93:
                import exercicio93
                webbrowser.open("https://www.youtube.com/watch?v=JGztEBLGj5E&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=27")

                opcao = int(input("""{}
                            +---------------------------------+
                            |ESCOLHA UMA OPÇÂO PARA JOGAR:    |{}
                            {}|{}    {}SAIR MENU{} {}[ 0 ]{}              {}|{}
                            {}|{}    {}CONTINUAR{} {}[ 1 ]{}              {}|{}
                            {}|{}{}CONSIDERAÇÔES{} {}[ 2 ]{}              {}|{}
                            {}|{}   {}VER CODIGO{} {}[ 3 ]{}              {}|{}
                            {}|{}                                 {}|{}
                            {}|{}{}digite sua opção aqui: {}          {}|{}
                            {}+---------------------------------+: {}""".format("\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[37m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[36m", "\033[m",
                                                                                "\033[35m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m", "\033[32m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m")))
                if opcao == 0:
                    break
                elif opcao == 1:
                    opcao1 = int(input("ECOLHA UMA FASE: "))
                elif opcao == 2:
                    import consideracoes
                elif opcao == 3:
                    fou = open("exercicio57.py", "r")
                    for c in fou.readlines():
                        print(c)
                    fou.close()
                else:
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
                    print("{}o MENU não tem essa opção. Tente novamente!{}".format("\033[31m", "\033[m"))
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
            elif opcao1 == 94:
                import exercicio94
                webbrowser.open("https://www.youtube.com/watch?v=-QkOIHJ1Chw&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=28")

                opcao = int(input("""{}
                            +---------------------------------+
                            |ESCOLHA UMA OPÇÂO PARA JOGAR:    |{}
                            {}|{}    {}SAIR MENU{} {}[ 0 ]{}              {}|{}
                            {}|{}    {}CONTINUAR{} {}[ 1 ]{}              {}|{}
                            {}|{}{}CONSIDERAÇÔES{} {}[ 2 ]{}              {}|{}
                            {}|{}   {}VER CODIGO{} {}[ 3 ]{}              {}|{}
                            {}|{}                                 {}|{}
                            {}|{}{}digite sua opção aqui: {}          {}|{}
                            {}+---------------------------------+: {}""".format("\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[37m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[36m", "\033[m",
                                                                                "\033[35m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m", "\033[32m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m")))
                if opcao == 0:
                    break
                elif opcao == 1:
                    opcao1 = int(input("ECOLHA UMA FASE: "))
                elif opcao == 2:
                    import consideracoes
                elif opcao == 3:
                    fou = open("exercicio58.py", "r")
                    for c in fou.readlines():
                        print(c)
                    fou.close()
                else:
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
                    print("{}o MENU não tem essa opção. Tente novamente!{}".format("\033[31m", "\033[m"))
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
            elif opcao1 == 95:
                import exercicio95
                webbrowser.open("https://www.youtube.com/watch?v=OBJL5vPj4-E&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=29")

                opcao = int(input("""{}
                            +---------------------------------+
                            |ESCOLHA UMA OPÇÂO PARA JOGAR:    |{}
                            {}|{}    {}SAIR MENU{} {}[ 0 ]{}              {}|{}
                            {}|{}    {}CONTINUAR{} {}[ 1 ]{}              {}|{}
                            {}|{}{}CONSIDERAÇÔES{} {}[ 2 ]{}              {}|{}
                            {}|{}   {}VER CODIGO{} {}[ 3 ]{}              {}|{}
                            {}|{}                                 {}|{}
                            {}|{}{}digite sua opção aqui: {}          {}|{}
                            {}+---------------------------------+: {}""".format("\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[37m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[36m", "\033[m",
                                                                                "\033[35m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m", "\033[32m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m")))
                if opcao == 0:
                    break
                elif opcao == 1:
                    opcao1 = int(input("ECOLHA UMA FASE: "))
                elif opcao == 2:
                    import consideracoes
                elif opcao == 3:
                    fou = open("exercicio59.py", "r")
                    for c in fou.readlines():
                        print(c)
                    fou.close()
                else:
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
                    print("{}o MENU não tem essa opção. Tente novamente!{}".format("\033[31m", "\033[m"))
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
            elif opcao1 == 96:
                import exercicio96
                webbrowser.open("https://www.youtube.com/watch?v=9dlBZlkvvxY&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=30")

                opcao = int(input("""{}
                            +---------------------------------+
                            |ESCOLHA UMA OPÇÂO PARA JOGAR:    |{}
                            {}|{}    {}SAIR MENU{} {}[ 0 ]{}              {}|{}
                            {}|{}    {}CONTINUAR{} {}[ 1 ]{}              {}|{}
                            {}|{}{}CONSIDERAÇÔES{} {}[ 2 ]{}              {}|{}
                            {}|{}   {}VER CODIGO{} {}[ 3 ]{}              {}|{}
                            {}|{}                                 {}|{}
                            {}|{}{}digite sua opção aqui: {}          {}|{}
                            {}+---------------------------------+: {}""".format("\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[37m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[36m", "\033[m",
                                                                                "\033[35m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m", "\033[32m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m")))
                if opcao == 0:
                    break
                elif opcao == 1:
                    opcao1 = int(input("ECOLHA UMA FASE: "))
                elif opcao == 2:
                    import consideracoes
                elif opcao == 3:
                    fou = open("exercicio60.py", "r")
                    for c in fou.readlines():
                        print(c)
                    fou.close()
                else:
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
                    print("{}o MENU não tem essa opção. Tente novamente!{}".format("\033[31m", "\033[m"))
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
            elif opcao1 == 97:
                import exercicio97
                webbrowser.open("https://www.youtube.com/watch?v=vu5ehetQGe8&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=31")

                opcao = int(input("""{}
                            +---------------------------------+
                            |ESCOLHA UMA OPÇÂO PARA JOGAR:    |{}
                            {}|{}    {}SAIR MENU{} {}[ 0 ]{}              {}|{}
                            {}|{}    {}CONTINUAR{} {}[ 1 ]{}              {}|{}
                            {}|{}{}CONSIDERAÇÔES{} {}[ 2 ]{}              {}|{}
                            {}|{}   {}VER CODIGO{} {}[ 3 ]{}              {}|{}
                            {}|{}                                 {}|{}
                            {}|{}{}digite sua opção aqui: {}          {}|{}
                            {}+---------------------------------+: {}""".format("\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[37m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[36m", "\033[m",
                                                                                "\033[35m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m", "\033[32m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m")))
                if opcao == 0:
                    break
                elif opcao == 1:
                    opcao1 = int(input("ECOLHA UMA FASE: "))
                elif opcao == 2:
                    import consideracoes
                elif opcao == 3:
                    fou = open("exercicio61.py", "r")
                    for c in fou.readlines():
                        print(c)
                    fou.close()
                else:
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
                    print("{}o MENU não tem essa opção. Tente novamente!{}".format("\033[31m", "\033[m"))
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
            elif opcao1 == 98:
                import exercicio98
                webbrowser.open("https://www.youtube.com/watch?v=BWAWq7n6PCk&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=32")

                opcao = int(input("""{}
                            +---------------------------------+
                            |ESCOLHA UMA OPÇÂO PARA JOGAR:    |{}
                            {}|{}    {}SAIR MENU{} {}[ 0 ]{}              {}|{}
                            {}|{}    {}CONTINUAR{} {}[ 1 ]{}              {}|{}
                            {}|{}{}CONSIDERAÇÔES{} {}[ 2 ]{}              {}|{}
                            {}|{}   {}VER CODIGO{} {}[ 3 ]{}              {}|{}
                            {}|{}                                 {}|{}
                            {}|{}{}digite sua opção aqui: {}          {}|{}
                            {}+---------------------------------+: {}""".format("\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[37m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[36m", "\033[m",
                                                                                "\033[35m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m", "\033[32m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m")))
                if opcao == 0:
                    break
                elif opcao == 1:
                    opcao1 = int(input("ECOLHA UMA FASE: "))
                elif opcao == 2:
                    import consideracoes
                elif opcao == 3:
                    fou = open("exercicio62.py", "r")
                    for c in fou.readlines():
                        print(c)
                    fou.close()
                else:
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
                    print("{}o MENU não tem essa opção. Tente novamente!{}".format("\033[31m", "\033[m"))
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
            elif opcao1 == 99:
                import exercicio99
                webbrowser.open("https://www.youtube.com/watch?v=w7yn1_Mfu0E&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=33")

                opcao = int(input("""{}
                            +---------------------------------+
                            |ESCOLHA UMA OPÇÂO PARA JOGAR:    |{}
                            {}|{}    {}SAIR MENU{} {}[ 0 ]{}              {}|{}
                            {}|{}    {}CONTINUAR{} {}[ 1 ]{}              {}|{}
                            {}|{}{}CONSIDERAÇÔES{} {}[ 2 ]{}              {}|{}
                            {}|{}   {}VER CODIGO{} {}[ 3 ]{}              {}|{}
                            {}|{}                                 {}|{}
                            {}|{}{}digite sua opção aqui: {}          {}|{}
                            {}+---------------------------------+: {}""".format("\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[37m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[36m", "\033[m",
                                                                                "\033[35m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m", "\033[32m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m")))
                if opcao == 0:
                    break
                elif opcao == 1:
                    opcao1 = int(input("ECOLHA UMA FASE: "))
                elif opcao == 2:
                    import consideracoes
                elif opcao == 3:
                    fou = open("exercicio63.py", "r")
                    for c in fou.readlines():
                        print(c)
                    fou.close()
                else:
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
                    print("{}o MENU não tem essa opção. Tente novamente!{}".format("\033[31m", "\033[m"))
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
            elif opcao1 == 100:
                import exercicio100
                webbrowser.open("https://www.youtube.com/watch?v=mYlbttiLHM0&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=34")

                opcao = int(input("""{}
                            +---------------------------------+
                            |ESCOLHA UMA OPÇÂO PARA JOGAR:    |{}
                            {}|{}    {}SAIR MENU{} {}[ 0 ]{}              {}|{}
                            {}|{}    {}CONTINUAR{} {}[ 1 ]{}              {}|{}
                            {}|{}{}CONSIDERAÇÔES{} {}[ 2 ]{}              {}|{}
                            {}|{}   {}VER CODIGO{} {}[ 3 ]{}              {}|{}
                            {}|{}                                 {}|{}
                            {}|{}{}digite sua opção aqui: {}          {}|{}
                            {}+---------------------------------+: {}""".format("\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[37m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[36m", "\033[m",
                                                                                "\033[35m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m", "\033[32m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m")))
                if opcao == 0:
                    break
                elif opcao == 1:
                    opcao1 = int(input("ECOLHA UMA FASE: "))
                elif opcao == 2:
                    import consideracoes
                elif opcao == 3:
                    fou = open("exercicio64.py", "r")
                    for c in fou.readlines():
                        print(c)
                    fou.close()
                else:
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
                    print("{}o MENU não tem essa opção. Tente novamente!{}".format("\033[31m", "\033[m"))
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
            elif opcao1 == 101:
                import exercicio101
                webbrowser.open("https://www.youtube.com/watch?v=QNPuPlPM--0&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=35")

                opcao = int(input("""{}
                            +---------------------------------+
                            |ESCOLHA UMA OPÇÂO PARA JOGAR:    |{}
                            {}|{}    {}SAIR MENU{} {}[ 0 ]{}              {}|{}
                            {}|{}    {}CONTINUAR{} {}[ 1 ]{}              {}|{}
                            {}|{}{}CONSIDERAÇÔES{} {}[ 2 ]{}              {}|{}
                            {}|{}   {}VER CODIGO{} {}[ 3 ]{}              {}|{}
                            {}|{}                                 {}|{}
                            {}|{}{}digite sua opção aqui: {}          {}|{}
                            {}+---------------------------------+: {}""".format("\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[37m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[36m", "\033[m",
                                                                                "\033[35m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m", "\033[32m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m")))
                if opcao == 0:
                    break
                elif opcao == 1:
                    opcao1 = int(input("ECOLHA UMA FASE: "))
                elif opcao == 2:
                    import consideracoes
                elif opcao == 3:
                    fou = open("exercicio65.py", "r")
                    for c in fou.readlines():
                        print(c)
                    fou.close()
                else:
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
                    print("{}o MENU não tem essa opção. Tente novamente!{}".format("\033[31m", "\033[m"))
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
            elif opcao1 == 102:
                import exercicio102
                webbrowser.open("https://www.youtube.com/watch?v=d2ug6quC1bk&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=37")

                opcao = int(input("""{}
                            +---------------------------------+
                            |ESCOLHA UMA OPÇÂO PARA JOGAR:    |{}
                            {}|{}    {}SAIR MENU{} {}[ 0 ]{}              {}|{}
                            {}|{}    {}CONTINUAR{} {}[ 1 ]{}              {}|{}
                            {}|{}{}CONSIDERAÇÔES{} {}[ 2 ]{}              {}|{}
                            {}|{}   {}VER CODIGO{} {}[ 3 ]{}              {}|{}
                            {}|{}                                 {}|{}
                            {}|{}{}digite sua opção aqui: {}          {}|{}
                            {}+---------------------------------+: {}""".format("\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[37m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[36m", "\033[m",
                                                                                "\033[35m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m", "\033[32m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m")))
                if opcao == 0:
                    break
                elif opcao == 1:
                    opcao1 = int(input("ECOLHA UMA FASE: "))
                elif opcao == 2:
                    import consideracoes
                elif opcao == 3:
                    fou = open("exercicio66.py", "r")
                    for c in fou.readlines():
                        print(c)
                    fou.close()
                else:
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
                    print("{}o MENU não tem essa opção. Tente novamente!{}".format("\033[31m", "\033[m"))
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
            elif opcao1 == 103:
                import exercicio103
                webbrowser.open("https://www.youtube.com/watch?v=X0a5aZg93Uc&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=38")

                opcao = int(input("""{}
                            +---------------------------------+
                            |ESCOLHA UMA OPÇÂO PARA JOGAR:    |{}
                            {}|{}    {}SAIR MENU{} {}[ 0 ]{}              {}|{}
                            {}|{}    {}CONTINUAR{} {}[ 1 ]{}              {}|{}
                            {}|{}{}CONSIDERAÇÔES{} {}[ 2 ]{}              {}|{}
                            {}|{}   {}VER CODIGO{} {}[ 3 ]{}              {}|{}
                            {}|{}                                 {}|{}
                            {}|{}{}digite sua opção aqui: {}          {}|{}
                            {}+---------------------------------+: {}""".format("\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[37m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[36m", "\033[m",
                                                                                "\033[35m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m", "\033[32m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m")))
                if opcao == 0:
                    break
                elif opcao == 1:
                    opcao1 = int(input("ECOLHA UMA FASE: "))
                elif opcao == 2:
                    import consideracoes
                elif opcao == 3:
                    fou = open("exercicio67.py", "r")
                    for c in fou.readlines():
                        print(c)
                    fou.close()
                else:
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
                    print("{}o MENU não tem essa opção. Tente novamente!{}".format("\033[31m", "\033[m"))
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
            elif opcao1 == 104:
                import exercicio104
                webbrowser.open("https://www.youtube.com/watch?v=EIzgKCCDdc0&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=39")

                opcao = int(input("""{}
                            +---------------------------------+
                            |ESCOLHA UMA OPÇÂO PARA JOGAR:    |{}
                            {}|{}    {}SAIR MENU{} {}[ 0 ]{}              {}|{}
                            {}|{}    {}CONTINUAR{} {}[ 1 ]{}              {}|{}
                            {}|{}{}CONSIDERAÇÔES{} {}[ 2 ]{}              {}|{}
                            {}|{}   {}VER CODIGO{} {}[ 3 ]{}              {}|{}
                            {}|{}                                 {}|{}
                            {}|{}{}digite sua opção aqui: {}          {}|{}
                            {}+---------------------------------+: {}""".format("\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[37m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[36m", "\033[m",
                                                                                "\033[35m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m", "\033[32m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m")))
                if opcao == 0:
                    break
                elif opcao == 1:
                    opcao1 = int(input("ECOLHA UMA FASE: "))
                elif opcao == 2:
                    import consideracoes
                elif opcao == 3:
                    fou = open("exercicio68.py", "r")
                    for c in fou.readlines():
                        print(c)
                    fou.close()
                else:
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
                    print("{}o MENU não tem essa opção. Tente novamente!{}".format("\033[31m", "\033[m"))
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
            elif opcao1 == 105:
                import exercicio105
                webbrowser.open("https://www.youtube.com/watch?v=4Ca6iRJo3M0&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=40")

                opcao = int(input("""{}
                            +---------------------------------+
                            |ESCOLHA UMA OPÇÂO PARA JOGAR:    |{}
                            {}|{}    {}SAIR MENU{} {}[ 0 ]{}              {}|{}
                            {}|{}    {}CONTINUAR{} {}[ 1 ]{}              {}|{}
                            {}|{}{}CONSIDERAÇÔES{} {}[ 2 ]{}              {}|{}
                            {}|{}   {}VER CODIGO{} {}[ 3 ]{}              {}|{}
                            {}|{}                                 {}|{}
                            {}|{}{}digite sua opção aqui: {}          {}|{}
                            {}+---------------------------------+: {}""".format("\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[37m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[36m", "\033[m",
                                                                                "\033[35m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m", "\033[32m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m")))
                if opcao == 0:
                    break
                elif opcao == 1:
                    opcao1 = int(input("ECOLHA UMA FASE: "))
                elif opcao == 2:
                    import consideracoes
                elif opcao == 3:
                    fou = open("exercicio69.py", "r")
                    for c in fou.readlines():
                        print(c)
                    fou.close()
                else:
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
                    print("{}o MENU não tem essa opção. Tente novamente!{}".format("\033[31m", "\033[m"))
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
            elif opcao1 == 106:
                import exercicio106
                webbrowser.open("https://www.youtube.com/watch?v=hS8QdW-1HTo&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=41")

                opcao = int(input("""{}
                            +---------------------------------+
                            |ESCOLHA UMA OPÇÂO PARA JOGAR:    |{}
                            {}|{}    {}SAIR MENU{} {}[ 0 ]{}              {}|{}
                            {}|{}    {}CONTINUAR{} {}[ 1 ]{}              {}|{}
                            {}|{}{}CONSIDERAÇÔES{} {}[ 2 ]{}              {}|{}
                            {}|{}   {}VER CODIGO{} {}[ 3 ]{}              {}|{}
                            {}|{}                                 {}|{}
                            {}|{}{}digite sua opção aqui: {}          {}|{}
                            {}+---------------------------------+: {}""".format("\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[37m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[36m", "\033[m",
                                                                                "\033[35m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m",
                                                                                "\033[31m", "\033[m", "\033[32m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m",
                                                                                "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[31m", "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m",
                                                                                "\033[m", "\033[31m", "\033[m")))
                if opcao == 0:
                    break
                elif opcao == 1:
                    opcao1 = int(input("ECOLHA UMA FASE: "))
                elif opcao == 2:
                    import consideracoes
                elif opcao == 3:
                    fou = open("exercicio70.py", "r")
                    for c in fou.readlines():
                        print(c)
                    fou.close()
                else:
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
                    print("{}o MENU não tem essa opção. Tente novamente!{}".format("\033[31m", "\033[m"))
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
            elif opcao1 == 107:
                import exercicio107

                webbrowser.open(
                    "https://www.youtube.com/watch?v=_XGgwltYpYk&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=42")

                opcao = int(input("""{}
            +---------------------------------+
            |ESCOLHA UMA OPÇÂO PARA JOGAR:    |{}
            {}|{}    {}SAIR MENU{} {}[ 0 ]{}              {}|{}
            {}|{}    {}CONTINUAR{} {}[ 1 ]{}              {}|{}
            {}|{}{}CONSIDERAÇÔES{} {}[ 2 ]{}              {}|{}
            {}|{}   {}VER CODIGO{} {}[ 3 ]{}              {}|{}
            {}|{}                                 {}|{}
            {}|{}{}digite sua opção aqui: {}          {}|{}
            {}+---------------------------------+: {}""".format("\033[31m", "\033[m", "\033[31m", "\033[m", "\033[31m",
                                                                "\033[m", "\033[31m",
                                                                "\033[m", "\033[31m", "\033[m", "\033[31m", "\033[m",
                                                                "\033[37m", "\033[m", "\033[31m", "\033[m", "\033[31m",
                                                                "\033[m", "\033[36m", "\033[m", "\033[35m",
                                                                "\033[m", "\033[31m", "\033[m", "\033[31m", "\033[m",
                                                                "\033[31m", "\033[m", "\033[32m", "\033[m", "\033[31m",
                                                                "\033[m", "\033[31m", "\033[m", "\033[31m",
                                                                "\033[m", "\033[31m", "\033[31m", "\033[m", "\033[31m",
                                                                "\033[31m", "\033[m", "\033[31m", "\033[m", "\033[31m",
                                                                "\033[m", "\033[31m", "\033[m")))
                if opcao == 0:
                    break
                elif opcao == 1:
                    opcao1 = int(input("ECOLHA UMA FASE: "))
                elif opcao == 2:
                    import consideracoes
                elif opcao == 3:
                    fou = open("exercicio71.py", "r")
                    for c in fou.readlines():
                        print(c)
                    fou.close()
                else:
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
                    print("{}o MENU não tem essa opção. Tente novamente!{}".format("\033[31m", "\033[m"))
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
            elif opcao1 == 108:
                import exercicio108

                webbrowser.open(
                    "https://www.youtube.com/watch?v=_XGgwltYpYk&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=42")

                opcao = int(input("""{}
            +---------------------------------+
            |ESCOLHA UMA OPÇÂO PARA JOGAR:    |{}
            {}|{}    {}SAIR MENU{} {}[ 0 ]{}              {}|{}
            {}|{}    {}CONTINUAR{} {}[ 1 ]{}              {}|{}
            {}|{}{}CONSIDERAÇÔES{} {}[ 2 ]{}              {}|{}
            {}|{}   {}VER CODIGO{} {}[ 3 ]{}              {}|{}
            {}|{}                                 {}|{}
            {}|{}{}digite sua opção aqui: {}          {}|{}
            {}+---------------------------------+: {}""".format("\033[31m", "\033[m", "\033[31m", "\033[m", "\033[31m",
                                                                "\033[m", "\033[31m",
                                                                "\033[m", "\033[31m", "\033[m", "\033[31m", "\033[m",
                                                                "\033[37m", "\033[m", "\033[31m", "\033[m", "\033[31m",
                                                                "\033[m", "\033[36m", "\033[m", "\033[35m",
                                                                "\033[m", "\033[31m", "\033[m", "\033[31m", "\033[m",
                                                                "\033[31m", "\033[m", "\033[32m", "\033[m", "\033[31m",
                                                                "\033[m", "\033[31m", "\033[m", "\033[31m",
                                                                "\033[m", "\033[31m", "\033[31m", "\033[m", "\033[31m",
                                                                "\033[31m", "\033[m", "\033[31m", "\033[m", "\033[31m",
                                                                "\033[m", "\033[31m", "\033[m")))
                if opcao == 0:
                    break
                elif opcao == 1:
                    opcao1 = int(input("ECOLHA UMA FASE: "))
                elif opcao == 2:
                    import consideracoes
                elif opcao == 3:
                    fou = open("exercicio71.py", "r")
                    for c in fou.readlines():
                        print(c)
                    fou.close()
                else:
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
                    print("{}o MENU não tem essa opção. Tente novamente!{}".format("\033[31m", "\033[m"))
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
            elif opcao1 == 109:
                import exercicio109

                webbrowser.open(
                    "https://www.youtube.com/watch?v=_XGgwltYpYk&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=42")

                opcao = int(input("""{}
            +---------------------------------+
            |ESCOLHA UMA OPÇÂO PARA JOGAR:    |{}
            {}|{}    {}SAIR MENU{} {}[ 0 ]{}              {}|{}
            {}|{}    {}CONTINUAR{} {}[ 1 ]{}              {}|{}
            {}|{}{}CONSIDERAÇÔES{} {}[ 2 ]{}              {}|{}
            {}|{}   {}VER CODIGO{} {}[ 3 ]{}              {}|{}
            {}|{}                                 {}|{}
            {}|{}{}digite sua opção aqui: {}          {}|{}
            {}+---------------------------------+: {}""".format("\033[31m", "\033[m", "\033[31m", "\033[m", "\033[31m",
                                                                "\033[m", "\033[31m",
                                                                "\033[m", "\033[31m", "\033[m", "\033[31m", "\033[m",
                                                                "\033[37m", "\033[m", "\033[31m", "\033[m", "\033[31m",
                                                                "\033[m", "\033[36m", "\033[m", "\033[35m",
                                                                "\033[m", "\033[31m", "\033[m", "\033[31m", "\033[m",
                                                                "\033[31m", "\033[m", "\033[32m", "\033[m", "\033[31m",
                                                                "\033[m", "\033[31m", "\033[m", "\033[31m",
                                                                "\033[m", "\033[31m", "\033[31m", "\033[m", "\033[31m",
                                                                "\033[31m", "\033[m", "\033[31m", "\033[m", "\033[31m",
                                                                "\033[m", "\033[31m", "\033[m")))
                if opcao == 0:
                    break
                elif opcao == 1:
                    opcao1 = int(input("ECOLHA UMA FASE: "))
                elif opcao == 2:
                    import consideracoes
                elif opcao == 3:
                    fou = open("exercicio71.py", "r")
                    for c in fou.readlines():
                        print(c)
                    fou.close()
                else:
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
                    print("{}o MENU não tem essa opção. Tente novamente!{}".format("\033[31m", "\033[m"))
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
            elif opcao1 == 110:
                import exercicio110

                webbrowser.open(
                    "https://www.youtube.com/watch?v=_XGgwltYpYk&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=42")

                opcao = int(input("""{}
            +---------------------------------+
            |ESCOLHA UMA OPÇÂO PARA JOGAR:    |{}
            {}|{}    {}SAIR MENU{} {}[ 0 ]{}              {}|{}
            {}|{}    {}CONTINUAR{} {}[ 1 ]{}              {}|{}
            {}|{}{}CONSIDERAÇÔES{} {}[ 2 ]{}              {}|{}
            {}|{}   {}VER CODIGO{} {}[ 3 ]{}              {}|{}
            {}|{}                                 {}|{}
            {}|{}{}digite sua opção aqui: {}          {}|{}
            {}+---------------------------------+: {}""".format("\033[31m", "\033[m", "\033[31m", "\033[m", "\033[31m",
                                                                "\033[m", "\033[31m",
                                                                "\033[m", "\033[31m", "\033[m", "\033[31m", "\033[m",
                                                                "\033[37m", "\033[m", "\033[31m", "\033[m", "\033[31m",
                                                                "\033[m", "\033[36m", "\033[m", "\033[35m",
                                                                "\033[m", "\033[31m", "\033[m", "\033[31m", "\033[m",
                                                                "\033[31m", "\033[m", "\033[32m", "\033[m", "\033[31m",
                                                                "\033[m", "\033[31m", "\033[m", "\033[31m",
                                                                "\033[m", "\033[31m", "\033[31m", "\033[m", "\033[31m",
                                                                "\033[31m", "\033[m", "\033[31m", "\033[m", "\033[31m",
                                                                "\033[m", "\033[31m", "\033[m")))
                if opcao == 0:
                    break
                elif opcao == 1:
                    opcao1 = int(input("ECOLHA UMA FASE: "))
                elif opcao == 2:
                    import consideracoes
                elif opcao == 3:
                    fou = open("exercicio71.py", "r")
                    for c in fou.readlines():
                        print(c)
                    fou.close()
                else:
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
                    print("{}o MENU não tem essa opção. Tente novamente!{}".format("\033[31m", "\033[m"))
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
            elif opcao1 == 111:
                import exercicio111

                webbrowser.open(
                    "https://www.youtube.com/watch?v=_XGgwltYpYk&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=42")

                opcao = int(input("""{}
            +---------------------------------+
            |ESCOLHA UMA OPÇÂO PARA JOGAR:    |{}
            {}|{}    {}SAIR MENU{} {}[ 0 ]{}              {}|{}
            {}|{}    {}CONTINUAR{} {}[ 1 ]{}              {}|{}
            {}|{}{}CONSIDERAÇÔES{} {}[ 2 ]{}              {}|{}
            {}|{}   {}VER CODIGO{} {}[ 3 ]{}              {}|{}
            {}|{}                                 {}|{}
            {}|{}{}digite sua opção aqui: {}          {}|{}
            {}+---------------------------------+: {}""".format("\033[31m", "\033[m", "\033[31m", "\033[m", "\033[31m",
                                                                "\033[m", "\033[31m",
                                                                "\033[m", "\033[31m", "\033[m", "\033[31m", "\033[m",
                                                                "\033[37m", "\033[m", "\033[31m", "\033[m", "\033[31m",
                                                                "\033[m", "\033[36m", "\033[m", "\033[35m",
                                                                "\033[m", "\033[31m", "\033[m", "\033[31m", "\033[m",
                                                                "\033[31m", "\033[m", "\033[32m", "\033[m", "\033[31m",
                                                                "\033[m", "\033[31m", "\033[m", "\033[31m",
                                                                "\033[m", "\033[31m", "\033[31m", "\033[m", "\033[31m",
                                                                "\033[31m", "\033[m", "\033[31m", "\033[m", "\033[31m",
                                                                "\033[m", "\033[31m", "\033[m")))
                if opcao == 0:
                    break
                elif opcao == 1:
                    opcao1 = int(input("ECOLHA UMA FASE: "))
                elif opcao == 2:
                    import consideracoes
                elif opcao == 3:
                    fou = open("exercicio71.py", "r")
                    for c in fou.readlines():
                        print(c)
                    fou.close()
                else:
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
                    print("{}o MENU não tem essa opção. Tente novamente!{}".format("\033[31m", "\033[m"))
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
            elif opcao1 == 112:
                import exercicio112

                webbrowser.open(
                    "https://www.youtube.com/watch?v=_XGgwltYpYk&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=42")

                opcao = int(input("""{}
            +---------------------------------+
            |ESCOLHA UMA OPÇÂO PARA JOGAR:    |{}
            {}|{}    {}SAIR MENU{} {}[ 0 ]{}              {}|{}
            {}|{}    {}CONTINUAR{} {}[ 1 ]{}              {}|{}
            {}|{}{}CONSIDERAÇÔES{} {}[ 2 ]{}              {}|{}
            {}|{}   {}VER CODIGO{} {}[ 3 ]{}              {}|{}
            {}|{}                                 {}|{}
            {}|{}{}digite sua opção aqui: {}          {}|{}
            {}+---------------------------------+: {}""".format("\033[31m", "\033[m", "\033[31m", "\033[m", "\033[31m",
                                                                "\033[m", "\033[31m",
                                                                "\033[m", "\033[31m", "\033[m", "\033[31m", "\033[m",
                                                                "\033[37m", "\033[m", "\033[31m", "\033[m", "\033[31m",
                                                                "\033[m", "\033[36m", "\033[m", "\033[35m",
                                                                "\033[m", "\033[31m", "\033[m", "\033[31m", "\033[m",
                                                                "\033[31m", "\033[m", "\033[32m", "\033[m", "\033[31m",
                                                                "\033[m", "\033[31m", "\033[m", "\033[31m",
                                                                "\033[m", "\033[31m", "\033[31m", "\033[m", "\033[31m",
                                                                "\033[31m", "\033[m", "\033[31m", "\033[m", "\033[31m",
                                                                "\033[m", "\033[31m", "\033[m")))
                if opcao == 0:
                    break
                elif opcao == 1:
                    opcao1 = int(input("ECOLHA UMA FASE: "))
                elif opcao == 2:
                    import consideracoes
                elif opcao == 3:
                    fou = open("exercicio71.py", "r")
                    for c in fou.readlines():
                        print(c)
                    fou.close()
                else:
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
                    print("{}o MENU não tem essa opção. Tente novamente!{}".format("\033[31m", "\033[m"))
                    print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
            else:
                print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[32m", "\033[m"))
                print("{}o MUNDO DO FOGO não tem essa fase. Tente novamente!{}".format("\033[32m", "\033[m"))
                print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[32m", "\033[m"))
                break
    elif opcao == 2:
        import consideracoes
    else:
        print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
        print("{}o MENU não tem essa opção. Tente novamente!{}".format("\033[31m", "\033[m"))
        print("{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}".format("\033[31m", "\033[m"))
