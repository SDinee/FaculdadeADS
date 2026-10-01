import pandas as pd

s = pd.Series([10,20,30,40,50])
print("Series: \n", s)

dados = {
    "Nome" : ["Ana", "Sidne", "João", "Carla"],
    "Idade" : [22, 21, 19, 40],
    "Nota" : [5.9, 8.3, 4.6, 7.0]
}

df = pd.DataFrame(dados)

print(f"\nDataFrame: \n {df}")
print(f" \nPrimeira linha do DataFrame: \n {df.head(1)}")