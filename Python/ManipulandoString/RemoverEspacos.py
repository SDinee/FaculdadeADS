nome = str(input("Digite o seu nome: "))

# Exibe o nome exatamente como foi digitado (incluindo espaços antes e depois)
print(f"Olá {nome}! ")

# lstrip() remove os espaços em branco do lado esquerdo (início da string)
print(f"Olá, {nome.lstrip()}!")

# rstrip() remove os espaços em branco do lado direito (final da string)
print(f"Olá, {nome.rstrip()}!")