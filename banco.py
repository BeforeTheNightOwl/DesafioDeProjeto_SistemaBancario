# Criar um banco onde posso: depositar, sacar e ver o extrato, com a opção de sair.
# Máximo de vezes que posso sacar em um dia: 3
# Máximo de dinheiro que posso sacar por vez: R$ 500
# Formato moeda: R$ xxxx.xx

LIMITE_SAQUE = 3
saque = 0
quantidade_saques=0
saldo = 0
depositar = 0
extrato = ""

escolha = ""

while escolha != "q":
    print('''
========Seja bem vindo ao menu do Banco========
        Aperte "s" para sacar.
        Aperte "d" para depositar.
        Aperte "e" para ver o extrato.
        Aperte "q" caso deseje sair.''')
    escolha = input("Digite aqui: ")


    #QUITAR
    if escolha == "q":
        break


    # SACAR
    if escolha == "s":

        # Verifica se já sacou mais de 3 vezes e avisa caso for verdade
        if quantidade_saques >= 3:
            print("Você já sacou mais que 3 vezes, volte outro dia para sacar mais.")
        else:
            saque = float(input("Informar quantidade para sacar: "))

            # Verifica se o saque é maior que 500 reais ou menor igual que 0 e avisa caso for 
            if saque > 500 or saque <= 0:
                print("Deve sacar algum valor entre R$ 0 e R$ 500, nada fora desses parâmetros")
            else:
                # Verifica se possui saldo suficiente para o saque e avisa se não tiver
                if saque > saldo:
                    print("Você tentou sacar mais dinheiro do que possui.")
                else:
                    saldo -= saque
                    quantidade_saques +=1
                    print(quantidade_saques)
                    extrato += f"\n    saque: R$ {saque:.2f}"


    #DEPOSITAR
    if escolha == "d":
        depositar = float(input("Digite o valor que deseje depositar: "))
        if depositar < 0:
            print("Você deve depositar valores positivos, caso queira sacar deve presionar 's'.")
        else:
            saldo += depositar
            extrato +=f"\nDepositou: R$ {depositar:.2f}"

    if escolha == "e":
        print(f'''
===================================
              EXTRATO
    {extrato}

    Saldo: R$ {saldo}
''')