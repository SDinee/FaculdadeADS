CREATE TABLE cidade (
  id     SERIAL PRIMARY KEY,
  nome   VARCHAR(60) NOT NULL,
  estado CHAR(2)
);

CREATE TABLE cliente (
  id         SERIAL PRIMARY KEY,
  nome       VARCHAR(80) NOT NULL,
  email      VARCHAR(100),
  telefone   VARCHAR(20),
  cidade_id  INT REFERENCES cidade(id),
  ativo      BOOLEAN DEFAULT TRUE
);