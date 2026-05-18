import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        self.texto_padrao = "Digite algo..."
        
        self.entrada = tk.Entry(root, fg="gray", width=30)
        self.entrada.insert(0, self.texto_padrao)
        self.entrada.pack(pady=20)
        
        self.entrada.bind("<FocusIn>", self.limpar)
        self.entrada.bind("<FocusOut>", self.restaurar)
        
    def limpar(self, event):
        if self.entrada.get() == self.texto_padrao:
            self.entrada.delete(0, tk.END)
            self.entrada.config(fg="black")

    def restaurar(self, event):
        if not self.entrada.get():
            self.entrada.insert(0, self.texto_padrao)
            self.entrada.config(fg="gray")
            
    #get() é um método usado para obter o texto atual do widget de entrada (Entry). Ele retorna o conteúdo do campo de entrada como uma string. 
    #No exemplo, é usado para verificar se o texto atual é igual ao texto padrão e para atualizar o rótulo com o texto digitado pelo usuário.
    
root = tk.Tk()
app = App(root)
root.mainloop()