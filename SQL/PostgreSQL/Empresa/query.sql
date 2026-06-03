select * from departamento

-- Ordenar funcionários por nome (crescente)

SELECT nome, salario
FROM funcionario
ORDER BY nome ASC;
 
-- Ordenar por salário do maior para o menor

SELECT nome, salario, data_admissao
FROM funcionario
ORDER BY salario DESC;
 
-- Ordenar por departamento e depois por nome dentro de cada depto

SELECT f.nome AS funcionario,
       d.nome AS departamento,
       f.salario
FROM funcionario f
JOIN departamento d ON d.id = f.depto_id
ORDER BY d.nome ASC, f.nome ASC;
 
-- Os 3 funcionários mais recentes (ORDER BY + LIMIT)

SELECT nome, data_admissao
FROM funcionario
ORDER BY data_admissao DESC
LIMIT 3;