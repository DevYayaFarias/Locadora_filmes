import utils as u
import catalogo as c

u.bd_locadora()

print("_-_-_- Bem vindo a sessão de aluguel de filmes! -_-_-_")
print()

while True:
    ver = input("Deseja ver nosso catálogo? (s/n): ")
    print()

    if ver == "s":
        u.display_catalog(u.bd_locadora())
        break
    elif ver == "n":
        break
    else:
        print("Valor inválido, tente novamente")
        print()
        continue

filme_choice, attempt_choice = u.get_movie_info(u.bd_locadora())

u.get_additional_movie_info(u.bd_locadora(), filme_choice, attempt_choice)

print("_-_-_- ALUGUEL -_-_-_")
print()
u.rent_movies(u.bd_locadora())