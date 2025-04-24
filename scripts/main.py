from utils import menu_principal, carregar_contatos

if __name__ ==  "__main__":
    lista_contatos = carregar_contatos()
    menu_principal(lista_contatos)