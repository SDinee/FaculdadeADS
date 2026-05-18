import tkinter as tk

janela = tk.Tk()

frame1 = tk.Frame(master=janela, width=100, height=100, bg="red")
frame1.pack(fill=tk.BOTH,side=tk.LEFT, expand=True)  
#O argumento fill=tk.BOTH faz com que o frame preencha tanto horizontal quanto verticalmente, e expand=True permite que ele se expanda para ocupar o espaço disponível.
#side=tk.LEFT alinha o frame à esquerda da janela, e os próximos frames serão alinhados à direita do frame anterior.

frame2 = tk.Frame(master=janela, width=100, height=100, bg="green")
frame2.pack(fill=tk.BOTH,side=tk.LEFT, expand=True)

frame3 = tk.Frame(master=janela, width=100, height=100, bg="blue")
frame3.pack(fill=tk.BOTH,side=tk.LEFT, expand=True)

janela.mainloop()