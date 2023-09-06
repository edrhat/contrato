from tkcalendar import DateEntry
from tkinter import *
import os
from tkinter import messagebox

class Tela():

     def __init__(self, event):

        
        #IMAGEM DO CABEÇALHO
        cab = PhotoImage(file="cab.png")
        img = Label(janela, image=cab)
        img.config(bg="black")
        img.cab = cab
        img.place(x=0,y=0)

        
        #IMAGEM DO RODAPÉ
        cab2 = PhotoImage(file="cab.png")
        img2 = Label(janela, image=cab2)
        img2.config(bg="black")
        img2.cab2 = cab2
        img2.place(x=0,y=570)

        self.nome= Label(janela, text="Nome:")
        self.nome["font"] = ("Calibri", "25", "bold")
        self.nome.place(x=20, y=50)

        self.nomeE= Entry(janela)
        self.nomeE["font"] = ("Calibri", "25")
        self.nomeE.place(x=125, y=50, width=700)




         


janela = Tk()
Tela(janela)
janela.title("Assistência técnica - CJ Systems")
janela.geometry("900x600")
janela.resizable(width=False, height=False)
janela.mainloop()
