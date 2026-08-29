# Primeiro importamos a biblioteca pandas, que é usada para manipulação de dados em tabelas (DataFrames).
import pandas as pd

# Criamos um dicionário chamado 'dados' com três listas:
# - "Nome": lista de nomes
# - "Idade": lista de idades
# - "Cidade": lista de cidades
dados = {
    "Nome": ["João", "Maria", "Pedro", "Ana"],
    "Idade": [25, 30, 22, 28],
    "Cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba"]
}

# Transformamos o dicionário em um DataFrame (estrutura de tabela do pandas).
df = pd.DataFrame(dados)

# Exibimos o DataFrame completo para visualizar todos os dados.
print(df)

print("\n")  # Adiciona uma linha em branco para melhor visualização

# Agora aplicamos um filtro: queremos apenas as linhas em que a idade seja maior que 25.
# O resultado é um novo DataFrame com apenas essas linhas.
print(df[df["Idade"] > 25])
