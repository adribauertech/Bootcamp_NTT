menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite_transacao = 500
lista_saques = []
lista_depositos = []
extrato = {"depositos": lista_depositos
    ,"saques": lista_saques }
saques_efetuados = 0
LIMITE_SAQUES_DIA = 3
MSG_ERRO_VALOR_DIGITADO = "Valor inválido. Digite um número separado por ."


while True:

    opcao = input(menu)

    if(opcao == "d"):
        valor_deposito = input("Digite o valor desejado: ")
        try:
            valor_deposito = float(valor_deposito)
            
        except:
            print(MSG_ERRO_VALOR_DIGITADO)   
        else:
            saldo = saldo + valor_deposito
            lista_depositos.append(valor_deposito)
            print(f"Saldo atual R$ {saldo}")  
        
    elif opcao == "s":
        if saldo == 0:
            print("Saldo zerado.")
        elif saques_efetuados >= 3:
            print("Limite de saques atingido")
        else:
            valor_saque = input("Digite o valor desejado: ")
            try:
                valor_saque = float(valor_saque)
            except:
                print(MSG_ERRO_VALOR_DIGITADO)  
            else:
                if (valor_saque > saldo):
                    print("Saldo insuficiente")
                elif (valor_saque > limite_transacao):
                    print("Valor acima do máximo permitido (R$ 500)")
                else:
                    saldo = saldo - valor_saque
                    lista_saques.append(valor_saque)
                    saques_efetuados = saques_efetuados + 1
                    print(f"Saque efetuado. Saldo atual R$ {saldo}")
            
    elif opcao == "e":
        print(extrato)
        
    elif opcao == "q":
        break

    else: 
        print("Opção inválida. Por favor selecione uma das opções do menu")
