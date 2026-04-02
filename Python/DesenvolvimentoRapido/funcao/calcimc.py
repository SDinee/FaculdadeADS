def calcula_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 24.9:
        return "Peso normal"
    elif imc < 29.9:
        return "Sobrepeso"
    elif imc < 34.9:
        return "Obesidade grau 1"
    elif imc < 39.9:
        return "Obesidade grau 2"
    else:
        return "Obesidade grau 3"

while True:
    try:
        print("Calculadora de IMC")
        print("digite -1 para sair")
        peso = float(input("Digite o peso (kg): "))

        if peso == -1:
            print("Encerrando a calculadora de IMC. Até mais!")
            break

        altura = float(input("Digite a altura (m): "))

        if peso <= 0 or altura <= 0:
            print("Peso e altura devem ser positivos.")
            continue

        imc = calcula_imc(peso, altura)
        classificacao = classificar_imc(imc)

        print(f"Seu IMC é: {imc:.2f}")
        print(f"Classificação: {classificacao}")
        
    except ValueError:
        print("Entrada inválida. Por favor, digite números válidos.")