print ('1 - Calculadora')
print ('2 - criar uma lista')


opcao = (input('Escolha uma opção: ')).strip()


#importando o arquivo calculadora.py  (não precisa de .py)
if opcao == '1':
    import calculadora

elif opcao == '2':
    import lista

else:
    print ('Opção inválida')
    