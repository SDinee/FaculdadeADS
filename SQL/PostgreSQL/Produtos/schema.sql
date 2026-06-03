CREATE TABLE categoria (
  id        SERIAL PRIMARY KEY,
  nome      VARCHAR(50) NOT NULL,
  ativa     BOOLEAN DEFAULT TRUE
);
 
CREATE TABLE produto (
  id           SERIAL PRIMARY KEY,
  nome         VARCHAR(80) NOT NULL,
  preco        NUMERIC(10,2),
  estoque      INT,
  categoria_id INT REFERENCES categoria(id)
);