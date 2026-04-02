quant = int(input("Digite a quantidade de números a serem somados: "))

soma = 0

for i in range(1, quant + 1):
    num = int(input(f"Digite o número {i}: "))
    soma = soma + num
    
print(f"A soma dos {quant} números é: {soma}")