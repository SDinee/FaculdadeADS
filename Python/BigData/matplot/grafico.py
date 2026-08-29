# 1. Importamos o módulo pyplot da biblioteca matplotlib, usado para criar gráficos
import matplotlib.pyplot as plt

# 2. Definimos os dados: anos (eixo x) e vendas (eixo y)
anos = [2015, 2016, 2017, 2018, 2019]
vendas = [1000, 1500, 900, 4000, 2500]

# 3. Criamos o gráfico de linha com os dados
# marker='o' coloca bolinhas nos pontos, color="blue" deixa a linha azul
plt.plot(anos, vendas, marker='o', color="blue")

# 4. Personalizamos o gráfico com título e rótulos dos eixos
plt.title("Vendas Anuais")           # título do gráfico
plt.xlabel("Ano")                    # rótulo do eixo x
plt.ylabel("Vendas (em unidades)")   # rótulo do eixo y

# 5. Adicionamos uma grade para facilitar a leitura
plt.grid(True)

# 6. Exibimos o gráfico na tela
plt.show()
