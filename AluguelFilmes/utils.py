def bd_locadora():
    filmes = {
        "Matrix": {"ano": 1999, "genero": "Ficção", "disponibilidade": "disponível",
                   "diretor": "Lana Wachowski, Lilly Wachowski", "empresa produtora": "Warner Bros.", "avaliação": 87},
        "Titanic": {"ano": 1997, "genero": "Romance", "disponibilidade": "disponível", "diretor": "James Cameron",
                    "empresa produtora": "Paramount Pictures", "avaliação": 89},
        "Vingadores": {"ano": 2012, "genero": "Ação", "disponibilidade": "disponível", "diretor": "Joss Whedon",
                       "empresa produtora": "Marvel Studios", "avaliação": 91},
        "Shrek": {"ano": 2001, "genero": "Animação", "disponibilidade": "disponível",
                  "diretor": "Andrew Adamson, Vicky Jenson", "empresa produtora": "DreamWorks Animation",
                  "avaliação": 88},
        "Coringa": {"ano": 2019, "genero": "Drama", "disponibilidade": "disponível", "diretor": "Todd Phillips",
                    "empresa produtora": "Warner Bros.", "avaliação": 68},
        "Interestelar": {"ano": 2014, "genero": "Ficção", "disponibilidade": "disponível",
                         "diretor": "Christopher Nolan", "empresa produtora": "Paramount Pictures", "avaliação": 86},
        "O Senhor dos Anéis": {"ano": 2001, "genero": "Fantasia", "disponibilidade": "disponível",
                               "diretor": "Peter Jackson", "empresa produtora": "New Line Cinema", "avaliação": 91},
        "Harry Potter": {"ano": 2001, "genero": "Fantasia", "disponibilidade": "disponível",
                         "diretor": "Chris Columbus", "empresa produtora": "Warner Bros.", "avaliação": 81},
        "Star Wars": {"ano": 1977, "genero": "Ficção", "disponibilidade": "disponível", "diretor": "George Lucas",
                      "empresa produtora": "Lucasfilm", "avaliação": 92},
        "Jurassic Park": {"ano": 1993, "genero": "Aventura", "disponibilidade": "disponível",
                          "diretor": "Steven Spielberg", "empresa produtora": "Universal Pictures", "avaliação": 91},
        "O Poderoso Chefão": {"ano": 1972, "genero": "Crime", "disponibilidade": "disponível",
                              "diretor": "Francis Ford Coppola", "empresa produtora": "Paramount Pictures",
                              "avaliação": 98},
        "Casablanca": {"ano": 1942, "genero": "Romance", "disponibilidade": "disponível", "diretor": "Michael Curtiz",
                       "empresa produtora": "Warner Bros.", "avaliação": 97},
        "O Senhor dos Anéis: As Duas Torres": {"ano": 2002, "genero": "Fantasia", "disponibilidade": "disponível",
                                               "diretor": "Peter Jackson", "empresa produtora": "New Line Cinema",
                                               "avaliação": 95},
        "O Senhor dos Anéis: O Retorno do Rei": {"ano": 2003, "genero": "Fantasia", "disponibilidade": "disponível",
                                                 "diretor": "Peter Jackson", "empresa produtora": "New Line Cinema",
                                                 "avaliação": 93},
        "O Grande Lebowski": {"ano": 1998, "genero": "Comédia", "disponibilidade": "disponível",
                              "diretor": "Joel Coen, Ethan Coen", "empresa produtora": "PolyGram Filmed Entertainment",
                              "avaliação": 83},
        "Pulp Fiction": {"ano": 1994, "genero": "Crime", "disponibilidade": "disponível",
                         "diretor": "Quentin Tarantino", "empresa produtora": "Miramax Films", "avaliação": 92},
        "O Rei Leão": {"ano": 1994, "genero": "Animação", "disponibilidade": "disponível",
                       "diretor": "Roger Allers, Rob Minkoff", "empresa produtora": "Walt Disney Feature Animation",
                       "avaliação": 93},
        "Forrest Gump": {"ano": 1994, "genero": "Drama", "disponibilidade": "disponível", "diretor": "Robert Zemeckis",
                         "empresa produtora": "Paramount Pictures", "avaliação": 71},
        "O Silêncio dos Inocentes": {"ano": 1991, "genero": "Terror", "disponibilidade": "disponível",
                                     "diretor": "Jonathan Demme", "empresa produtora": "Orion Pictures",
                                     "avaliação": 96},
        "Clube da Luta": {"ano": 1999, "genero": "Drama", "disponibilidade": "disponível", "diretor": "David Fincher",
                          "empresa produtora": "20th Century Fox", "avaliação": 79},
        "O Exorcista": {"ano": 1973, "genero": "Terror", "disponibilidade": "disponível", "diretor": "William Friedkin",
                        "empresa produtora": "Warner Bros.", "avaliação": 84},
        "O Iluminado": {"ano": 1980, "genero": "Terror", "disponibilidade": "disponível", "diretor": "Stanley Kubrick",
                        "empresa produtora": "Warner Bros.", "avaliação": 93},
        "O Labirinto do Fauno": {"ano": 2006, "genero": "Fantasia", "disponibilidade": "disponível",
                                 "diretor": "Guillermo del Toro", "empresa produtora": "Warner Bros.", "avaliação": 95},
        "O Pianista": {"ano": 2002, "genero": "Drama", "disponibilidade": "disponível", "diretor": "Roman Polanski",
                       "empresa produtora": "Canal+", "avaliação": 85},
        "O Cavaleiro das Trevas": {"ano": 2008, "genero": "Ação", "disponibilidade": "disponível",
                                   "diretor": "Christopher Nolan", "empresa produtora": "Warner Bros.",
                                   "avaliação": 94},
        "A Origem": {"ano": 2010, "genero": "Ficção", "disponibilidade": "disponível", "diretor": "Christopher Nolan",
                     "empresa produtora": "Warner Bros.", "avaliação": 86},
        "O Lobo de Wall Street": {"ano": 2013, "genero": "Comédia", "disponibilidade": "disponível",
                                  "diretor": "Martin Scorsese", "empresa produtora": "Paramount Pictures",
                                  "avaliação": 79},
        "A Lista de Schindler": {"ano": 1993, "genero": "Drama", "disponibilidade": "disponível",
                                 "diretor": "Steven Spielberg", "empresa produtora": "Universal Pictures",
                                 "avaliação": 93},
        "O Poderoso Chefão: Parte II": {"ano": 1974, "genero": "Crime", "disponibilidade": "disponível",
                                        "diretor": "Francis Ford Coppola", "empresa produtora": "Paramount Pictures",
                                        "avaliação": 97},
        "O Poderoso Chefão: Parte III": {"ano": 1990, "genero": "Crime", "disponibilidade": "disponível",
                                         "diretor": "Francis Ford Coppola", "empresa produtora": "Paramount Pictures",
                                         "avaliação": 68},
        "O Grande Hotel Budapeste": {"ano": 2014, "genero": "Comédia", "disponibilidade": "disponível",
                                     "diretor": "Wes Anderson", "empresa produtora": "Fox Searchlight Pictures",
                                     "avaliação": 91},
        "O Menino do Pijama Listrado": {"ano": 2008, "genero": "Drama", "disponibilidade": "disponível",
                                        "diretor": "Mark Herman", "empresa produtora": "Miramax Films",
                                        "avaliação": 74},
        "O Regresso": {"ano": 2015, "genero": "Aventura", "disponibilidade": "disponível",
                       "diretor": "Alejandro González Iñárritu", "empresa produtora": "20th Century Fox",
                       "avaliação": 78},
        "O Discurso do Rei": {"ano": 2010, "genero": "Drama", "disponibilidade": "disponível", "diretor": "Tom Hooper",
                              "empresa produtora": "The Weinstein Company", "avaliação": 86},
        "O Labirinto de Pan": {"ano": 2006, "genero": "Fantasia", "disponibilidade": "disponível",
                               "diretor": "Guillermo del Toro", "empresa produtora": "Warner Bros.", "avaliação": 95},
        "O Grande Truque": {"ano": 2006, "genero": "Mistério", "disponibilidade": "disponível",
                            "diretor": "Christopher Nolan", "empresa produtora": "Warner Bros.", "avaliação": 92},
        "O Quarto de Jack": {"ano": 2015, "genero": "Drama", "disponibilidade": "disponível",
                             "diretor": "Lenny Abrahamson", "empresa produtora": "Element Pictures", "avaliação": 93}
    }
    return filmes

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