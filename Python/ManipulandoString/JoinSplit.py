texto = "Seja bem-vindo a aula de python."

print(' '.join(texto))
print(texto.split())
print(' '.join(texto.split()))

# join() concatena os elementos de um iterável utilizando a string
# informada como separador.

# split() divide a string em uma lista de substrings.
# Por padrão, a divisão ocorre em espaços em branco.