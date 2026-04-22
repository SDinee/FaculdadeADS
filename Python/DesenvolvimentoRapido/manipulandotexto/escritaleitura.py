caminho_arquivo = 'C:/Users/kingg/Desktop/FaculdadeADS/Python/DesenvolvimentoRapido/manipulandotexto/escritaleitura.txt'

arquivo = open (caminho_arquivo, 'w')
arquivo.write('Nome: Luiza\n')
arquivo.writelines(['Idade: 25\n', 'Cidade: São Paulo\n', 'Profissão: Desenvolvedora\n'])
arquivo.close()

arquivo = open (caminho_arquivo, 'r')
conteudo = arquivo.readlines()
for i, linha in enumerate(conteudo, start = 1):
    print(f'linha {i}: {linha}')