from database import *

criar_tabela()


def cadastrar_produto():
    nome = input("Nome do produto: ")
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço: R$ "))

    adicionar_produto(nome, quantidade, preco)

    print("Produto cadastrado com sucesso!")


def mostrar_produtos():
    produtos = listar_produtos()

    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    print("\n=== PRODUTOS ===")

    for produto in produtos:
        print(
            f"ID: {produto[0]} | "
            f"Nome: {produto[1]} | "
            f"Qtd: {produto[2]} | "
            f"Preço: R$ {produto[3]:.2f}"
        )


def adicionar_estoque():
    id_produto = int(input("ID do produto: "))
    quantidade = int(input("Quantidade a adicionar: "))

    entrada_estoque(id_produto, quantidade)

    print("Estoque atualizado!")


def remover_estoque():
    id_produto = int(input("ID do produto: "))
    quantidade = int(input("Quantidade a remover: "))

    saida_estoque(id_produto, quantidade)

    print("Estoque atualizado!")


def pesquisar_produto():
    nome = input("Nome do produto: ")

    produtos = buscar_produto(nome)

    for produto in produtos:
        print(
            f"ID: {produto[0]} | "
            f"Nome: {produto[1]} | "
            f"Qtd: {produto[2]} | "
            f"Preço: R$ {produto[3]:.2f}"
        )


def remover_produto():
    id_produto = int(input("ID do produto: "))

    excluir_produto(id_produto)

    print("Produto excluído com sucesso!")


while True:
    print("\n===== SISTEMA DE ESTOQUE =====")
    print("1 - Cadastrar Produto")
    print("2 - Listar Produtos")
    print("3 - Entrada de Estoque")
    print("4 - Saída de Estoque")
    print("5 - Buscar Produto")
    print("6 - Excluir Produto")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_produto()

    elif opcao == "2":
        mostrar_produtos()

    elif opcao == "3":
        adicionar_estoque()

    elif opcao == "4":
        remover_estoque()

    elif opcao == "5":
        pesquisar_produto()

    elif opcao == "6":
        remover_produto()

    elif opcao == "0":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida.")