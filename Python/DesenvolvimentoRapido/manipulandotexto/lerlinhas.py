def linhas(camonho_arquivo: str, modo: str) -> list:
    arquivo = open(caminho_arquivo, modo)
    linhas = arquivo.readlines()
    arquivo.close()
    return linhas

if __name__ == "__main__":
    caminho_arquivo = 'C:/Users/kingg/Desktop/FaculdadeADS/Python/DesenvolvimentoRapido/manipulandotexto/escritaleitura.txt'
    tipo = 'r'
    linhas_arquivo = linhas(caminho_arquivo, tipo)
    for i, linha in enumerate(linhas_arquivo, start = 1): # enumerate para obter o número da linha
        print(f'linha {i}: {linha}')

