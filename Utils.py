import bancosDeDados as c

#==========================================================================================
#CADASTRO e LOGIN cliente
#==========================================================================================

def cadastro_cliente():
    nome = input("Qual o seu nome completo? ")
    cpf = input("Qual seu CPF? ")

    if len(cpf) != 11:
        print("CPF inválido! Deve conter exatamente 11 dígitos.")
        return

    data_nascimento = input("Digite sua data de nascimento: ")
    email = input("Digite seu email: ")
    senha = input("Crie uma senha: ")

    if nome in c.clientes:
        print("Você já tem um cadastro!")
        print()

    else:
        cliente = {
            "nome": nome,
            "cpf": cpf,
            "data_nascimento": data_nascimento,
            "email": email,
            "senha": senha
        }

        c.clientes[nome] = cliente
        print("Cadastro realizado com sucesso Cliente!")
        print()

def login():
    nome = input("Digite seu nome completo: ")
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    if nome in c.clientes:
        cliente = c.clientes[nome]
        if cliente["email"] == email and cliente["senha"] == senha:
            print("Login realizado com sucesso Cliente!")
            print()
            return True
        else:
            print("Email ou senha incorretos.")
            print()

    else:
        print("Nome não encontrado no cadastro.")
        print()

    return False

#==========================================================================================
#CADASTRO e LOGIN FUNCIONÁRIO
#==========================================================================================

def cadastro_adm():
    nome = input("Qual o seu nome? ")
    cpf = input("Qual seu CPF? ")
    if len(cpf) != 11:
        print("CPF inválido! Deve conter exatamente 11 dígitos.")
        print()
        return
    data_nascimento = input("Digite sua data de nascimento: ")
    email = input("Digite seu email: ")
    senha = input("Crie uma senha: ")
    carga_horaria = int(input("Qual a sua carga horária? "))

    if nome in c.funcionarios:
        print("Você já tem um cadastro!")
        print()

    else:
        adm = {
            "nome": nome,
            "cpf": cpf,
            "data_nascimento": data_nascimento,
            "email": email,
            "senha": senha,
            "carga_horaria": carga_horaria
        }
    c.funcionarios[nome] = adm

    print("Cadastro realizado com sucesso funcionário!")
    print()


def login_adm():
    nome = input("Digite seu nome completo: ")
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")


    if nome in c.funcionarios:
        funcionario = c.funcionarios[nome]
        if funcionario["email"] == email and funcionario["senha"] == senha:
            print("Login realizado com sucesso funcionário!")
            print()
            return True
        else:
            print("Email ou senha incorretos para funcionário.")
            print()

    else:
        print("Nome de funcionário não encontrado no cadastro.")
        print()

    return False

#==========================================================================================
#AlUGUEL DE FILMES
#==========================================================================================

