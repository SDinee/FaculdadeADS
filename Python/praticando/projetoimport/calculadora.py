print('=========================================')
print('---------Bem-vindo a calculadora---------')
print('=========================================')

print('\n---------OPÇÕES---------\n')

print('1 - Somar')
print('2 - Subtrair')
print('3 - Multiplicar')
print('4 - Dividir')
print('5 - Sair')

opcao = (input('Escolha uma opção: ')).strip()


if opcao == '1':
    n = int(input('quantos números deseja somar? '))

#Array para armazenar os números a serem somados
    numeros = []

    for i in range(n):
        valores = float(input(f'Informe o {i+1}º número: '))

#Adicionando os valores à lista de números
        numeros.append(valores)

#Função sum() para somar os números da lista
    resultado = sum(numeros)
    print(f'O resultado da soma de {numeros} é: {resultado}')
