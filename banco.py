conta1_numero = 1
conta1_nome =
conta1_saldo =
conta1_transacoes = []

conta2_numero = 2
conta2_nome =
conta2_saldo =
conta2_transacoes = []

def depositar(conta, valor):
    global conta1_saldo, conta2_saldo
    if conta == 1:
        conta1_saldo += valor
        conta1_transacoes.append(f"Depósito de R${valor}")
    elif conta == 2:
        conta2_saldo += valor
        conta2_transacoes.append(f"Depósito de R${valor}")
    else:
        print("Conta não encontrada.")

def sacar(conta, valor):
    global conta1_saldo, conta2_saldo
    if conta == 1:
        if conta1_saldo >= valor:
            conta1_saldo -= valor
            conta1_transacoes.append(f"Saque de R${valor}")
        else:
            print("Saldo insuficiente.")
    elif conta == 2:
        if conta2_saldo >= valor:
            conta2_saldo -= valor
            conta2_transacoes.append(f"Saque de R${valor}")
        else:
            print("Saldo insuficiente.")
    else:
        print("Conta não encontrada.")


def transferir(origem, destino, valor):
    global conta1_saldo, conta2_saldo
    if origem == 1 and destino == 2:
        if conta1_saldo >= valor:
            conta1_saldo -= valor
            conta2_saldo += valor
            conta1_transacoes.append(f"Transferência de R${valor} para conta 2")
            conta2_transacoes.append(f"Recebimento de R${valor} da conta 1")
        else:
            print("Saldo insuficiente para transferência.")
    elif origem == 2 and destino == 1:
        if conta2_saldo >= valor:
            conta2_saldo -= valor
            conta1_saldo += valor
            conta2_transacoes.append(f"Transferência de R${valor} para conta 1")
            conta1_transacoes.append(f"Recebimento de R${valor} da conta 2")
        else:
            print("Saldo insuficiente para transferência.")
    else:
        print("Operação de transferência inválida.")

def extrato(conta):
    if conta == 1:
        print(f"Extrato da Conta 1 de {conta1_nome}:")
        print(f"Saldo: R${conta1_saldo}")
        print("Transações:")
        for transacao in conta1_transacoes:
            print(transacao)
    elif conta == 2:
        print(f"Extrato da Conta 2 de {conta2_nome}:")
        print(f"Saldo: R${conta2_saldo}")
        print("Transações:")
        for transacao in conta2_transacoes:
            print(transacao)
    else:
        print("Conta não encontrada.")
