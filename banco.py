# Criar um banco onde posso: deposito, sacar e ver o extrato, com a opção de sair.
# Máximo de vezes que posso sacar em um dia: 3
# Máximo de dinheiro que posso sacar por vez: R$ 500
# Formato moeda: R$ xxxx.xx

LIMITE_SAQUE = 3
MAXIMO_SAQUE = 500
MINIMO_SAQUE = 0

saque = 0
quantidade_saques=0
saldo = 0
deposito = 0

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
    if escolha.lower() == "q":
        break


    # SACAR
    elif escolha.lower() == "s":

        # Verifica se já sacou mais de 3 vezes e avisa caso for verdade
        if quantidade_saques >= LIMITE_SAQUE:
            print("Você já sacou mais que 3 vezes, volte outro dia para sacar mais.")
        else:
            saque = float(input("Informar quantidade para sacar: "))

            # Verifica se o saque é maior que 500 reais ou menor igual que 0 e avisa caso for 
            if saque > MAXIMO_SAQUE or saque <= MINIMO_SAQUE:
                print("Deve sacar algum valor entre R$ 0 e R$ 500, nada fora desses parâmetros")
            else:
                # Verifica se possui saldo suficiente para o saque e avisa se não tiver
                if saque > saldo:
                    print("Você tentou sacar mais dinheiro do que possui.")
                else:
                    saldo -= saque
                    quantidade_saques +=1
                    extrato += f"\n    saque: R$ {saque:.2f}"


    # DEPOSITAR
    elif escolha.lower() == "d":
        deposito = float(input("Digite o valor que deseje depositar: "))
        if deposito < 0:
            print("Você deve depositar valores positivos, caso queira sacar deve presionar 's'.")
        else:
            saldo += deposito
            extrato +=f"\nDepositou: R$ {deposito:.2f}"

    # EXIBIR EXTRATO
    elif escolha.lower() == "e":
        print(f'''
===================================
              EXTRATO
    {extrato if extrato else "Não foi realizada nenhuma ação"}

    Saldo: R$ {saldo:.2f}
''')
    else:
        print("sinal inválido. Tente novamente")