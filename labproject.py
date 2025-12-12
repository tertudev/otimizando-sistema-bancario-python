# Sistema Bancário em Python

saldo = 0
limite = 500
extrato = ""
saques = 0
limite_saques = 3

while True:
    print("\n[d] Depositar")
    print("[s] Sacar")
    print("[e] Extrato")
    print("[q] Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "d":
        valor = float(input("Quanto deseja depositar? "))
        if valor > 0:
            saldo = saldo + valor
            extrato = extrato + "Depósito: " + str(valor) + "\n"
            print("Depósito realizado!")
        else:
            print("Valor inválido!")

    elif opcao == "s":
        valor = float(input("Quanto deseja sacar? "))
        if valor > saldo:
            print("Saldo insuficiente!")
        elif valor > limite:
            print("Valor acima do limite!")
        elif saques >= limite_saques:
            print("Limite de saques atingido!")
        elif valor > 0:
            saldo = saldo - valor
            extrato = extrato + "Saque: " + str(valor) + "\n"
            saques = saques + 1
            print("Saque realizado!")
        else:
            print("Valor inválido!")

    elif opcao == "e":
        print("\n=== EXTRATO ===")
        if extrato == "":
            print("Nenhuma movimentação.")
        else:
            print(extrato)
        print("Saldo:", saldo)
        print("===============")

    elif opcao == "q":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida!")
