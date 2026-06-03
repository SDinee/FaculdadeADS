select * from turma

-- Quantidade de avaliações e média por turma

SELECT t.codigo,
       t.curso,
       COUNT(a.id)   AS total_avaliacoes,
       AVG(a.nota)   AS media_geral,
       MAX(a.nota)   AS maior_nota,
       MIN(a.nota)   AS menor_nota
FROM avaliacao a
JOIN turma t ON t.id = a.turma_id
GROUP BY t.id, t.codigo, t.curso
ORDER BY media_geral DESC;
 
-- Média por disciplina

SELECT disciplina,
       COUNT(*)      AS qtd_alunos,
       ROUND(AVG(nota), 2) AS media
FROM avaliacao
GROUP BY disciplina;
 
-- Somente turmas com média >= 7 (HAVING)

SELECT t.codigo,
       ROUND(AVG(a.nota), 2) AS media
FROM avaliacao a
JOIN turma t ON t.id = a.turma_id
GROUP BY t.codigo
HAVING AVG(a.nota) >= 7
ORDER BY media DESC;