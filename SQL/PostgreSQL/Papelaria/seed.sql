INSERT INTO fornecedor (nome) VALUES
  ('Tech Imports Ltda'),
  ('Distribuidora Sul'),
  ('Mega Suprimentos'),
  ('Norte Atacado'),
  ('Centro Comercial');
 
INSERT INTO item_pedido (fornecedor_id, descricao, quantidade, preco_unit, desconto_pct) VALUES
  (1, 'Teclado Mecânico',    20, 180.00, 5.00),
  (1, 'Mouse sem fio',       50,  75.50, 0.00),
  (2, 'Monitor 24"',          8, 950.00, 8.00),
  (2, 'Cabo HDMI 2m',        30,  25.00, 0.00),
  (3, 'Webcam HD',           15, 220.00, 10.00),
  (3, 'Headset USB',         25, 135.00, 5.00),
  (4, 'Papel A4 (resma)',   100,  22.80, 12.00),
  (4, 'Caneta esferográfica',200,  1.50, 0.00),
  (5, 'Cadeira Gamer',        5, 1200.00, 15.00),
  (5, 'Mesa para escritório', 3,  650.00, 7.00);