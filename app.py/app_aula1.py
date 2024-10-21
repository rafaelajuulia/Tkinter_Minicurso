from tkinter import *
import tkinter as tk
class Janela_Principal:
    def __init__(self,janela):
        self.janela=janela
        self.janela.title('Raju')
        self.janela['background'] = ('lightblue')
        self.janela.geometry('300x200+550+100')
        self.janela.resizable(width = False, height = False)
        
        #primeiro botão
        self.botao1 = tk.Label(self.janela,text = 'Entrar no sistema', bg = 'lightblue', font= ('Arial',12,'bold'))
        self.botao1.pack()
        self.botao_entrar = tk.Button(self.janela, text= 'Entrar',
                                     height = 2, width = 10,
                                     foreground ='blue',
                                     background ='lightgreen',
                                     font=('verdana',12,'bold')
                                     )
        self.botao_entrar.pack()
        
        #segundo botão
        self.botao2 = tk.Label(self.janela,text = 'Sair do sistema', bg = 'lightblue', font= ('Arial',12,'bold'))
        self.botao2.pack()
        self.botao_sair = tk.Button(self.janela, text = 'Sair',
                                    height=2,width= 10,
                                    foreground= 'black',
                                    background='lightpink',
                                    font= ('verdana',12,'bold')
                                    )
        self.botao_sair.pack()
        
    
        
janela = tk.Tk()
objeto = Janela_Principal(janela)
janela.mainloop()
