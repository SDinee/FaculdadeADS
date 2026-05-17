arquivo = open ('C:/Users/kingg/Desktop/FaculdadeADS/Python/DesenvolvimentoRapido/manipulandotexto/escritaleitura.txt', 'w')

arquivo.write('Escrevendo no arquivo usando write')
arquivo.close()


arquivo = open ('C:/Users/kingg/Desktop/FaculdadeADS/Python/DesenvolvimentoRapido/manipulandotexto/simplesopen.txt')

print(arquivo.readline())
arquivo.close()