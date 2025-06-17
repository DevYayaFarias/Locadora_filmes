import Utils as u

def main_aluguel():
    filmes_para_alugar_ids = []
    while True:
        print("_-_-_- Bem-vindo à sessão de aluguel de filmes! -_-_-_")
        print()

        catalogo_filtrado = u.filtrar_catalogo()
        u.mostrar_detalhes_filmes(catalogo_filtrado)
        u.processo_aluguel(filmes_para_alugar_ids)
        continuar = u.finalizar_ou_cancelar_aluguel(filmes_para_alugar_ids)
        if not continuar:
            break
