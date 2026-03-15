nome = input("Qual é o nome do individuo: ")
idade = int(input("Qual é a idade do individuo: "))
peso = float(input("Qual é o peso do individuo (em kg): "))
altura = float(input("Qual é a altura do individuo (em metros): "))

imc = peso / (altura ** 2)

print(f"O IMC (índice de massa corporal) de {nome}, que tem {idade} anos, é de {imc:.2f}") 