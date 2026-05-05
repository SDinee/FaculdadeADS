contribuintes = {}

def adicionar_contribuinte():
    nome = input("Nome do contribuinte: ").strip().title()
    cpf = input("CPF(somente números): ").strip()
    renda = float(input("Renda mensal (R$): "))

    contribuintes[cpf] = {
        "nome": nome,
        "renda": renda
    }

    print(f"Contribuinte {nome} adicionado com sucesso.")

def calcular_imposto(renda):
    if renda <= 2112:
        return 0
    elif renda <= 2826.65:
        return renda * 0.075 - 158.40
    elif renda <= 3751.05:
        return renda * 0.15 - 370.40
    elif renda <= 4664.68:
        return renda * 0.225 - 651.73  
    else:
        return renda * 0.275 - 884.96
    
def ver_contribuintes():
    print("\n==== LISTA DE CONTRIBUINTES ====")
    if not contribuintes:
        print("Nenhum contribuinte cadastrado.")
    else:
        for cpf, dados in contribuintes.items():
            print(f"{dados['nome']} (CPF: {cpf}): Renda = R$ {dados['renda']:.2f}")

def calcular_imposto_contribuinte():
    cpf = input("CPF do contribuinte para calcular imposto: ").strip()
    if cpf in contribuintes:
        renda = contribuintes[cpf]["renda"]
        nome = contribuintes[cpf]["nome"]
        imposto = calcular_imposto(renda)
        print(f"\nImposto de Renda para {nome} (CPF: {cpf})")
        print(f"Renda: R$ {renda:.2f}, Imposto a pagar: R$ {imposto:.2f}")
    else:
        print(f"Contribuinte com CPF {cpf} não encontrado.")

def menu():
    while True:
        print("\n==== Menu de opções ====")
        print("1. Adicionar contribuinte")
        print("2. Ver contribuintes")
        print("3. Calcular imposto de um contribuinte")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            adicionar_contribuinte()
        elif escolha == '2':
            ver_contribuintes()
        elif escolha == '3':
            calcular_imposto_contribuinte()
        elif escolha == '4':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()