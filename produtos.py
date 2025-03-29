from cadastro import DATABASE

class BancoDeDados:
    def __init__(self):
        self.conexao = DATABASE.connect(
            host="localhost",
            user="root",
            password="12345678",
            database="Loja"
        )
        self.cursor = self.conexao.cursor()

    def fechar_conexao(self):
        self.cursor.close()
        self.conexao.close()

class Produto:
    def __init__(self, nome, descricao, quantidade, preco):
        self.nome = nome
        self.descricao = descricao
        self.quantidade = quantidade
        self.preco = preco

    def salvar(self):
        db = BancoDeDados()
        sql = "INSERT INTO Produtos (nome, descricao, quantidade_disponivel, preco) VALUES (%s, %s, %s, %s)"
        valores = (self.nome, self.descricao, self.quantidade, self.preco)
        db.cursor.execute(sql, valores)
        db.conexao.commit()
        db.fechar_conexao()

    def listar():
        db = BancoDeDados()
        db.cursor.execute("SELECT * FROM Produtos")
        produtos = db.cursor.fetchall()
        db.fechar_conexao()
        return produtos

    def atualizar_quantidade(id_produto, nova_quantidade):
        db = BancoDeDados()
        sql = "UPDATE Produtos SET quantidade_disponivel = %s WHERE id = %s"
        valores = (nova_quantidade, id_produto)
        db.cursor.execute(sql, valores)
        db.conexao.commit()
        db.fechar_conexao()

    def remover(id_produto):
        db = BancoDeDados()
        sql = "DELETE FROM Produtos WHERE id = %s"
        valores = (id_produto,)
        db.cursor.execute(sql, valores)
        db.conexao.commit()
        db.fechar_conexao()

class Venda:
    def __init__(self, produto_id, quantidade_vendida):
        self.produto_id = produto_id
        self.quantidade_vendida = quantidade_vendida

    def registrar(self):
        db = BancoDeDados()
        db.cursor.execute("SELECT quantidade_disponivel FROM Produtos WHERE id = %s", (self.produto_id,))
        produto = db.cursor.fetchone()

        if produto and produto[0] >= self.quantidade_vendida:
            sql_venda = "INSERT INTO Vendas (produto_id, quantidade_vendida) VALUES (%s, %s)"
            valores_venda = (self.produto_id, self.quantidade_vendida)
            db.cursor.execute(sql_venda, valores_venda)
            
            nova_quantidade = produto[0] - self.quantidade_vendida
            sql_update = "UPDATE Produtos SET quantidade_disponivel = %s WHERE id = %s"
            valores_update = (nova_quantidade, self.produto_id)
            db.cursor.execute(sql_update, valores_update)
            db.conexao.commit()
            print("Venda registrada com sucesso!")
        else:
            print("Estoque insuficiente!")
        
            db.fechar_conexao()

    def listar_vendas():
        db = BancoDeDados()
        db.cursor.execute("SELECT * FROM Vendas")
        vendas = db.cursor.fetchall()
        db.fechar_conexao()
        return vendas
    
            
