CREATE DATABASE Loja;
USE Loja;

CREATE TABLE Produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT,
    quantidade_disponivel INT NOT NULL,
    preco DECIMAL(10,2) NOT NULL
);

CREATE TABLE Vendas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    produto_id INT,
    quantidade_vendida INT NOT NULL,
    data_venda DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (produto_id) REFERENCES Produtos(id)
);