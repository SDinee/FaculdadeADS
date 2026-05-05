pacientes = {}

def adicionar_paciente():
    nome = input("Nome do paciente: ").strip().title()
    if nome in pacientes:
        print(f"Paciente {nome} já cadastrado.")
        return
    try:
        peso = float(input("Peso (kg): "))
        altura = float(input("Altura (m): "))
        if peso <= 0 or altura <= 0:
            print("Peso e altura devem ser maior que zero.")
            return
        
        pacientes[nome] = {
            "peso": peso,
            "altura": altura
        }
        
        print(f"Paciente {nome} cadastrado com sucesso.")
    except ValueError:
        print("Erro: Digite valores numéricos válidos para peso e altura.")

def ver_pacientes():
    print("\n==== LISTA DE PACIENTES ====")
    if not pacientes:
        print("Nenhum paciente cadastrado.")
    else:
        for nome, dados in pacientes.items():
            imc = dados["peso"] / (dados["altura"] ** 2)
            print(f"{nome}: Peso = {dados['peso']} kg, Altura = {dados['altura']} m, IMC = {imc:.2f}")

def atualizar_dados():
    nome = input("Nome do paciente para atualizar: ").strip().title()
    if nome not in pacientes:
        print(f"Paciente {nome} não encontrado.")
        return
    try:
        novo_peso = float(input("Novo peso (kg): "))
        nova_altura = float(input("Nova altura (m): "))
        
        pacientes[nome]["peso"] = novo_peso
        pacientes[nome]["altura"] = nova_altura
        
        print(f"Dados do paciente {nome} atualizados com sucesso.")
    except ValueError:
        print("Erro: Digite valores numéricos válidos para peso e altura.")

def calcular_imc():
    nome = input("Nome do paciente para calcular IMC: ").strip().title()
    if nome not in pacientes:
        print(f"Paciente {nome} não encontrado.")
        return
    
    peso = pacientes[nome]["peso"]
    altura = pacientes[nome]["altura"]
    imc = peso / (altura ** 2)
    
    print(f"\nIMC do paciente {nome}")
    print(f"Peso: {peso} kg, Altura: {altura} m, IMC: {imc:.2f}")

    if imc < 18.5:
        print("Classificação: Abaixo do peso")
    elif imc < 25:
        print("Classificação: Peso normal")
    elif imc < 30:
        print("Classificação: Sobrepeso")
    else:
        print("Classificação: Obesidade")

def menu():
    while True:
        print("\n==== Menu de opções ====")
        print("1. Adicionar paciente")
        print("2. Ver pacientes")
        print("3. Atualizar dados")
        print("4. Calcular IMC")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            adicionar_paciente()
        elif opcao == "2":
            ver_pacientes()
        elif opcao == "3":
            atualizar_dados()
        elif opcao == "4":
            calcular_imc()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()