import numpy as np

lista_notas = np.array([9.1, 3.0, 5.7, 9.2])

print("Máximo: ", lista_notas.max())
print("Mínimo: ", lista_notas.min())
print("Média: ", lista_notas.mean())
print("Posição da menor nota: ", lista_notas.argmin())