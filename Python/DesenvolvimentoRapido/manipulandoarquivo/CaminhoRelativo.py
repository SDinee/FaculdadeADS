import os

#Diretório base
diretorio_base = "C:\\Users\\kingg\\Desktop\\FaculdadeADS\\Python\\DesenvolvimentoRapido\\manipulandoarquivo" # Obtém o diretório onde este script está localizado

#subdiretório e nome do arquivo
subdiretorio = "manipularquivo"
nome_arquivo = "exemplo_caminho_relativo.txt"

#Constroi o caminho relativo
caminho_relativo = os.path.join(diretorio_base, subdiretorio, nome_arquivo)

caminho_absoluto = os.path.abspath(caminho_relativo) # Converte o caminho relativo para absoluto

#Escreve os resultados 
print(f"Caminho relativo: {caminho_relativo}")
print(f"Caminho absoluto: {caminho_absoluto}")