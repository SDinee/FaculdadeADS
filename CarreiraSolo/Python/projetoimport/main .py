import calculadora
import lista
# Importa os módulos completos para evitar conflitos de nomes
# e mantém o código mais organizado.

while True:
    print('========================')
    print('---------Opções---------')
    print('========================')

    print ('1 - Calculadora')
    print ('2 - criar uma lista')


    opcao = input('Escolha uma opção: ').strip()


    
    if opcao == '1':
        calculadora.menu()

    elif opcao == '2':
        lista.menu()

    else:
        print ('Opção inválida')
    