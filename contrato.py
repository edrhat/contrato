from tkcalendar import DateEntry
from tkinter import *
import os
from tkinter import ttk
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
        self.nomeE.config(foreground="#696969")
        self.nomeE.place(x=125, y=50, width=700)


        self.data= Label(janela, text="Data:")
        self.data["font"] = ("Calibri", "25", "bold")
        self.data.place(x=20, y=120)

        self.dataE= DateEntry(janela, locale="pt_br")
        self.dataE["font"] = ("Calibri", "25")
        self.dataE.config(foreground="#696969")
        self.dataE.place(x=125, y=120, width=200)

        self.cpf= Label(janela, text="CPF:")
        self.cpf["font"] = ("Calibri", "25", "bold")
        self.cpf.place(x=450,y=120)

        self.cpfE= Entry(janela)
        self.cpfE["font"] = ("Calibri", "25")
        self.cpfE.config(foreground="#696969")
        self.cpfE.place(x=525, y=120, width=300)


         #LINHA
        linha = PhotoImage(file="linha.png")
        img3 = Label(janela, image=linha)
        img3.config(bg="black")
        img3.linha = linha
        img3.place(x=0,y=190)

        self.dispositivo= Label(janela, text="Dispositivo:")
        self.dispositivo["font"] = ("Calibri", "25", "bold")
        self.dispositivo.place(x=20, y=210)

        dis = ["Computador", "Notebook", "Smartphone"]  
        self.dispositivoE= ttk.Combobox(janela, values=dis)
        self.dispositivoE["font"] = ("Calibri", "25")
        self.dispositivoE.config(foreground="#696969")
        self.dispositivoE.place(x=195, y=210, width=200)


        self.servico= Label(janela, text="Serviço:")
        self.servico["font"] = ("Calibri", "25", "bold")
        self.servico.place(x=420, y=210)

        servicos = ["Formatação", "Troca de peças", "Limpeza", "Recuperação de dados","Quebra de senha","Upgrade","Outro..."]  
        self.dispositivoE= ttk.Combobox(janela, values=servicos)
        self.dispositivoE["font"] = ("Calibri", "25")
        self.dispositivoE.config(foreground="#696969")
        self.dispositivoE.place(x=540, y=210, width=330)



         


janela = Tk()
Tela(janela)
janela.title("Assistência técnica - CJ Systems")
janela.geometry("900x600")
janela.resizable(width=False, height=False)
janela.mainloop()
