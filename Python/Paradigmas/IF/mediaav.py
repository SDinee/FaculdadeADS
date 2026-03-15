nome = input("Qual é o nome do aluno? ")
av1 = float(input("Qual foi a nota da AV1? "))
av2 = float(input("Qual foi a nota da AV2? "))

media = (av1 + av2) / 2

if media >= 6:
    print(f"Parabéns {nome}! Você foi aprovado com média {media:.2f}.")
elif (media >= 4):
    print(f"{nome}, você está de recuperação com média {media:.2f}.")
else:
    print(f"Infelizmente {nome}, você foi reprovado com média {media:.2f}.")