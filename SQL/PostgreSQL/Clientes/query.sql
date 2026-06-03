-- 5a) Clientes cujo nome começa com 'A'
SELECT nome, email
FROM cliente
WHERE nome LIKE 'A%';

-- 5b) Clientes com e-mail do Gmail
SELECT nome, email, telefone
FROM cliente
WHERE email LIKE '%@gmail.com'
ORDER BY nome;

-- 5c) Clientes cujo nome tem 'Ferreira' em qualquer posição
SELECT nome, email
FROM cliente
WHERE nome LIKE '%Ferreira%';

-- 5e) NOT LIKE – clientes sem e-mail Gmail ou Hotmail
SELECT nome, email
FROM cliente
WHERE email NOT LIKE '%@gmail.com'
  AND email NOT LIKE '%@hotmail.com';
