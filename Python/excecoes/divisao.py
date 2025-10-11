try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    if num2 == 0:
        print("Erro: não é possivel dividir por zero.")
    else:
        resultado = num1 / num2
        print(f"O resultado da divisão de {num1} por {num2} é {resultado:.2f}")
        
except ValueError:
    print("Erro: insire apenas valores numéricos válidos.")