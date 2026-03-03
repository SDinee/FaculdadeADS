print ('1 - Calculadora')

opcao = (input('Escolha uma opção: '))


#importando o arquivo calculadora.py  (não precisa de .py)
if opcao == '1':
    __import__('calculadora')
