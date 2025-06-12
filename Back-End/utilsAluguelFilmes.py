def display_catalog(filmes):
    print("_-_-_- CATÁLOGO -_-_-_")
    print()
    for filme in filmes:
        print(filme)
    print()
    print("_-_-_-_-_-_-_-_-_-_-_-_")
    print()

def get_movie_info(filmes):
    while True:
        filme = input("Deseja informações sobre algum filme específico? (Ano / Gênero / Se ele está disponível...) \nDigite o nome dele! (n para sair): ")
        print()

        if filme in filmes:
            dados = filmes[filme]
            print(f"_-_-_-{filme.upper()}-_-_-_")
            print()
            for chave, valor in dados.items():
                print(f"{chave.capitalize()}: {valor}")
            print()
            break
        elif filme == "n":
            break
        else:
            print("Filme não encontrado ou resposta inválida.")
            tenta = input("Deseja tentar novamente? (s/n): ")
            print()
            while tenta != "s" and tenta != "n":
                print("inválido! tente novamente!")
                tenta = input("Deseja tentar novamente? (s/n): ")
                print()

            if tenta == "s":
                continue
            elif tenta == "n":
                break
    return filme, tenta

def get_additional_movie_info(filmes, initial_movie_choice, initial_attempt_choice):
    while initial_movie_choice != "n" and initial_attempt_choice != "n":
        interesse = input("Quer saber mais sobre algum outro filme? (Ano / Gênero / Se ele está disponível) \nDigite o nome dele! (n para sair): ")
        print()

        if interesse in filmes:
            dados = filmes[interesse]
            print(f"_-_-_-{interesse.upper()}-_-_-_")
            for chave, valor in dados.items():
                print(f"{chave.capitalize()}: {valor}")
            print()
            continue
        elif interesse == "n":
            break
        else:
            print("inválido, favor tentar novamente")
            print()

def rent_movies(filmes):
    filmes_alugar = []
    while True:
        alugar = input("Deseja alugar algum filme? (s/n): ")
        print()

        if alugar == "s":
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
                    print("Valor inválido, por favor digite outra quantidade (entre 1 e 100)")
                    print()
                    continue

                i = 1
                while i <= quantos:
                    filme_alugar = input(f"Digite o nome do {i}º filme (ou 0 para sair): ")
                    print()

                    if filme_alugar == '0':
                        break
                    elif filme_alugar in filmes:
                        if filmes[filme_alugar]["disponibilidade"].lower() == "disponível" and filme_alugar not in filmes_alugar:
                            filmes_alugar.append(filme_alugar)
                            i += 1
                            filmes[filme_alugar]["disponibilidade"] = "indisponível"
                        else:
                            print(f"Desculpe, o filme '{filme_alugar}' está indisponível no momento ou já foi inserido.")
                            print()
                    else:
                        print(f"Infelizmente não temos o filme '{filme_alugar}'")
                        print()
                break

            print(f"Esses são os filmes que você escolheu: {filmes_alugar}")
            print()
            fim = input(f"Deseja finalizar aluguel? ('s' para continuar / 'n' para cancelar / qualquer coisa para escolher filmes novamente): ")
            print()

            if fim == 's':
                total_price = len(filmes_alugar) * 15
                print(f"O total ficou {total_price} reais, para {len(filmes_alugar)} filme(s)")
                print("Obrigado por alugar com a gente!")
                break
            elif fim == 'n':
                for item in filmes_alugar:
                    filmes[item]["disponibilidade"] = "disponível"
                filmes_alugar = []
                print("Seu pedido foi cancelado.")
                break
            else:
                for item in filmes_alugar:
                    filmes[item]["disponibilidade"] = "disponível"
                filmes_alugar = []
                print()
                continue

        elif alugar == "n":
            print("_-_-_- Obrigado por acessar nossa locadora! -_-_-_")
            break
        else:
            print("Você não digitou um valor válido, por favor tente novamente!")