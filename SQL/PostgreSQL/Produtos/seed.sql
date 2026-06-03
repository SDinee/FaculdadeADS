INSERT INTO categoria (nome, ativa) VALUES
  ('Eletrônicos', TRUE),
  ('Livros',      TRUE),
  ('Vestuário',   FALSE),
  ('Alimentos',   TRUE),
  ('Brinquedos',  TRUE);
 
INSERT INTO produto (nome, preco, estoque, categoria_id) VALUES
  ('Notebook',          3500.00, 10, 1),
  ('Fone de ouvido',     150.00, 45, 1),
  ('Dom Casmurro',        35.00, 80, 2),
  ('Camiseta Polo',       89.90, 30, 3),
  ('Arroz 5kg',           22.50, 200, 4),
  ('Lego City',          250.00, 15, 5),
  ('Smartphone',        2200.00,  8, 1),
  ('Clean Code (livro)',  95.00, 22, 2),
  ('Calça Jeans',        179.90, 18, 3),
  ('Boneca Barbie',       99.00, 40, 5);