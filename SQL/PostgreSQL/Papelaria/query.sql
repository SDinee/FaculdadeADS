-- Valor bruto, desconto em R$ e valor líquido por item

SELECT descricao,
       quantidade,
       preco_unit,
       quantidade * preco_unit                           AS valor_bruto,
       quantidade * preco_unit * desconto_pct / 100     AS valor_desconto,
       quantidade * preco_unit * (1 - desconto_pct/100) AS valor_liquido
FROM item_pedido
ORDER BY valor_liquido DESC;

-- Total geral do pedido por fornecedor

SELECT f.nome AS fornecedor,
       SUM(i.quantidade * i.preco_unit)                           AS total_bruto,
       SUM(i.quantidade * i.preco_unit * (1 - i.desconto_pct/100)) AS total_liquido
FROM item_pedido i
JOIN fornecedor f ON f.id = i.fornecedor_id
GROUP BY f.nome
ORDER BY total_liquido DESC;
 
-- Preço com reajuste de 10% e novo preço arredondado

SELECT descricao,
       preco_unit                      AS preco_atual,
       preco_unit * 1.10               AS preco_reajustado,
       ROUND(preco_unit * 1.10, 2)     AS preco_reajustado_arredondado
FROM item_pedido;