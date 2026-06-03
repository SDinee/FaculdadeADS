CREATE TABLE turma (
  id     SERIAL PRIMARY KEY,
  codigo VARCHAR(10) NOT NULL,
  curso  VARCHAR(50)
);
 
CREATE TABLE avaliacao (
  id        SERIAL PRIMARY KEY,
  turma_id  INT REFERENCES turma(id),
  aluno     VARCHAR(80),
  disciplina VARCHAR(50),
  nota      NUMERIC(4,1)
);