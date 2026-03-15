base = int(input("Digite o valor da base: "))
expoente = int(input("Digite o valor do expoente: "))

pot = base ** expoente

if (pot % 2 == 0):
    print(f"O resultado é {pot}, trata-se de um número par.")
else:
    print(f"O resultado é {pot}, trata-se de um número ímpar.")