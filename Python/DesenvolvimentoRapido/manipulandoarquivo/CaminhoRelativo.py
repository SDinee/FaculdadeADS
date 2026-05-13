import os

subdiretorio = "manipularquivo"
nome_arquivo = "exemplo_caminho_relativo.txt"

# caminho relativo
caminho_relativo = os.path.join(subdiretorio, nome_arquivo)

# converte para absoluto
caminho_absoluto = os.path.abspath(caminho_relativo)

print(f"Caminho relativo: {caminho_relativo}")
print(f"Caminho absoluto: {caminho_absoluto}")
