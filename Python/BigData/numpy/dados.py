import numpy as np

dados = np.random.randint(0, 51, 100)

contagem = np.bincount(dados)
moda = np.argmax(contagem)
print("Moda: ", moda)
print("Contagem: ", contagem)