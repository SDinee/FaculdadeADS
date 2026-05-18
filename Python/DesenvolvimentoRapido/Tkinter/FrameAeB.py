import tkinter as tk

janela = tk.Tk()  

frame_a = tk.Frame()
frame_b = tk.Frame()
# O método Frame() é usado para criar um contêiner dentro da janela, que pode ser usado para organizar outros widgets (como rótulos, botões, etc.) de forma mais estruturada.

# Labels são widgets usados para exibir texto ou imagens na interface gráfica. Eles são úteis para fornecer informações ou instruções ao usuário.
label_a = tk.Label(master=frame_a, text="Frame A")
label_a.pack()

label_b = tk.Label(master=frame_b, text="Frame B")
label_b.pack()

frame_a.pack()
frame_b.pack()

janela.mainloop()