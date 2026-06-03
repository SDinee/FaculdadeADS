-- Selecionar todas as colunas da tabela produto

SELECT * FROM produto;

-- Selecionar apenas nome e preço com alias

SELECT nome AS nome_produto,
       preco AS preco_unitario
FROM produto;
 
-- Selecionar produtos e nome da categoria (duas tabelas)

SELECT p.nome   AS produto,
       c.nome   AS categoria,
       p.preco,
       p.estoque
FROM produto p, categoria c
WHERE p.categoria_id = c.id;