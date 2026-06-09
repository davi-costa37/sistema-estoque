import sqlite3


def conectar():
    return sqlite3.connect("estoque.db")


def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        quantidade INTEGER NOT NULL,
        preco REAL NOT NULL
    )
    """)

    conexao.commit()
    conexao.close()


def adicionar_produto(nome, quantidade, preco):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO produtos (nome, quantidade, preco)
    VALUES (?, ?, ?)
    """, (nome, quantidade, preco))

    conexao.commit()
    conexao.close()


def listar_produtos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM produtos")

    produtos = cursor.fetchall()

    conexao.close()

    return produtos


def buscar_produto(nome):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM produtos
    WHERE nome LIKE ?
    """, (f"%{nome}%",))

    resultado = cursor.fetchall()

    conexao.close()

    return resultado


def excluir_produto(id_produto):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    DELETE FROM produtos
    WHERE id = ?
    """, (id_produto,))

    conexao.commit()
    conexao.close()


def entrada_estoque(id_produto, quantidade):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    UPDATE produtos
    SET quantidade = quantidade + ?
    WHERE id = ?
    """, (quantidade, id_produto))

    conexao.commit()
    conexao.close()


def saida_estoque(id_produto, quantidade):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    UPDATE produtos
    SET quantidade = quantidade - ?
    WHERE id = ?
    """, (quantidade, id_produto))

    conexao.commit()
    conexao.close()