def filtrar_catalogo():
    filtros = {}
    filmes_filtrados = {}

    while True:
        print("Deseja filtrar o catálogo? Temos as seguintes opções:")
        print("1. Gênero")
        print("2. Ano")
        print("3. Diretor")
        print("4. Empresa Produtora")
        print("5. Avaliação (mínima desejada)")
        print("6. Mostrar filtros E FILMES ENCONTRADOS (catálogo inteiro se não houver filtro nenhum)")
        print("7. Limpar filtros")
        print("0. Sair da filtragem e continuar")
        opcao = input("Digite o número da opção que deseja seguir: ")
        print()

        if opcao == '1':
            genero = input("Digite o gênero desejado: ").strip()
            filtros['genero'] = genero

        elif opcao == '2':
            try:
                ano = int(input("Digite o ano desejado: ").strip())
                filtros['ano'] = ano
            except ValueError:
                print("Ano inválido. Por favor, digite um número.")

        elif opcao == '3':
            diretor = input("Digite o nome do diretor: ").strip()
            filtros['diretor'] = diretor

        elif opcao == '4':
            empresa = input("Digite o nome da empresa produtora: ").strip()
            filtros['empresa produtora'] = empresa

        elif opcao == '5':
            try:
                avaliacao = int(input("Digite a avaliação mínima desejada (0-100): ").strip())
                if 0 <= avaliacao <= 100:
                    filtros['avaliação'] = avaliacao
                else:
                    print("Avaliação inválida. Digite um número entre 0 e 100.")
            except ValueError:
                print("Avaliação inválida. Por favor, digite um número.")

        elif opcao == '6':
            if not filtros:
                print("Nenhum filtro aplicado ainda.")
            else:
                print("\n--- Filtros Atuais ---")
                for key, value in filtros.items():
                    print(f"{key.capitalize()}: {value}")
                print("----------------------")

            for filme_id, dados_filme in c.catalogo.items():
                match = True
                for criterio, valor_filtro in filtros.items():
                    if criterio == 'avaliação':
                        if dados_filme.get(criterio, 0) < valor_filtro:
                            match = False
                            break
                    elif criterio in dados_filme:
                        if isinstance(dados_filme[criterio], str) and isinstance(valor_filtro, str):
                            if valor_filtro.lower() not in dados_filme[criterio].lower():
                                match = False
                                break
                        elif dados_filme[criterio] != valor_filtro:
                            match = False
                            break
                    else:
                        match = False
                        break
                if match:
                    filmes_filtrados[filme_id] = dados_filme

            if filmes_filtrados:
                print("\n--- Filmes Encontrados (Filtrados) ---")
                for filme_id, dados_filme in filmes_filtrados.items():
                    print(
                        f"Código: {filme_id} - Nome: {dados_filme['nome']} (Gênero: {dados_filme['genero']}, Ano: {dados_filme['ano']})")
                print("--------------------------------------\n")
            else:
                print("Nenhum filme encontrado com os filtros aplicados.")

        elif opcao == '7':
            filtros = {}
            print("Filtros limpos com sucesso!")
        elif opcao == '0':
            print("Saindo da filtragem.")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

        continuar_filtrando = input("Digite 's' para escolher VER FILMES FILTRADOS ou ADICIONAR MAIS FILTROS, ou 'n' para seguir direto (s/n): ")
        print()
        if continuar_filtrando.lower() == 'n':
            break

    return filmes_filtrados


def mostrar_detalhes_filmes(catalogo_filtrado):
    tentar_novamente = ""
    filme_id_input = input(
        "Deseja mais informações sobre algum filme específico filtrado? (Ano / Gênero / Se ele está disponível...)\nDigite o CÓDIGO dele! (n se nn desejar): ")
    print()

    if filme_id_input.lower() == "n":
        return

    if filme_id_input in catalogo_filtrado:
        dados = catalogo_filtrado[filme_id_input]
        print(f"_-_-_-{dados['nome'].upper()} (CÓDIGO: {filme_id_input})-_-_-_")
        print()
        for chave, valor in dados.items():
            print(f"{chave.capitalize()}: {valor}")
        print()
    else:
        print("Código de filme não encontrado no catálogo filtrado ou resposta inválida.")
        tentar_novamente = input("Deseja tentar novamente? (s/n): ")
        print()
        while tentar_novamente.lower() not in ["s", "n"]:
            print("Inválido! Tente novamente!")
            tentar_novamente = input("Deseja tentar novamente? (s/n): ")
            print()

        if tentar_novamente.lower() == "s":
            mostrar_detalhes_filmes(catalogo_filtrado)
        elif tentar_novamente.lower() == "n":
            return

    while filme_id_input.lower() != "n" and tentar_novamente.lower() != "n":
        interesse_id = input(
            "Quer saber mais sobre algum outro filme? (Ano / Gênero / Se ele está disponível)\nDigite o CÓDIGO dele! (n para sair): ")
        print()

        if interesse_id.lower() == "n":
            break

        if interesse_id in catalogo_filtrado:
            dados = catalogo_filtrado[interesse_id]
            print(f"_-_-_-{dados['nome'].upper()} (CÓDIGO: {interesse_id})-_-_-_")
            for chave, valor in dados.items():
                print(f"{chave.capitalize()}: {valor}")
            print()
            continue
        else:
            print("Código de filme inválido no catálogo filtrado, favor tentar novamente.")
            print()


