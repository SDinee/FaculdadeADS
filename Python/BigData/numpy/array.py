# Primeiro importamos a biblioteca NumPy, que é muito usada para cálculos numéricos e matrizes.
import numpy as np

# Criamos um array simples (vetor) com os números de 1 a 5.
arr = np.array([1, 2, 3, 4, 5])

# np.sum(arr) calcula a soma de todos os elementos do array.
print("Soma:", np.sum(arr))

# np.mean(arr) calcula a média aritmética dos elementos.
print("Média:", np.mean(arr))

# np.std(arr) calcula o desvio padrão, que mede a dispersão dos valores em relação à média.
print("Desvio padrão:", np.std(arr))

# Agora criamos uma matriz 2x2.
matriz = np.array([[1, 2], [3, 4]])

# np.linalg.det(matriz) calcula o determinante da matriz.
# O determinante é um valor importante em álgebra linear, usado em sistemas lineares e transformações.
print("determinante da matriz:", np.linalg.det(matriz))
