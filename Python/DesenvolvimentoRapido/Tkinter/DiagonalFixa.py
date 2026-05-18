import tkinter as tk

class GradeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Exemplo Grid")
        self.root.columnconfigure(0, minsize=250)
        self.root.rowconfigure([0,1], minsize=100)
        
        # Rótulo A: Norte (n) + Leste (e) = Canto superior direito
        self.label = tk.Label(self.root, text="A", bg="red", fg="white")
        self.label.grid(row=0, column=0, sticky="ne")
        
        # Rótulo B: Sul (s) + Oeste (w) = Canto inferior esquerdo
        self.label2 = tk.Label(self.root, text="B", bg="blue", fg="white")
        self.label2.grid(row=1, column=0, sticky="sw")
        
root = tk.Tk()
GradeApp(root)
root.mainloop()