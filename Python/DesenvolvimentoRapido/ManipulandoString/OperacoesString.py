texto = "Nossa aula Manipulando String."

print(len(texto))
print(texto.count("a"))
print(texto.count("a", 5, 29))
# len() retorna a quantidade total de caracteres da string,
# incluindo espaços e caracteres especiais.

# count() retorna quantas vezes um caractere ou substring aparece na string.
# Também é possível definir um intervalo de busca usando índice inicial e final.

texto2 = "Nossa aula manipulando string."

print(texto2.find("manipulando"))
print(texto2.find("python"))
print("Nossa" in texto2)

# find() retorna o índice da substring encontrada.
# Caso não encontre, retorna -1.