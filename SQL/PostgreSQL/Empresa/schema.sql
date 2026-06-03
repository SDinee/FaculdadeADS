CREATE TABLE departamento (
  id   SERIAL PRIMARY KEY,
  nome VARCHAR(50) NOT NULL
);
 
CREATE TABLE funcionario (
  id             SERIAL PRIMARY KEY,
  nome           VARCHAR(80) NOT NULL,
  salario        NUMERIC(10,2),
  data_admissao  DATE,
  depto_id       INT REFERENCES departamento(id)
);
 