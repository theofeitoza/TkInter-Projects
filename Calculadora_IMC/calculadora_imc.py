from tkinter import *
from tkinter import ttk

cor1="#3d3d3d" #preto
cor2="#fafcff" #branco
cor3="#21c25c" #verde
cor4="#eb463b" #vermelho
cor5="#dedcdc" #cinza
cor6="#3080f0" #azul

def get_nome():
    global nome_entry
    nome=nome_entry.get()
    try:
        return str(nome)
    except ValueError:
        return None
    
def get_altura():
    global altura_entry
    altura=altura_entry.get()
    try:
        return float(altura)
    except ValueError:
        return None

def get_peso():
    global peso_entry
    peso=peso_entry.get()
    try:
        return float(peso)
    except ValueError:
        return None

def calculo_imc():
    altura=get_altura()
    peso=get_peso()
    imc= peso / altura ** 2
    return imc

def mensagem():
    nome=get_nome()
    altura=get_altura()
    peso=get_peso()
    imc=calculo_imc()
    imctext.config(text=f'{imc:.3}')
    if imc<18.5:
        retorno.config(text=f'Olá {nome}, você mede {altura}m, pesa {peso}kgs \n e se encontra abaixo do peso')
    elif 18.6<imc<24.9:
        retorno.config(text=f'Olá {nome}, você mede {altura}m, pesa {peso}kgs \n e se encontra no peso ideal')
    elif 25<imc<29.9:
        retorno.config(text=f'Olá {nome}, você mede {altura}m, pesa {peso}kgs \n e se encontra levemente acima do peso')
    elif 30<imc<34.9:
        retorno.config(text=f'Olá {nome}, você mede {altura}m, pesa {peso}kgs \n e se encontra em obesidade grau 1')
    elif 35<imc<39.9:
        retorno.config(text=f'Olá {nome}, você mede {altura}m, pesa {peso}kgs \n e se encontra em obesidade severa')
    else:
        retorno.config(text=f'Olá {nome}, você mede {altura}, pesa {peso} \n e se encontra em obesidade mórbida')

janela = Tk()
janela.title('')
janela.geometry('320x150')
janela.resizable(width=FALSE, height=FALSE)
janela.config(bg=cor2)

frame_cima= Frame(janela, width=320, height=20, bg=cor2)
frame_cima.grid(row=0, column=0)

frame_meio=Frame(janela, width=320, height=90, bg=cor2)
frame_meio.grid(row=1, column=0)

frame_baixo= Frame(janela, width=320, height=40, bg=cor2)
frame_baixo.grid(row=2, column=0)

nome=Label(frame_cima,text='Calculadora IMC', bg=cor2,fg=cor1,font='Ivy 12', anchor='center',relief='flat')
nome.place(x=100, y=0)

nome=Label(frame_meio,text='Digite seu nome:', bg=cor2,fg=cor1)
nome.place(x=0, y=0)

nome_entry=ttk.Entry(frame_meio, width=10, background=cor1)
nome_entry.place(x=100, y=0)

altura=Label(frame_meio,text='Digite sua altura:', bg=cor2, fg=cor1)
altura.place(x=0, y=20)

altura_entry=ttk.Entry(frame_meio, width=10, background=cor1)
altura_entry.place(x=100, y=20)

peso=Label(frame_meio,text='Digite seu peso', bg=cor2, fg=cor1)
peso.place(x=0, y=40)

peso_entry=ttk.Entry(frame_meio, width=10, background="#3d3d3d")
peso_entry.place(x=100, y=40)

botao=ttk.Button(frame_meio,text="Fazer cálculo", command=mensagem)
botao.place(x=0, y=60)

retorno=Label(frame_baixo, text="", bg=cor2, fg=cor1)
retorno.place(x=0, y=0)

imctext=Label(frame_meio,text="", bg=cor6, fg=cor1, width=5, height=2, font='Ivy 18')
imctext.place(x=200, y=5)

janela.mainloop()