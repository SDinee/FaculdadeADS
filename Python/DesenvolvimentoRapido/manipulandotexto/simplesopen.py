arquivo = open ('C:/Users/kingg/Desktop/FaculdadeADS/Python/DesenvolvimentoRapido/manipulandotexto/simplesopen.txt')

print('nome do arquivo:', arquivo.name)
print('tamanho em bytes:', arquivo.tell)
print('modo do arquivo:', arquivo.mode)
print('arquivo fechado?', arquivo.closed)

arquivo.close() 

print('arquivo fechado?', arquivo.closed)   