from datetime import datetime

clientes = []
contas = []
extrato = []
saques_diarios = {}

AGENCIA = '0001'
LIMITE_SAQUE = 500
LIMITE_SAQUES_DIA = 3

def formatar_moeda(valor):
    return f"R${valor:.2f}"

def buscar_cliente(cpf):
    for cliente in clientes:
        if cliente['cpf'] == cpf:
            return cliente
    return None

def criar_cliente():
    nome = input("Nome completo: ")
    nascimento = input("Data de Nascimento: ")
    cpf = input("Digite seu CPF (somente com números): ")

    if buscar_cliente(cpf):
        print("Cliente já cadastrado")
        return
    
    clientes.append({
        "nome": nome,
        "nascimento": nascimento,
        "cpf": cpf
    })
    print("Cliente cadastrado!")

def criar_conta():
    cpf = input("Digite o CPF do cliente: ")
    cliente = buscar_cliente(cpf)

    if not cliente:
        print("Cliente não encontrado")
        return
    
    numero = len(contas) + 1
    conta = {
        "agencia": AGENCIA,
        "numero": numero,
        "cliente": cliente,
        "saldo": 0
    }

    contas.append(conta)
    print(f"Conta criada\nAgência: {AGENCIA}, Número da Conta: {numero}")

def depositar():
    numero = int(input("Número da conta: "))
    valor = float(input("Valor do depósito: "))

    conta = next((c for c in contas if c["numero"] == numero), None)

    if not conta:
        print("Conta não encontrada")
        return
    
    if valor <= 0:
        print("O valor do depósito deve ser maior que 0")
        return

    conta["saldo"] += valor
    extrato.append(f"[{numero}] Depósito: {formatar_moeda(valor)}")
    print("Depósito realizado com sucesso")

def sacar():
    numero = int(input("Número da Conta: "))
    valor = float(input("Valor do saque: "))

    conta = next((c for c in contas if c["numero"] == numero), None)

    if not conta:
        print("Conta não encontrada")
        return

    hoje = datetime.now().date()
    chave = (numero, hoje)
    saques_realizados = saques_diarios.get(chave, 0)

    if saques_realizados >= LIMITE_SAQUES_DIA:
        print("Limite de saques diários atingido")
        return

    if valor <= 0:
        print("Valor inválido")
    elif valor > LIMITE_SAQUE:
        print("O valor excede o limite de saque")
    elif valor > conta["saldo"]:
        print("Saldo insuficiente")
    else:
        conta["saldo"] -= valor
        saques_diarios[chave] = saques_realizados + 1
        extrato.append(f"[{numero}] Saque: -{formatar_moeda(valor)}")
        print("Saque realizado com sucesso")

def mostrar_extrato():
    numero = int(input("Número da conta: "))
    conta = next((c for c in contas if c["numero"] == numero), None)

    if not conta:
        print("Conta não encontrada")
        return
    
    print("\nExtrato da conta:")
    for linha in extrato:
        if f"[{numero}]" in linha:
            print(linha)
    print(f"Saldo atual: {formatar_moeda(conta['saldo'])}\n")

while True:
    print("\nBem-vindo ao sistema bancário")
    print("1 - Criar Cliente")
    print("2 - Criar Conta")
    print("3 - Depositar")
    print("4 - Sacar")
    print("5 - Extrato")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            criar_cliente()
        case "2":
            criar_conta()
        case "3":
            depositar()
        case "4":
            sacar()
        case "5":
            mostrar_extrato()
        case "0":
            print("Saindo do sistema.")
            break
        case _:
            print("Opção inválida. Tente novamente.")
