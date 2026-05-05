def write(caminho: str, modo: tuple) -> None: # tuple para receber mais de um tipo de dado, lista imutável, ideal para dados fixos 
    arquivo = open(caminho, modo)
    arquivo.write('escrevendo no arquivo usando write')
    arquivo.writelines(['\nEscrevendo no arquivo usando writelines', '\nOutra linha usando writelines'])
    arquivo.close()

def read(caminho_arquivo: str, modo: str) -> list:
    arquivo = open(caminho_arquivo, modo)
    linhas = arquivo.readlines()
    arquivo.close()
    return linhas

if __name__ == "__main__":
    caminho_arquivo = 'C:/Users/kingg/Desktop/FaculdadeADS/Python/DesenvolvimentoRapido/manipulandotexto/escritaleitura.txt'
    modo = 'r', 'w'

    write(caminho_arquivo, modo[1])
    leitura = read(caminho_arquivo, modo[0])
    for i, linha in enumerate(leitura, start = 1):
        print(f'linha {i}: {linha}')