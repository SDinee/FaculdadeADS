INSERT INTO livros(titulo,autor,categoria,ano_publicado)
VALUES
('Dom casmurro','Machado de Assis','Romance',1899),
('O Hobbit','J.R.R Tolkien','Fantasia',1937),
('Clean Code','Robert Martin','Tecnologia',2008),
('A Revolução dos Bichos','George Orwell','Ficção',1945),
('Python para Data Science','João Ribeiro','Tecnologia',2021);

INSERT INTO emprestimos(nome_leitor,data_emprestimo,data_devolucao,livro_id)
VALUES
('Ana Souza','2026-05-01','2026-05-10',1),
('Carlos Lima','2026-05-03','2026-05-12',2),
('Mariana Alves','2026-05-04','2026-05-15',3),
('Fernanda Costa','2026-05-05','2026-05-14',4),
('Ricardo Mendes','2026-05-06','2026-05-16',5);