import tkinter as tk

# Cria a janela principal da aplicação
janela = tk.Tk()

# Cria um botão dentro da janela
# text = texto exibido no botão
# command = ação executada quando o botão é clicado
# lambda cria uma função anônima simples (sem nome) para executar o print
botao = tk.Button(
    janela,
    text="Clique aqui!",
    command=lambda: print("Botão clicado!")
)

# O método pack() é um gerenciador de geometria do Tkinter
# Ele organiza o widget (botão) automaticamente dentro da janela
# Neste caso, posiciona o botão ocupando o espaço necessário
botao.pack()

# Inicia o loop principal da interface gráfica
# Mantém a janela aberta e escutando eventos (cliques, ações do usuário, etc.)
janela.mainloop()