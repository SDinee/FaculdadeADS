import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Exemplo Tkinter")
        
        self.label = tk.Label(self.root, text="Olá, Tkinter!")
        self.label.pack(padx=10)
        
        self.button = tk.Button(self.root, text="Clique aqui", command=self.clicado)
        self.button.pack(pady=10)
        
    def clicado(self):
        # Atualiza o texto do rótulo quando o botão é clicado
        self.label.config(text="Botão clicado!")
        
root = tk.Tk()
App(root)
root.mainloop()