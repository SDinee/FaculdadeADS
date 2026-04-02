def menu():
    print("----Calculadora Simples----")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")

def somar(v1, v2):
    return v1 + v2

def subtrair(v1, v2):
    return v1 - v2

def multiplicar(v1, v2):
    return v1 * v2

def dividir(v1, v2):
        return v1 / v2
 
v1 = float(input("Digite o primeiro valor: "))
v2 = float(input("Digite o segundo valor: "))

menu()

opcao = eval(input("Escolha uma opção: "))

if opcao == 1:
     res = somar(v1, v2)
    
elif opcao == 2:
    res = subtrair(v1, v2)

elif opcao == 3:
    res = multiplicar(v1, v2)

elif opcao == 4:
    res = dividir(v1, v2)

else:
    print("Opção inválida")
    exit(0)

print(f"O resultado é: {res}")