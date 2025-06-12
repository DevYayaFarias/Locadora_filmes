def cadastro_cliente():
    nome = input("Qual o seu nome? ")
    cpf = input("Qual seu CPF? ")
    if len(cpf) == 11:
        pass
    data_nascimento = input("Digite sua data de nascimento: ")
    email = input("Digite seu email: ")
    senha = input("Crie uma senha: ")

    cliente = {
        "nome": nome,
        "cpf": cpf,
        "data_nascimento": data_nascimento,
        "email": email,
        "senha": senha
    }

    return cliente


def cadastro_adm():
    nome = input("Qual o seu nome? ")
    cpf = input("Qual seu CPF? ")
    if len(cpf) == 11:
        pass
    data_nascimento = input("Digite sua data de nascimento: ")
    email = input("Digite seu email: ")
    senha = input("Crie uma senha: ")
    carga_horaria = int(input("Qual a sua carga horária? "))

    adm = {
        "nome": nome,
        "cpf": cpf,
        "data_nascimento": data_nascimento,
        "email": email,
        "senha": senha,
        "carga_horaria": carga_horaria 
    }

    return adm


if __name__ == '__main__':
    cadastros = { 
        "clientes": ["Clientes:"],
        "administradores": ["Admnistradores:"]
    }

    while True:
        escolha = input("Qual cadastro deseja realizar? 1.Cliente 2.Administrador 3.Sair: ")

        if escolha == '1':
            cliente = cadastro_cliente()
            cadastros["clientes"].append(cliente)
            print("Cliente cadastrado com sucesso!")
            print(cadastros["clientes"])

        elif escolha == '2':
            codigo = input("Digite o código de acesso para administradores: ")
            if codigo.lower() == "banana":
                adm = cadastro_adm()
                cadastros["administradores"].append(adm)
                print("Administrador cadastrado com sucesso!")
                print(cadastros["administradores"])
            else:
                print("Código de acesso inválido!")

        elif escolha == '3':
            break

        else:
            print("Opção inválida, tente novamente.")
