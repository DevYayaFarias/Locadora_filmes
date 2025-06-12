"""
AÇOES:
cadastrar filmes
remover filmes
ver quantidade de filmes laugados
ver total do dinheiro ganho no dia
"""

films_alugados = 0      #Quantidades de filmes no estado: "alugados"
val_alugados = 0        #Somatoria do valor de cada filme "alugado" no dia
catalg_films = {"1":["Back to the Future I","Goonies","Senhor dos aneis"],
                "2":["Terminator II", "James Bond:NO TIME TO DIE","Missão Impossível III"],
                "3":["Escola de Rock", "Free Guy"],
                "4":[],
                "5":[]
                   }
generos = [
        "1. Aventura",
        "2. Ação",
        "3. Comedia",
        "4. Animaçao",
        "5. Drama"
    ]


# Imprimindo menu com as opções e recebendo seleção da ferramenta
def menu(options):
    print("***** BEM-VINDO ADMINISTRADOR *****")
    for option in options:
        print(option)
    return get_int_option(1, 5, "Digite o numero da opçao selecionada(1 a 5): ")

#Mostra Generos
def show_generos():
    print("-- Generos ---")
    for gen in generos:
        print(gen)
    return get_int_option(1, 5, "Selecione um genero: ")

#Mostra filmes do genero selecionado
def filmes_in_genero(genero):
    print("\nFilmes do genero:")
    contador = 0
    for filme in catalg_films[genero]:
        contador += 1
        print(f"{contador} - {filme}")
    return get_int_option(1, len(catalg_films[genero]), "Digite o codigo do filme a selecionar: ")


# Verifica que a escolha da opçao inserida esteja dentro das fornecidas no menu
def get_int_option(min, max, message):
    while True:
        try:
            op = int(input(message))
            if op >= min and op <= max:
                return op
            else:
                print("O valor deve estar entre", min, "e", max)
        except:
            print("Valor inválido")


# Adicionar filme
def add_film():
    print("Adicionar filme - selecionado\n")
    genero = show_generos()
    filmes_in_genero(genero)
    adicionar = input("Escreva o nome do filme a adicionar: ")
    catalg_films[genero].append(adicionar)
    print("Filme adicionado com sucesso :)\n")


# Deletar filme
def del_film():
    print("Deletar filme - selecionado\n")
    genero = show_generos()
    deletar = filmes_in_genero(genero)
    catalg_films[genero].pop(deletar)
    print("Filme adicionado com sucesso :)\n")

# Mostrar filmes alugados
def mostrar_alugados():
    print(films_alugados)


#Mostrar soma dos valores alugados no dia
def valor_do_dia():
    print(val_alugados)

# Função principal
def main(option):
    while True:
        op = menu(option)
        if op == 1:
            add_film()
        elif op == 2:
            del_film()
        elif op == 3:
            mostrar_alugados()
        elif op == 4:
            mostrar_alugados()
        else:
            break

if __name__ == '__main__':
    menu_adm = [
        "1. Cadastrar Filme",
        "2. Remover Filme",
        "3. Quantidade de filmes alugados no dia",
        "4. Valor total do dia",
        "5. Sair"
    ]
main(menu_adm)