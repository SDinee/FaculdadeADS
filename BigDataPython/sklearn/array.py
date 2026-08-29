# 1. Importamos o modelo de regressão linear do scikit-learn
from sklearn.linear_model import LinearRegression
import numpy as np

# 2. Criamos os dados de entrada (x) e saída (y).
# x é um array 2D (cada valor dentro de colchetes),
# y é um array 1D com os valores correspondentes.
x = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 5, 4, 5])

# 3. Instanciamos o modelo de regressão linear.
modelo = LinearRegression()

# 4. Treinamos o modelo com os dados (x, y).
modelo.fit(x, y)

# 5. Fazemos uma previsão para x = 10.
print("Previsto:", modelo.predict([[10]]))
