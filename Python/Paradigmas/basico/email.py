nome = input("Digite seu nome: ")
curso = input("Digite seu curso: ")

print(f"\nOlá {nome}, seja bem-vindo ao curso de {curso}!")
print("\n")
print("*" * 20)
print("Informações do aluno:")
print("*" * 20)

email = input("Digite seu email: ")
tel = input("Digite seu telefone: ")
idade = input("Digite sua idade: ")
renda = input("Digite sua renda mensal: ")

print("\n")
print("***Relatorio de dados***\n")

print(f"Nome: {nome}")
print(f"Curso: {curso}")
print(f"Email: {email}")
print(f"Telefone: {tel}")
print(f"Idade: {idade}")
print(f"Renda: {renda:.2f}")