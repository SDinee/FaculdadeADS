estoque = {}

def adicionar_produto():
    produto = input("Nome do produto: ").strip().title()
    quantidade = int(input("Quantidade inicial: "))
    estoque[produto] = quantidade
    print(f"Produto '{produto}' adicionado com quantidade {quantidade} unidades.")

def ver_estoque():
    print("Estoque atual:")
    if not estoque:
        print("O estoque está vazio.")
    else:
        for produto, quantidade in estoque.items():
            print(f"{produto}: {quantidade} unidades")

def atualizar_quantidade():
    produto = input("Nome do produto para atualizar: ").strip().title()
    if produto in estoque:
        nova_quantidade = int(input(f"Nova quantidade para '{produto}': "))
        estoque[produto] = nova_quantidade
        print(f"Quantidade de '{produto}' atualizada para {nova_quantidade} unidades.")
    else:
        print(f"Produto '{produto}' não encontrado no estoque.")

def verificar_disponibilidade():
    produto = input("Nome do produto para verificar disponibilidade: ").strip().title()
    if produto in estoque:
        if estoque[produto] > 0:
            print(f"Produto '{produto}' está disponível com {estoque[produto]} unidades.")
        else:
            print(f"Produto '{produto}' está esgotado.")
    else:
        print(f"Produto '{produto}' não encontrado no estoque.")

def menu():
    while True:
        print("\nMenu de opções:")
        print("1. Adicionar produto")
        print("2. Ver estoque")
        print("3. Atualizar quantidade")
        print("4. Verificar disponibilidade")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            adicionar_produto()
        elif escolha == '2':
            ver_estoque()
        elif escolha == '3':
            atualizar_quantidade()
        elif escolha == '4':
            verificar_disponibilidade()
        elif escolha == '5':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()