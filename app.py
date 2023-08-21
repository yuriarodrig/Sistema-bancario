saldo = 0.0
depositos = []
saques = []

def depositar(valor):
    global saldo
    depositos.append(valor)
    saldo += valor
    print(f"Depósito de R${valor:.2f} realizado com sucesso.")

def sacar(valor):
    global saldo
    if saldo >= valor and len(saques) < 3 and valor <= 500:
        saques.append(valor)
        saldo -= valor
        print(f"Saque de R${valor:.2f} realizado com sucesso.")
    elif saldo < valor:
        print("Não é possível sacar. Saldo insuficiente.")
    elif len(saques) >= 3:
        print("Você já realizou o número máximo de saques diários (3).")
    elif valor > 500:
        print("O valor máximo de saque por vez é R$500.")

def exibir_extrato():
    print("Extrato:")
    if not (depositos or saques):
        print("Não foram realizadas movimentações.")
    else:
        for deposito in depositos:
            print(f"Depósito: R${deposito:.2f}")
        for saque in saques:
            print(f"Saque: -R${saque:.2f}")
        print(f"Saldo atual: R${saldo:.2f}")

while True:
    menu = '''
    Escolha uma operação:
    1 - Depositar
    2 - Sacar
    3 - Exibir Extrato
    4 - Sair
    '''
    print(menu)

    escolha = int(input())

    if escolha == 1:
        valor = float(input("Digite o valor a depositar: "))
        depositar(valor)
    elif escolha == 2:
        valor = float(input("Digite o valor a sacar: "))
        sacar(valor)
    elif escolha == 3:
        exibir_extrato()
    elif escolha == 4:
        print("Encerrando o sistema.")
        break
    else:
        print("Opção inválida. Escolha uma operação válida.")
