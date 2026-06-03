INSERT INTO cidade (nome, estado) VALUES
  ('Rio de Janeiro', 'RJ'),
  ('São Paulo',      'SP'),
  ('Belo Horizonte', 'MG'),
  ('Salvador',       'BA'),
  ('Recife',         'PE');

INSERT INTO cliente (nome, email, telefone, cidade_id, ativo) VALUES
  ('Amanda Souza',       'amanda@gmail.com',    '(21)99001-1111', 1, TRUE),
  ('André Costa',        'andre@hotmail.com',   '(21)99002-2222', 1, TRUE),
  ('Beatriz Lemos',      'beatriz@gmail.com',   '(11)98003-3333', 2, TRUE),
  ('Carlos Andrade',     'carlos@empresa.com',  '(31)97004-4444', 3, FALSE),
  ('Daniela Ferreira',   'daniela@gmail.com',   '(71)96005-5555', 4, TRUE),
  ('Eduardo Mendes',     'edu@yahoo.com',       '(81)95006-6666', 5, TRUE),
  ('Fernanda Alves',     'fernanda@gmail.com',  '(21)94007-7777', 1, TRUE),
  ('Gustavo Barbosa',    'gustavo@hotmail.com', '(11)93008-8888', 2, FALSE),
  ('Helena Rodrigues',   'helena@empresa.com',  '(31)92009-9999', 3, TRUE),
  ('Igor Santana',       'igor@gmail.com',      '(71)91010-0000', 4, TRUE);
