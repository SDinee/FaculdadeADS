n = int(input("Digite a quantidade de elementos: "))

lista = [0]*n

for i in range(n):
    lista[i] = int(input(f"Digite o elemento {i + 1}: "))

pares = 0
impares = 0

for num in lista:
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Lista de números: {lista}")
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")