def processo_aluguel(filmes_para_alugar_ids):
    alugar_filme = input("Deseja alugar algum filme? (s/n): ")
    print()

    while True:
        if alugar_filme.lower() == "s":
            while True:
                quantos_alugar_str = input("Quantos filmes você deseja alugar? (máx - 100): ")
                print()

                try:
                    quantos = int(quantos_alugar_str)
                except ValueError:
                    print("Você não digitou um número! Tente novamente!")
                    print()
                    continue

                if not (1 <= quantos <= 100):
                    print("Valor inválido, por favor digite outra quantidade (entre 1 e 100).")
                    print()
                    continue

                i = 0
                while i < quantos:
                    filme_id_alugar = input(f"Digite o CÓDIGO do {i + 1}º filme (ou 0 para sair): ")
                    print()

                    if filme_id_alugar == '0':
                        break

                    if filme_id_alugar in c.catalogo:
                        if c.catalogo[filme_id_alugar]["disponibilidade"].lower() == "disponível":
                            filmes_para_alugar_ids.append(filme_id_alugar)
                            c.catalogo[filme_id_alugar]["disponibilidade"] = "indisponível"
                            i += 1
                        else:
                            print(
                                f"Desculpe, o filme '{c.catalogo[filme_id_alugar]['nome']}' (CÓDIGO: {filme_id_alugar}) está indisponível no momento ou já foi inserido.")
                            print()
                    else:
                        print(f"Infelizmente não encontramos filme com o código '{filme_id_alugar}'.")
                        print()
                break
            break

        elif alugar_filme.lower() == "n":
            print("_-_-_- Obrigado por acessar nossa locadora! -_-_-_")
            break
        else:
            print("Você não digitou um valor válido, por favor tente novamente!")
            alugar_filme = input("Deseja alugar algum filme? (s/n): ")
            print()


def finalizar_ou_cancelar_aluguel(filmes_para_alugar_ids):
    if filmes_para_alugar_ids:
        print("Esses são os filmes que você escolheu:")
        for filme_id in filmes_para_alugar_ids:
            print(f"- {c.catalogo[filme_id]['nome']} (CÓDIGO: {filme_id})")
        print()
        fim_aluguel = input(
            "Deseja finalizar aluguel? ('s' para continuar / 'n' para cancelar / qualquer coisa para escolher filmes novamente): ")
        print()

        if fim_aluguel.lower() == 's':
            print(f"O total ficou R${len(filmes_para_alugar_ids) * 15:.2f}, para {len(filmes_para_alugar_ids)} filme(s).")
            print("Obrigado por alugar com a gente!")
            mais = input("Deseja continuar nessa sessão? (s/n): ")
            print()

            if mais == "s":
                return True
            else:
                return False
        elif fim_aluguel.lower() == 'n':
            for filme_id_alugado in filmes_para_alugar_ids:
                c.catalogo[filme_id_alugado]["disponibilidade"] = "disponível"
            filmes_para_alugar_ids.clear()
            print("Seu pedido foi cancelado.")
            mais = input("Deseja continuar nessa sessão? (s/n): ")
            print()
            if mais == "s":
                return True
            else:
                return False

        else:
            for filme_id_alugado in filmes_para_alugar_ids:
                c.catalogo[filme_id_alugado]["disponibilidade"] = "disponível"
            filmes_para_alugar_ids.clear()
            print("Sessão de aluguel reiniciada. Por favor, comece novamente a seleção de filmes.")
            return True