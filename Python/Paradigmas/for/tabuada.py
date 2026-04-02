valor = int(input("Digite um número para ver a tabuada: "))

print("*" * 18)
print(f"Tabuada do {valor}")
print("*" * 18)

for i in range(11):
    print(f"{i} x {valor} = {i * valor}")