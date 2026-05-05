caminho_arquivo = 'C:/Users/kingg/Desktop/FaculdadeADS/Python/DesenvolvimentoRapido/manipulandotexto/escritaleitura.txt'

arquivo = open (caminho_arquivo, 'r')

linha1 = arquivo.readline()
print(f'linha 1: {linha1}')

linha2 = arquivo.readline()
print(f'linha 2: {linha2}')

arquivo.close()