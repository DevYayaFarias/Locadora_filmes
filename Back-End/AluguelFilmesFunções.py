import utilsAluguelFilmes as u

filmes = {
    "Matrix": {"ano": 1999, "genero": "Ficção", "disponibilidade": "disponível", "diretor": "Lana Wachowski, Lilly Wachowski", "empresa produtora": "Warner Bros.", "avaliação": 87},
    "Titanic": {"ano": 1997, "genero": "Romance", "disponibilidade": "disponível", "diretor": "James Cameron", "empresa produtora": "Paramount Pictures", "avaliação": 89},
    "Vingadores": {"ano": 2012, "genero": "Ação", "disponibilidade": "disponível", "diretor": "Joss Whedon", "empresa produtora": "Marvel Studios", "avaliação": 91},
    "Shrek": {"ano": 2001, "genero": "Animação", "disponibilidade": "disponível", "diretor": "Andrew Adamson, Vicky Jenson", "empresa produtora": "DreamWorks Animation", "avaliação": 88},
    "Coringa": {"ano": 2019, "genero": "Drama", "disponibilidade": "disponível", "diretor": "Todd Phillips", "empresa produtora": "Warner Bros.", "avaliação": 68},
    "Interestelar": {"ano": 2014, "genero": "Ficção", "disponibilidade": "disponível", "diretor": "Christopher Nolan", "empresa produtora": "Paramount Pictures", "avaliação": 86},
    "O Senhor dos Anéis": {"ano": 2001, "genero": "Fantasia", "disponibilidade": "disponível", "diretor": "Peter Jackson", "empresa produtora": "New Line Cinema", "avaliação": 91},
    "Harry Potter": {"ano": 2001, "genero": "Fantasia", "disponibilidade": "disponível", "diretor": "Chris Columbus", "empresa produtora": "Warner Bros.", "avaliação": 81},
    "Star Wars": {"ano": 1977, "genero": "Ficção", "disponibilidade": "disponível", "diretor": "George Lucas", "empresa produtora": "Lucasfilm", "avaliação": 92},
    "Jurassic Park": {"ano": 1993, "genero": "Aventura", "disponibilidade": "disponível", "diretor": "Steven Spielberg", "empresa produtora": "Universal Pictures", "avaliação": 91},
    "O Poderoso Chefão": {"ano": 1972, "genero": "Crime", "disponibilidade": "disponível", "diretor": "Francis Ford Coppola", "empresa produtora": "Paramount Pictures", "avaliação": 98},
    "Casablanca": {"ano": 1942, "genero": "Romance", "disponibilidade": "disponível", "diretor": "Michael Curtiz", "empresa produtora": "Warner Bros.", "avaliação": 97},
    "O Senhor dos Anéis: As Duas Torres": {"ano": 2002, "genero": "Fantasia", "disponibilidade": "disponível", "diretor": "Peter Jackson", "empresa produtora": "New Line Cinema", "avaliação": 95},
    "O Senhor dos Anéis: O Retorno do Rei": {"ano": 2003, "genero": "Fantasia", "disponibilidade": "disponível","diretor": "Peter Jackson", "empresa produtora": "New Line Cinema", "avaliação": 93},
    "O Grande Lebowski": {"ano": 1998, "genero": "Comédia", "disponibilidade": "disponível", "diretor": "Joel Coen, Ethan Coen", "empresa produtora": "PolyGram Filmed Entertainment", "avaliação": 83},
    "Pulp Fiction": {"ano": 1994, "genero": "Crime", "disponibilidade": "disponível", "diretor": "Quentin Tarantino", "empresa produtora": "Miramax Films", "avaliação": 92},
    "O Rei Leão": {"ano": 1994, "genero": "Animação", "disponibilidade": "disponível", "diretor": "Roger Allers, Rob Minkoff", "empresa produtora": "Walt Disney Feature Animation", "avaliação": 93},
    "Forrest Gump": {"ano": 1994, "genero": "Drama", "disponibilidade": "disponível", "diretor": "Robert Zemeckis", "empresa produtora": "Paramount Pictures", "avaliação": 71},
    "O Silêncio dos Inocentes": {"ano": 1991, "genero": "Terror", "disponibilidade": "disponível", "diretor": "Jonathan Demme", "empresa produtora": "Orion Pictures", "avaliação": 96},
    "Clube da Luta": {"ano": 1999, "genero": "Drama", "disponibilidade": "disponível", "diretor": "David Fincher", "empresa produtora": "20th Century Fox", "avaliação": 79},
    "O Exorcista": {"ano": 1973, "genero": "Terror", "disponibilidade": "disponível", "diretor": "William Friedkin", "empresa produtora": "Warner Bros.", "avaliação": 84},
    "O Iluminado": {"ano": 1980, "genero": "Terror", "disponibilidade": "disponível", "diretor": "Stanley Kubrick", "empresa produtora": "Warner Bros.", "avaliação": 93},
    "O Labirinto do Fauno": {"ano": 2006, "genero": "Fantasia", "disponibilidade": "disponível", "diretor": "Guillermo del Toro", "empresa produtora": "Warner Bros.", "avaliação": 95},
    "O Pianista": {"ano": 2002, "genero": "Drama", "disponibilidade": "disponível", "diretor": "Roman Polanski", "empresa produtora": "Canal+", "avaliação": 85},
    "O Cavaleiro das Trevas": {"ano": 2008, "genero": "Ação", "disponibilidade": "disponível", "diretor": "Christopher Nolan", "empresa produtora": "Warner Bros.", "avaliação": 94},
    "A Origem": {"ano": 2010, "genero": "Ficção", "disponibilidade": "disponível", "diretor": "Christopher Nolan", "empresa produtora": "Warner Bros.", "avaliação": 86},
    "O Lobo de Wall Street": {"ano": 2013, "genero": "Comédia", "disponibilidade": "disponível", "diretor": "Martin Scorsese", "empresa produtora": "Paramount Pictures", "avaliação": 79},
    "A Lista de Schindler": {"ano": 1993, "genero": "Drama", "disponibilidade": "disponível", "diretor": "Steven Spielberg", "empresa produtora": "Universal Pictures", "avaliação": 93},
    "O Poderoso Chefão: Parte II": {"ano": 1974, "genero": "Crime", "disponibilidade": "disponível", "diretor": "Francis Ford Coppola", "empresa produtora": "Paramount Pictures", "avaliação": 97},
    "O Poderoso Chefão: Parte III": {"ano": 1990, "genero": "Crime", "disponibilidade": "disponível", "diretor": "Francis Ford Coppola", "empresa produtora": "Paramount Pictures", "avaliação": 68},
    "O Grande Hotel Budapeste": {"ano": 2014, "genero": "Comédia", "disponibilidade": "disponível", "diretor": "Wes Anderson", "empresa produtora": "Fox Searchlight Pictures", "avaliação": 91},
    "O Menino do Pijama Listrado": {"ano": 2008, "genero": "Drama", "disponibilidade": "disponível", "diretor": "Mark Herman", "empresa produtora": "Miramax Films", "avaliação": 74},
    "O Regresso": {"ano": 2015, "genero": "Aventura", "disponibilidade": "disponível", "diretor": "Alejandro González Iñárritu", "empresa produtora": "20th Century Fox", "avaliação": 78},
    "O Discurso do Rei": {"ano": 2010, "genero": "Drama", "disponibilidade": "disponível", "diretor": "Tom Hooper", "empresa produtora": "The Weinstein Company", "avaliação": 86},
    "O Labirinto de Pan": {"ano": 2006, "genero": "Fantasia", "disponibilidade": "disponível", "diretor": "Guillermo del Toro", "empresa produtora": "Warner Bros.", "avaliação": 95},
    "O Grande Truque": {"ano": 2006, "genero": "Mistério", "disponibilidade": "disponível", "diretor": "Christopher Nolan", "empresa produtora": "Warner Bros.", "avaliação": 92},
    "O Quarto de Jack": {"ano": 2015, "genero": "Drama", "disponibilidade": "disponível", "diretor": "Lenny Abrahamson", "empresa produtora": "Element Pictures", "avaliação": 93}
}

print("_-_-_- Bem vindo a sessão de aluguel de filmes! -_-_-_")
print()

while True:
    ver = input("Deseja ver nosso catálogo? (s/n): ")
    print()

    if ver == "s":
        u.display_catalog(filmes)
        break
    elif ver == "n":
        break
    else:
        print("Valor inválido, tente novamente")
        print()
        continue

filme_choice, attempt_choice = u.get_movie_info(filmes)

u.get_additional_movie_info(filmes, filme_choice, attempt_choice)

print("_-_-_- ALUGUEL -_-_-_")
print()
u.rent_movies(filmes)