
#primeira questão
SELECT u.nome, u.email, l.titulo, a.nome, emp.data_emprestimo, emp.data_devolucao
FROM `emprestimo` emp

LEFT JOIN usuario u ON
emp.ID_usuario = u.ID
LEFT join livro l ON
emp.ID_livro = l.ID
LEFT join autor a ON
l.ID_autor = a.ID
WHERE data_emprestimo BETWEEN '2024-06-05' and '2024-07-30'
AND u.nome LIKE '%a%'

#segunda questão
SELECT COUNT(*) AS quantidade_usuario FROM `usuario` 

#terceira questão
SELECT COUNT(*) as quantidade_de_emprestimos FROM `emprestimo` WHERE data_emprestimo BETWEEN '2024-06-01'AND '2024-06-30'

#quarta questão
SELECT u.nome, COUNT(emp.id) as quantidade_de_emprestimos
FROM emprestimo emp
LEFT JOIN usuario u ON
emp.ID_usuario = u.ID
GROUP BY u.ID
