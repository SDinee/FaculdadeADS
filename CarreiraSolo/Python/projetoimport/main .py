import calculadora
import lista

while True:
    print ('1 - Calculadora')
    print ('2 - criar uma lista')


    opcao = input('Escolha uma opção: ').strip()


    #importando o arquivo calculadora.py  (não precisa de .py)
    if opcao == '1':
        calculadora.executar()

    elif opcao == '2':
        lista.executar()

    else:
        print ('Opção inválida')
    