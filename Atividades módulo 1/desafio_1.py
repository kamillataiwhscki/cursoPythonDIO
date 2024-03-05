#desafio 2
menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>'''

saldo = 0
limite = 500
extrato =""
numero_saques = 0
LIMITE_SAQUES = 3
saque_op = []
deposito_op = []


while True:
    opcao = input(menu)

    if(opcao == "d"):
        valor= float(input("Novo valor: "))
        if(valor<=0):
            print("Valor inválido!")
        else:
            saldo +=valor
            deposito_op.append(valor)
            extrato = extrato + f"\nDEPOSITO REALIZADO: VALOR = R${valor:.2f}"
            print("Depósito realizado!")
    elif opcao =="s":
        if(saldo <=0):
            print("Você não possui saldo para realizar essa operação")
            continue
        elif(LIMITE_SAQUES<=0):
            print("Você já atingiu o limite diário de saque!")
            continue
        else: 
            valor = float(input("Valor a ser sacado: "))
        
        if(valor<=0):
            print("Valor inválido!")
        else:
            if(valor > saldo):
                print("Saldo insuficiente")
                continue
            elif (valor >500):
                print("Valor maior que o limite por saque")
            else:
                saldo-=valor
                LIMITE_SAQUES-=1
                extrato = extrato + f"\nSAQUE REALIZADO: VALOR = R${valor:.2f}"
                print("Saque realizado com sucesso!")
    elif (opcao =="e"):
        if(extrato == ""):
            print("Extrato vazio!")
        else:
            print(extrato)
    elif (opcao == "q"):
        break
    else:
        print("Opção inválida!! Tente novamente.")
