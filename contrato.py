from tkcalendar import DateEntry
from tkinter import *
import os
from tkinter import ttk

class Tela():

     def __init__(self, master):

        
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
        self.servicoE= ttk.Combobox(janela, values=servicos)
        self.servicoE["font"] = ("Calibri", "25")
        self.servicoE.config(foreground="#696969")
        self.servicoE.place(x=540, y=210, width=330)

  
        self.adicional= Label(janela, text="Dados adicionais:")
        self.adicional["font"] = ("Calibri", "25", "bold")
        self.adicional.place(x=20, y=300)

        self.adicionalE= Text(janela)
        self.adicionalE["font"] = ("Calibri", "20")
        self.adicionalE.config(foreground="red")
        self.adicionalE.place(x=270, y=300, width=600, height=150)

        self.limpar= Button(janela, text="Limpar tudo")
        self.limpar["font"] = ("Lucida", "17", "bold")
        self.limpar.config(foreground="white", bg="red")
        self.limpar.place(x=230, y=490)
        self.limpar.bind("<Button-1>", self.limpa)
       

        self.gerar= Button(janela, text="Gerar contrato")
        self.gerar["font"] = ("Lucida", "17", "bold")
        self.gerar.config(foreground="white", bg="green")
        self.gerar.place(x=490, y=490)
        self.gerar.bind("<Button-1>", self.gerar_contrato)

     def limpa(self, event):
          
          self.nomeE.delete(0,"end")
          self.cpfE.delete(0,"end")
          self.dataE.delete(0, "end")
          self.dispositivoE.delete(0, "end")
          self.servicoE.delete(0, "end")
          self.adicionalE.delete("1.0", "end")

     def gerar_contrato(self, event):

          nome = self.nomeE.get()
          cpf = self.cpfE.get()
          d = self.dispositivoE.get()
          s = self.servicoE.get()

          valor = 1400

          if(s == "Formatação"):
               valor = 90
               
          if(s == "Troca de peças"):
               valor = 50

          if(s == "Limpeza"):
               valor = 50
               
          if(s == "Recuperação de dados"):
               valor = 100
               
          if(s == "Quebra de senha"):
               valor = 30

          if(s == "Upgrade"):
               valor = 200

          if(s == "Outro..."):
               valor = "?"

               
          
          

          self.nomeE.delete(0,"end")
          self.cpfE.delete(0,"end")
          self.dataE.delete(0, "end")
          self.dispositivoE.delete(0, "end")
          self.servicoE.delete(0, "end")
          self.adicionalE.delete("1.0", "end")

          
          contrato = Tk()
          contrato.geometry("630x700")
          contrato.config(bg="white")

          self.lb1 = Label(contrato, text="CONTRATO DIGITAL - CJ SYSTEMS")
          self.lb1["font"] = ("Arial", "15")
          self.lb1.config(bg="white")
          self.lb1.place(x=80,y=5)

          self.lb2 = Label(contrato, text="CONTRATANTE: {}".format(nome))
          self.lb2["font"] = ("Arial", "13")
          self.lb2.config(bg="white", foreground="black")
          self.lb2.place(x=10,y=100)

          self.lb3 = Label(contrato, text="CPF: {}".format(cpf))
          self.lb3["font"] = ("Arial", "13")
          self.lb3.config(bg="white", foreground="black")
          self.lb3.place(x=10,y=130)

          self.lb4 = Label(contrato, text="O presente contrato tem por objeto a prestação continuada de\n serviços de manutenção corretiva e preventiva em {},\n será realizada especificamente a {} do dispositivo, \n podendo ter acréscimo no valor final caso o prestador \n precise fazer outro reparo.".format(d,s))
          self.lb4["font"] = ("Arial", "14")
          self.lb4.config(bg="white", foreground="black")
          self.lb4.place(x=4,y=200)

          self.lb5 = Label(contrato, text="Valor: R${}".format(valor))
          self.lb5["font"] = ("Arial", "14")
          self.lb5.config(bg="white", foreground="red")
          self.lb5.place(x=4,y=600)


          

      
          

   
    




janela = Tk()
Tela(janela)
janela.title("Assistência técnica - CJ Systems")
janela.geometry("900x600+100+100")
janela.resizable(width=False, height=False)
janela.mainloop()
