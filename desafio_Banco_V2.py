import textwrap

def montar_menu():
    menu = """\n
    ================= MENU ===============
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tLista contas
    [nu]\tNovo usuario
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato,transacoes_efetuadas,/):
    if valor > 0:
        saldo += valor
        transacoes_efetuadas += 1
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("Por favor, informe um valor acima de 0")
        
    return saldo, extrato,transacoes_efetuadas

def sacar (*,saldo, valor, extrato,limite,saques_efetuados,limite_saques,transacoes_efetuadas):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = saques_efetuados >= limite_saques
    
    if excedeu_saldo:
        print("\nNão há saldo suficiente")
    elif excedeu_limite:
        print("\nO valor está acima do limite permitido")
    elif excedeu_saques:
        print("\nExcedeu a quantidade de saques")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        saques_efetuados += 1
        transacoes_efetuadas += 1
        print("\n=== Saque realizado com sucesso! ===")
    
    return saldo, saques_efetuados, extrato,transacoes_efetuadas
        
def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("Usuários já cadastrado")
        return
    
    nome = input("Nome: ")
    data_nascimento = input("Data de nascimento: ")
    endereco = input("Endereço: ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário criado com sucesso!")
    
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF: ")
    usuario = filtrar_usuario(cpf,usuarios)
    
    if usuario:
        print("Conta criada com sucesso")
        return {"agencia": agencia, "numero_conta": numero_conta,"usuario":usuario}
    
    print("Usuário não econtrado")
    
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    
    saldo = 0
    limite_valor_saque = 500
    extrato = ""
    saques_efetuados = 0
    transacoes_efetuadas = 0
    usuarios = []
    contas = []
    LIMITE_SAQUES_DIA = 3
    LIMITE_TRANSACOES_DIA = 10
    MSG_ERRO_VALOR_DIGITADO = "Valor inválido. Digite um número separado por ."
    MSG_ERRO_LIMITE_TRANSACOES = "Número máximo de transações diárias atingido"
    AGENCIA = '0001'
    while True:

        opcao = montar_menu()

        if opcao == "q":
            break
        
        elif opcao == "e":
            exibir_extrato(saldo,extrato=extrato)
        elif opcao == 'nu':
            criar_usuario(usuarios)
        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta,usuarios)
            
            if conta:
                contas.append(conta)
        elif opcao == 'lc':
            listar_contas(contas)
        elif(opcao == "d"):
            if transacoes_efetuadas >= LIMITE_TRANSACOES_DIA:
                print(MSG_ERRO_LIMITE_TRANSACOES)
            else:
                valor_deposito = input("Digite o valor desejado: ")
                try:
                    valor_deposito = float(valor_deposito)
                except:
                    print(MSG_ERRO_VALOR_DIGITADO)   
                else:
                    saldo, extrato,transacoes_efetuadas = depositar(saldo, valor_deposito, extrato,transacoes_efetuadas)
            
    
        elif opcao == "s":
            if transacoes_efetuadas >= LIMITE_TRANSACOES_DIA:
                print(MSG_ERRO_LIMITE_TRANSACOES)
            else:
                valor_saque = input("Digite o valor desejado: ")
                try:
                    valor_saque = float(valor_saque)
                except:
                    print(MSG_ERRO_VALOR_DIGITADO)  
                else:
                    saldo, saques_efetuados, extrato,transacoes_efetuadas = sacar(
                        saldo=saldo
                        ,valor = valor_saque
                        ,extrato=extrato
                        ,limite=limite_valor_saque
                        ,saques_efetuados=saques_efetuados
                        ,limite_saques=LIMITE_SAQUES_DIA
                        ,transacoes_efetuadas=transacoes_efetuadas
                    )
                    print(f"saques_efetuados {saques_efetuados}")
    else: 
        print("Opção inválida. Por favor selecione uma das opções do menu")


main()