from models import Conta
from Banco import Banco



while True:
    print("\n1 - Cadastrar")
    print("2 - Login")
    print("3 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        username = input("Usuário: ")
        senha = input("Senha: ")
        Banco.cadastrar_usuario(username, senha)

    elif opcao == "2":
        username = input("Usuário: ")
        senha = input("Senha: ")
        usuario_logado = Banco.autenticar(username, senha)

        if usuario_logado:
            print("Login realizado.")
            
            # Menu da conta
            while True:
                print("\n1 - Depositar")
                print("2 - Sacar")
                print("3 - Saldo")
                print("4 - Logout")

                op = input("Escolha: ")

                if op == "1":
                    valor = float(input("Valor: "))
                    usuario_logado.conta.depositar(valor)

                elif op == "2":
                    valor = float(input("Valor: "))
                    usuario_logado.conta.sacar(valor)

                elif op == "3":
                    print("Saldo:", usuario_logado.conta.saldo)

                elif op == "4":
                    usuario_logado = None
                    break
        else:
            print("Credenciais inválidas.")

    elif opcao == "3":
        break

        