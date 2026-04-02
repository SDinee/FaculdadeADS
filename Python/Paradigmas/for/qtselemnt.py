n = int(input("Digite a quantidade de elementos: "))

lista = [0]*n

for i in range(n):
    lista[i] = int(input(f"Digite o elemento {i + 1}: "))

print(lista)
print(sorted(lista)) ##sorted() é uma função que retorna uma nova lista ordenada, sem modificar a lista original.  
print(len(lista)) ##len() é uma função que retorna o número de elementos em um objeto.
print(sum(lista)) ##sum() é uma função que retorna a soma de todos os elementos em um objeto.
print(max(lista)) ##max() é uma função que retorna o maior elemento de um objeto.
print(min(lista)) ##min() é uma função que retorna o menor elemento de um objeto.  
