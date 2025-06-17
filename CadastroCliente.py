import Utils as u
import bancosDeDados as c

def main_cadastro():
    opcao2 = input("Você deseja se cadastrar ou fazer login? (c/l): ")
    print()
    if opcao2 == "c":
        u.cadastro_cliente()

    elif opcao2 == "l":
        u.login()

def main_cadastro_funcionario():
    opcao2 = input("Você deseja se cadastrar ou fazer login? (c/l): ")
    print()
    if opcao2 == "c":
        u.cadastro_adm()

    elif opcao2 == "l":
        u.login_adm()