texto = "Nossa aula manipulando String."

novo = texto.replace("manipulando", "operando com")
print(novo)

# replace() substitui uma substring por outra.
# Retorna uma nova string com a alteração.

print(texto.startswith("Nossa"))
print(texto.startswith("aula"))

# startswith() verifica se a string começa com a substring informada.
# Retorna True ou False.

print(texto.endswith("String"))
print(texto.endswith("."))

# endswith() verifica se a string termina com a substring informada.
# Retorna True ou False.