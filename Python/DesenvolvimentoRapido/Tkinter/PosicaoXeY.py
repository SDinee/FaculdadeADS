import tkinter as tk

class Janela:
    def __init__(self):
        self.janela = tk.Tk()
        self.frame = tk.Frame(self.janela, width=210, height=210)
        self.frame.pack()
        
        self.x, self.y = 0,0
        self.label_posicao = tk.Label(self.frame, text=f"Posição: ({self.x}, {self.y})", bg="red")
        self.label_posicao.place(x=self.x, y=self.y)
        
        self.x, self.y = 75,75
        self.label_posicao2 = tk.Label(self.frame, text=f"Posição: ({self.x}, {self.y})", bg="blue")
        self.label_posicao2.place(x=self.x, y=self.y)

        self.janela.mainloop()
        
if __name__ == "__main__":
    Janela = Janela()