from tkinter import Tk
import os

janela = Tk()
janela.title("Nos Love Python")

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
icone_filename = "icon.ico"
caminho_icone = os.path.join(diretorio_atual, icone_filename)
janela.iconbitmap(caminho_icone)

janela.geometry("600x250")
janela.eval('tk::PlaceWindow . center')
janela.mainloop()