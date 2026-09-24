import numpy as np

matriz = np.arange(1, 17).reshape(4,4)
print(matriz)
print("\n", matriz.sum())
print("\n", matriz.mean())
print("\n", matriz[:,0])
print("\n", matriz[-1, -1])