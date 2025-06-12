import os
import json

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

def login(cadastros):
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    for cliente in cadastros["clientes"]:
        if cliente["email"] == email and cliente["senha"] == senha:
            print("Login realizado com sucesso (Cliente)!")
            return

    for adm in cadastros["administradores"]:
        if adm["email"] == email and adm["senha"] == senha:
            print("Login realizado com sucesso (Administrador)!")
            return

    print("Email ou senha incorretos.")

def salvar_dados(cadastros, nome_arquivo="cadastros.json"):
    with open(nome_arquivo, "w") as arquivo:
        json.dump(cadastros, arquivo, indent=4)

def carregar_dados(nome_arquivo="cadastros.json"):
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, "r") as arquivo:
            return json.load(arquivo)
    else:
        return {"clientes": [], "administradores": []}

if __name__ == '__main__':
    cadastros = carregar_dados()

    while True:
        escolha = input("Qual operação deseja realizar? 1.Cliente 2.Administrador 3.Login 4.Sair: ")

        if escolha == '1':
            cliente = cadastro_cliente()
            cadastros["clientes"].append(cliente)
            salvar_dados(cadastros)
            print("Cliente cadastrado com sucesso!")

        elif escolha == '2':
            codigo = input("Digite o código de acesso para administradores: ")
            if codigo.lower() == "banana":
                adm = cadastro_adm()
                cadastros["administradores"].append(adm)
                salvar_dados(cadastros)
                print("Administrador cadastrado com sucesso!")
            else:
                print("Código de acesso inválido!")

        elif escolha == '3':
            login(cadastros)

        elif escolha == '4':
            break

        else:
            print("Opção inválida, tente novamente.")
