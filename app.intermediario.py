usuarios = []
contas = []
numero_conta = 1
saldo_inicial = 0.0

def criar_usuario(nome, data_nascimento, cpf, endereco):
    cpf_numeros = cpf.replace('.', '').replace('-', '')
    for usuario in usuarios:
        if usuario['cpf'] == cpf_numeros:
            print("CPF já cadastrado. Não é possível criar o usuário.")
            return
    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf_numeros, 'endereco': endereco})
    print("Usuário cadastrado com sucesso.")

def criar_conta(usuario):
    global numero_conta
    contas.append({'agencia': '0001', 'numero_conta': numero_conta, 'usuario': usuario})
    numero_conta += 1
    print(f"Conta corrente criada com sucesso. Número da conta: {numero_conta - 1}")

def depositar(valor):
    global saldo_inicial
    saldo_inicial += valor
    print(f"Depósito de R${valor:.2f} realizado com sucesso.")

def sacar(valor):
    global saldo_inicial
    if saldo_inicial >= valor:
        saldo_inicial -= valor
        print(f"Saque de R${valor:.2f} realizado com sucesso.")
    else:
        print("Não é possível sacar. Saldo insuficiente.")

def exibir_extrato(depositos, saques):
    print("Extrato:")
    for deposito in depositos:
        print(f"Depósito: R${deposito:.2f}")
    for saque in saques:
        print(f"Saque: -R${saque:.2f}")
    print(f"Saldo atual: R${saldo_inicial:.2f}")

def main():
    global saldo_inicial
    while True:
        menu = '''
        Escolha uma operação:
        1 - Cadastrar Usuário
        2 - Criar Conta Corrente
        3 - Depositar
        4 - Sacar
        5 - Exibir Extrato
        6 - Sair
        '''
        print(menu)

        escolha = int(input())

        if escolha == 1:
            nome = input("Digite o nome do usuário: ")
            data_nascimento = input("Digite a data de nascimento: ")
            cpf = input("Digite o CPF: ")
            endereco = input("Digite o endereço: ")
            criar_usuario(nome, data_nascimento, cpf, endereco)
        elif escolha == 2:
            if usuarios:
                print("Usuários cadastrados:")
                for i, usuario in enumerate(usuarios):
                    print(f"{i + 1} - {usuario['nome']} - CPF: {usuario['cpf']}")
                usuario_escolhido = int(input("Digite o número do usuário para criar a conta: ")) - 1
                if 0 <= usuario_escolhido < len(usuarios):
                    criar_conta(usuarios[usuario_escolhido])
                else:
                    print("Usuário não encontrado.")
            else:
                print("Não há usuários cadastrados.")
        elif escolha == 3:
            valor = float(input("Digite o valor a depositar: "))
            depositar(valor)
        elif escolha == 4:
            valor = float(input("Digite o valor a sacar: "))
            sacar(valor)
        elif escolha == 5:
            exibir_extrato([], [])
        elif escolha == 6:
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida. Escolha uma operação válida.")

if __name__ == "__main__":
    main()
