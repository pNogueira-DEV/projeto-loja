from conexao import conector

def criar_tabela():
    conexao,cursor = conector()
    if conexao:
        try:
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS produtos(
                id SERIAL PRIMARY KEY,
                nome TEXT NOT NULL,
                categoria TEXT NOT NULL,
                preco REAL NOT NULL,
                quantidade INTEGER
                )
            """)
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao criar tabela:{erro}")
        finally:
            cursor.close()
            conexao.close()



def cadastrar_produto(nome_produto, categoria_produto, preco_produto, quant_produto):
    conexao, cursor = conector()
    if conexao:
        try:
            cursor.execute(
                "INSERT INTO produtos (nome, categoria, preco, quantidade) VALUES (%s, %s, %s, %s)",
                 (nome_produto, categoria_produto, preco_produto, quant_produto)
            )
            conexao.commit()
        except Exception as erro:
            print(f" Erro ao cadastrar o produto: {erro}")
        finally:
            cursor.close()
            conexao.close()

def listar_produto():
    conexao, cursor = conector()
    if conexao:
        try:
            cursor.execute(
                "SELECT * FROM produtos ORDER BY ID"
            )
            return cursor.fetchall()
        except Exception as erro:
            print(f"Erro ao tentar exibir produtos: {erro}")
            return[]
        finally:
            cursor.close()
            conexao.close()




            





    




