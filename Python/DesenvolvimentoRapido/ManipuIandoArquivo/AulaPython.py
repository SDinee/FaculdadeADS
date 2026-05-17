import os

caminho_arquivo = ''

with open(caminho_arquivo, 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

caminho_saida = ''

with open(caminho_saida, 'w')as arquivo:
    arquivo.write("Nossa Aula!")

with open(caminho_saida, 'a') as arquivo:
    arquivo.write("\nde Python, explorando manipulação de arquivos.")