def escrever(caminho_arquivo: str, modo: str, texto: list, texto2: list) -> None:
    with open (caminho_arquivo, modo) as arquivo:
        arquivo.write(texto[0])
        arquivo.write(texto[1])
        linhas = texto2
        arquivo.writelines(linhas)

if __name__ == "__main__":
    caminho_arquivo = 'C:/Users/kingg/Desktop/FaculdadeADS/Python/DesenvolvimentoRapido/manipulandotexto/escritaleitura.txt'
    lista_texto = ['write com with 1\n', 'write com with 2\n']
    lista_texto2 = ['hellow world\n', 'python é vida\n']
    escrever(caminho_arquivo, 'w', lista_texto, lista_texto2)