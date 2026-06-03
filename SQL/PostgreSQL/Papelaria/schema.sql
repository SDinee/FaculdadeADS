CREATE TABLE fornecedor (
  id   SERIAL PRIMARY KEY,
  nome VARCHAR(60) NOT NULL
);
 
CREATE TABLE item_pedido (
  id            SERIAL PRIMARY KEY,
  fornecedor_id INT REFERENCES fornecedor(id),
  descricao     VARCHAR(80),
  quantidade    INT,
  preco_unit    NUMERIC(10,2),
  desconto_pct  NUMERIC(5,2)  -- percentual de desconto (ex: 10 = 10%)
);