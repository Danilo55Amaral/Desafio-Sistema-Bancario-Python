balance = 0
remove_limit = 500
extract = ""
remove_number = 0
NUMBER_LIMIT_REMOVE = 3

menu = """
    Bem vindo!               MyBank
==================================================

Realize uma operação!

[3] Depositar
[2] Sacar
[1] Extrato
[0] Sair

==================================================
Informe o número da operação => """

while True:
    option = input(menu)

    if option == "3":
        value = float(input("Adicione o valor do depósito: "))

        if value > 0:
            balance += value
            extract += f"Depósito: R$ {value:.2f}\n"
            print("Operação de depósito bem-sucedida!")
            
        else:
            print("A operação não pôde ser concluída! O valor informado é inválido.")

    elif option == "2":
        value = float(input("Adicione o valor do saque: "))

        if value > balance:
            print("A operação não pôde ser concluída! Você não tem saldo suficiente.")

        elif value > remove_limit:
            print("A operação não pôde ser concluída! O valor do saque excede o limite.")

        elif remove_number >= NUMBER_LIMIT_REMOVE:
            print("A operação não pôde ser concluída! Número máximo de saques excedido.")

        elif value > 0:
            balance -= value
            extract += f"Saque: R$ {value:.2f}\n"
            remove_number += 1
            print("Operação de saque concluída com sucesso!")

        else:
            print("A operação não pôde ser concluída! O valor informado é inválido.")

    elif option == "1":
        print(" EXTRATO ".center(50,"="))
        print("Não foram realizadas movimentações." if not extract else extract)
        print(f"\nSaldo: R$ {balance:.2f}\n"+("="*50))

    elif option == "0":
        print("Seção finalizada!\nObrigado por utilizar o MyBank ^-^")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")