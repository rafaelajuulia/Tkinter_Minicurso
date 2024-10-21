from tkinter import *
import tkinter as tk
class Janela_Principal:
    def __init__(self,janela):
        self.janela=janela
        self.janela.title('Raju')
        self.janela.geometry('300x200+550+100')
        
        self.Label_nome = tk.Label(self.janela, text='Esceve o teu nome:',font= ('Arial',11,'bold'))
        self.Label_nome.pack()
        self.campo1 = tk.Entry(self.janela)
        self.campo1.pack()
        
        
        self.botao_Executar = tk.Button(self.janela, text = 'Executar',
                                    height=2,width= 5,
                                    foreground= 'black',
                                    background='lightgrey',
                                    font= ('verdana',5,'bold'))
            
        self.botao_Executar.pack()
        
       
        
        
        
janela = tk.Tk()
objeto = Janela_Principal(janela)
janela.mainloop()
