usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

if usuario == "admin":
    if senha == "1234":
        print("Login bem-sucedido!")
    else:
        print("Senha incorreta.")
else:
    print("Usuário não encontrado.")