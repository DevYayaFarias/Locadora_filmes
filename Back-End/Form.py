
def recomendar_filmes(catalogo):
    print("*-*-*- Bem-vindo à nossa locadora de filmes!! -*-*-*")

    genero = input("Digite o gênero de sua preferência: ").strip().lower()
    ano = input("Digite o ano de sua preferência (ou deixe em branco): ").strip()
    
     recomendados = []


    for filme in catalogo:
        genero_certo = genero.lower() in filme["genero"].lower() if genero else True
        ano_certo = filme["ano"] == ano if ano else True

        if genero_certo and ano_certo:
            recomendados.append(filme)


    if recomendados:
        print("\n Filmes recomendados para você:")
        for filme in recomendados:
            print(f"- {filme['titulo']} ({filme['ano']}) - Gênero: {filme['genero']}")
    else:
        print("\nDesculpe, não encontramos filmes com essas preferências.")


catalogo = []
recomendar_filmes(catalogo)
