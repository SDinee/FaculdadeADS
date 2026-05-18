import tkinter as tk    

janela = tk.Tk()
entry = tk.Entry(janela)
entry.pack()        

label = tk.Label(janela, text="Digite algo e pressione Enter")
entry.insert(0, "Digite aqui...")  # Texto inicial no campo de entrada
label.pack()

def atualizar_label(event):
    texto = entry.get()  # Obtém o texto digitado no campo de entrada
    label.config(text=texto)  # Atualiza o texto do rótulo com o valor do campo de entrada

entry.bind('<Return>', atualizar_label)
# O método bind() é usado para associar um evento (neste caso, a tecla Enter) a uma função (atualizar_label)

janela.mainloop()