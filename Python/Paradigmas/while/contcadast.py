continua = "s"
idade = []

while (continua == "s" or continua == "S"):
    id = int(input("Digite a idade: "))
    idade.append(id)
    continua = input("Deseja continuar? (s/n): ")

soma_idade = sum(idade)
n = len(idade)
media_idade = soma_idade / n

print(f"Esta turma tem {n} alunos.")
print(f"A média de idade é {media_idade:.2f} anos.")