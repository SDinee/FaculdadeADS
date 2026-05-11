CREATE TABLE livros(
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    autor VARCHAR(255) NOT NULL,
    categoria VARCHAR(255) NOT NULL,
    ano_publicado INT NOT NULL
);

CREATE TABLE emprestimos(
    id SERIAL PRIMARY KEY,
    nome_leitor VARCHAR(255) NOT NULL,
    data_emprestimo DATE NOT NULL,
    data_devolucao DATE NOT NULL,
    livro_id INT NOT NULL,
  	FOREIGN KEY (livro_id)  REFERENCES livros(id) 
);