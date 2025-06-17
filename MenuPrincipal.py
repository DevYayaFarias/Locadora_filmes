import AluguelFilmes as aluguel
import CadastroCliente as cadastro

def show_menu():
    print("_-_-_- Bem Vindo a nossa Locadora -_-_-_")
    print()

    while True:
        tipo = input("Você é cliente ou funcionário? (c/f): ")
        print()
        if tipo == "c":
            print("_-_-_- Menu -_-_-_")
            print()
            print("1. Fazer cadastro ou login")
            print("2. Fazer Aluguel de filmes")

            opcao1 = input("Digite o número referente a opção desejada: ")
            print()
            try:
                opcao1 = int(opcao1)
            except ValueError:
                print("Inválido, começando de novo")

            if opcao1 == 1:
                cadastro.main_cadastro()

            if opcao1 == 2:
                aluguel.main_aluguel()


        elif tipo == "f":
            senhageral = input("Digite a senha geral para acessar essa sessão: ")

            if senhageral == "banana":
                print()
                print("_-_-_- Menu -_-_-_")
                print()
                print("1. Fazer cadastro ou login")

                opcao11 = input("Digite o número referente a opção desejada: ")
                print()
                try:
                    opcao11 = int(opcao11)
                except ValueError:
                    print("Inválido, começando de novo")

                if opcao11 == 1:
                    cadastro.main_cadastro_funcionario()

            else:
                print("Senha incorreta")
                print()

        else:
            print("erro, tente digitar novamente")

if __name__ == '__main__':
    show_menu()