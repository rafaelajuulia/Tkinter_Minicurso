from tkinter import *
from tkinter import messagebox
import tkinter as tk
class Janela_principal:
    def __init__(self,janela):
        self.janela= janela
        self.janela.title('TK')
        self.janela['background'] = ('magenta')
        self.janela.geometry('300x200+550+100')
        self.janela.resizable(width = False, height = False)
        
        self.texto1 = tk.Label(self.janela,text = 'Login:', bg = 'magenta', font= ('Arial',14,'bold'))
        self.texto1.place(x='20',y='40')
        
        self.texto2 = tk.Label(self.janela,text = 'Senha:', bg = 'magenta', font= ('Arial',14,'bold'))
        self.texto2.place(x='20',y='90')
        
        self.campo1 = tk.Entry(self.janela,fg='black', bg='white')
        self.campo1.place(x='90',y='45')
        
        self.campo2 = tk.Entry(self.janela,fg= 'black',bg= 'white')
        self.campo2.place(x='90',y='90')
        
        self.botao_entrar = tk.Button(self.janela,text='Entrar', fg='purple', bg='white',relief='raised', command= self.entrar)
        self.botao_entrar.place(x='130',y='120')
        
        
    def entrar(self):
        self.c1= self.campo1.get()
        self.c2 = self.campo2.get()
        
        if self.c1 == '' or self.c2 == '':
            messagebox.showwarning('atenção','Preencha todos os campos')
        elif self.c1 == 'rafaela' and self.c2 == '456':
            self.nova_pagina()
        else:
            messagebox.showerror('atenção','senha ou usúario incorreto ')
 
    def nova_pagina(self):
        self.janela2= Toplevel()
        self.janela2.geometry('600x400+550+100')
        
        self.cadastro = tk.Label(self.janela2,text = 'Bem vindo ao cadastro de interresse',fg='purple', bg ='white', font= ('Arial',12))
        self.cadastro.pack()
        
        self.nome = tk.Label(self.janela2,text = 'Qual o seu nome?', fg='black',bg ='white', font= ('Arial',12))
        self.nome.place(x='20',y='80')
        self.campo3 = tk.Entry(self.janela2,fg='black', bg='white' )
        self.campo3.place(x='200',y='80')
        
        self.genero = tk.Label(self.janela2, text= 'Qual o seu gênero? ', fg='black', bg= 'white', font= ('Arial',12))
        self.genero.place(x='20',y='110')
        self.campo4 = tk.Entry(fg='black',bg='white')
        self.campo4.place(x='200',y='80')
        
    
        self.idade = tk.Label(self.janela2, text='Qual a sua idade?',fg='black', bg='white',font=('Arial',12))
        self.idade.place(x='20',y='140')
        self.campo5 =tk.Entry(fg='black',bg='white')
        self.campo5.place(x='200',y='80')
        
        
    
            
        
        
    
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
janela= tk.Tk()
objeto = Janela_principal(janela)
janela.mainloop()