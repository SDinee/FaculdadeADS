INSERT INTO turma (codigo, curso) VALUES
  ('T001', 'Análise e Desenvolvimento de Sistemas'),
  ('T002', 'Ciência da Computação'),
  ('T003', 'Gestão da TI'),
  ('T004', 'Sistemas de Informação'),
  ('T005', 'Análise e Desenvolvimento de Sistemas');
 
INSERT INTO avaliacao (turma_id, aluno, disciplina, nota) VALUES
  (1, 'Alice',    'Banco de Dados', 8.5),
  (1, 'Bruno',    'Banco de Dados', 6.0),
  (1, 'Carla',    'Banco de Dados', 9.0),
  (2, 'Diego',    'Banco de Dados', 7.5),
  (2, 'Elaine',   'Banco de Dados', 5.0),
  (3, 'Fábio',    'Banco de Dados', 8.0),
  (3, 'Giovana',  'Banco de Dados', 9.5),
  (4, 'Henrique', 'Banco de Dados', 4.5),
  (4, 'Isabela',  'Banco de Dados', 7.0),
  (5, 'João',     'Banco de Dados', 6.5),
  (1, 'Alice',    'Redes',          7.0),
  (2, 'Diego',    'Redes',          8.0),
  (3, 'Fábio',    'Redes',          9.0),
  (4, 'Henrique', 'Redes',          6.0),
  (5, 'João',     'Redes',          5.5);