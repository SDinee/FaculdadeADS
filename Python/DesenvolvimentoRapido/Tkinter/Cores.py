import tkinter as tk

janela = tk.Tk()

frame1 = tk.Frame(master=janela, width=100, height=100, bg="red")
frame1.pack()

frame2 = tk.Frame(master=janela, width=100, height=100, bg="green")
frame2.pack()

frame3 = tk.Frame(master=janela, width=100, height=100, bg="blue")
frame3.pack()

janela.mainloop()