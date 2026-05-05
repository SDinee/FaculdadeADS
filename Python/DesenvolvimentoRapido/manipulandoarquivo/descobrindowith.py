caminho_arquivo = 'C:/Users/kingg/Desktop/FaculdadeADS/Python/DesenvolvimentoRapido/manipulandotexto/escritaleitura.txt'

with open (caminho_arquivo, 'w') as arquivo: # o with é um gerenciador de contexto, ele garante que o arquivo seja fechado automaticamente após o bloco de código ser executado.
    arquivo.write('Nome: Dumbo\n')
    arquivo.write('Idade: 18\n')

    linhas = ['primeira. \n', 'segunda. \n']
    arquivo.writelines(linhas)